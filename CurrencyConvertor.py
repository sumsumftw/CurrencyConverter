from Modules import (currencyFrom,
                     currencyTo,
                     ammount,
                     convert,
                     escape,
                     validCurrencies
                     )

currency_values = {'USD':1,
                   'EURO':0.920444,
                   'CAD':1.34524,
                   'RUPEE':83.1177,
                   'MEXICO_PESO':17.1595,
                   'JPY':148.185,
                   'CNY':7.1774
                   }

valid_currencies = validCurrencies(currency_values)

flag = False
while not flag:
    currency_from = currencyFrom(valid_currencies)
    currency_to = currencyTo(valid_currencies,currency_from)
    money = ammount(currency_from,currency_to)
    total = convert(F=currency_from, T=currency_to, M=money,CV=currency_values)
    print(f"{total:.2f} {currency_to}")
    flag = escape()