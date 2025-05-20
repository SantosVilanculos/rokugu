from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QWidget,
)


class Playground(QWidget):
    def __init__(self) -> None:
        super().__init__()

        q_h_box_layout = QVBoxLayout(self)
        q_h_box_layout.setContentsMargins(0, 0, 0, 0)
        q_h_box_layout.setSpacing(0)

        q_h_box_layout.addWidget(QLabel("Hello, World!"))
