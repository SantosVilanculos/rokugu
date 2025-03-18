# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- `IconButton`: disabled mouse events propagation and enabled focus events
- `ListWidget` enable tab key navigation

### Changed

- `Router` rename append method, initial_name parametter and widget_appended signal
  1. append -> add
  2. initial_name -> default
  3. widget_appended -> widget_added
- `Listing`:
  1. renamed to `ListWidget`
     only expose select and remove functions
  2. Remove item insertion and filtering methods
  3. `changed` event not only passes a QItemWidgetItem object

### Fixed

- `IconButton`: import Widget from internall package

### Removed

- Remove bundle_path method from support module. The removal is because the method is related to pyinstaller and not all
  that may use this library will use it

## [0.0.1] - 2025-03-17

## [0.0.0] - 2025-03-17

### Added

- **Core Utilities:**
  - `OS` class: Provides basic operating system helper functions.
  - Path helpers: Functions for retrieving the bundle path and standard paths.
  - `file_size`: Function that calculates the file size in appropriate units (bytes, KB, MB, GB, etc.) and returns it as a human-readable string based on the provided byte size.
- **UI Components:**
  - `IconButton`: A button with an icon.
  - `ImageBackground`: A component for displaying an image as a background.
  - `Label`: A text display component.
  - `Popup`: A component for displaying modal or transient content.
  - `Router`: A component for managing application navigation.
  - `Widget`: A base class for UI components.
  - `Window`: A top-level application window component.
- **Layouts:**
  - `AutoLayout`: Automatically arranges child components.
  - `FlowLayout`: Arranges child components in a flow-like manner.

[unreleased]: https://github.com/santosvilanculos/rokugu/compare/v0.0.1...HEAD
[0.0.1]: https://github.com/santosvilanculos/rokugu/releases/tag/v0.0.0...v0.0.1
[0.0.0]: https://github.com/santosvilanculos/rokugu/releases/tag/v0.0.0
