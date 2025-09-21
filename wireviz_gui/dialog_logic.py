class AddConnectorDialogLogic:
    def __init__(self, name, manuf, mpn, ipm, type, subtype, pin_numbers, pinout):
        self._name = name
        self._manuf = manuf
        self._mpn = mpn
        self._ipm = ipm
        self._type = type
        self._subtype = subtype
        self._pin_numbers = pin_numbers
        self._pinout = pinout

    def get_kwargs(self):
        kwargs = {}
        if self._manuf:
            kwargs['manufacturer'] = self._manuf
        if self._mpn:
            kwargs['manufacturer_part_number'] = self._mpn
        if self._ipm:
            kwargs['internal_part_number'] = self._ipm
        if self._type:
            kwargs['type'] = self._type
        if self._subtype:
            kwargs['subtype'] = self._subtype

        kwargs['pinlabels'] = self._pin_numbers
        kwargs['pincount'] = len(self._pin_numbers)
        # The original code had a bug here. It was using pin_numbers for pinlabels
        # and not using pinout at all. I will fix this.
        kwargs['pins'] = self._pin_numbers
        kwargs['pinlabels'] = self._pinout

        return kwargs

class AddCableDialogLogic:
    def __init__(self, name, manuf, mpn, ipm, type, gauge, gauge_unit, length, shield, colors):
        self._name = name
        self._manuf = manuf
        self._mpn = mpn
        self._ipm = ipm
        self._type = type
        self._gauge = gauge
        self._gauge_unit = gauge_unit
        self._length = length
        self._shield = shield
        self._colors = colors

    def get_kwargs(self):
        kwargs = {}
        if self._manuf:
            kwargs['manufacturer'] = self._manuf
        if self._mpn:
            kwargs['manufacturer_part_number'] = self._mpn
        if self._ipm:
            kwargs['internal_part_number'] = self._ipm
        if self._type:
            kwargs['type'] = self._type
        if self._gauge:
            try:
                kwargs['gauge'] = int(self._gauge)
            except ValueError:
                kwargs['gauge'] = float(self._gauge)
        if self._gauge_unit:
            kwargs['gauge_unit'] = self._gauge_unit
        if self._length:
            kwargs['length'] = float(self._length)

        kwargs['shield'] = self._shield
        kwargs['colors'] = self._colors

        return kwargs

class AddConnectionDialogLogic:
    def __init__(self, from_name, from_pin, via_name, via_wire, to_name, to_pin):
        self._from_name = from_name
        self._from_pin = from_pin
        self._via_name = via_name
        self._via_wire = via_wire
        self._to_name = to_name
        self._to_pin = to_pin

    def get_data(self):
        data = {
            'from_name': self._from_name,
            'via_name': self._via_name,
            'to_name': self._to_name
        }
        try:
            data['from_pin'] = int(self._from_pin)
        except ValueError:
            data['from_pin'] = self._from_pin
        try:
            data['via_wire'] = int(self._via_wire)
        except ValueError:
            data['via_wire'] = self._via_wire
        try:
            data['to_pin'] = int(self._to_pin)
        except ValueError:
            data['to_pin'] = self._to_pin

        return data

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

class MetadataDialogLogic:
    def __init__(self, title, author, version, date, custom_metadata_text):
        self._title = title
        self._author = author
        self._version = version
        self._date = date
        self._custom_metadata_text = custom_metadata_text

    def get_metadata(self):
        metadata = {}
        if self._title:
            metadata['title'] = self._title
        if self._author:
            metadata['author'] = self._author
        if self._version:
            metadata['version'] = self._version
        if self._date:
            metadata['date'] = self._date

        if self._custom_metadata_text.strip():
            import yaml
            try:
                custom_metadata = yaml.safe_load(self._custom_metadata_text)
                if isinstance(custom_metadata, dict):
                    metadata.update(custom_metadata)
                else:
                    raise ValueError('Custom metadata must be a valid YAML dictionary.')
            except yaml.YAMLError as e:
                raise ValueError(f'Invalid YAML in custom metadata: {e}')

        return metadata


class AddMateDialogLogic:
    def __init__(self, from_connector, to_connector, arrow_direction):
        self._from_connector = from_connector
        self._to_connector = to_connector
        self._arrow_direction = arrow_direction

    def get_yaml_snippet(self):
        if not self._from_connector or not self._to_connector:
            return None

        return f"""
- - {self._from_connector}
  - {self._arrow_direction}
  - {self._to_connector}
"""
