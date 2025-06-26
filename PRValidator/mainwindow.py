# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py


from PRValidator import find_errors, fix_errors
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_file.clicked.connect(self.openFileDialog)
        self.ui.btn_validate.clicked.connect(self.validate)
        self.ui.btn_fix.clicked.connect(self.fix)

    def openFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        fileName, _ = QFileDialog.getOpenFileName(self, "Select File", "", "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            self.ui.line_file.setText(fileName)
            self.ui.text_result.setPlainText("")

    def validate(self):
        fileName = self.ui.line_file.text()
        kommune = self.ui.checkKommune.isChecked()
        dato = self.ui.checkDato.isChecked()
        personnr = self.ui.checkPersonnr.isChecked()
        navn = self.ui.checkNavn.isChecked()
        self.ui.text_result.setPlainText(find_errors(fileName, kommune, dato, personnr, navn))
        self.ui.text_result.update()

    def fix(self):
        fileName = self.ui.line_file.text()
        self.ui.text_result.setPlainText(fix_errors(fileName))
        self.ui.text_result.update()
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
