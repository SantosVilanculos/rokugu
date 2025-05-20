import sys
from logging import DEBUG, StreamHandler, basicConfig

from PySide6.QtCore import QCommandLineParser
from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtWidgets import QApplication
from root import Root
from utils import asset

from rokugu import Window


def main() -> None:
    # ---
    q_application = QApplication(sys.argv)

    # ---
    q_application.setApplicationName("")
    q_application.setApplicationDisplayName("")
    q_application.setApplicationVersion("")
    q_application.setOrganizationName("")
    q_application.setOrganizationDomain("")

    # ---
    q_command_line_parser = QCommandLineParser()
    q_command_line_parser.setApplicationDescription("")
    q_command_line_parser.addHelpOption()
    q_command_line_parser.addVersionOption()
    q_command_line_parser.process(q_application)

    # ---
    basicConfig(
        encoding="UTF-8",
        format="%(asctime)s:%(levelname)s:%(filename)s:%(lineno)d:%(message)s",
        level=DEBUG,
        handlers=[StreamHandler()],
    )

    # ---
    # q_icon = QIcon("")
    # q_application.setWindowIcon(q_icon)

    # ---
    QFontDatabase.addApplicationFont(
        asset("fonts/inter/4.1/thin.ttf").as_posix()
    )
    QFontDatabase.addApplicationFont(
        asset("fonts/inter/4.1/extra_light.ttf").as_posix()
    )
    QFontDatabase.addApplicationFont(
        asset("fonts/inter/4.1/light.ttf").as_posix()
    )
    QFontDatabase.addApplicationFont(
        asset("fonts/inter/4.1/normal.ttf").as_posix()
    )
    QFontDatabase.addApplicationFont(
        asset("fonts/inter/4.1/medium.ttf").as_posix()
    )
    QFontDatabase.addApplicationFont(
        asset("fonts/inter/4.1/demi_bold.ttf").as_posix()
    )
    QFontDatabase.addApplicationFont(
        asset("fonts/inter/4.1/bold.ttf").as_posix()
    )
    QFontDatabase.addApplicationFont(
        asset("fonts/inter/4.1/extra_bold.ttf").as_posix()
    )
    QFontDatabase.addApplicationFont(
        asset("fonts/inter/4.1/black.ttf").as_posix()
    )

    q_font = QFont("Inter")
    q_font.setPixelSize(14)
    q_font.setWeight(QFont.Weight.Normal)
    q_font.setStyleStrategy(QFont.StyleStrategy.PreferAntialias)
    q_application.setFont(q_font)

    # ---
    q_main_window = Window()
    q_screen = q_application.primaryScreen()
    q_rect = q_screen.availableGeometry()
    screen_width = q_rect.width()
    screen_height = q_rect.height()

    if screen_width > screen_height:  # Landscape
        width = round((screen_width / 100) * 60)
        height = round((width * 3) / 4)
    else:  # Portrait
        height = round((screen_height / 100) * 60)
        width = round((height * 4) / 3)
    q_main_window.resize(width, height)

    # ---
    q_main_window.setCentralWidget(Root())
    q_main_window.show()

    # ---
    sys.exit(q_application.exec())


if __name__ == "__main__":
    main()
