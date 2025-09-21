# Agent Instructions

This document provides instructions for agents working on the `wireviz-gui` repository.

## Project Overview

The purpose of this project is to provide a user-friendly graphical interface for the `wireviz` library. The application is built using Python and the Tkinter library.

## Development Environment

To set up the development environment, follow these steps:

1.  Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

To run the application, use the following command:
```bash
python -m wireviz_gui
```

## Keeping in Sync with `wireviz`

It is important to keep the GUI in sync with the latest version of the `wireviz` library. Before implementing any new features, please review the `wireviz` documentation and source code to ensure that the feature is implemented correctly.

## To-Do List

For a list of potential tasks and future improvements, please see the `todo.md` file.
