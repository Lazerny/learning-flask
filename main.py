# github.com/Lazerny/learning-flask

import json
from flask_login import LoginManager, current_user, login_user, login_required, logout_user

import sqlalchemy

from data import db_session

from flask import Flask, url_for, request, render_template, redirect

from forms.Job import JobsForm
from forms.user import RegisterForm

from data.users import User
from data.jobs import Jobs
from forms.user import LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/auto_answer')
def answer():
    data = {"title": "Анкета", 'surname': 'Ivanov', 'name': 'Ivan', "education": 'высшее', 'profession': 'Инженер', }
    return render_template('auto_answer.html', title=data['title'], data=data)


@app.route('/training/<prof>')
def new_prof(prof):
    return render_template('input.html', prof=prof, title='Тренировки')


@app.route('/list_prof/<list>')
def list_prof(list):
    prof = ['инженер', 'строитель', 'врач', 'программист', 'биолог', 'химик', "летчик", "физик"]
    return render_template('prof.html', list=list, prof=prof)


@app.route('/promotion')
def promotion():
    strings = ['Человечество вырастает из детства.', "Человечеству мала одна планета.",
               "Мы сделаем обитаемыми безжизненные пока планеты.", "И начнем с Марса!", "Присоединяйся!"]
    return '<br>'.join(strings)


@app.route('/image_sample')
def image():
    return f'''<img src="{url_for('static', filename='img/riana.jpg')}" 
           alt="здесь должна была быть картинка, но не нашлась">'''


@app.route('/image_mars')
def return_sample_page():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.jpg')}"
                    alt="здесь должна была быть картинка, но не нашлась">
                  </body>
                </html>"""


@app.route('/promotion_image')
def bootstrap():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Жди нас Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас Марс!</h1>
                                        <img src="{url_for('static', filename='img/mars.jpg')}"
                    alt="здесь должна была быть картинка, но не нашлась">
                    <div class="alert alert-primary" role="alert">
                      Человечество вырастает из детства.
                    </div>

                    <div class="alert alert-secondary" role="alert">
                      Человечеству мала одна планета.
                    </div>

                    <div class="alert alert-info" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>

                    <div class="alert alert-warning" role="alert">
                      И начнем с Марса!
                    </div>

                    <div class="alert alert-danger" role="alert">
                      Присоединяйся!
                    </div>
                  </body>
                </html>'''


@app.route('/greeting/<username>')
def greeting(username):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                   <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>Привет, {username}</title>
                  </head>
                  <body>
                    <h1>Привет, {username}!</h1>
                  </body>
                </html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Анкета претендента <br> на участие в миссии</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите фамилию" name="surname">
                                    <input type="text" class="form-control" id="password" placeholder="Введите имя" name="name">
                                    <input type="email" class="form-control" id="password" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>
                                     <div class="form-group">
                                             <label for="form-check">Какие у вас профессии</label>
                                             <div class="form-check">
                                                <input type="checkbox" class="form-check-input" id="acceptRules1" name="accept">
                                                <label class="form-check-label" for="acceptRules1">Инженер-строитель</label>
                                            </div>
                                             <div class="form-check">
                                                <input type="checkbox" class="form-check-input" id="acceptRules2" name="accept">
                                                <label class="form-check-label" for="acceptRules2">Пилот</label>
                                            </div>

                                             <div class="form-check">
                                                <input type="checkbox" class="form-check-input" id="acceptRules3" name="accept">
                                                <label class="form-check-label" for="acceptRules3">Программист</label>
                                            </div>

                                             <div class="form-check">
                                                <input type="checkbox" class="form-check-input" id="acceptRules4" name="accept">
                                                <label class="form-check-label" for="acceptRules4">Строитель</label>
                                            </div>

                                             <div class="form-check">
                                                <input type="checkbox" class="form-check-input" id="acceptRules5" name="accept">
                                                <label class="form-check-label" for="acceptRules5">Космонавт</label>
                                            </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="acceptt">
                                        <label class="form-check-label" for="acceptRules">Готовы ли вы остаться на Марсе</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>                            
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['sex'])
        print(request.form['about'])
        print(request.form['acceptt'])
        print(request.form['file'])
        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def choice_your_planet(planet_name):
    return f"""<head>
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                  </head>
    <h1>Моё предложение: {planet_name}<h1>
                <h2>Эта планета близка к земле<h2>

                    <div class="alert alert-info" role="alert">
                    На ней много необходимых ресурсов
                    </div>

                    <div class="alert alert-warning" role="alert">
                    На ней есть вода и атмосфера
                    </div>

                    <div class="alert alert-success" role="alert">
                    На ней есть небольшое магнитное поле
                    </div>

                    <div class="alert alert-primary" role="alert">
                    Наконец, она просто красива!
                    </div>
