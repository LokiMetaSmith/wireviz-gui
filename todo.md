# Wireviz GUI - To-Do List

This document outlines the necessary updates to the `wireviz-gui` project to make it compatible with the latest version of `wireviz` and to improve its functionality.

## Documentation Updates

- [x] **Update `README.md`:**
    - [x] Change the `wireviz` installation instructions from manual git clone to `pip install wireviz`.
    - [x] Update the URL for the `wireviz` repository to `https://github.com/wireviz/WireViz`.
    - [x] Review and update any other outdated information.

## Code Updates

- [x] **Update `requirements.txt`:**
    - [x] Add `wireviz` to the requirements file, specifying a recent version.
    - [x] Ensure all other dependencies are up to date.

- [x] **Update `wireviz` Integration:**
    - [x] **Imports:** Update the `import` statements in `wireviz_gui/app.py` and other files to match the new `wireviz` package structure.
    - [x] **`parse` function:** Update the call to the `parse` function to match the new API, including any changes to its arguments and return value.
    - [x] **`Harness` object:**
        - Update the code to use the new method for generating output files instead of the old `Harness.output()` method.
        - Find the new way to get the rendered PNG image data for display in the GUI, replacing the access to the `Harness.png` attribute.
    - [x] **Error Handling:** Update the error handling to catch the new exceptions that may be raised by the latest `wireviz` library.

- [x] **GUI Functionality:**
    - [x] **YAML Generation:** Review and update the dialogs for adding connectors, cables, and connections to generate YAML that is compatible with the latest `wireviz` syntax.
    - [x] **Enable Dialogs:** Re-enable the GUI buttons for adding connectors, cables, and connections after the underlying functionality is fixed.

## Potential New Features

- [ ] **Expose New `wireviz` Features:**
    - [ ] Add GUI elements to allow users to take advantage of new `wireviz` features, such as:
        - [x] Connector mating
        - Improved technical drawings
        - [x] Harness metadata
        - [x] Part numbers and supplier information
        - Custom color schemes

- [ ] **Improve User Experience:**
    - [ ] Provide better error messages and feedback to the user.
    - [ ] Add a settings dialog to configure `wireviz` rendering options.
    - [ ] Improve the layout and design of the GUI.
