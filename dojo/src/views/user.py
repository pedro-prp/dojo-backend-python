from flask import Blueprint, request
from controllers.user import insert_new_user, get_all_users


user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/api/user/', methods=['GET', 'POST'])
def view_user():
    if request.method == 'POST':
        content = request.json

        response, status = insert_new_user(content)

    elif request.method == 'GET':
        response, status = get_all_users()

    return response, status
        