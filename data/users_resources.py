from flask import jsonify, request
from flask_restful import abort, Resource

from data import db_session
from data.users import User
from data.parser import parser_user
from werkzeug.security import generate_password_hash


def abort_if_user_not_found(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        abort(404, message=f"User {user_id} not found")


def set_password(password):
    return generate_password_hash(password)


class UserResource(Resource):
    def get(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        return jsonify({'user': user.to_dict(
            only=('name', 'surname', 'age', 'position', 'speciality', 'address', 'email', 'hashed_password'))})

    def delete(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})

    def put(self, user_id):
        abort_if_user_not_found(user_id)
        # if not request.json:
        #     return make_response(jsonify({'error': 'Empty request'}), 400)
        db_sess = db_session.create_session()
        user_to_edit = db_sess.query(User).get(user_id)
        # if not user_to_edit:
        #     return make_response(jsonify({'error': 'Not found'}), 404)
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
        user_to_edit.hashed_password = user_to_edit.hashed_password if 'hashed_password' not in request.json else \
        request.json[
            'hashed_password']
        db_sess.add(user_to_edit)
        db_sess.commit()
        return jsonify({'successful': 'OK'})


class UserListResource(Resource):
    def get(self):
        session = db_session.create_session()
        user = session.query(User).all()
        return jsonify({'user': [item.to_dict(
            only=('name', 'surname', 'age', 'position', 'speciality', 'address', 'email', 'hashed_password')) for item
            in user]})

    def post(self):
        args = parser_user.parse_args()
        session = db_session.create_session()
        user = User(
            name=args['name'],
            surname=args['surname'],
            age=args['age'],
            position=args['position'],
            speciality=args['speciality'],
            address=args['address'],
            email=args['email'],
            hashed_password=set_password(args['hashed_password'])
        )
        session.add(user)
        session.commit()
        return jsonify({'id': user.id})
