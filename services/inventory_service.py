from flask import Blueprint, jsonify, request
import sneaker_model

inventory_services_bp = Blueprint('inventory_services', __name__)

# Routes pour les sneakers
@inventory_services_bp.route('/sneakers', methods=['GET'])
def get_sneakers():
    sneakers = sneaker_model.get_all_sneakers()
    return jsonify(sneakers)

@inventory_services_bp.route('/sneakers/<int:sneaker_id>', methods=['GET'])
def get_sneaker(sneaker_id):
    sneaker = sneaker_model.query.get(sneaker_id)
    if not sneaker:
        return jsonify({'message': 'Sneaker not found'}), 404
    return jsonify(sneaker.serialize())

@inventory_services_bp.route('/sneakers', methods=['POST'])
def create_sneaker():
    data = request.json
    sneaker = sneaker_model(name=data['name'], brand=data['brand'], size=data['size'], color=data['color'], price=data['price'])
    sneaker.save()
    return jsonify(sneaker.serialize()), 201
