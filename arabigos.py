Romanos = ['','I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
Arabigos = [0,1,4,5,9,10,40,50,90,100,400,500,900,1000]


def arabigo_a_romano(numero_arabigo):
    
    if  numero_arabigo >= 4000:
        return 'Overflow'
    
    else:

        Result_Rom = ''
        
        for indice in range(len(Arabigos)-1,0,-1):
            while numero_arabigo >= Arabigos[indice]:
                numero_arabigo -= Arabigos[indice]
                Result_Rom += Romanos[indice]        
        return Result_Rom