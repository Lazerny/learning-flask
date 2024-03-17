# github.com/Lazerny/learning-flask

import json
import os

import flask

from flask_login import LoginManager, current_user, login_user, login_required, logout_user

import sqlalchemy
from werkzeug.utils import secure_filename

from data import db_session, jobs_api, users_resources, job_resources

from flask import Flask, url_for, request, render_template, redirect, make_response, jsonify, send_from_directory, abort

from forms.Job import JobsForm
from forms.user import RegisterForm
from forms.Department import DepartmentForm
from flask import Flask, url_for, request, render_template, redirect, flash

from data.users import User
from data.departments import Department
from data.jobs import Jobs
from forms.user import LoginForm
from data.category import Category, association_table
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)

@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)


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
    jobs = db_sess.query(Jobs).filter(Jobs.is_finished is not True)
    for i in jobs:
        print(i.team_leader)
    return render_template("works.html", jobs=jobs)


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
def add_jobs():
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
    return render_template('jobs.html', title='Добавление работы',
                           form=form)


@app.route('/jobs/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_jobs(id):
    form = JobsForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).filter(Jobs.id == id,
                                          Jobs.team_leader == current_user.id
                                          ).first()
        if jobs:
            form.job.data = jobs.job
            form.work_size.data = jobs.work_size
            form.coloborators.data = jobs.collaborators
            form.is_finished.data = jobs.is_finished
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).filter(Jobs.id == id,
                                          Jobs.team_leader == current_user.id
                                          ).first()
        if jobs:
            jobs.job = form.job.data
            jobs.work_size = form.work_size.data
            jobs.collaborators = form.coloborators.data
            jobs.is_finished = form.is_finished.data
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('jobs.html',
                           title='Редактирование работы',
                           form=form
                           )


@app.route('/jobs_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def jobs_delete(id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).filter(Jobs.id == id,
                                      Jobs.team_leader == current_user.id
                                      ).first()
    if jobs:
        db_sess.delete(jobs)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')


@app.route('/departments')
def departments():
    session = db_session.create_session()
    departments = session.query(Department)
    return render_template("departments.html", departments=departments)


@app.route("/departments/<int:id>", methods=["GET", "POST"])
@login_required
def edit_departments(id):
    form = DepartmentForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        department = db_sess.query(Department).filter(Department.id == id,
                                                      Department.chief == current_user.id
                                                      ).first()
        if department:
            form.title.data = department.title
            current_user.id = department.chief
            form.members.data = department.members
            form.email.data = department.email
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        department = db_sess.query(Department).filter(Department.id == id,
                                                      Department.chief == current_user.id
                                                      ).first()
        if department:

            department.title = form.title.data
            department.chief = current_user.id
            department.members = form.members.data
            department.email = form.email.data
            db_sess.commit()
            return redirect('/departments')
        else:
            abort(404)
    return render_template('add-department.html',
                           title='Редактирование отдела',
                           form=form
                           )


@app.route('/departments_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def department_delete(id):
    db_sess = db_session.create_session()
    department = db_sess.query(Department).filter(Department.id == id,
                                      Department.chief == current_user.id
                                      ).first()
    if department:
        db_sess.delete(department)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/departments')


@app.route("/departments/add", methods=['GET', 'POST'])
@login_required
def add_department():
    form = DepartmentForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        department = Department()

        department.title = form.title.data
        department.chief = current_user.id
        department.members = form.members.data
        department.email = form.email.data

        current_user.department.append(department)
        session.merge(current_user)
        session.commit()
        return redirect('/departments')
    return render_template('add-department.html', title='Добавление отдела',
                           form=form)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


if __name__ == '__main__':
    # name_db = input()
    db_session.global_init(f'db/mars_explorer.db')
    # app.register_blueprint(jobs_api.blueprint)
    api.add_resource(users_resources.UserListResource, '/api/v2/users')
    api.add_resource(job_resources.JobListResource, '/api/v2/jobs')
    api.add_resource(users_resources.UserResource, '/api/v2/users/<int:user_id>')
    api.add_resource(job_resources.JobResource, '/api/v2/jobs/<int:job_id>')
    app.run(port=8080, host='127.0.0.1')

    # session = db_session.create_session()
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

    # departament = Department()
    # departament.title = 'team_1'
    # departament.chief = 1
    # departament.members = '1, 2, 3, 4'
    # departament.email = 'departament1@mail.net'
    # session.add(departament)
    # session.commit()
    # mans = []
    # dep = session.query(Department).filter(Department.id == 1).first()
    # for user in dep.members.split(', '):
    #     time = 0
    #     for job in session.query(Jobs).filter(Jobs.collaborators.like(f'%{user}%')):
    #         time += job.work_size
    #     if time > 25:
    #         man = session.query(User).filter(User.id == user).first()
    #         if man not in mans:
    #             mans.append(man)
    #             print(man.surname, man.name)
