# coding: utf-8

"""This is a simple demonstration library"""

__date__ = "01/04/2019"
__license__ = "MIT"


import PyQt5


from PyQt5 import Qt
from . import polynom


class PolynomSolver(Qt.QMainWindow):

    def __init__(self, parent=None):
        super(PolynomSolver, self).__init__(parent=parent)
        self.initGui()

    def initGui(self):
        self.setWindowTitle("Polygon Solver")
        self._inputLine = Qt.QLineEdit(self)
        self._processButton = Qt.QPushButton(self)
        self._processButton.setText(u"Solve ax² + bx + c = 0")
        self._processButton.clicked.connect(self.processing)
        self._resultWidget = Qt.QLabel(self)

        widget = Qt.QWidget()
        layout = Qt.QFormLayout(widget)
        layout.addRow("Coefs a b c:", self._inputLine)
        layout.addRow("Solutions:", self._resultWidget)
        layout.addRow(self._processButton)
        self.setCentralWidget(widget)

    def getCoefs(self):
        text = self._inputLine.text()
        data = [float(i) for i in text.split()]
        a, b, c = data
        return a, b, c

    def processing(self):
        try:
            a, b, c = self.getCoefs()
        except Exception as e:
            Qt.QMessageBox.critical(self, "Error while reaching polygon coefs", str(e))
            return
        try:
            result = polynom.polynom(a, b, c)
        except Exception as e:
            Qt.QMessageBox.critical(self, "Error while computing the polygon solution", str(e))
            return

        if len(result) == 0:
            text = "No solution"
        else:
            text = ["%0.3f" % x for x in result]
            text = " ".join(text)
        self._resultWidget.setText(text)

if __name__ == "__main__":
    app = Qt.QApplication([])
    widget = PolynomSolver()
    widget.show()
    app.exec_()
