from PyQt5.QtWidgets import *
from scraper_main import *

app = QApplication([])
window = QWidget()

mainline = QVBoxLayout()

query_lbl = QLabel("Введіть пошуковий запит")
query_text = QLineEdit()
price_from_lbl = QLabel("Введіть ціну від якої потрібно шукати (0-10000000)")
price_from_text = QLineEdit()
price_to_lbl = QLabel("Введіть ціну до якої потрібно шукати (До 10000000)")
price_to_text = QLineEdit()
start_btn = QPushButton("Розпочати парсинг")
scraping_status = QLabel("Парсинг зупинений")

mainline.addWidget(query_lbl)
mainline.addWidget(query_text)
mainline.addWidget(price_from_lbl)
mainline.addWidget(price_from_text)
mainline.addWidget(price_to_lbl)
mainline.addWidget(price_to_text)
mainline.addWidget(start_btn)
mainline.addWidget(scraping_status)

def start_scraping():
    try:
        scraping_status.setText("Парсинг розпочато!")
        query = query_text.text()
        price_from = price_from_text.text()
        price_to = price_to_text.text()
        main(query, price_from, price_to)
        scraping_status.setText("Парсинг завершено!")
    except Exception as e:
        print(f"[ERROR] {e}")

start_btn.clicked.connect(start_scraping)

window.setLayout(mainline)

if __name__ == "__main__":
    try:
        window.show()
        app.exec()
    except KeyboardInterrupt:
        print("[!] Programm was forcefully closed")
