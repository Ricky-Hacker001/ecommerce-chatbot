# routes.py
from flask import request, jsonify
from models import Product
from extensions import db
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models import User
from flask_jwt_extended import jwt_required, get_jwt_identity


def init_routes(app):
     # -------------------- Product Search Endpoint --------------------
    @app.route("/api/products/search", methods=["GET"])
    @app.route('/api/products/search')
    def search_products():
        query = request.args.get('q', '').lower()

        results = Product.query.filter(
            (Product.name.ilike(f"%{query}%")) |
            (Product.brand.ilike(f"%{query}%")) |
            (Product.category.ilike(f"%{query}%")) |
            (Product.description.ilike(f"%{query}%"))
        ).all()

        return jsonify([p.to_dict() for p in results])
     # -------------------- Cart Management Endpoint --------------------
    @app.route('/api/cart', methods=['GET', 'POST'])
    @jwt_required()
    def manage_cart():
        user_id = get_jwt_identity()  # get logged-in user id from token
        # Your cart logic here, e.g., fetch or update cart for user_id
        return jsonify({"msg": "Cart accessed for user", "user_id": user_id})
    # -------------------- User Profile Endpoint --------------------
    @app.route('/api/user/profile', methods=['GET'])
    @jwt_required()
    def user_profile():
        user_id = get_jwt_identity()
        user = User.query.get(user_id)

        if not user:
            return jsonify({'msg': 'User not found'}), 404

        return jsonify({
            'username': user.username,
            'email': user.email if hasattr(user, 'email') else ''
        })
