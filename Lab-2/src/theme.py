black_theme_settings = {
	'.': {
		'configure': {
			'background': 'black',
			'foreground': 'white',
			'focuscolor': '',
			'font': ("Helvetica", 12)
		}
	},
	'TNotebook': {
		'configure': {
			"padding": [-1],
			"tabposition": 'n'
		}
	},
	'TNotebook.Tab': {
		'configure': {
			'padding': [20, 10],
			'width': 999,
			'borderwidth': 0
		},
		'map': {
			'background': [
				('selected', 'gray30'),
				('active', 'gray15')
			],
			'foreground': [
				('selected', 'white')
			]
			# "expand": [("selected", [1, 1, 1, 0])]
		}
	}
}
