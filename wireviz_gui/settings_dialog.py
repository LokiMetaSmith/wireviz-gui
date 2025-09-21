import logging
import tkinter as tk
from tkinter.messagebox import showerror
import tkinter.ttk as ttk
import yaml

from wireviz_gui._base import BaseFrame
from wireviz_gui.dialog_logic import SettingsDialogLogic


class SettingsDialog(BaseFrame):
    def __init__(self, parent,
                 on_save_callback: callable = None,
                 loglevel=logging.INFO):
        super().__init__(parent, loglevel=loglevel)

        self._on_save_callback = on_save_callback

        r = 0
        tk.Label(self, text='Settings', **self._heading)\
            .grid(row=r, column=0, columnspan=2, sticky='ew')

        r += 1
        tk.Label(self, text='Colors', **self._bold)\
            .grid(row=r, column=0, columnspan=2, sticky='w')

        r += 1
        tk.Label(self, text='Background Color:', **self._normal)\
            .grid(row=r, column=0, sticky='e')
        self._bgcolor_entry = tk.Entry(self)
        self._bgcolor_entry.grid(row=r, column=1, sticky='ew')

        r += 1
        tk.Label(self, text='Node Color:', **self._normal)\
            .grid(row=r, column=0, sticky='e')
        self._bgcolor_node_entry = tk.Entry(self)
        self._bgcolor_node_entry.grid(row=r, column=1, sticky='ew')

        r += 1
        tk.Label(self, text='Connector Color:', **self._normal)\
            .grid(row=r, column=0, sticky='e')
        self._bgcolor_connector_entry = tk.Entry(self)
        self._bgcolor_connector_entry.grid(row=r, column=1, sticky='ew')

        r += 1
        tk.Label(self, text='Cable Color:', **self._normal)\
            .grid(row=r, column=0, sticky='e')
        self._bgcolor_cable_entry = tk.Entry(self)
        self._bgcolor_cable_entry.grid(row=r, column=1, sticky='ew')

        r += 1
        tk.Label(self, text='Bundle Color:', **self._normal)\
            .grid(row=r, column=0, sticky='e')
        self._bgcolor_bundle_entry = tk.Entry(self)
        self._bgcolor_bundle_entry.grid(row=r, column=1, sticky='ew')

        r += 1
        tk.Label(self, text='Color Mode:', **self._normal)\
            .grid(row=r, column=0, sticky='e')
        self._color_mode_cb = ttk.Combobox(self, values=['full', 'FULL', 'hex', 'HEX', 'short', 'SHORT', 'ger', 'GER'])
        self._color_mode_cb.grid(row=r, column=1, sticky='ew')

        r += 1
        tk.Label(self, text='Fonts', **self._bold)\
            .grid(row=r, column=0, columnspan=2, sticky='w')

        r += 1
        tk.Label(self, text='Font Name:', **self._normal)\
            .grid(row=r, column=0, sticky='e')
        self._fontname_entry = tk.Entry(self)
        self._fontname_entry.grid(row=r, column=1, sticky='ew')

        r += 1
        tk.Label(self, text='BOM', **self._bold)\
            .grid(row=r, column=0, columnspan=2, sticky='w')

        r += 1
        tk.Label(self, text='Mini BOM Mode:', **self._normal)\
            .grid(row=r, column=0, sticky='e')
        self._mini_bom_mode_var = tk.BooleanVar()
        self._mini_bom_mode_cb = ttk.Checkbutton(self, variable=self._mini_bom_mode_var)
        self._mini_bom_mode_cb.grid(row=r, column=1, sticky='ew')

        r += 1
        tk.Label(self, text='Autogeneration', **self._bold)\
            .grid(row=r, column=0, columnspan=2, sticky='w')

        r += 1
        tk.Label(self, text='Template Separator:', **self._normal)\
            .grid(row=r, column=0, sticky='e')
        self._template_separator_entry = tk.Entry(self)
        self._template_separator_entry.grid(row=r, column=1, sticky='ew')

        r += 1
        tk.Button(self, text='Save Settings',
                  command=self._save,
                  **self._normal)\
            .grid(row=r, column=0, columnspan=2, sticky='ew')

    def _save(self):
        logic = SettingsDialogLogic(
            bgcolor=self._bgcolor_entry.get(),
            bgcolor_node=self._bgcolor_node_entry.get(),
            bgcolor_connector=self._bgcolor_connector_entry.get(),
            bgcolor_cable=self._bgcolor_cable_entry.get(),
            bgcolor_bundle=self._bgcolor_bundle_entry.get(),
            color_mode=self._color_mode_cb.get(),
            fontname=self._fontname_entry.get(),
            mini_bom_mode=self._mini_bom_mode_var.get(),
            template_separator=self._template_separator_entry.get()
        )
        options = logic.get_options()

        if self._on_save_callback is not None:
            self._on_save_callback(options)
