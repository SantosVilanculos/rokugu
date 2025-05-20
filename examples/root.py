from PySide6.QtWidgets import QStackedLayout, QWidget
from screens.examples import Examples


class Root(QWidget):
    def __init__(self) -> None:
        super().__init__()

        q_staked_layout = QStackedLayout(self)
        examples = Examples()
        q_staked_layout.addWidget(examples)
