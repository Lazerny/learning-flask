from requests import post, get, put, delete
# get работы
# print(get('http://127.0.0.1:8080/api/jobs').json())
# print(get('http://127.0.0.1:8080/api/jobs/1').json())
# print(get('http://127.0.0.1:8080/api/jobs/88').json())
# print(get('http://127.0.0.1:8080/api/jobs/rr').json())

# ДОБАВЛЕНИЕ РАБОТ
# print()

# print(post('http://127.0.0.1:8080/api/jobs', json={}).json())
#
# print(post('http://127.0.0.1:8080/api/jobs',
#            json={'title': 'Заголовок'}).json())
#
# print(post('http://127.0.0.1:8080/api/jobs',
#            json={'job': 'Заголовок',
#                  'work_size': 5,
#                  'collaborators': '1',
#                  'team_leader': 1}).json())
# print()
# УДАЛЕНИЕ РАБОТ
# print(delete('http://127.0.0.1:8080/api/jobs/delete/35').json())
# print(delete('http://127.0.0.1:8080/api/jobs/delete').json())
# print(delete('http://127.0.0.1:8080/api/jobs/delete/1111111').json())
# ИЗМЕНЕНИЕ РАБОТ
# print(put('http://127.0.0.1:8080/api/jobs/edit/34',
#            json={'job': 'tutol',
#                  'work_size': 9,
#                  'collaborators': '1, 2',
#                  'team_leader': 1,
#                  'is_finished': False}).json())
# print(put('http://127.0.0.1:8080/api/jobs/edit/',
#            json={'job': 'tutol',
#                  'work_size': 9,
#                  'collaborators': '1, 2',
#                  'team_leader': 1,
#                  'is_finished': False}).json())
#
# print(put('http://127.0.0.1:8080/api/jobs/edit/99999999',
#            json={'job': 'tutol',
#                  'work_size': 9,
#                  'collaborators': '1, 2',
#                  'team_leader': 1,
#                  'is_finished': False}).json())
# print(put('http://127.0.0.1:8080/api/jobs/edit/34', json={}).json())
# print()
# print(get('http://127.0.0.1:8080/api/jobs').json())
#тест пользователей
print(get('http://127.0.0.1:8080/api/users').json())
print(get('http://127.0.0.1:8080/api/users/7').json())
# print(post('http://127.0.0.1:8080/api/users', json={
#     'name': 'name',
#     'surname': 'surname',
#     'age': 55,
#     'position': 'position',
#     'speciality': 'speciality',
#     'address': 'address',
#     'email': 'email@',
#     'hashed_password': 'hashed_password'
# }).json())
# print(delete('http://127.0.0.1:8080/api/users/delete/8').json())
# print(put('http://127.0.0.1:8080/api/users/edit/7', json={
#     'position': 'developer',
#     'speciality': 'frontend'
# }).json())
# ...
# print(get('http://localhost:8080/api/v2/users').json())
# print(get('http://localhost:8080/api/v2/users/1').json())
# print(get('http://localhost:8080/api/v2/users/44').json())
# print()
# print(post('http://localhost:8080/api/v2/users').json())
# print(post('http://localhost:8080/api/v2/users', json={'name': 'Nika'}).json())
# print(post('http://localhost:8080/api/v2/users', json={'name': 'Nika',
#                                                        'surname': 'Frolova',
#                                                        'age': 16,
#                                                        'position': 'fat',
#                                                        'speciality': 'speciality',
#                                                        'address': 'module_4',
#                                                        'email': 'email',
#                                                        'hashed_password': 'hashed_password'}).json())
# print(get('http://localhost:8080/api/v2/jobs').json())
# print(get('http://localhost:8080/api/v2/jobs/1').json())
# print(get('http://localhost:8080/api/v2/jobs/asdf').json())
# print(get('http://localhost:8080/api/v2/jobs/43').json())
# print()
# print(post('http://localhost:8080/api/v2/jobs', json={'job': 'JOB!!'}).json())
# print(post('http://localhost:8080/api/v2/jobs', json={'job': 'JOB!!',
#                                                        'team_leader': 1,
#                                                        'work_size': 16,
#                                                        'collaborators': '1, 2, 3, 4',}).json())
