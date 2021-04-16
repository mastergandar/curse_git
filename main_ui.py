from PySide2 import QtWidgets
from ui import Ui_ui
import sys


# Главный класс
class MakeCurse(QtWidgets.QMainWindow, Ui_ui):

    # Атрибуты данных класса
    lvl_out = []
    dic_chop = []

    # Конструктор класса
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.file_open()

        self.Search.clicked.connect(self.search_pressed)

    # Метод обработки нажатия кнопки "Поиск"
    def search_pressed(self):
        self.search()
        self.sort()
        self.output()

    # Метод обработки файла
    def file_open(self):
        with open('sotrudniki.txt', encoding="utf-8") as file:
            for i in file:
                i = i.strip()
                self.lvl_out = self.lvl_out + [i]
                self.dic_chop = [self.lvl_out[x:4 + x] for x in range(0, len(self.lvl_out), 4)]
            return self

    # Метод поиска подходящих по условию сотрудников
    def search(self):
        file_out = []
        for i in range(len(self.dic_chop)):
            if int(self.dic_chop[i][3]) > int(self.Input.text()):
                file_out.append(self.dic_chop[i])
        return file_out

    # Метод сортировки списков по возрастанию стажа
    def sort(self):
        new_result = sorted(self.search(), key=lambda arg: int(arg[3]))
        return new_result

    # Метод форматированного вывода результатов на экран
    def output(self):
        a = 0
        b = 0
        c = 0
        if len(self.sort()) == 0:
            self.textBrowser.setText('Нет сотрудников удовлетворяющих введенным требованиям.')
        else:
            self.textBrowser.setPlainText("Кол-во сотрудников удволетворяющих требованию: %s\n" % len(self.sort()))
            for i in range(len(self.sort())):
                if len(self.sort()[i][0]) > a:
                    a = len(self.sort()[i][0])
                if len(self.sort()[i][1]) > b:
                    b = len(self.sort()[i][1])
                if len(str(i + 1)) > c:
                    c = len(str(i + 1))
            for i in range(len(self.sort())):
                self.textBrowser.append("%s-й: Фамилия: %s | Отдел: %s | Дата рожденья: %s | Стаж работы: %s" %
                                        (str(i + 1).rjust(c), self.sort()[i][0].ljust(a), self.sort()[i][1].ljust(b),
                                         self.sort()[i][2], self.sort()[i][3]))


if __name__ == '__main__':
    # Новый экземпляр QApplication
    app = QtWidgets.QApplication(sys.argv)
    # Сздание инстанса класса
    quest = MakeCurse()
    # Запуск
    sys.exit(app.exec_())
