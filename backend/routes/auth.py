from flask import Blueprint, request, jsonify, session

# Blueprint
auth_bp = Blueprint("auth", __name__)

#########################################################
# LOGIN
#########################################################

@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    email = data["email"]
    password = data["password"]

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({"message":"User not found"}),404

    if user.password != password:
        return jsonify({"message":"Invalid Password"}),401

    session["loggedIn"] = True
    session["role"] = user.role
    session["username"] = user.fullname

    return jsonify({

        "message":"Login Successful",

        "role":user.role,

        "username":user.fullname

    })


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