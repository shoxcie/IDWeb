tk = [
	['*TEntry*Font', ('Arial', 14, 'bold')],
	
	['*TCombobox*Font', ('Helvetica', 12, 'bold')],
	['*TCombobox*Background', 'black'],
	['*TCombobox*Foreground', 'white'],
	
	['*Text*Background', 'black'],
	['*Text*Foreground', 'white'],
	['*Text*selectbackground', 'white'],
	['*Text*insertwidth', 2],
	['*Text*Font', ('Arial', 14)],
	['*Text*width', 0],
	['*Text*height', 0],
	['*Text*relief', 'flat'],
]

ttk = {
	'.': {
		'configure': {
			'background': 'black',
			'foreground': 'white',
			'font': ('Helvetica', 12),
			'borderwidth': 4,
		}
	},
	'TNotebook': {
		'configure': {
			"padding": [-2, 0],
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
		}
	},
	'TEntry': {
		'configure': {
			'fieldbackground': 'black',
			'insertcolor': 'white',
			'selectbackground': 'gray30',
			'selectforeground': 'red',
			'insertwidth': 2,
			'padding': 10,
		}
	},
	'TButton': {
		'configure': {
			'background': 'gray25',
			'foreground': 'white',
			'focuscolor': 'gray60',
			'padding': [40, 20],
			'anchor': 'center'
		},
		'map': {
			'background': [
				('active', 'gray15')
			]
		}
	},
	'Treeview': {
		'configure': {
			'fieldbackground': 'black',
			'rowheight': 40
		},
		'map': {
			'background': [
				('selected', 'gray30')
			]
		}
	},
	'Treeview.Heading': {
		'configure': {
			'relief': 'sunken'
		}
	},
	'TCombobox': {
		'configure': {
			'fieldbackground': 'black',
			'padding': 10,
			'arrowcolor': 'white',
			'arrowsize': 18,
			'relief': 'flat'
		},
		'map': {
			'background': [
				('focus', 'grey30')
			]
		}
	},
	'ComboboxPopdownFrame': {
		'configure': {
			'relief': 'groove'
		}
	},
	'TScrollbar': {
		'configure': {
			'relief': 'flat',
			'borderwidth': 1,
			'background': 'black',
			'troughcolor': 'gray30'
		}
	}
}
