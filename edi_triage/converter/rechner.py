def add(number1, number2):
    try:
        summe = float(number1) + float(number2)
    except:
        return 'Error: there are no numbers'
    return summe
