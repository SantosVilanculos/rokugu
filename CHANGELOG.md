# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Now you can set and get and text elide mode to `ElidedText` widget.
  widget for setting and getting the text elide mode and.
- Now you can get the current icon size, get and set the prefered aspect ratio mode on the `IconButton` widget.

### Changed

- `IconButton` load method now returns a boolean.

## [0.0.3] - 2025-03-19

- No Changes

## [0.0.2] - 2025-03-19

### Added

- Enabled focus events for `IconButton` and disabled mouse events propagation.
- Enabled tab key navigation for `ListWidget`.
- Added `ElidedText` widget for displaying elided text.

### Changed

- `Router` API Renamed:
  - `append` renamed to `add`.
  - `initial_name` parameter renamed to `default`.
  - `widget_appended` signal renamed to `widget_added`.
- `Listing` Widget Refactored and Renamed:
  - Renamed to `ListWidget`.
  - Exposed only `select` and `remove` functions.
  - Removed item insertion and filtering methods.
  - `changed` event now passes a generic object instead of `QItemWidgetItem`.

### Removed

- Removed `bundle_path` method from support module due to its specific relation
  to PyInstaller.
- Removed `Label` widget.

### Fixed

- `IconButton`: Corrected import of `Widget`. The widget was previously
  importing a non-existent `Widget`. Now it imports correctly from its own
  package.

## [0.0.1] - 2025-03-17

### Added

- Initial Release - No Changes

## [0.0.0] - 2025-03-17

### Added

- **Core Utilities:**
  - `OS` class: Provides basic operating system helper functions.
  - Path helpers: Functions for retrieving the bundle path and standard paths.
  - `file_size`: Function that calculates the file size in appropriate units
    (bytes, KB, MB, GB, etc.) and returns it as a human-readable string based
    on the provided byte size.
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

[unreleased]: https://github.com/rokugu/rokugu/compare/v0.0.3...HEAD
[0.0.2]: https://github.com/rokugu/rokugu/releases/tag/v0.0.2...v0.0.3
[0.0.1]: https://github.com/rokugu/rokugu/releases/tag/v0.0.0...v0.0.1
[0.0.0]: https://github.com/rokugu/rokugu/releases/tag/v0.0.0
