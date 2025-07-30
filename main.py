from PyQt6.QtWidgets import *

app = QApplication([])
window = QWidget()

mainline = QVBoxLayout()

query_lbl = QLabel("Введіть пошуковий запит")
query_text = QLineEdit()
price_from_lbl = QLabel("Введіть ціну від якої потрібно шукати (0-10000000)")
price_from_text = QLineEdit()
price_to_lbl = QLabel("Введіть ціну від якої потрібно шукати (До 10000000)")
price_to_text = QLineEdit()

mainline.addWidget(query_lbl)
mainline.addWidget(query_text)
mainline.addWidget(price_from_lbl)
mainline.addWidget(price_from_text)
mainline.addWidget(price_to_lbl)
mainline.addWidget(price_to_text)

window.setLayout(mainline)

window.show()
app.exec()
