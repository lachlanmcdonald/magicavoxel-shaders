from os import path
from datetime import datetime
import yaml

DIR = path.dirname(path.realpath(__file__))

with open(path.join(DIR, 'shaders.yml')) as f:
	data = yaml.safe_load(f)
	SHADERS = {k: v['params'] for k, v in data['shaders'].items()}
	TYPES = data['types']

lines = []
toc = []

for shader_path, args in SHADERS.items():
	shader_name = shader_path.split('/')[-1]

	xs_args = []
	example_args = []

	for arg in args:
		if 'type' in arg and arg['type'] in TYPES:
			arg.update({
				**TYPES[arg['type']],
				**arg,
			})

		xs_args.append('[{}]'.format(arg['name']))
		example_args.append(str(arg['value']))

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

	for index, arg in enumerate(args):
		arg_value = arg['value'] if 'value' in arg else '—'
		arg_type = 'Integer' if arg['decimal'] == 0 else 'Float'
		arg_range = '-'.join(arg['range'].split(' ')) if 'range' in arg else '—'

		lines.append('`{}` | **{}** | {} | {}'.format(index, arg['name'], arg_type, arg_range))

	lines.append('\nExample:\n')
	lines.append('```')
	lines.append('xs {} {}'.format(shader_path, ' '.join(example_args)))
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
