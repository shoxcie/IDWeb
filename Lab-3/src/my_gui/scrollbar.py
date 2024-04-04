from tkinter.ttk import Scrollbar


class AutoScrollbar(Scrollbar):
	def set(self, low, high):
		if float(low) <= 0.0 and float(high) >= 1.0:
			self.pack_forget()
		else:
			self.pack(side='left', fill='y')
		Scrollbar.set(self, low, high)
