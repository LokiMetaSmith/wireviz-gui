import logging
import tkinter as tk

from wireviz_gui._base import BaseMenu


class Menu(BaseMenu):
    def __init__(self, parent,
                 export_all: callable,
                 refresh: callable,
                 color_schemes: callable,
                 about: callable,
                 loglevel=logging.INFO, **kwargs):
        super().__init__(parent=parent, loglevel=loglevel, **kwargs)

        self.add_cascade(label='File', menu=FileMenu(self._parent, export_all=export_all, refresh=refresh))
        self.add_cascade(label='Edit', menu=EditMenu(self._parent, color_schemes=color_schemes))
        self.add_cascade(label='Help', menu=HelpMenu(self._parent, about=about))


class FileMenu(BaseMenu):
    def __init__(self, parent,
                 export_all: callable,
                 refresh: callable,
                 loglevel=logging.INFO, **kwargs):
        super().__init__(parent=parent, loglevel=loglevel, **kwargs)

        command_lookup = {
            'Export All':   lambda: export_all(),
            'Refresh (CTRL+L)':      lambda: refresh(),
        }

        for label, command in command_lookup.items():
            self.add_command(label=label, command=command)


class EditMenu(BaseMenu):
    def __init__(self, parent,
                 color_schemes: callable,
                 loglevel=logging.INFO, **kwargs):
        super().__init__(parent=parent, loglevel=loglevel, **kwargs)

        self.add_command(label='Color Schemes', command=color_schemes)


class HelpMenu(BaseMenu):
    def __init__(self, parent, about: callable, loglevel=logging.INFO, **kwargs):
        super().__init__(parent=parent, loglevel=loglevel, **kwargs)

        command_lookup = {
            'About': lambda: about()
        }

        for label, command in command_lookup.items():
            self.add_command(label=label, command=command)


if __name__ == '__main__':
    window = tk.Tk()

    menu = Menu(window)
    window.config(menu=menu)

    window.mainloop()
