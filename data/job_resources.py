# from flask import jsonify
# from flask_restful import abort, Resource
#
# from data import db_session
# from data.jobs import Jobs
# from data.parser import parser_job
# from werkzeug.security import generate_password_hash
#
#
# def abort_if_job_not_found(job_id):
#     session = db_session.create_session()
#     job = session.query(Jobs).get(job_id)
#     if not job:
#         abort(404, message=f"Job {job_id} not found")
#
#
# def set_password(password):
#     return generate_password_hash(password)
#
#
#
# class JobResource(Resource):
#     def get(self, job_id):
#         abort_if_job_not_found(job_id)
#         session = db_session.create_session()
#         job = session.query(Jobs).get(job_id)
#         return jsonify({'job': job.to_dict(
#             only=('job', 'team_leader', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished'))})
#
#     def delete(self, job_id):
#         abort_if_job_not_found(job_id)
#         session = db_session.create_session()
#         job = session.query(Jobs).get(job_id)
#         session.delete(job)
#         session.commit()
#         return jsonify({'success': 'OK'})
#
#
# class JobListResource(Resource):
#     def get(self):
#         session = db_session.create_session()
#         job = session.query(Jobs).all()
#         return jsonify({'job': [item.to_dict(
#             only=('job', 'team_leader', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished')) for item
#             in job]})
#
#     def post(self):
#         args = parser_job.parse_args()
#         session = db_session.create_session()
#         job = Jobs(
#             job=args['job'],
#             team_leader=args['team_leader'],
#             work_size=args['work_size'],
#             collaborators=args['collaborators'],
#             start_date=args['start_date'],
#             end_date=args['end_date'],
#             is_finished=args['is_finished']
#         )
#         session.add(job)
#         session.commit()
#         return jsonify({'id': job.id})