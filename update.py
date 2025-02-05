#!/usr/bin/env python3

# Copyright (c) 2023 Lachlan McDonald
# This work is licensed under the MIT License (MIT)
# https://github.com/lachlanmcdonald/magicavoxel-shaders
import re
from datetime import datetime
from os import path

import yaml

DIR = path.dirname(path.realpath(__file__))
TAB_EXPR = re.compile("^( {4})+", re.MULTILINE)
AUTHOR = "@lmcdx.bsky.social"

ARG_FORMAT = "{} = '{}'"

FIX_GLOBAL_VARS = {
	"iArgs": "i_args",
	"iVolumeSize": "i_volume_size",
	"iColorIndex": "i_color_index",
	"iMirror": "i_mirror",
	"iAxis": "i_axis",
	"iIter": "i_iter",
}

with open(path.join(DIR, "shaders.yml"), "r") as f:
	data = yaml.safe_load(f)
	LICENSES = data["licenses"]
	SHADERS = data["shaders"]
	TYPES = data["types"]
	CITES = data["cites"]
	BASE_PARAM = data["base_param"]


def get_shader_source(shader_path):
	shader_source = []
	existing_copyright = None

	with open(shader_path, "r") as f:
		lines = f.readlines()
		has_header_comment = lines[0].startswith("//")

		for line in lines:
			if has_header_comment and line.startswith("//"):
				match = re.search(r"Copyright.+?(\d{4})", line, re.IGNORECASE)

				if existing_copyright is None and match:
					existing_copyright = match.group(1)

				continue
			else:
				has_header_comment = False
				shader_source.append(line.rstrip())

	return shader_source, existing_copyright


for shader_key, props in SHADERS.items():
	shader_path = path.join(DIR, "shader", *"{}.txt".format(shader_key).split("/"))

	if path.exists(shader_path) is False:
		print("Could not update shader {}, path does not exist: {}".format(shader_key, shader_path))
		continue

	print("Updating: {}".format(shader_key))

	# Read shader file and strip existing header
	shader_source, copyright_year = get_shader_source(shader_path)

	# Shader header
	has_params = "params" in props and len(props["params"]) > 0
	header = []

	# License header
	license_key = props["license"] if "license" in props else "mit"

	if license_key not in LICENSES:
		print("Could not update shader {}, license does not exist: {}".format(shader_key, license_key))
		continue

	copyright_year = copyright_year or datetime.now().year
	header.extend(LICENSES[license_key].format(copyright_year).strip().splitlines())
	header.append("")

	# Additional cites
	if "cites" in props:
		header.append("This script utilises or modifies code from other projects or publications.")
		header.append("Please see the attributions below for more information:")
		header.append("")

		for i, k in enumerate(props["cites"]):
			if k not in CITES:
				print("Citation does not exist: ", k)
			else:
				c = CITES[k].strip().splitlines()
				c[0] = "{}. {}".format(i + 1, c[0])
				c[1:] = map(lambda a: "   {}".format(a), c[1:])

				header.extend(c)
				header.append("")

	# Process params
	if has_params:
		for param in props["params"]:
			# Merge params on types
			if "type" in param and param["type"] in TYPES:
				param.update(
					{
						**TYPES[param["type"]],
						**param,
					}
				)

			# Default "value" using "range" if one does not exist
			if "value" not in param and "range" in param:
				param["value"] = param["range"].split(" ")[0]

			# Update with base params
			param.update(
				{
					**BASE_PARAM,
					**param,
				}
			)

			if "name" not in param:
				print("Missing name attribute: ", param)

	# Console command instructions
	if "params" in props:
		param_strings = " ".join(["[{}]".format(x["name"]) for x in props["params"]])
	else:
		param_strings = ""
	header.append("xs {} {}".format(shader_key, param_strings))

	# MagicaVoxel configuration
	header.append("")
	header.append("xs_begin")
	header.append("author : '{}'".format(AUTHOR))

	if has_params:
		for param in props["params"]:
			arg = [ARG_FORMAT.format("name", param["name"])]

			for k in ["var", "range", "value", "step", "precision"]:
				if k in param:
					arg.append(ARG_FORMAT.format(k, param[k]))
			header.append("arg : {{ {} }}".format("  ".join(arg)))

	header.append("xs_end")
	header_text = "\n".join(["// {}".format(x).rstrip() for x in header])

	# Shader text
	shader_text = header_text + "\n" + "\n".join(shader_source)

	# Fix global variables which change between releases of MagicaVoxel
	for old, new in FIX_GLOBAL_VARS.items():
		shader_text = shader_text.replace(old, new)

	# Replace i_args with the variable names
	if has_params:
		for index, param in enumerate(props["params"]):
			if "var" in param:
				shader_text = shader_text.replace("i_args[{}]".format(index), param["var"])

	# Change indentation to tabs
	def tab_replace(m):
		return "\t" * int(len(m.group(0)) / 4)

	shader_text = TAB_EXPR.sub(tab_replace, shader_text)

	# Write shader to file
	if len(shader_text) > 0:
		with open(shader_path, "w", encoding="utf8", newline="\n") as f:
			f.write(shader_text + "\n")
