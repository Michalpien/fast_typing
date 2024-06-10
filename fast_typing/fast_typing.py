from PySide2.QtWidgets import QMainWindow, QApplication
from ui_fast_typing import Ui_FastTyping
import sys
from text_meneger import Statistics, TextGetter
from threading import Timer
import time


class FastWriterWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_FastTyping()
        self.ui.setupUi(self)
        self.counter = 0


def guiMain(args):
    app = QApplication(args)
    window = FastWriterWindow()
    text = TextGetter().get_lines()
    statistics = Statistics(text=text)
    statistics._entered_text.append("")

    def change_index_1():
        '''
        changing window to select time page
        '''
        window.ui.stackedWidget.setCurrentIndex(1)

    def change_index_0():
        '''
        changing window to start page
        '''
        window.ui.stackedWidget.setCurrentIndex(0)

    def change_to_typing_page(time):
        '''
        change window to typing page and set statistics._time to time
        '''
        window.ui.stackedWidget.setCurrentIndex(2)
        statistics._time = time

    def change_to_statistic_page():
        '''
        change window to statistic page
        change labels to show statistics
        '''
        chars_per_min = str(statistics.chars_per_minute())
        words_per_min = str(statistics.words_per_minute())
        mistakes = str(statistics.mistakes())
        chars_text = f'chars per min: {chars_per_min}'
        words_text = f'words per min: {words_per_min}'
        mistakes_text = f'mistakes: {mistakes}'
        window.ui.stackedWidget.setCurrentIndex(3)
        window.ui.char_per_minute_label.setText(chars_text)
        window.ui.words_per_minute_label.setText(words_text)
        window.ui.mistakes_label.setText(mistakes_text)

    def selected_time_10():
        change_to_typing_page(10)

    def selected_time_20():
        change_to_typing_page(20)

    def selected_time_30():
        change_to_typing_page(30)

    def selected_time_40():
        change_to_typing_page(40)

    def check_text():
        '''
        Compare entered_text and draw text and marks mistakes
        '''
        current_text = text[window.counter]
        entered_text = str(window.ui.enterText.toPlainText())
        number_of_letter = 0
        window.ui.displayText.clear()
        for letter in current_text:
            window.ui.displayText.setTextBackgroundColor('white')
            try:
                if entered_text[number_of_letter] == letter:
                    window.ui.displayText.setTextColor('green')
                else:
                    window.ui.displayText.setTextColor('red')
                    if letter == " ":
                        window.ui.displayText.setTextBackgroundColor('red')
            except (IndexError):
                window.ui.displayText.setTextColor('black')
            window.ui.displayText.insertPlainText(letter)
            number_of_letter += 1

    def change_line():
        '''
        change window.number if entered_text is longer than display
        save entered line to statistics
        '''
        entered_text = str(window.ui.enterText.toPlainText())
        if len(entered_text) > len(text[window.counter]):
            statistics._entered_text.append('')
            statistics._entered_text[window.counter] = entered_text[:-1]
            window.counter += 1
            window.ui.displayText.clear()
            window.ui.enterText.clear()
            window.ui.displayText.insertPlainText(text[window.counter])

    def save_current_entered_text():
        '''
        saving current entered text
        '''
        entered_text = str(window.ui.enterText.toPlainText())
        statistics._entered_text[window.counter] = entered_text

    def start_counting():
        '''
        start counting to the end of writing when we enter first char
        '''
        if window.counter == 0:
            if len(str(window.ui.enterText.toPlainText())) == 1:
                timer = Timer(statistics._time, change_to_statistic_page)
                timer.start()

    def typing_functions():
        '''
        functions called by typing
        '''
        if window.ui.stackedWidget.currentIndex() == 2:
            change_line()
            check_text()
            save_current_entered_text()
            start_counting()

    window.ui.displayText.insertPlainText(text[window.counter])
    window.ui.StartButton.clicked.connect(change_index_1)
    window.ui.ExitButton.clicked.connect(sys.exit)
    window.ui.BackButton.clicked.connect(change_index_0)
    window.ui.pushButton_1.clicked.connect(selected_time_10)
    window.ui.pushButton_2.clicked.connect(selected_time_20)
    window.ui.pushButton_3.clicked.connect(selected_time_30)
    window.ui.pushButton_4.clicked.connect(selected_time_40)
    window.ui.ExitButton_2.clicked.connect(sys.exit)
    window.ui.enterText.textChanged.connect(typing_functions)
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
