
romanos = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

def romano_a_entero(numero_romano):
    if numero_romano == '':
        return 'Error en formato'
    

    
    entero = 0
    numRepes = 0
    letraAnt = ''
    for letra in numero_romano:
        if letra == letraAnt and numRepes == 3:
            return 'Error en formato'
        elif letra == letraAnt:
            numRepes += 1
        else:
            numRepes = 1
       
        if letra in romanos:
            entero += romanos[letra]
        else:
            return 'Error en formato'
        letraAnt = letra

    return entero

'''if __name__=='__main__':
    romano_a_entero('')'''