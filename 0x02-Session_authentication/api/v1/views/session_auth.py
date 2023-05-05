#!/usr/bin/env python3
"""Session authentication view"""

from api.v1.views import app_views
from flask import abort, request, jsonify, Response
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=True)
def session_login():
    """session login route"""
    email = request.form.get('email')
    if email is None:
        return jsonify({'error': 'missing email'}), 400
    password = request.form.get('password')
    if password is None:
        return jsonify({'error': 'password missing'}), 400

    users = User.search({"email": email})
    if users == []:
        return jsonify({'error': 'no user found for this email'}), 404
    user = users[0]
    if user.is_valid_password(password):
        from api.v1.app import auth
        session_id = auth.create_session(user.id)
        response = jsonify(user.to_json())
        response.set_cookie(os.getenv('SESSION_NAME'), session_id)
        return response
    return jsonify({'error': "wrong password"}), 401


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=True)
def delete_session():
    """delete a session"""
    from api.v1.app import auth
    if auth.destroy_session(request):
        return jsonify({}), 200
    abort(404)
