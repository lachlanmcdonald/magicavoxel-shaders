from os import path
from datetime import datetime
import yaml

DIR = path.dirname(path.realpath(__file__))
ARG_FORMAT = "{} = '{}'"
FIX_GLOBAL_VARS = {
	'iArgs': 'i_args',
	'iVolumeSize': 'i_volume_size',
	'iColorIndex': 'i_color_index',
	'iMirror': 'i_mirror',
	'iAxis': 'i_axis',
	'iIter': 'i_iter',
}

with open(path.join(DIR, 'shaders.yml')) as f:
	data = yaml.safe_load(f)
	params = { k: v['params'] for k, v in data['shaders'].items() }
	TYPES = data['types']

# Update shaders
for shader_name in params.keys():
	print("Updating {}".format(shader_name))

	# Updated copyright header
	header = [
		'MIT License (MIT)',
		'https://github.com/lachlanmcdonald/magicavoxel-shaders',
		'Copyright (c) {} Lachlan McDonald'.format(datetime.now().year).strip(),
		'',
	]

	# Console command instructions
	param_strings = ' '.join([ '[{}]'.format(x['name']) for x in params[shader_name] ])
	header.append('xs {} {}'.format(shader_name, param_strings))

	# Append headers
	if len(params[shader_name]) > 0:
		header.append('')
		header.append('xs_begin')
		header.append('author : \'@lachlanmcdonald\'')
		for index, param in enumerate(params[shader_name]):
			shader_lines = [
				ARG_FORMAT.format('id', index),
				ARG_FORMAT.format('name', param['name'])
			]

			for k in ['value', 'var', 'range', 'step', 'decimal']:
				if k in param:
					shader_lines.append(ARG_FORMAT.format(k, param[k]))
				elif 'type' in param and k in TYPES[param['type']]:
					shader_lines.append(ARG_FORMAT.format(k, TYPES[param['type']][k]))

			header.append('arg : {{ {} }}'.format('  '.join(shader_lines)))
		header.append('xs_end')

	header_text = '\n'.join([ '// {}'.format(x) for x in header ])
	shader_path = shader_name.replace('/', path.sep)

	# Read shader file
	with open(path.join(DIR, 'shader', "{}.txt".format(shader_path)), 'r') as f:
		shader = f.readlines()

	# Write updated shader file
	with open(path.join(DIR, 'shader', "{}.txt".format(shader_path)), 'w', newline="\n") as f:
		has_comment = shader[0].startswith('//')
		shader_lines = []

		# Strip lines of whitespace
		for line in shader:
			if has_comment and line.startswith('//'):
				continue
			else:
				has_comment = False
				shader_lines.append(line.rstrip())

		shader_text = header_text + '\n' + '\n'.join(shader_lines)
		shader_text = '\n'.join([line.rstrip() for line in shader_text.splitlines()])

		# Fix global variables which change between releases of MagicaVoxel
		for old, new in FIX_GLOBAL_VARS.items():
			shader_text = shader_text.replace(old, new)

		f.write(shader_text + '\n')
