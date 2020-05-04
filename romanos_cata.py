
Romanos = {'M':1000,'C':100,'L':50,'X':10,'V':5,'I':1}
existen = ['IV','IX','XL','XC','CD','CM']
def romano_a_entero(numero_romano):
    if numero_romano == '':
        return 'Error en formato'

    entero = 0
    numRepes = 0
    letraAnt = ''
    fueResta = False
    
    for letra in numero_romano:

        if letra in Romanos:

            if letraAnt != '' and Romanos[letraAnt] >= Romanos[letra]:
                entero += Romanos[letra]
                fueResta = False
            else:
                if letraAnt + letra in existen and numRepes < 2 and not fueResta:
                    entero = entero - Romanos[letraAnt] * 2 + Romanos[letra]
                    fueResta = True 
                else:
                    return 'Error en formato'
        else:
            return 'Error en formato'
        
        if letra == letraAnt and numRepes < 2:
            return 'Error en formato'
        elif letra == letraAnt:
            numRepes += 1

        else:
            numRepes = 1
    
        letraAnt = letra
    
    return entero
        