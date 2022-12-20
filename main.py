import logging
import json
from forex_python.converter import CurrencyRates

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    """
    The Lambda handler function that gets invoked when the API endpoint is hit
    """
    amount = event['queryStringParameters']['amount']
    fromCurrency = event['queryStringParameters']['fromCurrency']
    toCurrency = event['queryStringParameters']['toCurrency']
    logger.info('## Input Parameters: %s, %s, %s', amount, fromCurrency, toCurrency)
    res = convert_currency(amount, fromCurrency, toCurrency)
    logger.info('## Currency result: %s', res)
    response = {
        "statusCode": 200,
        "body": json.dumps({'result': res}),
    }
    logger.info('## Response returned: %s', response)
    return response


def convert_currency(amount: float, fromCurrency: str, toCurrency: str) -> float:
    """
    Function to convert an amount from one currency to another
    """
    c = CurrencyRates()
    res = c.convert(fromCurrency, toCurrency, float(amount))
    return float(res)
