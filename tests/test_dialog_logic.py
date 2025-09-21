import pytest
from wireviz_gui.dialog_logic import CustomColorSchemesDialogLogic

def test_custom_color_schemes_dialog_logic():
    logic = CustomColorSchemesDialogLogic(
        color_schemes_text='''
my_scheme:
  BK: '#000000'
  RD: '#FF0000'
'''
    )
    color_schemes = logic.get_color_schemes()
    assert color_schemes['my_scheme']['BK'] == '#000000'

def test_custom_color_schemes_dialog_logic_invalid_yaml():
    with pytest.raises(ValueError):
        logic = CustomColorSchemesDialogLogic(
            color_schemes_text='not: yaml:'
        )
        logic.get_color_schemes()

def test_custom_color_schemes_dialog_logic_not_a_dict():
    with pytest.raises(ValueError):
        logic = CustomColorSchemesDialogLogic(
            color_schemes_text='- item1\\n- item2'
        )
        logic.get_color_schemes()
