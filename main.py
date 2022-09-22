from flask import Flask, jsonify
# from apis.parnters import api_partners
# from models.service import Engine

api_core=Flask(__name__)
# api_core.register_blueprint(api_partners)

@api_core.get('/')
@api_core.get('/apis')
def home():
    return jsonify("Didim365 K8s Home")

# Engine.create()
api_core.run(host="0.0.0.0", port=5000)