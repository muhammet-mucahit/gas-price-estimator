from decimal import Decimal

import pytest

from gas_estimator.eip1559 import EIP1559GasFeeEstimator
from third_party.web3_infura.client import web3_client

ESTIMATION_TOLERANCE = Decimal(1.0)


def test_get_estimated_gas_fee_by_percentiles_with_empty_percentiles():
    with pytest.raises(Exception) as exp:
        EIP1559GasFeeEstimator._get_estimated_gas_fee_by_percentiles([], 20)
        assert exp.value == "You must enter percentiles!"


def test_get_estimated_gas_fee_by_percentiles():
    prices = EIP1559GasFeeEstimator._get_estimated_gas_fee_by_percentiles([5.0], 20)

    assert "value" in prices
    assert "priority_fee" in prices
    assert "base_fee" in prices

    actual_priority_fee = prices['priority_fee']
    expected_priority_fee = web3_client.fromWei(web3_client.eth.max_priority_fee, 'gwei')
    assert abs(expected_priority_fee - actual_priority_fee) < ESTIMATION_TOLERANCE
