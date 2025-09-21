class SettingsDialogLogic:
    def __init__(self, bgcolor, bgcolor_node, bgcolor_connector, bgcolor_cable, bgcolor_bundle, color_mode, fontname, mini_bom_mode, template_separator):
        self._bgcolor = bgcolor
        self._bgcolor_node = bgcolor_node
        self._bgcolor_connector = bgcolor_connector
        self._bgcolor_cable = bgcolor_cable
        self._bgcolor_bundle = bgcolor_bundle
        self._color_mode = color_mode
        self._fontname = fontname
        self._mini_bom_mode = mini_bom_mode
        self._template_separator = template_separator

    def get_options(self):
        options = {}
        if self._bgcolor:
            options['bgcolor'] = self._bgcolor
        if self._bgcolor_node:
            options['bgcolor_node'] = self._bgcolor_node
        if self._bgcolor_connector:
            options['bgcolor_connector'] = self._bgcolor_connector
        if self._bgcolor_cable:
            options['bgcolor_cable'] = self._bgcolor_cable
        if self._bgcolor_bundle:
            options['bgcolor_bundle'] = self._bgcolor_bundle
        if self._color_mode:
            options['color_mode'] = self._color_mode
        if self._fontname:
            options['fontname'] = self._fontname
        if self._mini_bom_mode:
            options['mini_bom_mode'] = self._mini_bom_mode
        if self._template_separator:
            options['template_separator'] = self._template_separator
        return options
