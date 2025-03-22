# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

- No changes yet.

## [0.0.4] - 2025-03-23

### Added

- Added an example application to demonstrate the usage of the library.
- Added the ability to set and get the text elide mode for the `ElidedText` widget.
- Added the ability to get the current icon size and set the preferred aspect ratio mode on the `IconButton` widget.

### Changed

- The `IconButton.load()` method now returns a boolean value.

## [0.0.3] - 2025-03-19

### Added

- No changes.

## [0.0.2] - 2025-03-19

### Added

- Enabled focus events for the `IconButton` and disabled mouse event propagation.
- Enabled tab key navigation for the `ListWidget`.
- Added the `ElidedText` widget for displaying elided text.

### Changed

- **Router API:**
  - Renamed `append` to `add`.
  - Renamed the `initial_name` parameter to `default`.
  - Renamed the `widget_appended` signal to `widget_added`.
- **`Listing` Widget:**
  - Refactored and renamed to `ListWidget`.
  - Exposed only the `select` and `remove` functions.
  - Removed item insertion and filtering methods.
  - The `changed` event now passes a generic object instead of `QItemWidgetItem`.

### Removed

- Removed the `bundle_path` method from the support module because it is specific to PyInstaller.
- Removed the `Label` widget.

### Fixed

- **`IconButton`:** Corrected the import of `Widget`. The widget was previously importing a non-existent `Widget`. It now imports correctly from its own package.

## [0.0.1] - 2025-03-17

### Added

- Initial Release - No changes.

## [0.0.0] - 2025-03-17

### Added

- **Core Utilities:**
  - Added the `OS` class, providing basic operating system helper functions.
  - Added path helper functions for retrieving the bundle path and standard paths.
  - Added the `file_size` function to calculate the file size in appropriate units (bytes, KB, MB, GB, etc.) and return it as a human-readable string based on the provided byte size.
- **UI Components:**
  - Added the `IconButton` widget: A button with an icon.
  - Added the `ImageBackground` widget: A component for displaying an image as a background.
  - Added the `Label` widget: A text display component.
  - Added the `Popup` widget: A component for displaying modal or transient content.
  - Added the `Router` widget: A component for managing application navigation.
  - Added the `Widget` class: A base class for UI components.
  - Added the `Window` widget: A top-level application window component.
- **Layouts:**
  - Added the `AutoLayout` widget: Automatically arranges child components.
  - Added the `FlowLayout` widget: Arranges child components in a flow-like manner.

[unreleased]: https://github.com/rokugu/rokugu/compare/v0.0.4...HEAD
[0.0.4]: https://github.com/rokugu/rokugu/compare/tag/v0.0.3...v0.0.4
[0.0.3]: https://github.com/rokugu/rokugu/compare/tag/v0.0.2...v0.0.3
[0.0.2]: https://github.com/rokugu/rokugu/compare/tag/v0.0.1...v0.0.2
[0.0.1]: https://github.com/rokugu/rokugu/compare/tag/v0.0.0...v0.0.1
[0.0.0]: https://github.com/rokugu/rokugu/releases/tag/v0.0.0
