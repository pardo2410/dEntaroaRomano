import romanos , arabigos

opcion = input('Desea convertir de romano a arabigo (R) o arabigo a romano (A): ')
if opcion == 'R' or opcion == 'r':
    numero_romano = input('Ingrese numero romano: ')
    print('***',romanos.romano_a_entero(numero_romano),'***')
else:
    numero_arabigo =int( input('Ingrese numero arabigo: '))
    print('***',arabigos.arabigo_a_romano(numero_arabigo),'***')
