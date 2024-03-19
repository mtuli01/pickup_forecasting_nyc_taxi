from flask import Flask, request
from flask import Blueprint
from flask import current_app as app
from src.ml import service

bp = Blueprint('demo', __name__, url_prefix='/')

@bp.route('/demo', methods=['GET, POST'])
def get_request_details():
    input_details = request.json()
    model_output = get_model_prediction(input_details)


def get_model_prediction(inp_payload: dict):
    longitude = inp_payload['longitude']
    latitude = inp_payload['latitude']
    time = inp_payload['time']
    return service.nyc_yellow_taxi_prediction(longitude, latitude, time)
