import json
from forex_python.converter import CurrencyRates

def lambda_handler(event, context):
    """
    The Lambda handler function that gets invoked when the API endpoint is hit
    """
    amount = event['queryStringParameters']['amount']
    fromCurrency = event['queryStringParameters']['fromCurrency']
    toCurrency = event['queryStringParameters']['toCurrency']
    res = convert_currency(amount, fromCurrency, toCurrency)
    response = {
        "statusCode": 200,
        "body": json.dumps({'result': res}),
    }
    return response


def convert_currency(amount: float, fromCurrency: str, toCurrency: str) -> int:
    """
    Function to convert an amount from one currency to another
    """
    c = CurrencyRates()
    res = c.convert(fromCurrency, toCurrency, float(amount))
    return res
