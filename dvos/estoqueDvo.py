import re


class ProdutoDvo:
    def isEan13(value):
        if not re.search("^[0-9]{13}$", value):
            return false

        somaPares = value[1] + value[3] + \
            value[5] + value[7] + value[9] + value[11]
        somaImpares = value[0] + value[2] + \
            value[4] + value[6] + value[8] + value[10]
        resultado = somaImpares + somaPares * 3
        digitoVerificador = 10 - resultado % 10
        return digitoVerificador == value[12]
