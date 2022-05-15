#создай приложение для запоминания информации
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QMessageBox, QHBoxLayout, QGroupBox, QButtonGroup, QRadioButton
from random import shuffle, randint

class Question():
    def __init__(self, question,right_answer ,wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Какой сегодня день недели?', 'Воскресенье', 'Понедельник', 'Среда', 'Четверг'))
question_list.append(Question('Какой год?', '2021', '2029', '2020', '2017'))
question_list.append(Question('Копенгаген - столица...', 'Дании', 'Москвы', 'Нидерландов', 'Швеции'))
question_list.append(Question('В каком году канал получил "золотую кнопку" от YouTube', '2015', '2020', '2019', '2000'))
question_list.append(Question('Какое из этих чисел является простым?', '7', '18', '12', ' 100'))
question_list.append(Question('Какая планета известна своими кольцами?', 'Сатурн', 'Венера', 'Юпитер', 'Земл'))
question_list.append(Question('Солнце встает на...', 'Востоке', 'Западе', 'Севере', 'Юге'))
question_list.append(Question('В каком фрукте больше витамина C, чем в апельсинах?', 'В клубнике', 'В лимоне', 'В банане', 'В грейпфруте'))
question_list.append(Question('Как называется детеныш лошади?', 'Жеребенок', 'Теленок', 'Пони', 'Единороги'))
question_list.append(Question('На каком континенте расположено большее количество стран?', 'Северная америка', 'Южная Америка', 'Африка', 'Европа'))


app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.resize(400, 200)

lbl_question = QLabel('Какой национальности не существует?')
btn_answer = QPushButton('Ответить')

RadioGroupBox = QGroupBox('Варианты ответа')
rbtn1 = QRadioButton('1')
rbtn2 = QRadioButton('2')
rbtn3 = QRadioButton('3')
rbtn4 = QRadioButton('4')
layoutanw1 = QHBoxLayout()
layoutanw2 = QVBoxLayout()
layoutanw3 = QVBoxLayout()

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)

#создание виджетов главного окна


layoutanw2.addWidget(rbtn1)
layoutanw2.addWidget(rbtn2)
layoutanw3.addWidget(rbtn3)
layoutanw3.addWidget(rbtn4)
layoutanw1.addLayout(layoutanw2)
layoutanw1.addLayout(layoutanw3)

RadioGroupBox.setLayout(layoutanw1)
RadioGroupBox.show()



#Группа ответов

AnswerGroupBox = QGroupBox('Результат твоего ответа')
lbl_ans1 = QLabel('Правильно/Неправильно')
lbl_ans2 = QLabel('Правильный ответ')
layout_ans4 = QVBoxLayout()
layout_ans4.addWidget(lbl_ans1)
layout_ans4.addWidget(lbl_ans2)
AnswerGroupBox.setLayout(layout_ans4)
AnswerGroupBox.hide()


layout_main = QVBoxLayout()
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()

layoutH1.addWidget(lbl_question, alignment=Qt.AlignCenter)
layoutH2.addWidget(RadioGroupBox)
layoutH2.addWidget(AnswerGroupBox)
layoutH3.addWidget(btn_answer, stretch=2)

layout_main.addLayout(layoutH1, stretch=2)
layout_main.addLayout(layoutH2, stretch=8)
layout_main.addLayout(layoutH3, stretch=1)

main_win.setLayout(layout_main)
main_win.show()
answers = [rbtn1, rbtn2, rbtn3, rbtn4]

#Задаём вопрос
def ask(q):
    shuffle(answers)
    lbl_question.setText(q.question)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lbl_ans2.setText(q.right_answer)

#Проверяем ответ на вопрос
def check_answer():
    if answers[0].isChecked():
        show_result("Правильно")
        main_win.score += 1
    else:
        show_result('Неправильно')

#Выводим результат
def show_result(res):
    lbl_ans1.setText(res)
    show_answer()

#Показываем следующий вопрос
def show_answer():
    RadioGroupBox.hide()
    AnswerGroupBox.show()
    btn_answer.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnswerGroupBox.hide()
    btn_answer.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)

def next_question():
    main_win.total += 1
    cur_question = randint(0, len(question_list) - 1)
    ask(question_list[cur_question])
    show_question()

def click_ok():
    if btn_answer.text() == 'Ответить':
        check_answer()
    else:
        next_question()

main_win.current_question = -1

main_win.score = 0
main_win.total = 0      
next_question()

btn_answer.clicked.connect(click_ok)  

app.exec_()
print('Процент правильных ответов - ', round(main_win.score/main_win.total*100, 2))

input('Нажмите enter')
