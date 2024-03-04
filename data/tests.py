from requests import post, get

print(get('http://localhost:8080/api/jobs').json())
print(get('http://localhost:8080/api/jobs/1').json())
print(get('http://localhost:8080/api/jobs/rr').json())

print()

print(post('http://localhost:8080/api/jobs', json={}).json())

print(post('http://localhost:8080/api/jobs',
           json={'title': 'Заголовок'}).json())
#
# print(post('http://localhost:8080/api/jobs',
#            json={'job': 'Заголовок',
#                  'work_size': 5,
#                  'collaborators': '1',
#                  'team_leader': 1}).json())