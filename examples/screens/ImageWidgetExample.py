from PySide6.QtCore import Slot
from PySide6.QtGui import Qt
from PySide6.QtWidgets import (
    QComboBox,
    QFileDialog,
    QFormLayout,
    QHBoxLayout,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)
from utils import asset

from rokugu import ImageWidget


class ImageWidgetExample(ImageWidget):
    def __init__(self) -> None:
        super().__init__(
            asset("images/0f3ba378-05e8-11f0-8474-0f5febd4ad14.png")
        )

        self.setStyleSheet("ImageBackground{border: 1px solid red}")

        q_h_box_layout = QHBoxLayout(self)
        q_h_box_layout.setContentsMargins(0, 0, 0, 0)
        q_h_box_layout.setSpacing(0)
        q_h_box_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        q_widget = QWidget()
        q_widget.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred
        )
        q_widget.setMaximumWidth(256)
        q_v_box_layout = QVBoxLayout(q_widget)
        q_v_box_layout.setContentsMargins(24, 24, 24, 24)
        q_v_box_layout.setSpacing(0)
        q_form_layout = QFormLayout()
        q_form_layout.setSpacing(6)
        self._q_combo_box = QComboBox()
        self._q_combo_box.addItem("Contain", ImageWidget.ObjectFit.Contain)
        self._q_combo_box.addItem("Cover", ImageWidget.ObjectFit.Cover)
        self._q_combo_box.addItem("Fill", ImageWidget.ObjectFit.Fill)
        self._q_combo_box.addItem(
            "Scale down", ImageWidget.ObjectFit.ScaleDown
        )
        self._q_combo_box.addItem("Unset", ImageWidget.ObjectFit.Unset)
        self._q_combo_box.setCurrentIndex(1)
        self._q_combo_box.currentIndexChanged.connect(
            self._current_index_changed
        )
        self._q_combo_box.setFixedHeight(36)
        q_form_layout.addRow("OBJECT FIT", self._q_combo_box)
        self.q_file_dialog = QFileDialog(self)
        self.q_file_dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptOpen)
        self.q_file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        self.q_file_dialog.setMimeTypeFilters(
            ["image/png", "image/jpeg", "image/svg+xml"]
        )
        self.q_file_dialog.fileSelected.connect(self._file_selected)
        q_push_button = QPushButton("Change")
        q_push_button.setFixedHeight(36)
        q_push_button.pressed.connect(self.q_file_dialog.open)
        q_form_layout.addWidget(q_push_button)
        q_v_box_layout.addLayout(q_form_layout)
        q_h_box_layout.addWidget(q_widget)

    @Slot(int)
    def _current_index_changed(self, index: int) -> None:
        user_role = self._q_combo_box.currentData(Qt.ItemDataRole.UserRole)
        self.setObjectFit(user_role)

    @Slot(str)
    def _file_selected(self, q_string: str) -> None:
        print(q_string)
        self.load(q_string)
