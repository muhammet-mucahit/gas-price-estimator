import os

from dotenv import load_dotenv

from web3 import Web3
from web3.gas_strategies.time_based import medium_gas_price_strategy

load_dotenv()

PROJECT_ID = os.getenv('PROJECT_ID')
INFURA_URL = f"https://mainnet.infura.io/v3/{PROJECT_ID}"

web3_client = Web3(Web3.HTTPProvider(INFURA_URL))
web3_client.eth.set_gas_price_strategy(medium_gas_price_strategy)