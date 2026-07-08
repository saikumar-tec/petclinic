from flask import Blueprint, request, jsonify, session

# Blueprint
auth_bp = Blueprint("auth", __name__)

#########################################################
# LOGIN
#########################################################

@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    # Default Admin Credentials
    if username == "admin" and password == "admin123":

        session["loggedIn"] = True
        session["username"] = username

        return jsonify({

            "message": "Login Successful",
            "username": username

        }), 200

    return jsonify({

        "message": "Invalid Username or Password"

    }), 401


#########################################################
# LOGOUT
#########################################################

@auth_bp.route("/logout", methods=["POST"])
def logout():

    session.clear()

    return jsonify({

        "message": "Logged Out Successfully"

    }), 200


#########################################################
# CHECK LOGIN STATUS
#########################################################

@auth_bp.route("/check-login", methods=["GET"])
def check_login():

    if session.get("loggedIn"):

        return jsonify({

            "loggedIn": True,
            "username": session.get("username")

        }), 200

    return jsonify({

        "loggedIn": False

    }), 401


#########################################################
# HEALTH
#########################################################

@auth_bp.route("/health", methods=["GET"])
def health():

    return jsonify({

        "status": "Healthy",
        "application": "Pet Clinic API",
        "version": "1.0"

    })