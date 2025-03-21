from platform import python_version

from PySide6.QtCore import Signal, qVersion
from PySide6.QtGui import QFont, Qt
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

from rokugu.widgets.widget import Widget


class Welcome(Widget):
    continue_ = Signal()

    def __init__(self) -> None:
        super().__init__()

        # self.setStyleSheet("QWidget{border: 1px solid red}")

        self.setObjectName("bg")
        self.setStyleSheet(
            """
        #bg{
            background-color: #1f1f1f;
        }
        QLabel{
            color: #d1cfc0;
        }
        """
        )
        q_h_box_layout = QHBoxLayout(self)
        q_h_box_layout.setContentsMargins(0, 0, 0, 0)
        q_h_box_layout.setSpacing(0)
        q_h_box_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        q_widget = QWidget()
        q_widget.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred
        )
        q_widget.setMaximumWidth(800)
        q_v_box_layout = QVBoxLayout(q_widget)
        q_v_box_layout.setContentsMargins(0, 0, 0, 0)
        q_v_box_layout.setSpacing(24)
        q_label1 = QLabel(f"PySide {qVersion()} (Python {python_version()})")
        q_label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        q_label1.font()
        q_font = q_label1.font()
        q_font.setWeight(QFont.Weight.Medium)
        q_label1.setFont(q_font)
        q_v_box_layout.addWidget(q_label1)
        q_label = QLabel(
            "An opinionated PySide6 library that delivers ready-to-use components and utilities."
        )
        q_label.setWordWrap(True)
        q_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        q_v_box_layout.addWidget(q_label)
        q_push_button = QPushButton("Continue")
        q_push_button.setMaximumWidth(240)
        q_push_button.setFixedHeight(36)
        q_push_button.pressed.connect(self.continue_.emit)
        q_v_box_layout.addWidget(
            q_push_button, alignment=Qt.AlignmentFlag.AlignCenter
        )
        q_h_box_layout.addWidget(q_widget)
