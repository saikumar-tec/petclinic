# ==========================================
# database.py
# SQLAlchemy Database Initialization
# ==========================================

from flask_sqlalchemy import SQLAlchemy

# Create SQLAlchemy object
db = SQLAlchemy()


# Optional helper function
def init_db(app):
    """
    Initialize database with Flask application.
    """

    db.init_app(app)

    with app.app_context():
        db.create_all()