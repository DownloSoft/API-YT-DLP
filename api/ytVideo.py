
from flask import Blueprint, jsonify

ytvideo = Blueprint('ytvideo', __name__)

@ytvideo.route('/api/ytvideo', methods=['GET'])

def custom1():
    return jsonify({'message': 'Custom1 API endpoint'})
