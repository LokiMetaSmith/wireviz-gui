# Purpose

To provide an easy-to-use graphical interface for [wireviz](https://github.com/formatc1702/WireViz).

# Screenshot

Note: The UI has been updated since this screenshot was taken, but the core functionality remains the same.

![screenshot](/docs/screenshots/screenshot.png)

# Motivation

The graphics generated using `wireviz` are quite good with minimum effort, but it is a command-line tool. This GUI aims to make `wireviz` accessible to those who are less comfortable with the command line.

# Features

- Real-time preview of the wire harness diagram as you type.
- YAML syntax highlighting.
- Export diagrams to PNG and SVG.
- **New**: Export Bill of Materials (BOM) to a CSV file compatible with [Homebox](https://github.com/hay-kot/homebox).

# Pre-Requisites

## Install `graphviz`

Before using `wireviz-gui`, you need to install `graphviz`. Head over to the [graphviz download page](https://graphviz.org/download/) and install a version that suits your system.

**Important**: Make sure the `graphviz` executable directory is in your system's `PATH` environment variable. You may need to restart your system after this step.

# Installation

The easiest way to install `wireviz-gui` is using `pip`.

1.  **Create and Activate a Virtual Environment** (Recommended)
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate.bat
    # On macOS/Linux
    source venv/bin/activate
    ```

2.  **Install `wireviz-gui`**
    This will also install `wireviz` and other dependencies.
    ```bash
    pip install wireviz-gui
    ```
    Or, for the latest development version, you can install directly from this repository:
    ```bash
    pip install git+https://github.com/slightlynybbled/wireviz-gui.git
    ```

# Execution

To run the GUI after installation:

    wireviz-gui

Or, if you have cloned the repository and are running from the source directory:

    python -m wireviz_gui
