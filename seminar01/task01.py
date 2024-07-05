'''
1 Напишите простое веб-приложение на Flask, которое будет выводить на экран текст "Hello, World!".

Добавьте две дополнительные страницы в ваше вебприложение:
○ страницу "about"
○ страницу "contact".

Написать функцию, которая будет принимать на вход два числа и выводить на экран их сумму.

Написать функцию, которая будет принимать на вход строку и выводить на экран ее длину.

Написать функцию, которая будет выводить на экран HTML страницу с заголовком "Моя первая HTML страница" и абзацем "Привет, мир!".

Написать функцию, которая будет выводить на экран HTML страницу с таблицей, содержащей информацию о студентах.
Таблица должна содержать следующие поля: "Имя", "Фамилия", "Возраст", "Средний балл".
Данные о студентах должны быть переданы в шаблон через контекст.

Написать функцию, которая будет выводить на экран HTML страницу с блоками новостей.
Каждый блок должен содержать заголовок новости, краткое описание и дату публикации.
Данные о новостях должны быть переданы в шаблон через контекст.

Создать базовый шаблон для всего сайта, содержащий общие элементы дизайна (шапка, меню, подвал), и
дочерние шаблоны для каждой отдельной страницы.
Например, создать страницу "О нас" и "Контакты", используя базовый шаблон.


'''
from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/about/')
def about():
    return 'ABOUT'


@app.route('/contact/')
def contact():
    return 'CONTACT'


@app.route('/<int:num_1>/<int:num_2>')
def sum_nums(num_1, num_2):
    return str(num_1 + num_2)


@app.route('/len/<string:text>/')
def len_str(string: str):
    return str(len(string))


@app.route('/html1/')
def html1():
    ryiba = 'Привет, мир!'
    text = '<h1> Моя первая HTML страница </h1>\n<p>' + ryiba + '</p>'
    return text


@app.route('/html1_tem/')
def html1_tem():
    return render_template('html1.html')


@app.route('/students/')
def students():
    head = {'first_name': 'Имя',
            'last_name': 'Фамилия',
            'age': 'Возраст',
            'grade': 'Средний бал'}
    _users = [

        {'first_name': 'Иван',
         'last_name': 'Пагодов',
         'age': 24,
         'grade': 84},

        {'first_name': 'Алексей',
         'last_name': 'Свидов',
         'age': 28,
         'grade': 88},

        {'first_name': 'Анна',
         'last_name': 'Лакшина',
         'age': 21,
         'grade': 94}

    ]
    context = {'users': _users}
    # return render_template('students.html', **context)
    return render_template('stud2.html', **head, **context)


@app.route('/news/')
def news():
    _news = [
        {
            'title': 'Пожар',
            'text': 'Горит здание Евроньюс',
            'date': datetime.now().strftime('%H:%M - %d.%m.%Y года')
        },
        {
            'title': 'Молния',
            'text': 'Страны активно покидают комиссию ООН',
            'date': datetime.now().strftime('%H:%M - %d.%m.%Y года')
        },
        {
            'title': 'Задержание',
            'text': 'Задержали последнюю падлу - вымогателя Гуся Гасана',
            'date': datetime.now().strftime('%H:%M - %d.%m.%Y года')
        }
    ]
    context = {'news': _news}
    return render_template('news.html', **context)


@app.route('/abt/')
def abt():
    context = {'title': 'О нас'}
    return render_template('about.html', **context)


@app.route('/contacts/')
def contacts():
    context = {'title': 'Контакты'}
    return render_template('contacts.html', **context)

# Продолжение на семинарах

if __name__ == '__main__':
    app.run(debug=True)
