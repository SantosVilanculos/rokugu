from PySide6.QtCore import QXmlStreamReader, Slot
from PySide6.QtGui import QClipboard, QShowEvent, Qt
from PySide6.QtWidgets import (
    QFileDialog,
    QHBoxLayout,
    QPushButton,
    QScrollArea,
    QSlider,
    QVBoxLayout,
    QWidget,
)

from rokugu import SvgWidget


class SvgWidgetExample(QWidget):
    def __init__(self) -> None:
        super().__init__()

        q_h_box_layout = QVBoxLayout(self)
        q_h_box_layout.setContentsMargins(0, 0, 0, 0)
        q_h_box_layout.setSpacing(0)

        q_scroll_area = QScrollArea()
        self._q_widget = SvgWidget(
            QXmlStreamReader(
                """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 113.02 28.1942764712217" width="2500" height="624"><path fill="#ff2d20" d="M4.44 0v23.05h8.34v3.97H0V0h4.44zm24 11.46V9.03h4.22v18h-4.2v-2.44c-.58.9-1.38 1.6-2.42 2.1-1.04.53-2.1.78-3.15.78-1.37 0-2.62-.25-3.75-.75a8.76 8.76 0 0 1-2.92-2.06 9.6 9.6 0 0 1-1.9-3 9.72 9.72 0 0 1-.67-3.64c0-1.26.23-2.47.68-3.6a9.56 9.56 0 0 1 1.9-3.04 8.77 8.77 0 0 1 2.9-2.08c1.14-.5 2.4-.75 3.75-.75 1.05 0 2.1.26 3.14.77 1.04.52 1.84 1.22 2.4 2.12zm-.38 8.77a6.3 6.3 0 0 0 .4-2.2c0-.78-.14-1.5-.4-2.2A5.58 5.58 0 0 0 26.98 14a5.23 5.23 0 0 0-1.68-1.22 5.16 5.16 0 0 0-2.18-.47c-.8 0-1.52.17-2.16.48A5.3 5.3 0 0 0 19.3 14a5.3 5.3 0 0 0-1.06 1.83 6.56 6.56 0 0 0-.37 2.2c0 .77.12 1.5.37 2.2.24.7.6 1.3 1.06 1.8a5.28 5.28 0 0 0 1.66 1.25c.64.3 1.36.46 2.16.46s1.53-.15 2.18-.46a5.22 5.22 0 0 0 1.68-1.24 5.58 5.58 0 0 0 1.08-1.8zm7.92 6.8v-18H47.4v4.14h-7.22v13.85h-4.2zm26.67-15.57V9.03h4.2v18h-4.2v-2.44c-.56.9-1.37 1.6-2.4 2.1-1.05.53-2.1.78-3.16.78-1.37 0-2.62-.25-3.75-.75a8.76 8.76 0 0 1-2.92-2.06 9.6 9.6 0 0 1-1.9-3 9.72 9.72 0 0 1-.66-3.64c0-1.26.22-2.47.67-3.6a9.56 9.56 0 0 1 1.9-3.04 8.77 8.77 0 0 1 2.9-2.08c1.14-.5 2.4-.75 3.75-.75 1.05 0 2.1.26 3.14.77 1.04.52 1.85 1.22 2.4 2.12zm-.38 8.77a6.3 6.3 0 0 0 .38-2.2c0-.78-.13-1.5-.38-2.2A5.58 5.58 0 0 0 61.2 14a5.23 5.23 0 0 0-1.7-1.22c-.65-.3-1.38-.47-2.17-.47-.8 0-1.52.17-2.17.48A5.3 5.3 0 0 0 53.5 14a5.3 5.3 0 0 0-1.06 1.83 6.56 6.56 0 0 0-.36 2.2c0 .77.12 1.5.36 2.2.25.7.6 1.3 1.06 1.8a5.28 5.28 0 0 0 1.66 1.25c.65.3 1.37.46 2.17.46.8 0 1.52-.15 2.18-.46a5.22 5.22 0 0 0 1.7-1.24 5.58 5.58 0 0 0 1.07-1.8zm21.46-11.2H88l-6.9 18h-5.3l-6.9-18h4.25l5.3 13.78 5.28-13.77zm13.44-.46c5.73 0 9.64 5.08 8.9 11.02H92.1c0 1.54 1.58 4.54 5.3 4.54 3.2 0 5.35-2.8 5.35-2.8l2.84 2.2c-2.55 2.7-4.63 3.95-7.9 3.95-5.82 0-9.76-3.7-9.76-9.47 0-5.23 4.08-9.46 9.23-9.46zm-5.05 7.9h10.1c-.04-.35-.6-4.56-5.08-4.56-4.5 0-4.98 4.22-5.02 4.56zM108.82 27V0h4.2v27.02h-4.2z"/></svg>
        """
            )
        )
        pw = QWidget()
        phbl = QHBoxLayout(pw)
        phbl.setContentsMargins(0, 0, 0, 0)
        phbl.setSpacing(0)
        phbl.addWidget(self._q_widget)
        q_scroll_area.setWidget(pw)
        q_scroll_area.setWidgetResizable(True)
        q_h_box_layout.addWidget(q_scroll_area, stretch=1)

        self.q_slider = QSlider()
        self.q_slider.setFixedHeight(36)
        self.q_slider.setOrientation(Qt.Orientation.Horizontal)
        self.q_slider.setMaximum(1_000)
        self.q_slider.setValue(24)
        self.q_slider.valueChanged.connect(self._value_changed)
        q_h_box_layout.addWidget(self.q_slider)
        self.q_file_dialog = QFileDialog(self)
        self.q_file_dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptOpen)
        self.q_file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        self.q_file_dialog.setMimeTypeFilters(["image/svg+xml"])
        self.q_file_dialog.fileSelected.connect(self._file_selected)
        q_push_button = QPushButton("Upload svg")
        q_push_button.setFixedHeight(36)
        q_push_button.pressed.connect(self.q_file_dialog.open)
        q_h_box_layout.addWidget(q_push_button)
        q_push_button2 = QPushButton("Paste svg code")
        q_push_button2.setFixedHeight(36)
        q_push_button2.pressed.connect(self._pressed)
        q_h_box_layout.addWidget(q_push_button2)
        q_push_button3 = QPushButton("Reset")
        q_push_button3.setFixedHeight(36)
        q_push_button3.pressed.connect(self._reset)
        q_h_box_layout.addWidget(q_push_button3)

    @Slot(str)
    def _file_selected(self, q_string: str) -> None:
        print(q_string)
        self._q_widget.load(q_string)

    @Slot()
    def _pressed(self) -> None:
        q_clipboard = QClipboard()
        q_clipboard.text()
        q_xml_stream_reader = QXmlStreamReader(q_clipboard.text())
        self._q_widget.load(q_xml_stream_reader)

    def showEvent(self, event: QShowEvent, /) -> None:
        self.q_slider.setValue(self._q_widget.width())
        return super().showEvent(event)

    @Slot(int)
    def _value_changed(self, value: int):
        self._q_widget.setFixedSize(value, value)

    @Slot()
    def _reset(self):
        self._q_widget.load(
            QXmlStreamReader(
                """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 113.02 28.1942764712217" width="2500" height="624"><path fill="#ff2d20" d="M4.44 0v23.05h8.34v3.97H0V0h4.44zm24 11.46V9.03h4.22v18h-4.2v-2.44c-.58.9-1.38 1.6-2.42 2.1-1.04.53-2.1.78-3.15.78-1.37 0-2.62-.25-3.75-.75a8.76 8.76 0 0 1-2.92-2.06 9.6 9.6 0 0 1-1.9-3 9.72 9.72 0 0 1-.67-3.64c0-1.26.23-2.47.68-3.6a9.56 9.56 0 0 1 1.9-3.04 8.77 8.77 0 0 1 2.9-2.08c1.14-.5 2.4-.75 3.75-.75 1.05 0 2.1.26 3.14.77 1.04.52 1.84 1.22 2.4 2.12zm-.38 8.77a6.3 6.3 0 0 0 .4-2.2c0-.78-.14-1.5-.4-2.2A5.58 5.58 0 0 0 26.98 14a5.23 5.23 0 0 0-1.68-1.22 5.16 5.16 0 0 0-2.18-.47c-.8 0-1.52.17-2.16.48A5.3 5.3 0 0 0 19.3 14a5.3 5.3 0 0 0-1.06 1.83 6.56 6.56 0 0 0-.37 2.2c0 .77.12 1.5.37 2.2.24.7.6 1.3 1.06 1.8a5.28 5.28 0 0 0 1.66 1.25c.64.3 1.36.46 2.16.46s1.53-.15 2.18-.46a5.22 5.22 0 0 0 1.68-1.24 5.58 5.58 0 0 0 1.08-1.8zm7.92 6.8v-18H47.4v4.14h-7.22v13.85h-4.2zm26.67-15.57V9.03h4.2v18h-4.2v-2.44c-.56.9-1.37 1.6-2.4 2.1-1.05.53-2.1.78-3.16.78-1.37 0-2.62-.25-3.75-.75a8.76 8.76 0 0 1-2.92-2.06 9.6 9.6 0 0 1-1.9-3 9.72 9.72 0 0 1-.66-3.64c0-1.26.22-2.47.67-3.6a9.56 9.56 0 0 1 1.9-3.04 8.77 8.77 0 0 1 2.9-2.08c1.14-.5 2.4-.75 3.75-.75 1.05 0 2.1.26 3.14.77 1.04.52 1.85 1.22 2.4 2.12zm-.38 8.77a6.3 6.3 0 0 0 .38-2.2c0-.78-.13-1.5-.38-2.2A5.58 5.58 0 0 0 61.2 14a5.23 5.23 0 0 0-1.7-1.22c-.65-.3-1.38-.47-2.17-.47-.8 0-1.52.17-2.17.48A5.3 5.3 0 0 0 53.5 14a5.3 5.3 0 0 0-1.06 1.83 6.56 6.56 0 0 0-.36 2.2c0 .77.12 1.5.36 2.2.25.7.6 1.3 1.06 1.8a5.28 5.28 0 0 0 1.66 1.25c.65.3 1.37.46 2.17.46.8 0 1.52-.15 2.18-.46a5.22 5.22 0 0 0 1.7-1.24 5.58 5.58 0 0 0 1.07-1.8zm21.46-11.2H88l-6.9 18h-5.3l-6.9-18h4.25l5.3 13.78 5.28-13.77zm13.44-.46c5.73 0 9.64 5.08 8.9 11.02H92.1c0 1.54 1.58 4.54 5.3 4.54 3.2 0 5.35-2.8 5.35-2.8l2.84 2.2c-2.55 2.7-4.63 3.95-7.9 3.95-5.82 0-9.76-3.7-9.76-9.47 0-5.23 4.08-9.46 9.23-9.46zm-5.05 7.9h10.1c-.04-.35-.6-4.56-5.08-4.56-4.5 0-4.98 4.22-5.02 4.56zM108.82 27V0h4.2v27.02h-4.2z"/></svg>
        """
            )
        )
