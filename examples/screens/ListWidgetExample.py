from functools import cmp_to_key
from typing import List

from PySide6.QtGui import Qt
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidgetItem,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

from rokugu import ListWidget, Widget

names = [
    "Mr. Sylvan McGlynn IV",
    "Prof. Brandt Dietrich",
    "Rebeka Schamberger",
    "Jaylin Mueller",
    "Armani Ernser",
    "Mose Tillman",
    "Mr. Jadon Lueilwitz",
    "Anita McClure",
    "Judah Considine",
    "Jayden Little",
    "Dr. Rhianna Parisian",
    "Dr. Vincent Block DVM",
    "Prof. Ezekiel Monahan I",
    "Heloise Paucek",
    "Jovany Konopelski",
    "Hope Stroman",
    "Mrs. Ernestine Heaney PhD",
    "Adriana Schiller",
    "Devonte Gottlieb MD",
    "Kaleb Streich",
    "Ms. Abbie Beier",
    "Wilford Adams",
    "Margot Wehner",
    "Dr. Iliana Reichert II",
    "Keenan Wolff",
    "Loma Kutch",
    "Mike Osinski",
    "Bessie Sanford DVM",
    "Mrs. Marilou Stroman",
    "Bart Little",
    "Roberto Bernier",
    "Rozella O'Kon",
    "Roslyn Morar I",
    "Marianne Jaskolski",
    "Javier Runolfsson",
    "Toy Quitzon",
    "Xavier Lynch",
    "Mackenzie Cormier",
    "Prof. Kayleigh Heathcote",
    "Tanya Rath",
    "Prof. Caitlyn Weber",
    "Miss Hertha Spencer",
    "Ms. Elfrieda Fritsch V",
    "Lizzie Huels",
    "Dixie Hintz",
    "Prof. Armand Orn II",
    "Danny Heathcote",
    "Rupert Schinner MD",
    "Mr. Jimmie Bogisich",
    "Coy Torp",
    "Mr. Skylar Douglas",
    "Mr. Myron Frami Sr.",
    "Eveline Gutkowski",
    "Rene Buckridge",
    "Donny Klocko DDS",
    "Coby Deckow",
    "Nelle Monahan",
    "Alden Krajcik",
    "Kade Mraz",
    "Rudolph Tremblay",
    "Kailey Botsford DVM",
    "Carolyne Mraz I",
    "Dr. Verona Paucek Jr.",
    "Nicolas Hane",
    "Adelbert Becker",
    "Lon Christiansen",
    "Mrs. Leonie Hayes",
    "Nestor Bednar DDS",
    "Vidal Streich V",
    "Roscoe Tremblay",
    "Claud Conroy",
    "Mr. Otho Flatley DDS",
    "Mr. Shayne Braun PhD",
    "Alberta Leuschke",
    "Douglas Pfeffer Jr.",
    "Jovanny Ernser",
    "Agustin Howe",
    "Sydnie Huels",
    "Ms. Maida Nikolaus Jr.",
    "Mara Spencer DDS",
    "Prof. Chaz Sawayn",
    "Dr. Ali Howe",
    "Johathan Ferry V",
    "Maribel Berge II",
    "Cornell Parker",
    "Foster Kautzer",
    "Prof. Ova Hessel II",
    "Reilly Stehr",
    "Victoria Bruen MD",
    "Mrs. Michele Volkman Jr.",
    "Raymundo Bradtke",
    "Ms. Verda Schaden V",
    "Dr. Adolfo Wiegand DVM",
    "Jovan Corwin",
    "Mr. Horace Romaguera",
    "Henriette Bode",
    "Camron Kuvalis",
    "Kylie Stamm",
    "Adell Bradtke",
    "Prof. Yolanda Rau",
]


class ListWidgetExample(ListWidget):
    def __init__(self) -> None:
        super().__init__()

        for name in names:
            self.append(name)

    def get_widget(self, q_string: str) -> QWidget:
        q_label = QLabel(q_string)
        q_label.setContentsMargins(14, 0, 14, 0)
        q_label.setFixedHeight(48)
        return q_label

    def append(self, q_string: str) -> None:
        q_list_widget_item = QListWidgetItem()
        q_list_widget_item.setData(
            Qt.ItemDataRole.AccessibleTextRole, q_string
        )
        q_list_widget_item.setData(Qt.ItemDataRole.UserRole, q_string)
        q_label = self.get_widget(q_string)
        q_list_widget_item.setSizeHint(q_label.sizeHint())
        self.addItem(q_list_widget_item)
        self.setItemWidget(q_list_widget_item, q_label)

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

    def filter_items(self, q_string: str) -> None:
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
            q_widget = self.get_widget(
                str(item.data(Qt.ItemDataRole.UserRole))
            )
            self.setItemWidget(item, q_widget)


class List1(Widget):
    def __init__(self) -> None:
        super().__init__()

        # self.setStyleSheet("QWidget{border: 1px solid red}")

        q_h_box_layout = QHBoxLayout(self)
        q_h_box_layout.setContentsMargins(0, 0, 0, 0)
        q_h_box_layout.setSpacing(0)
        q_h_box_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        q_widget = QWidget()
        q_widget.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred
        )
        q_widget.setMaximumWidth(512)
        q_v_box_layout = QVBoxLayout(q_widget)
        q_v_box_layout.setContentsMargins(24, 24, 24, 24)
        q_v_box_layout.setSpacing(0)
        q_line_edit = QLineEdit()
        q_line_edit.setFixedHeight(48)
        q_line_edit.setTextMargins(14, 0, 14, 0)
        q_v_box_layout.addWidget(q_line_edit)
        l2 = Menu()
        l2.changed.connect(lambda _: l2.remove(QListWidgetItem()))
        q_v_box_layout.addWidget(l2)
        q_label = QLabel()
        q_v_box_layout.addWidget(q_label)
        q_h_box_layout.addWidget(q_widget)

        q_line_edit.textChanged.connect(l2.filter_items)
