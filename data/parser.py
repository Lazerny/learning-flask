from flask_restful import reqparse

parser_user = reqparse.RequestParser()
parser_user.add_argument('name', required=True)
parser_user.add_argument('surname', required=True)
parser_user.add_argument('age', required=True, type=int)
parser_user.add_argument('position', required=True)
parser_user.add_argument('speciality', required=True)
parser_user.add_argument('address', required=True)
parser_user.add_argument('email', required=True)
parser_user.add_argument('hashed_password', required=True)

parser_job = reqparse.RequestParser()
parser_job.add_argument('job', required=True)
parser_job.add_argument('team_leader', required=True, type=int)
parser_job.add_argument('work_size', required=True, type=int)
parser_job.add_argument('collaborators', required=True)
parser_job.add_argument('is_finished', required=True, type=bool)