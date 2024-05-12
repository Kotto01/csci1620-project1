# main.py
import sys
from PyQt6 import QtWidgets
from logic import print_votes, VoteMenu

def main() -> None:
    """Main loop for the program"""
    app = QtWidgets.QApplication(sys.argv)
    vote_menu = VoteMenu()
    app.aboutToQuit.connect(print_votes)
    vote_menu.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
