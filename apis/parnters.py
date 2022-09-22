from flask import jsonify, request
from flask.blueprints import Blueprint

api_partners=Blueprint("api_partners", __name__, url_prefix="/apis/partners")

@api_partners.get('/')
def list_all_partners():
    return jsonify("list all partners")

@api_partners.get('/<partner_id>')
def read_partner(partner_id):
    return jsonify("partner id is "+partner_id)

@api_partners.post('/')
def create_partner():
    print(request.form['hello'])
    return jsonify(200)

@api_partners.patch('/<partner_id>')
def update_partner(partner_id):
    print(request.get_json())
    return jsonify(200)

@api_partners.delete('/<partner_id>')
def delete_partner(partner_id):
    return jsonify(200)