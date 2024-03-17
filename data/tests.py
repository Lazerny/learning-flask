from requests import post, get, put, delete

# print(get('http://localhost:8080/api/jobs').json())
# print(get('http://localhost:8080/api/jobs/1').json())
# print(get('http://localhost:8080/api/jobs/rr').json())
#
# print()
#
# print(post('http://localhost:8080/api/jobs', json={}).json())
#
# print(post('http://localhost:8080/api/jobs',
#            json={'title': 'Заголовок'}).json())
#
# print(post('http://localhost:8080/api/jobs',
#            json={'job': 'Заголовок',
#                  'work_size': 5,
#                  'collaborators': '1',
#                  'team_leader': 1}).json())

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
# print(get('http://localhost:8080/api/v2/jobs/44').json())
# print()
# print(post('http://localhost:8080/api/v2/jobs').json())
# print(post('http://localhost:8080/api/v2/jobs', json={'job': 'JOB!!'}).json())
# print(post('http://localhost:8080/api/v2/jobs', json={
#                                                       'job': 'JOB!!',
#                                                       'team_leader': 1,
#                                                       'work_size': 16,
#                                                       'collaborators': '1, 2, 3, 4',
#                                                       'is_finished': False}).json())
# print(put('http://127.0.0.1:8080/api/v2/jobs/33',
#            json={'job': 'tutol',
#                  'work_size': 9,
#                  'collaborators': '1, 2',
#                  'team_leader': 1,
#                  'is_finished': False}).json())
# print(delete('http://127.0.0.1:8080/api/v2/jobs/32').json())
# print(get('http://127.0.0.1:8080/api/v2/jobs').json())
# print(post('http://127.0.0.1:8080/api/v2/jobs',
#            json={'job': 'tutol',
#                  'work_size': 9,
#                  'collaborators': '1, 2',
#                  'team_leader': 1,
#                  'is_finished': False}
#            ).json())

# print(get('http://127.0.0.1:8080//api/v2/users').json())
# print(post('http://127.0.0.1:8080//api/v2/users',
#            json={'name': 'tutol',
#                  'surname': 'tutolovich',
#                  'age': 1,
#                  'position': 'position',
#                  'speciality': 'speciality',
#                  'address': 'address',
#                  'email': 'OMG',
#                  'hashed_password': 'hashed_password'}
#            ).json())
print(put('http://127.0.0.1:8080//api/v2/users/8',
           json={'name': 'tutol',
                 'surname': 'tutolovich',
                 'age': 1,
                 'position': 'position',
                 'speciality': 'speciality',
                 'address': 'address',
                 'email': 'email@field',
                 'hashed_password': 'hashed_password'}
           ).json())
# print(delete('http://127.0.0.1:8080//api/v2/users/8').json())