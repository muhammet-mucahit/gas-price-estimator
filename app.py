from dotenv import load_dotenv

from flask import Flask, jsonify
from flask_cors import CORS

from gas_estimator.eip1559 import EIP1559GasFeeEstimator

# loads environment variables
load_dotenv()

application = Flask(__name__)
CORS(application)

INDEX_ENDPOINT = "/"
GAS_PRICE_ENDPOINT = "/api/gas_price"

WARNING_REDIRECT_MSG = f'Nothing here, go to {GAS_PRICE_ENDPOINT}'


@application.route(INDEX_ENDPOINT)
def index_view():
    return WARNING_REDIRECT_MSG


@application.route(GAS_PRICE_ENDPOINT)
def gas_price_eip_1559_view():
    return jsonify(EIP1559GasFeeEstimator.get_estimated_gas_fees_by_mode())
