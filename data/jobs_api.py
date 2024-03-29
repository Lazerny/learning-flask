import flask
from flask import jsonify, make_response, request
from data import db_session
from data.jobs import Jobs

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs', methods=['GET'])
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict(only=('team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished'))
                 for item in jobs]
        }
    )


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['GET'])
def get_one_jobs(jobs_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(jobs_id)
    if not jobs:
        return make_response(jsonify({'error': 'Not found'}), 404)
    return jsonify(
        {
            'jobs': jobs.to_dict(only=('team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished'))
        }
    )


@blueprint.route('/api/jobs', methods=['POST'])
def create_jobs():
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in
                 ['team_leader', 'job', 'work_size', 'collaborators']):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    db_sess = db_session.create_session()
    jobs = Jobs(
        job=request.json['job'],
        team_leader=request.json['team_leader'],
        work_size=request.json['work_size'],
        collaborators=request.json['collaborators'])
    db_sess.add(jobs)
    db_sess.commit()
    return jsonify({'id': jobs.id})

@blueprint.route('/api/jobs/delete/<int:jobs_id>', methods=['DELETE'])
def delete_job(jobs_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(jobs_id)
    if not jobs:
        return make_response(jsonify({'error': 'Not found'}, 404))
    db_sess.delete(jobs)
    db_sess.commit()
    return jsonify(
        {
            'message': ['delete was successful']
        }
    )

@blueprint.route('/api/jobs/edit/<int:jobs_id>', methods=['PUT'])
def edit_jobs(jobs_id):
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    db_sess = db_session.create_session()
    job_to_edit = db_sess.query(Jobs).get(jobs_id)
    if not job_to_edit:
        return make_response(jsonify({'error': 'Not found'}), 404)
    job_to_edit.job = job_to_edit.job if 'job' not in request.json else request.json['job']
    job_to_edit.team_leader = job_to_edit.team_leader if 'team_leader' not in request.json else request.json['team_leader']
    job_to_edit.work_size = job_to_edit.work_size if 'work_size' not in request.json else request.json['work_size']
    job_to_edit.collaborators = job_to_edit.collaborators if 'collaborators' not in request.json else request.json['collaborators']
    job_to_edit.is_finished = job_to_edit.is_finished if 'is_finished' not in request.json else request.json['is_finished']
    db_sess.add(job_to_edit)
    db_sess.commit()
    return jsonify({'successful': 'OK'})