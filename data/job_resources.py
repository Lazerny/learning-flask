from flask import jsonify, request
from flask_restful import abort, Resource

from data import db_session
from data.jobs import Jobs
from data.parser import parser_job
from werkzeug.security import generate_password_hash


def abort_if_job_not_found(job_id):
    session = db_session.create_session()
    job = session.query(Jobs).get(job_id)
    if not job:
        abort(404, message=f"Job {job_id} not found")


class JobResource(Resource):
    def get(self, job_id):
        abort_if_job_not_found(job_id)
        session = db_session.create_session()
        job = session.query(Jobs).get(job_id)
        return jsonify({'job': job.to_dict(
            only=('job', 'team_leader', 'work_size', 'collaborators', 'start_date',
                  'end_date', 'is_finished'))})

    def put(self, job_id):
        abort_if_job_not_found(job_id)
        # if not request.json:
        #     return make_response(jsonify({'error': 'Empty request'}), 400)
        db_sess = db_session.create_session()
        job_to_edit = db_sess.query(Jobs).get(job_id)
        # if not job_to_edit:
        #     return make_response(jsonify({'error': 'Not found'}), 404)
        job_to_edit.job = job_to_edit.job if 'job' not in request.json else request.json['job']
        job_to_edit.team_leader = job_to_edit.team_leader if 'team_leader' not in request.json else request.json[
            'team_leader']
        job_to_edit.work_size = job_to_edit.work_size if 'work_size' not in request.json else request.json['work_size']
        job_to_edit.collaborators = job_to_edit.collaborators if 'collaborators' not in request.json else request.json[
            'collaborators']
        job_to_edit.is_finished = job_to_edit.is_finished if 'is_finished' not in request.json else request.json[
            'is_finished']
        db_sess.add(job_to_edit)
        db_sess.commit()
        return jsonify({'successful': 'OK'})

    def delete(self, job_id):
        abort_if_job_not_found(job_id)
        session = db_session.create_session()
        job = session.query(Jobs).get(job_id)
        session.delete(job)
        session.commit()
        return jsonify({'success': 'OK'})


class JobListResource(Resource):
    def get(self):
        session = db_session.create_session()
        job = session.query(Jobs).all()
        return jsonify({'job': [item.to_dict(
            only=('job', 'team_leader', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished')) for item
            in job]})

    def post(self):
        args = parser_job.parse_args()
        session = db_session.create_session()
        job = Jobs(
            job=args['job'],
            team_leader=args['team_leader'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            is_finished=args['is_finished']
        )
        session.add(job)
        session.commit()
        return jsonify({'id': job.id})
