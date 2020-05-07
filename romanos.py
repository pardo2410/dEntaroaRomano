Romanos = {'M':1000,
           'CM':900,
           'D':500,
           'CD':400,
           'C':100,
           'XC':90,
           'L':50,
           'XL':40,
           'X':10,
           'IX':9,
           'V':5,
           'IV':4,
           'I':1,
}

def romano_a_entero(numero_romano):
    if numero_romano == '':
        return 'Error en formato'

    entero = 0
    numRepes = 1
    letraAnt = ''
    fueResta = False

    for letra in numero_romano:
        if letra in Romanos:
            if letraAnt == '' or Romanos[letraAnt] >= Romanos[letra]:
                    entero += Romanos[letra]
                    fueResta = False
            else:
                if letraAnt + letra in Romanos.keys() and numRepes < 2 and not fueResta:
                    entero = entero - Romanos[letraAnt] * 2 + Romanos[letra]
                    fueResta = True
                else:
                    return 'Error en formato'
        else:
            return 'Error en formato'

        if letra == letraAnt and numRepes == 3:
            return 'Error en formato'
        elif letra == letraAnt:
            numRepes += 1
        else:
            numRepes = 1
        
        letraAnt = letra
    return entero
