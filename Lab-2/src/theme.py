black_theme_settings = {
	'.': {
		'configure': {
			'background': 'black',
			'foreground': 'white',
			'font': ("Helvetica", 12),
			'focuscolor': 'gray60'
		}
	},
	'TNotebook': {
		'configure': {
			"padding": [-1, 0],
			"tabposition": 'n',
		}
	},
	'TNotebook.Tab': {
		'configure': {
			'padding': [20, 10],
			'width': 999,
			'borderwidth': 0,
			'focuscolor': ''
		},
		'map': {
			'background': [
				('selected', 'gray25'),
				('active', 'gray15')
			],
			'foreground': [
				('selected', 'white')
			]
			# "expand": [("selected", [1, 1, 1, 0])]
		}
	},
	'TEntry': {
		'configure': {
			'fieldbackground': 'black',
			'foreground': 'white',
			'insertcolor': 'white',
			'selectbackground': 'gray30',
			'selectforeground': 'red',
			'insertwidth': 2,
			'padding': 10,
			'borderwidth': 4,
		}
	},
	'TButton': {
		'configure': {
			'background': 'gray25',
			'foreground': 'white',
			'padding': [40, 20],
			'anchor': 'center'
		},
		'map': {
			'background': [
				('active', 'gray15')
			]
		}
	}
}
