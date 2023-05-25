from num2words import num2words#звертаємося до встановленого пакету

def convert(number: int):# -> str:
    return num2words(number, lang='uk')
