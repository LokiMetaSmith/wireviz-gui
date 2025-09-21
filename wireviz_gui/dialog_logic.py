class CustomColorSchemesDialogLogic:
    def __init__(self, color_schemes_text):
        self._color_schemes_text = color_schemes_text

    def get_color_schemes(self):
        if not self._color_schemes_text.strip():
            return {}

        import yaml
        try:
            color_schemes = yaml.safe_load(self._color_schemes_text)
            if not isinstance(color_schemes, dict):
                raise ValueError('Color schemes must be a valid YAML dictionary.')
            return color_schemes
        except yaml.YAMLError as e:
            raise ValueError(f'Invalid YAML in color schemes: {e}')
