import flask
from flask import jsonify, make_response, request
from werkzeug.security import generate_password_hash

from data import db_session
from data.users import User

blueprint = flask.Blueprint(
    'user_api',
    __name__,
    template_folder='templates'
)


def set_password(password):
    return generate_password_hash(password)


@blueprint.route('/api/users', methods=['GET'])
def get_users():
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    return jsonify(
        {
            'users':
                [item.to_dict(only=(
                    'name', 'surname', 'age', 'position', 'speciality', 'address', 'email', 'hashed_password',
                    'modified_date'))
                    for item in users]
        }
    )


@blueprint.route('/api/users/<int:user_id>', methods=['GET'])
def get_one_user(user_id):
    db_sess = db_session.create_session()
    users = db_sess.query(User).get(user_id)
    if not users:
        return make_response(jsonify({'error': 'Not found'}), 404)
    return jsonify(
        {
            'users': users.to_dict(only=(
                'name', 'surname', 'age', 'position', 'speciality', 'address', 'email', 'hashed_password',
                'modified_date'))
        }
    )


@blueprint.route('/api/users', methods=['POST'])
def create_user():
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in
                 ['name', 'surname', 'age', 'position', 'speciality', 'address', 'email', 'hashed_password']):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    db_sess = db_session.create_session()
    user = User(
        name=request.json['name'],
        surname=request.json['surname'],
        age=request.json['age'],
        position=request.json['position'],
        speciality=request.json['speciality'],
        address=request.json['address'],
        email=request.json['email'],
        hashed_password=set_password(request.json['hashed_password']),
    )
    db_sess.add(user)
    db_sess.commit()
    return jsonify({'id': user.id})


@blueprint.route('/api/users/delete/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    db_sess = db_session.create_session()
    users = db_sess.query(User).get(user_id)
    if not users:
        return make_response(jsonify({'error': 'Not found'}, 404))
    db_sess.delete(users)
    db_sess.commit()
    return jsonify(
        {
            'message': ['delete was successful']
        }
    )


@blueprint.route('/api/users/edit/<int:user_id>', methods=['PUT'])
def edit_user(user_id):
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    db_sess = db_session.create_session()
    user_to_edit = db_sess.query(User).get(user_id)
    if not user_to_edit:
        return make_response(jsonify({'error': 'Not found'}), 404)
    user_to_edit.name = user_to_edit.name if 'name' not in request.json else request.json['name']
    user_to_edit.surname = user_to_edit.surname if 'surname' not in request.json else request.json[
        'surname']
    user_to_edit.age = user_to_edit.age if 'age' not in request.json else request.json['age']
    user_to_edit.position = user_to_edit.position if 'position' not in request.json else request.json[
        'position']
    user_to_edit.speciality = user_to_edit.speciality if 'speciality' not in request.json else request.json[
        'speciality']
    user_to_edit.address = user_to_edit.address if 'address' not in request.json else request.json[
        'address']
    user_to_edit.email = user_to_edit.email if 'email' not in request.json else request.json[
        'email']
    user_to_edit.hashed_password = user_to_edit.hashed_password if 'hashed_password' not in request.json else request.json[
        'hashed_password']
    db_sess.add(user_to_edit)
    db_sess.commit()
    return jsonify({'successful': 'OK'})
