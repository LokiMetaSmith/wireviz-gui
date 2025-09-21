import pytest
from wireviz_gui.dialog_logic import (
    AddConnectorDialogLogic,
    AddCableDialogLogic,
    AddConnectionDialogLogic,
    SettingsDialogLogic,
    MetadataDialogLogic,
    AddMateDialogLogic,
)

def test_add_connector_dialog_logic():
    logic = AddConnectorDialogLogic(
        name='X1',
        manuf='Molex',
        mpn='1234',
        ipm='5678',
        type='KK',
        subtype='254',
        pin_numbers=[1, 2, 3],
        pinout=['GND', 'VCC', 'SIG']
    )
    kwargs = logic.get_kwargs()
    assert kwargs['manufacturer'] == 'Molex'
    assert kwargs['pins'] == [1, 2, 3]
    assert kwargs['pinlabels'] == ['GND', 'VCC', 'SIG']

def test_add_cable_dialog_logic():
    logic = AddCableDialogLogic(
        name='W1',
        manuf='Alpha Wire',
        mpn='9059C',
        ipm='1234',
        type='22AWG',
        gauge='22',
        gauge_unit='AWG',
        length='1.5',
        shield=True,
        colors=['BK', 'RD', 'WH']
    )
    kwargs = logic.get_kwargs()
    assert kwargs['gauge'] == 22
    assert kwargs['length'] == 1.5
    assert kwargs['shield'] is True
    assert kwargs['colors'] == ['BK', 'RD', 'WH']

def test_add_connection_dialog_logic():
    logic = AddConnectionDialogLogic(
        from_name='X1',
        from_pin='1',
        via_name='W1',
        via_wire='1',
        to_name='X2',
        to_pin='A'
    )
    data = logic.get_data()
    assert data['from_name'] == 'X1'
    assert data['from_pin'] == 1
    assert data['to_pin'] == 'A'

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
    assert 'bgcolor_node' not in options

def test_metadata_dialog_logic():
    logic = MetadataDialogLogic(
        title='My Harness',
        author='Jules',
        version='1.0',
        date='2025-09-21',
        custom_metadata_text='''
extra:
  key: value
'''
    )
    metadata = logic.get_metadata()
    assert metadata['title'] == 'My Harness'
    assert metadata['extra']['key'] == 'value'

def test_add_mate_dialog_logic():
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
