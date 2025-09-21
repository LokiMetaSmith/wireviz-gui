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
