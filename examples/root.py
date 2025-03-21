from PySide6.QtWidgets import QStackedLayout, QWidget
from routes.examples import Examples
from routes.welcome import Welcome


class Root(QWidget):
    def __init__(self) -> None:
        super().__init__()

        q_staked_layout = QStackedLayout(self)
        welcome = Welcome()
        q_staked_layout.addWidget(welcome)
        examples = Examples()
        index = q_staked_layout.addWidget(examples)

        welcome.continue_.connect(
            lambda: q_staked_layout.setCurrentIndex(index)
        )
