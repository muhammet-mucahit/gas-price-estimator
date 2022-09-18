import json

from app import INDEX_ENDPOINT, GAS_PRICE_ENDPOINT, WARNING_REDIRECT_MSG


def test_index_view(client):
    response = client.get(INDEX_ENDPOINT)
    res = response.data.decode('UTF-8')
    assert type(res) is str
    assert res == WARNING_REDIRECT_MSG
    assert response.status_code == 200


def test_gas_price_eip_1559_view(client, mocker):
    mocker.patch(
        "gas_estimator.eip1559.EIP1559GasFeeEstimator.get_estimated_gas_fees_by_mode",
        return_value={
            "prices": {
                "slow": 1,
                "normal": 2,
                "fast": 3,
            }
        }
    )

    response = client.get(GAS_PRICE_ENDPOINT)
    res = json.loads(response.data.decode('utf-8')).get('prices')
    assert type(res) is dict
    assert 'slow' in res
    assert 'normal' in res
    assert 'fast' in res
    assert response.status_code == 200
