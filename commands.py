#!/usr/bin/env python3

# Copyright (c) 2023 Lachlan McDonald
# This work is licensed under the MIT License (MIT)
# https://github.com/lachlanmcdonald/magicavoxel-shaders
from os import path
from datetime import datetime
import yaml

DIR = path.dirname(path.realpath(__file__))

with open(path.join(DIR, 'shaders.yml')) as f:
	data = yaml.safe_load(f)
	SHADERS = {k: v['params'] for k, v in data['shaders'].items()}
	TYPES = data['types']
	BASE_PARAMS = data['base_param']

lines = []
toc = []

for shader_path, params in SHADERS.items():
	shader_name = shader_path.split('/')[-1]
	xs_args = []
	example_params = []

	for param in params:
		param.update({
			**BASE_PARAMS,
			**param,
		})

		if 'type' in param and param['type'] in TYPES:
			param.update({
				**TYPES[param['type']],
				**param,
			})

		xs_args.append('[{}]'.format(param['name']))
		example_params.append(str(param['value']))

	# TOC
	toc.append('- [{}](#{})'.format(shader_name, shader_name))

	# Code block
	lines.append('# {}\n'.format(shader_name))
	lines.append('```')
	lines.append('xs {} {}'.format(shader_path, ' '.join(xs_args)))
	lines.append('```\n')

	# Arg table
	lines.append('ID | Argument | Type | Range')
	lines.append('-- | -------- | ---- | -----')

	for index, param in enumerate(params):
		arg_value = param['value'] if 'value' in param else '—'
		arg_range = '-'.join(param['range'].split(' ')) if 'range' in param else '—'
		arg_type = 'Integer' if param['precision'] == 0 else 'Float'
		lines.append('`{}` | **{}** | {} | {}'.format(index, param['name'], arg_type, arg_range))

	lines.append('\nExample:\n')
	lines.append('```')
	lines.append('xs {} {}'.format(shader_path, ' '.join(example_params)))
	lines.append('```\n[Top](#)')


print('\n'.join([
	'> The following page outlines the shader commands for use in MagicaVoxel\'s console.',
	'> ',
	'> Since the addition of the shader UI, default parameters and error-checking has been removed from the scripts. All arguments are required.',
	'',
	*toc,
	*lines,
	'',
	'<sub>This page was last generated: {}</sub>'.format(datetime.now()),
]))
