# Gas Price Estimator

## Requirements

- Python v3.9 (*Any Python version greater than 3.6 because of f strings*)
- API Key from [infura.io](https://infura.io)

## Installation

#### Package installation

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### Environment Variables

```bash
cp .env.example .env
```

Set **_PROJECT_ID_** to your **infura.io API Key**

## Run

```bash
flask run
```

## Test

```bash
pytest .
```

---

## API

#### Request

```http request
GET /api/gas_price
```

#### Response (Example)

```json
{
  "prices": {
    "fast": {
      "base_fee": "3.60",
      "priority_fee": "1.86",
      "value": "5.46"
    },
    "normal": {
      "base_fee": "3.60",
      "priority_fee": "1.56",
      "value": "5.16"
    },
    "slow": {
      "base_fee": "3.60",
      "priority_fee": "1.19",
      "value": "4.79"
    }
  }
}
```