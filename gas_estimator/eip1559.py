from functools import reduce
from typing import List

from gas_estimator.base import BaseGasFeeEstimator
from third_party.web3_infura.client import web3_client


class EIP1559GasFeeEstimator(BaseGasFeeEstimator):
    @classmethod
    def _get_estimated_gas_fee(
        cls,
        percentiles: List[int],
        latest_block_count: int = 20
    ) -> dict:
        pending_block = web3_client.eth.get_block('pending')
        base_fee = pending_block.baseFeePerGas

        fee_history = web3_client.eth.fee_history(
            block_count=latest_block_count,
            newest_block='pending',
            reward_percentiles=percentiles
        )
        rewards = reduce(lambda a, b: a+b, fee_history.reward)
        avg_reward = sum(rewards) // len(rewards)

        return {
            "value": avg_reward + base_fee,
            "priority_fee": avg_reward,
            "base_fee": base_fee
        }
