# WireViz GUI - To-Do List

This file tracks potential improvements and new features for the `wireviz-gui` application.

## High Priority
- [ ] **Update Documentation**: The `README.md` and any other user-facing documentation need to be updated to reflect the current state of the application.
- [ ] **Implement Custom Color Schemes**: Add a feature to define and use custom color schemes, as supported by `wireviz` v0.3+. This involves adding a new dialog and updating the YAML generation.
- [ ] **Implement Connector Mating**: Add support for defining mates between connectors, a feature introduced in `wireviz` v0.4. This will likely require a new dialog for managing mates.

## Medium Priority
- [ ] **Add Harness Metadata Dialog**: `wireviz` v0.3+ supports a `metadata` section in the YAML for title, author, date, etc. A new dialog should be added to manage this information.
- [ ] **Enhance Component Dialogs**: The "Add Connector" and "Add Cable" dialogs should be updated to support more attributes from `wireviz`, such as:
    - Supplier and Supplier Part Number (SPN).
    - Saving and loading pin names (`pinout`).
    - Length units for cables.
- [ ] **Improve Error Handling**: Provide more specific and helpful error messages to the user, especially for YAML parsing errors.

## Low Priority / Code Quality
- [ ] **Refactor UI and Logic**: The application logic is currently tightly coupled with the `tkinter` UI code. Refactor this to separate concerns, making the code easier to maintain and test.
- [ ] **Increase Test Coverage**: Add more unit tests for the application logic and UI components to improve stability and prevent regressions.
- [ ] **Support Graph Rendering Options**: Expose `wireviz` rendering options (e.g., background colors, fonts) to the user through a settings dialog.
- [ ] **Support Image Embedding**: Allow users to specify images to be embedded in the SVG output, as supported by `wireviz` v0.4.
