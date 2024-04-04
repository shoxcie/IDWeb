from tkinter.ttk import Notebook, Frame


class Tab:
	def __init__(self, parent: Notebook, title: str, image_png: str = ""):
		self.frame = Frame(parent)
		self.__notebook = parent
		self.__id = len(self.__notebook.tabs())
		# self.__logo = tk.PhotoImage(file=path.join(IMG_DIR, image_png))
		# parent.add(self.frame, text=title, image=self.__logo, compound='left')
		parent.add(self.frame, text=title, compound='left')
	
	def show(self):
		self.__notebook.add(self.__notebook.tabs()[self.__id])
	
	def hide(self):
		self.__notebook.hide(self.__id)
		return self