"""


@app.route('/distribution')
def distribution():
    with open('pilots.json', 'rb') as file:
        pilots = json.load(file)
    return render_template('distribution.html', pilots=pilots)


@app.route('/table/<sex>/<int:age>')
def table(sex, age):
    params = {}
    if sex == 'male':
        params['color'] = (0 + age, 191 - age, 255 - age)
        if age < 21:
            params['image'] = 'yong-alien.jpg'
        else:
            params['image'] = 'old-alien.jpg'
    elif sex == 'female':
        params['color'] = (255 - age, 192 - age, 203 - age)
        if age < 21:
            params['image'] = 'yong-alien.jpg'
        else:
            params['image'] = 'old-alien.jpg'
    return render_template('table.html', params=params)


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def result_selection(nickname, level, rating):
    return f"""                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
    <h1>Результаты отбора<h1>
    <h2>Претендента на участие в миссии {nickname}:<h2>

    <div class="alert alert-primary" role="alert">
    Поздравляем ваш рейтинг после {level} этапа отбора 
    </div>
    Составляет {rating}!
    <div class="alert alert-success" role="alert">
    Желаем удачи!
    </div>
"""


@app.route('/')
def work():
    db_sess = db_session.create_session()
    news = db_sess.query(Jobs).filter(Jobs.is_finished is not True)
    return render_template("works.html", news=news)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/add_jobs', methods=['GET', 'POST'])
@login_required
def add_news():
    form = JobsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        j = Jobs()
        j.job = form.job.data
        j.work_size = form.work_size.data
        j.collaborators = form.coloborators.data
        j.is_finished = False
        current_user.job.append(j)
        db_sess.merge(current_user)
        db_sess.commit()
        return redirect('/')
    return render_template('news.html', title='Добавление новости',
                           form=form)


if __name__ == '__main__':
    # name_db = input()
    db_session.global_init(f'db/mars_explorer.db')
    app.run(port=8080, host='127.0.0.1')
    # session = db_session.create_session()
    # user = User()
    # user.surname = "Scott"
    # user.name = "Ridley"
    # user.age = 21
    # user.position = "captain"
    # user.speciality = "research engineer"
    # user.address = "module_1"
    # user.email = "scott_chief@mars.org"
    # user.hashed_password = "cap"
    # session.add(user)
    #
    # user = User()
    # user.surname = "Robert"
    # user.name = "Smith"
    # user.age = 24
    # user.position = "no captain"
    # user.speciality = "engineer"
    # user.address = "module_2"
    # user.email = "robert_smith@mars.org"
    # user.hashed_password = "123"
    # session.add(user)
    #
    # user = User()
    # user.surname = "Rebecca"
    # user.name = "Smith"
    # user.age = 23
    # user.position = "no captain"
    # user.speciality = "developer"
    # user.address = "module_3"
    # user.email = "rebecca_smith@mars.org"
    # user.hashed_password = "qwe"
    # session.add(user)
    #
    # user = User()
    # user.surname = "North"
    # user.name = "Harvat"
    # user.age = 60
    # user.position = "no captain"
    # user.speciality = "developer"
    # user.address = "module_5"
    # user.email = "north_har@mars.org"
    # user.hashed_password = "bfbdg"
    # session.add(user)
    #
    # job = Jobs()
    # job.team_leader = 1
    # job.job = 'deployment of residential modules 1 and 2'
    # job.work_size = 15
    # job.collaborators = '2, 3'
    # job.is_finished = False
    # session.add(job)
    # session.commit()
    # for i in session.query(User).filter(sqlalchemy.and_(User.age < 21), (User.address == 'module_1')):
    #     i.address = 'module_3'
    #     session.commit()
