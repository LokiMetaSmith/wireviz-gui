import logging
import tkinter as tk
from tkinter.messagebox import showerror
import tkinter.ttk as ttk
import yaml

from wireviz_gui._base import BaseFrame
from wireviz_gui.dialog_logic import MetadataDialogLogic


class MetadataDialog(BaseFrame):
    def __init__(self, parent,
                 on_save_callback: callable = None,
                 loglevel=logging.INFO):
        super().__init__(parent, loglevel=loglevel)

        self._on_save_callback = on_save_callback

        r = 0
        tk.Label(self, text='Harness Metadata', **self._heading)\
            .grid(row=r, column=0, columnspan=2, sticky='ew')

        r += 1
        tk.Label(self, text='Title:', **self._normal)\
            .grid(row=r, column=0, sticky='e')
        self._title_entry = tk.Entry(self)
        self._title_entry.grid(row=r, column=1, sticky='ew')

        r += 1
        tk.Label(self, text='Author:', **self._normal)\
            .grid(row=r, column=0, sticky='e')
        self._author_entry = tk.Entry(self)
        self._author_entry.grid(row=r, column=1, sticky='ew')

        r += 1
        tk.Label(self, text='Version:', **self._normal)\
            .grid(row=r, column=0, sticky='e')
        self._version_entry = tk.Entry(self)
        self._version_entry.grid(row=r, column=1, sticky='ew')

        r += 1
        tk.Label(self, text='Date:', **self._normal)\
            .grid(row=r, column=0, sticky='e')
        self._date_entry = tk.Entry(self)
        self._date_entry.grid(row=r, column=1, sticky='ew')

        r += 1
        tk.Label(self, text='Custom Metadata (YAML):', **self._normal)\
            .grid(row=r, column=0, columnspan=2, sticky='w')

        r += 1
        self._custom_text = tk.Text(self, height=5)
        self._custom_text.grid(row=r, column=0, columnspan=2, sticky='ew')

        r += 1
        tk.Button(self, text='Save Metadata',
                  command=self._save,
                  **self._normal)\
            .grid(row=r, column=0, columnspan=2, sticky='ew')

    def _save(self):
        logic = MetadataDialogLogic(
            title=self._title_entry.get(),
            author=self._author_entry.get(),
            version=self._version_entry.get(),
            date=self._date_entry.get(),
            custom_metadata_text=self._custom_text.get('1.0', 'end')
        )
        try:
            metadata = logic.get_metadata()
        except ValueError as e:
            showerror('Error', str(e))
            return

        if self._on_save_callback is not None:
            self._on_save_callback(metadata)
