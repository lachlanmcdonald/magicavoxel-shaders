from os import path
from datetime import datetime
import json
import re

DIR = path.dirname(path.realpath(__file__))

TYPES = {
	'fraction': {
		'value': 0.5,
		'range': '0 1',
		'step': 0.01,
		'decimal': 1,
	},
	'color_a': {
		'value': 1,
		'range': '0 255',
		'step': 1,
		'decimal': 0
	},
	'color_b': {
		'value': 2,
		'range': '0 255',
		'step': 1,
		'decimal': 0
	},
	'size': {
		'value': 1,
		'range': '1 127',
		'step': 1,
		'decimal': 0
	},
	'position': {
		'value': 0,
		'range': '0 127',
		'step': 1,
		'decimal': 0
	}
}

ARG_FORMAT = "{} = '{}'"

with open(path.join(DIR, 'params.json')) as f:
	params = json.load(f)

for shader_name in params.keys():
	header = [
		'MIT License (MIT)',
		'https://github.com/lachlanmcdonald/magicavoxel-shaders',
		'Copyright (c) {} Lachlan McDonald'.format(datetime.now().year).strip(),
		'',
	]

	param_strings = ' '.join([ '[{}]'.format(x['name']) for x in params[shader_name] ])
	header.append('xs {} {}'.format(shader_name, param_strings))

	header.append('')
	header.append('xs_begin')
	for index, param in enumerate(params[shader_name]):
		t = [
			ARG_FORMAT.format('id', index),
			ARG_FORMAT.format('name', param['name'])
		]

		for k in ['value', 'range', 'step', 'decimal']:
			if k in param:
				t.append(ARG_FORMAT.format(k, param[k]))
			elif k in TYPES[param['type']]:
				t.append(ARG_FORMAT.format(k, TYPES[param['type']][k]))

		header.append('arg : {{ {} }}'.format('  '.join(t)))
	header.append('xs_end')

	header_text = '\n'.join([ '// {}'.format(x) for x in header ])

	with open(path.join(DIR, 'shader', "{}.txt".format(shader_name)), 'r') as f:
		shader = f.readlines()

	with open(path.join(DIR, 'shader', "{}.txt".format(shader_name)), 'w') as f:
		has_comment = shader[0].startswith('//')
		t = []

		for line in shader:
			if has_comment and line.startswith('//'):
				continue
			else:
				has_comment = False
				t.append(line.rstrip())

		f.write(header_text + '\n' + '\n'.join(t) + '\n')
