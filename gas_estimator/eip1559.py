from functools import reduce
from typing import List

from gas_estimator.base import BaseGasFeeEstimator
from third_party.web3_infura.client import web3_client


class EIP1559GasFeeEstimator(BaseGasFeeEstimator):
    @classmethod
    def _get_estimated_gas_fee_by_percentiles(
        cls,
        percentiles: List[float],
        latest_block_count: int = 20
    ) -> dict:
        if not percentiles:
            raise Exception("You must enter percentiles!")

        pending_block = web3_client.eth.get_block('pending')
        base_fee = pending_block.baseFeePerGas

        fee_history = web3_client.eth.fee_history(
            block_count=latest_block_count,
            newest_block='pending',
            reward_percentiles=percentiles
        )
        rewards = reduce(lambda a, b: a+b, fee_history.reward)

        # Exclude 0 (zero) values
        rewards = [reward for reward in rewards if reward != 0]
        avg_reward = sum(rewards) // len(rewards)

        # Concerts wei to gwei
        base_fee_gwei = web3_client.fromWei(base_fee, 'gwei')
        priority_fee_gwei = web3_client.fromWei(avg_reward, 'gwei')

        # Round values to have only 2 decimal after comma
        base_fee_gwei = round(base_fee_gwei, 2)
        priority_fee_gwei = round(priority_fee_gwei, 2)

        return {
            "value": priority_fee_gwei + base_fee_gwei,
            "priority_fee": priority_fee_gwei,
            "base_fee": base_fee_gwei
        }
