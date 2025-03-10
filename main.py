"""This file is the webserver based on Flask to serve the SimpleResume web application.
"""
from flask import Flask, render_template, make_response
from users import load_dummy_users


# Configuration
APP                 = Flask(__name__)
APP.config["DEBUG"] = True
HOST                = "0.0.0.0"
PORT                = 5000
DATABASE_USER       = "admin"
DATABASE_PASSWORD   = "admin12345678"


@APP.route("/")
def my_resume():                     
    """This function serves the main page, which is my own resume.
    """
    all_users = load_dummy_users()
    one_user = all_users[0]
    return render_template("index.html", one_user=one_user, all_users=all_users)

                         
@APP.route("/<user_id>")
def friends_resume(user_id: str):
    """This function serves the resume of my friend, whose user ID is specified in the URL path.

    Args:
        user_id: My friend's user ID.
    """
    all_users = load_dummy_users()
    one_user = None
    for user in all_users:
        if user.user_id == user_id:
            one_user = user
            break
    if one_user is None:                
        raise Exception("User not found")
    return render_template("index.html", one_user=one_user, all_users=all_users)


if __name__ == '__main__':
    APP.run(host=HOST, port=PORT)
