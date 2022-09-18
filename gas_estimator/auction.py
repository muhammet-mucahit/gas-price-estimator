from typing import List
from gas_estimator.base import BaseGasFeeEstimator

from third_party.web3_infura.client import web3_client


class AuctionGasPriceEstimator(BaseGasFeeEstimator):
    @classmethod
    def _get_estimated_gas_fee(
        cls,
        percentiles: List[int],
        latest_block_count: int = 4
    ) -> float:
        # latest_blogs = web3_client.eth.filter('latest')
        # (
        #     block_count=latest_block_count,
        #     newest_block='latest',
        #     reward_percentiles=percentiles,
        # )
        # fee_history.gas_ratio

        return 1
