import pytest
from wireviz_gui.settings_dialog_logic import SettingsDialogLogic
from wireviz_gui.mating_dialog_logic import AddMateDialogLogic

def test_settings_dialog_logic():
    logic = SettingsDialogLogic(
        bgcolor='BK',
        bgcolor_node='',
        bgcolor_connector='',
        bgcolor_cable='',
        bgcolor_bundle='',
        color_mode='HEX',
        fontname='monospace',
        mini_bom_mode=True,
        template_separator=':'
    )
    options = logic.get_options()

    assert options['bgcolor'] == 'BK'
    assert options['color_mode'] == 'HEX'
    assert options['fontname'] == 'monospace'
    assert options['mini_bom_mode'] is True
    assert options['template_separator'] == ':'
    assert 'bgcolor_node' not in options

def test_mating_dialog_logic():
    logic = AddMateDialogLogic(
        from_connector='X1',
        to_connector='X2',
        arrow_direction='==>'
    )
    yaml_snippet = logic.get_yaml_snippet()

    expected_snippet = """
- - X1
  - ==>
  - X2
"""
    assert yaml_snippet.strip() == expected_snippet.strip()

def test_mating_dialog_logic_no_connectors():
    logic = AddMateDialogLogic(
        from_connector='',
        to_connector='X2',
        arrow_direction='==>'
    )
    yaml_snippet = logic.get_yaml_snippet()
    assert yaml_snippet is None
