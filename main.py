from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def main():
    return "<h1>Миссия Колонизация Марса</h1>"


@app.route('/index')
def index():
    return "<h3>И на Марсе будут яблони цвести!<h3>"


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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
