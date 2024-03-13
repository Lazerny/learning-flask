from requests import post, get

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
print(get('http://localhost:8080/api/v2/jobs').json())
print(get('http://localhost:8080/api/v2/jobs/1').json())
print(get('http://localhost:8080/api/v2/jobs/asdf').json())
print(get('http://localhost:8080/api/v2/jobs/43').json())
print()
print(post('http://localhost:8080/api/v2/jobs').json())
print(post('http://localhost:8080/api/v2/jobs', json={'job': 'JOB!!'}).json())
print(post('http://localhost:8080/api/v2/jobs', json={'job': 'JOB!!',
                                                       'team_leader': 1,
                                                       'work_size': 16,
                                                       'collaborators': '1, 2, 3, 4',
                                                       'start_date': 'start_date',
                                                       'end_date': 'end_date',
                                                       'is_finished': False}).json())
