from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity
)
from extensions import db
from models import User

# Factory function to create and configure the Flask app
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'# Used for general app encryption
    app.config['JWT_SECRET_KEY'] = 'jwt-secret-key'# Secret for encoding JWT tokens
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'# SQLite DB

    CORS(app)
    JWTManager(app)
    db.init_app(app)

    with app.app_context():
        from models import Product
        db.create_all()

    from routes import init_routes
    init_routes(app)

    return app

app = create_app()

# ------------------ AUTH ROUTES ------------------

# User Signup Route
@app.route('/api/auth/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'msg': 'Username and password required'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'msg': 'Username already exists'}), 400

    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return jsonify({'msg': 'User created successfully'}), 201


# User Login Route
@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if not user or not user.check_password(password):
        return jsonify({'msg': 'Invalid username or password'}), 401

    access_token = create_access_token(identity=user.id)
    refresh_token = create_refresh_token(identity=user.id)

    return jsonify(access_token=access_token, refresh_token=refresh_token), 200

# Refresh Access Token Route
@app.route('/api/auth/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    return jsonify(access_token=access_token)


if __name__ == "__main__":
    app.run(debug=True)
