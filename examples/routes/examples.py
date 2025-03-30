from functools import cmp_to_key
from typing import List

from PySide6.QtCore import QSize, QXmlStreamReader, Signal
from PySide6.QtGui import Qt
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidgetItem,
    QSizePolicy,
    QSplitter,
    QVBoxLayout,
    QWidget,
)
from routes.image_background_example import ImageBackgroundExample
from routes.list_widget_example import ListWidgetExample

from rokugu.widgets.list_widget import ListWidget
from rokugu.widgets.router import Router
from rokugu.widgets.widget import Widget


class S1(Widget):
    text_changed = Signal(str)

    def __init__(self) -> None:
        super().__init__()
        self.setFixedHeight(40)
        self.setObjectName("n")
        self.setStyleSheet("QLineEdit{border:0;background-color:transparent}")

        q_h_box_layout = QHBoxLayout(self)
        q_h_box_layout.setContentsMargins(12, 0, 12, 0)
        q_h_box_layout.setSpacing(12)
        q_svg_widget = QSvgWidget()
        q_svg_widget.setFixedSize(16, 16)
        q_svg_widget.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        q_svg_renderer = q_svg_widget.renderer()
        q_svg_renderer.setAspectRatioMode(Qt.AspectRatioMode.KeepAspectRatio)
        q_svg_renderer.load(
            QXmlStreamReader(
                """
            <svg
            xmlns="http://www.w3.org/2000/svg"
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
            >
            <circle cx="11" cy="11" r="8" />
            <path d="m21 21-4.3-4.3" />
            </svg>
            """
            )
        )
        q_h_box_layout.addWidget(q_svg_widget)
        q_line_edit = QLineEdit()
        q_line_edit.textChanged.connect(self.text_changed.emit)
        q_line_edit.setPlaceholderText("")
        q_line_edit.setSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding
        )
        q_h_box_layout.addWidget(q_line_edit)


class S2(ListWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setStyleSheet("QListWidget{border:0}")

        self._add("Image backgound", "image")
        self._add("List Widget", "list")
        self._add("Test", "test")

    def _widget(self, accessible_text_role: str) -> QWidget:
        q_widget = QWidget()
        q_widget.setFixedHeight(40)
        q_h_box_layout = QHBoxLayout(q_widget)
        q_h_box_layout.setContentsMargins(0, 0, 0, 0)
        q_label = QLabel(accessible_text_role)
        q_label.setContentsMargins(12, 0, 12, 0)
        q_h_box_layout.addWidget(q_label)
        return q_widget

    def _add(self, accessible_text_role: str, user_role: str):
        q_list_widget_item = QListWidgetItem()
        q_list_widget_item.setSizeHint(QSize(0, 40))
        q_list_widget_item.setData(
            Qt.ItemDataRole.AccessibleTextRole, accessible_text_role
        )
        q_list_widget_item.setData(Qt.ItemDataRole.UserRole, user_role)
        self.addItem(q_list_widget_item)
        q_widget = self._widget(accessible_text_role)
        self.setItemWidget(q_list_widget_item, q_widget)

    def _compare_q_file_info(
        self, item1: QListWidgetItem, item2: QListWidgetItem, q_string: str
    ) -> int:
        index1 = (
            str(item1.data(Qt.ItemDataRole.AccessibleTextRole))
            .lower()
            .find(q_string.lower())
        )
        index2 = (
            str(item2.data(Qt.ItemDataRole.AccessibleTextRole))
            .lower()
            .find(q_string.lower())
        )

        if index1 < index2:
            return -1
        elif index1 > index2:
            return 1
        else:
            return 0

    def _get_sorted_data(
        self, data: List[QListWidgetItem], q_string: str
    ) -> List[QListWidgetItem]:
        f1 = list(
            filter(
                lambda item: q_string.lower()
                in str(item.data(Qt.ItemDataRole.AccessibleTextRole)).lower(),
                data,
            )
        )
        f2 = sorted(
            f1,
            key=cmp_to_key(
                lambda item1, item2: self._compare_q_file_info(
                    item1, item2, q_string
                )
            ),
        )
        return f2

    def find_(self, q_string: str) -> None:
        all_items = [self.item(i) for i in range(self.count())]

        if len(q_string) == 0:
            for item in all_items:
                item.setHidden(False)
            return

        filtered_items = self._get_sorted_data(all_items, q_string)

        for item in all_items:
            item.setHidden(True)

        for index, q_list_widget_item in enumerate(filtered_items):
            row = self.row(q_list_widget_item)

            if row == -1:
                continue

            self.removeItemWidget(q_list_widget_item)
            item = self.takeItem(row)

            self.insertItem(index, item)
            q_widget = self._widget(
                item.data(Qt.ItemDataRole.AccessibleTextRole)
            )
            self.setItemWidget(item, q_widget)


class Aside(Widget):
    to = Signal(str)

    def __init__(self) -> None:
        super().__init__()

        self.setFixedWidth(256)
        q_v_box_layout = QVBoxLayout(self)
        q_v_box_layout.setContentsMargins(0, 0, 0, 0)
        q_v_box_layout.setSpacing(0)
        s1 = S1()
        q_v_box_layout.addWidget(s1)
        q_frame = QFrame()
        q_frame.setFrameShadow(QFrame.Shadow.Plain)
        q_frame.setFrameShape(QFrame.Shape.HLine)
        q_frame.setStyleSheet("QFrame{color:#d1d5dc}")
        q_frame.setFixedHeight(1)
        q_v_box_layout.addWidget(q_frame)
        s2 = S2()
        s2.changed.connect(
            lambda _: self.to.emit(str(_.data(Qt.ItemDataRole.UserRole)))
        )
        q_v_box_layout.addWidget(s2, stretch=1)

        s1.text_changed.connect(s2.find_)


class Main(Router):
    def __init__(self) -> None:
        super().__init__()

        self.setStyleSheet("Router{border: 1px solid red}")
        self.add("image", ImageBackgroundExample())
        self.add("list", ListWidgetExample())
        self.add("test", QLabel("test"))


class Examples(Widget):
    def __init__(self) -> None:
        super().__init__()

        q_v_box_layout = QVBoxLayout(self)
        q_v_box_layout.setContentsMargins(0, 0, 0, 0)
        q_splitter = QSplitter()
        q_splitter.setStyleSheet("QSplitter:handle{background-color:#d1d5dc}")
        q_splitter.setHandleWidth(1)
        aside = Aside()
        q_splitter.addWidget(aside)
        main = Main()
        q_splitter.addWidget(main)
        q_v_box_layout.addWidget(q_splitter)

        aside.to.connect(lambda _: main.to_route(_))
