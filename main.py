from PyQt5.QtWidgets import *
from scraper_main import *
from file_manager import *

templates_dict = read_template()

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
templates_choice = QComboBox()
add_template_btn = QPushButton("Додати шаблон за значеннями")
delete_template_btn = QPushButton("Видалити обраний шаблон")
scraping_status = QLabel("Парсинг зупинений")

templates_choice.addItem("Не обрано")
templates_choice.addItems(templates_dict)

mainline.addWidget(templates_choice)
mainline.addWidget(query_lbl)
mainline.addWidget(query_text)
mainline.addWidget(price_from_lbl)
mainline.addWidget(price_from_text)
mainline.addWidget(price_to_lbl)
mainline.addWidget(price_to_text)
mainline.addWidget(start_btn)
mainline.addWidget(add_template_btn)
mainline.addWidget(delete_template_btn)
mainline.addWidget(scraping_status)

def start_scraping():
    try:
        query = query_text.text()
        if not query:
            QMessageBox.warning(window, "Помилка", "Парсинг не може бути розпочатий без параметрів")
            return
        price_from = price_from_text.text()
        price_to = price_to_text.text()
        scraping_status.setText("Парсинг розпочато!")
        main(query, price_from, price_to)
        scraping_status.setText("Парсинг завершено!")
    except Exception as e:
        print(f"[ERROR] {e}")

def add_template():
    if not query_text.text() or query_text.text() == "Не обрано":
        QMessageBox.warning(window, "Помилка", 'Назва шаблону недопустима')
        return
    
    templates_choice.blockSignals(True)
    templates_dict[query_text.text()] = {
        "price_from": price_from_text.text(),
        "price_to": price_to_text.text()
    }
    templates_choice.clear()
    templates_choice.addItem("Не обрано")
    templates_choice.addItems(templates_dict)
    write_template(templates_dict)
    templates_choice.setCurrentIndex(0)
    templates_choice.blockSignals(False)

def show_template():
    key = templates_choice.currentText()
    print(key)
    if key == "Не обрано":
        query_text.clear()
        price_from_text.clear()
        price_to_text.clear()
        return

    template_data = templates_dict.get(key, {})
    query = key
    price_from = template_data.get("price_from", ())
    price_to = template_data.get("price_to", ())

    query_text.setText(query)
    price_from_text.setText(price_from)
    price_to_text.setText(price_to)
    
def delete_template():
    key = templates_choice.currentText()
    if key == "Не обрано":
        QMessageBox.warning(window, "Помилка", "Цей шаблон не можливо видалити")
        return
    templates_choice.blockSignals(True)
    templates_dict.pop(key)
    templates_choice.clear()
    templates_choice.addItem("Не обрано")
    templates_choice.addItems(templates_dict)
    templates_choice.blockSignals(False)
    query_text.clear()
    price_from_text.clear()
    price_to_text.clear()
    
start_btn.clicked.connect(start_scraping)
add_template_btn.clicked.connect(add_template)
templates_choice.currentIndexChanged.connect(show_template)
delete_template_btn.clicked.connect(delete_template)

window.setStyleSheet("""
    QWidget {
        background-color: #f5f7fa;
        font-family: "Segoe UI", "Arial", sans-serif;
        font-size: 14px;
        color: #333;
    }

    QLabel {
        font-weight: bold;
        margin-top: 8px;
        margin-bottom: 4px;
    }

    QLineEdit, QComboBox {
        padding: 6px;
        border: 1px solid #ccc;
        border-radius: 4px;
        background-color: #fff;
    }

    QComboBox::drop-down {
        border-left: 1px solid #ccc;
    }

    QPushButton {
        background-color: #4a90e2;
        color: white;
        padding: 8px;
        border: none;
        border-radius: 4px;
        font-weight: bold;
    }

    QPushButton:hover {
        background-color: #357ab8;
    }

    QPushButton:pressed {
        background-color: #2d6399;
    }

    QLabel#scraping_status {
        margin-top: 10px;
        font-style: italic;
        color: #666;
    }
""")

window.setLayout(mainline)

if __name__ == "__main__":
    try:
        window.show()
        app.exec()
    except KeyboardInterrupt:
        print("[!] Programm was forcefully closed")
