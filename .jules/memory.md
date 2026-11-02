## Archived: 2026-11-02

* The `wireviz` library's `Cable` class does not support the `label` keyword argument; `wireviz-gui` works around this by moving user-provided labels to the `notes` field.
* Prioritize forward compatibility with newer library versions (e.g., `wireviz`) rather than just the currently installed version.
* The file `tests/test_dialog_integration.py` contains integration tests for dialog classes (e.g., `AddConnectorFrame`), utilizing `unittest.mock` to patch `tkinter` components for headless testing.
* To support metadata editing (including key deletion), `InputOutputFrame` uses a `_replace_yaml_section` method that fully replaces the target YAML section, unlike the merge-based `_update_yaml_section` used for additions.
* `AddMateDialog` returns a Python list `[from_connector, arrow_direction, to_connector]` (e.g., `['X1', '<=>', 'X2']`) for appending to the `connections` section of the YAML.
* File menu commands (Save, Export, Reload) delegate to the currently active tab (`InputOutputFrame`), except for 'New' (Ctrl+N), which invokes `Application.add_tab()` directly.
* The `wireviz_gui/version.py` module uses `importlib.metadata.version` but includes a fallback for `PackageNotFoundError` (returning `0.0.0+dev`) to support running the application from source without package installation.
* The `wireviz_gui` application architecture uses a `ttk.Notebook` to manage multiple `InputOutputFrame` instances, enabling a tabbed interface where each tab acts as an independent file editor with its own state.
* The project uses `tk-tools` for specific GUI components (e.g., `ToolTip`).
* The `HarnessViewFrame` renders diagrams on a `tk.Canvas` instead of a `tk.Label` to enable scrolling, panning, and zooming.
* Thicker AWG sizes (e.g., 1/0, 2/0, 3/0, 4/0) are missing from standard `wireviz` helper tables and must be manually appended to UI lists for user selection.
* The `wireviz` library does not natively support integers in connection lists; they must be converted to dictionaries (e.g., `[{'Component': Pin}]`).
* Unit testing `wireviz_gui` components requires a custom mock class for `tkinter.Frame` (simulating methods like `grid`, `pack`, `winfo_children`) instead of `MagicMock` to correctly support inheritance and instantiation logic.
* The `wireviz-gui` application utilizes a `preprocess_yaml_data` function (aliased as `normalize_connections`) to sanitize input data. It transforms nested connection structures, converts `Connector.Pin` strings to `{Connector: Pin}` dictionaries to prevent redefinition errors, and moves unsupported `label` attributes from cables to `notes`.
* The project uses `pyproject.toml` and `uv.lock` for configuration and dependency locking; no `requirements.txt` exists.
* The application triggers a `QSqlDatabasePrivate::addDatabase` duplicate connection warning on startup, likely due to external dependencies (e.g., Graphviz, system Qt); this is currently treated as a known, benign issue.
* The `wireviz.parse` function can validate YAML input without generating output files by setting `return_types=('harness',)`.
* When unit testing components inheriting from `BaseFrame` (defined in `wireviz_gui._base`), `wireviz_gui._base.Frame` must be patched directly to prevent `tkinter` instantiation, as `BaseFrame` imports `Frame` explicitly.
* The application menu structure includes an 'Edit' menu (containing 'Metadata') inserted between the 'File' and 'Help' menus.
* Unit testing `tkinter` menus (checking structure and callbacks) in a headless environment requires patching `sys.modules['tkinter']` with a custom `FakeTkModule` containing a `FakeMenu` class to record `add_command` and `add_cascade` calls, as standard `MagicMock` usage often fails with inheritance.
* In `wireviz` connection lists, string entries with dots (e.g., `A.B`) are parsed as `Template.Instance` definitions. To reference a pin on an existing component, the format `{Component: Pin}` must be used instead of dot notation to avoid redefinition errors.
* The `Graphviz executable not found` error indicates the system-level `dot` binary is missing from the system PATH, separate from the Python `graphviz` package.
* The `EditMetadataDialog` in `wireviz_gui.dialogs` enables editing of harness metadata by dynamically managing a list of key-value entry widgets.
* The `wireviz` library supports string values for wire gauges (e.g., "4/0 AWG"); the GUI input handling must accept strings if numeric conversion fails.
* The `InputOutputFrame` utilizes a `ttk.PanedWindow` to vertically split the `TextEntryFrame` and `HarnessViewFrame`, replacing the previous grid layout to allow resizing.
* The `wireviz` library requires `POS` and `NEG` to be explicitly defined as cables if used as connection components; they are not default global identifiers.
* To persist additions of connectors, cables, or connections, the application directly parses the YAML from the text editor, updates the data structure using a helper method `_update_yaml_section`, and dumps it back, rather than relying on the internal `Harness` object state.
* Project execution command: `python -m wireviz_gui`.
* Dialog classes (`AddConnectorFrame`, `AddCableFrame`, `AddConnectionFrame`) must return component data as dictionaries or lists to `app.py` via callbacks, allowing the main application to serialize them into the YAML.
* A library of example wiring diagrams (Demo 01-02, Ex 01-14) is stored in `wireviz_gui/examples.py` and accessible via an 'Examples' submenu that opens selected diagrams in new tabs.
* Running tests in a headless environment for `wireviz_gui` requires patching `tkinter` modules. Specifically, `tk.BooleanVar`, `tk.StringVar`, and `tk.IntVar` require a mocked `tk.Tk` instance (root) to be active or passed as master to avoid instantiation errors.
* Color mappings for the GUI are sourced from `wireviz.wv_colors._color_full`, which maps color codes (e.g., 'BK') to full names (e.g., 'black').
* The `wireviz` library expects connection entries to be flat lists following the sequence `[Component, Cable, Component]` and may fail if nested dictionary structures are passed directly.
* Zoom functionality in `HarnessViewFrame` is implemented by resizing the underlying PIL Image object using `Image.Resampling.LANCZOS` (or `Image.LANCZOS`) and updating the canvas.
* The `wireviz` library's `Harness` object (specifically version 0.4.1) does not have a `connections` attribute; attempts to access it will raise an `AttributeError`.
* The `wireviz` library's `Connector` and `Cable` objects use the attributes `mpn` and `pn` for Manufacturer and Internal Part Numbers; accessing `manufacturer_part_number` or `internal_part_number` raises an `AttributeError`.
* The `HarnessViewFrame` caches the currently rendered graph as a PIL Image in `self._image`, allowing export via `self._image.save()`.
* The `wireviz-gui` project depends on `wireviz>=0.4.1` and explicitly lists `graphviz` in `pyproject.toml`.
* The `wireviz.wireviz.Harness` class requires `metadata`, `options`, and `tweak` arguments for instantiation (e.g., `Harness(Metadata(), Options(), Tweak())`).
* The project has a flat layout with multiple top-level packages (`wireviz_gui`, `images`), preventing standard `pip install .` without explicit `setuptools` configuration adjustments.
* Always engage in 'deep planning mode' before changes: ask clarifying questions to ensure absolute certainty of requirements before creating a plan.
* The `wireviz.wv_helper` module provides `awg_equiv_table` and `mm2_equiv_table` for unit conversion, which are used to populate gauge selection lists in the GUI.
