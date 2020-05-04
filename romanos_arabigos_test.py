'Test de pruebas numeros romanos'

import unittest 
import romanos
import arabigos
import romanos_cata

class RomanNumberTest(unittest.TestCase):

    def test_symbols_romans(self):
        self.assertEqual(romanos.romano_a_entero('I'), 1)
        self.assertEqual(romanos.romano_a_entero('V'), 5)
        self.assertEqual(romanos.romano_a_entero('X'), 10)
        self.assertEqual(romanos.romano_a_entero('L'), 50)
        self.assertEqual(romanos.romano_a_entero('C'), 100)
        self.assertEqual(romanos.romano_a_entero('D'), 500)
        self.assertEqual(romanos.romano_a_entero('M'), 1000)
        self.assertEqual(romanos.romano_a_entero('K'), 'Error en formato')
        self.assertEqual(romanos.romano_a_entero(''), 'Error en formato')
    def test_repetitions(self):
        self.assertEqual(romanos.romano_a_entero('II'), 2)
        self.assertEqual(romanos.romano_a_entero('MMM'), 3000)
        self.assertEqual(romanos.romano_a_entero('KKK'), 'Error en formato')
        self.assertEqual(romanos.romano_a_entero('MK'), 'Error en formato')
    def test_only_three(self):
        self.assertEqual(romanos.romano_a_entero('IIII'), 'Error en formato')
    def test_digitos_decrecientes(self):
        self.assertEqual(romanos.romano_a_entero('XVIII'), 18)
        self.assertEqual(romanos.romano_a_entero('IL'), 'Error en formato')
        self.assertEqual(romanos.romano_a_entero('XIV'), 14)
        self.assertEqual(romanos.romano_a_entero('XLIX'), 49)
        self.assertEqual(romanos.romano_a_entero('XLVIII'), 48)
        self.assertEqual(romanos.romano_a_entero('VLIII'), 'Error en formato')
        self.assertEqual(romanos.romano_a_entero('XXL'), 'Error en formato')

class ArabigoNumberTest(unittest.TestCase):

    def test_symbols_arabigos(self):
        self.assertEqual(arabigos.arabigo_a_romano(3999), 'MMMCMXCIX')
        self.assertEqual(arabigos.arabigo_a_romano(1),'I')
        self.assertEqual(arabigos.arabigo_a_romano(2),'II')
        self.assertEqual(arabigos.arabigo_a_romano(3),'III')
        self.assertEqual(arabigos.arabigo_a_romano(4),'IV')
        self.assertEqual(arabigos.arabigo_a_romano(5),'V')
        self.assertEqual(arabigos.arabigo_a_romano(10),'X')
        self.assertEqual(arabigos.arabigo_a_romano(440),'CDXL')



     


if __name__=='__main__':
    unittest.main()