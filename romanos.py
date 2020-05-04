
Romanos = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

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
            letraAnt = letra
        else:
            numRepes = 1
            letraAnt = letra
    
    if letra not in Romanos:
        return 'Error en formato'  
    
    letraAnt = ''
    letraAnt2 = ''
    
    for letra in numero_romano:
        
        if letra == 'L' and letraAnt == 'I' or letra == 'C' and letraAnt == 'I' or letra == 'D' and letraAnt == 'I' or letra == 'M' and letraAnt == 'I':
            return 'Error en formato'
        elif letra == 'M' and letraAnt == 'V' or letra == 'D' and letraAnt == 'V'or letra == 'C' and letraAnt == 'V'or letra == 'L' and letraAnt == 'V'or letra == 'X' and letraAnt == 'V':
            return 'Error en formato'
        elif letra == 'M' and letraAnt == 'X' or letra == 'D' and letraAnt == 'X'or letra == 'C' and letraAnt == 'X':
            return 'Error en formato'
        elif letra == 'L' and  letraAnt == 'X' and  letraAnt2 == 'X' or letra == 'C' and  letraAnt == 'X' and  letraAnt2 == 'X' or letra == 'X' and  letraAnt == 'I' and  letraAnt2 == 'I' or letra == 'V' and  letraAnt == 'I' and  letraAnt2 == 'I':
            return 'Error en formato'
        else:
            letraAnt2 = letraAnt
            letraAnt = letra

   
    for local in range(0,len(numero_romano)):
        if local == 0 or Romanos[numero_romano[local]] <= Romanos[numero_romano[local-1]]:
            entero += Romanos[numero_romano[local]]
        else:
            entero += Romanos[numero_romano[local]] - 2*Romanos[numero_romano[local-1]] 
        

    return entero
