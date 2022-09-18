from dotenv import load_dotenv

from flask import Flask, jsonify
from flask_cors import CORS

from gas_estimator.auction import AuctionGasPriceEstimator
from gas_estimator.eip1559 import EIP1559GasFeeEstimator

# loads environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)


@app.route('/')
def index_view():
    return f'Nothing here, go to /api/gas_price or /api/gas_price_eip_1559'


@app.route('/api/gas_price')
def gas_price_view():
    return jsonify(AuctionGasPriceEstimator.get_estimated_gas_fees_by_mode())


@app.route('/api/gas_price_eip_1559')
def gas_price_eip_1559_view():
    return jsonify(EIP1559GasFeeEstimator.get_estimated_gas_fees_by_mode())
