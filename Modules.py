def validCurrencies(currency_values):
    valid_currencies = []
    for i in currency_values:
        valid_currencies.append(i)
    return valid_currencies

def currencyFrom(valid_currencies):
    temp_flag = False
    while not temp_flag:
        currency_from = input(f"Options:{valid_currencies}\n"
                              "What currency would you like to convert?: ").upper()
        if currency_from in valid_currencies:
            break
        else:
            print(f"{currency_from} is not a valid currency!\n"
                  f"")
    return currency_from

def currencyTo(valid_currencies,currency_from):
    temp_flag = False
    while not temp_flag:
        currency_to = input(f"Options:{valid_currencies}\n"
                            f"What would you like to convert {currency_from} to?: ").upper()
        if currency_to in valid_currencies:
            break
        else:
            print(f"{currency_to} is not a valid currency!\n"
                  f"")
    return currency_to

def ammount(currency_from,currency_to):
    temp_flag = False
    while not temp_flag:
        money = input(f"How much {currency_from} to {currency_to} would you want to convert? ")
        if money.isnumeric():
            money = int(money)
            if money > 0:
                break
            else:
                print(f"You can't use {money}.\n"
                      f"Only numbers that are more than O!")
        else:
            print(f"{money} is not a valid currency!")
    return money

def convert(F, T, M,CV):
    F = CV[F]
    T = CV[T]
    C = (F/F) * (T/F)
    total = C * M
    return total

def escape():
    flag = input('Would you like to keep converting? To continue type "Y".\n'
                 'Anything else to quit: ').upper()
    if flag == "Y":
        flag = False
        print("")
        return flag
    else:
        flag = True
        return flag