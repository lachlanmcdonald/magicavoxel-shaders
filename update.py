from os import path
from datetime import datetime
import yaml

DIR = path.dirname(path.realpath(__file__))
AUTHOR = '@lachlanmcdonald'
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
	LICENSES = data['licenses']
	SHADERS = data['shaders']
	TYPES = data['types']
	BASE_PARAM = data['base_param']

for shader_key, props in SHADERS.items():
	shader_path = path.join(DIR,
							'shader',
							*"{}.txt".format(shader_key).split('/'))

	if path.exists(shader_path) is False:
		print("Could not update shader {}, path does not exist: {}".format(shader_key, shader_path))
		continue

	print("Updating: {}".format(shader_key))

	# Shader header
	has_params = 'params' in props and len(props['params']) > 0
	header = []

	# License header
	license_key = props['license'] if 'license' in props else 'mit'
	if license_key not in LICENSES:
		print("Could not update shader {}, license does not exist: {}".format(shader_key, license_key))
		continue
	header.extend(LICENSES[license_key].format(datetime.now().year).strip().splitlines())
	header.append('')

	# Additional cites
	if 'cites' in props:
		cite_lines = props['cites'].strip().splitlines()
		header.extend(cite_lines)
		header.append('')

	# Process params
	if has_params:
		for param in props['params']:
			# Merge params on types
			if 'type' in param and param['type'] in TYPES:
				param.update({
					**TYPES[param['type']],
					**param,
				})

			# Default "value" using "range" if one does not exist
			if 'value' not in param and 'range' in param:
				param['value'] = param['range'].split(' ')[0]

			# Update with base params
			param.update({
				**BASE_PARAM,
				**param,
			})

			if 'name' not in param:
				print('Missing name attribute: ', param)

	# Console command instructions
	param_strings = ' '.join([ '[{}]'.format(x['name']) for x in props['params'] ])
	header.append('xs {} {}'.format(shader_key, param_strings))

	# MagicaVoxel configuration
	header.append('')
	header.append('xs_begin')
	header.append('author : \'{}\''.format(AUTHOR))

	if has_params:
		for index, param in enumerate(props['params']):
			arg = [
				ARG_FORMAT.format('id', index),
				ARG_FORMAT.format('name', param['name'])
			]

			for k in ['value', 'var', 'range', 'step', 'decimal']:
				if k in param:
					arg.append(ARG_FORMAT.format(k, param[k]))
			header.append('arg : {{ {} }}'.format('  '.join(arg)))

	header.append('xs_end')
	header_text = '\n'.join([ '// {}'.format(x).rstrip() for x in header ])

	# Read shader file and strip existing header
	with open(shader_path, 'r') as f:
		lines = f.readlines()
		shader_source =	[]
		has_header_comment = lines[0].startswith('//')

		for line in lines:
			if has_header_comment and line.startswith('//'):
				continue
			else:
				has_header_comment = False
				shader_source.append(line.rstrip())

	# Shader text
	shader_text = header_text + '\n' + '\n'.join(shader_source)

	# Fix global variables which change between releases of MagicaVoxel
	for old, new in FIX_GLOBAL_VARS.items():
		shader_text = shader_text.replace(old, new)

	# Replace i_args with the variable names
	if has_params:
		for index, param in enumerate(props['params']):
			if 'var' in param:
				shader_text = shader_text.replace("i_args[{}]".format(index), param['var'])

	# Write shader to file
	if len(shader_text) > 0:
		with open(shader_path, 'w', newline="\n") as f:
			f.write(shader_text + '\n')
