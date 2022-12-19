from forex_python.converter import CurrencyRates


def lambda_handler(event, context):
    res = convert_currency(
        event['amount'], event['fromCurrency'], event['toCurrency'])
    return res


def convert_currency(amount: float, fromCurrency: str, toCurrency: str) -> int:
    """
    Function to convert an amount from one currency to another
    """
    c = CurrencyRates()
    res = c.convert(fromCurrency, toCurrency, float(amount))
    return res
