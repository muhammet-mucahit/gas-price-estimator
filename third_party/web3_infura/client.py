import os

from dotenv import load_dotenv

from web3 import Web3, middleware

load_dotenv()

PROJECT_ID = os.getenv('PROJECT_ID')
INFURA_URL = f"https://mainnet.infura.io/v3/{PROJECT_ID}"

web3_client = Web3(Web3.HTTPProvider(INFURA_URL))

web3_client.middleware_onion.add(middleware.latest_block_based_cache_middleware)
web3_client.middleware_onion.add(middleware.simple_cache_middleware)
