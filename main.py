from currency_converter import CurrencyConverter


def convert_currency(amount: int, fromCurrency: str, toCurrency: str):
    c = CurrencyConverter()
    res = c.convert(amount, fromCurrency, toCurrency)
    return res


res = convert_currency(1, 'USD', 'CAD')
print(res)
