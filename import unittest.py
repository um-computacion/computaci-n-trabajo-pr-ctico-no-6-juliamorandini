import unittest

def romano_a_decimal(romano):
    dic_num = { 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, }
    resultado = 0
    anterior = 0
    for letra in reversed(romano):
        actual = dic_num[letra]
        if actual < anterior:
            resultado -= actual
        else:
            resultado += actual
        anterior = actual
    return resultado

class TestRomanoADecimal(unittest.TestCase):
    def test_romano_I(self):
        self.assertEqual(romano_a_decimal('I'), 1)

    def test_3(self):
        self.assertEqual(romano_a_decimal('III'), 3)
    
    def test_romano_V(self):
        self.assertEqual(romano_a_decimal('V'), 5)

    def test_6(self):
        self.assertEqual(romano_a_decimal('VI'), 6)
    
    def test_9(self):
        self.assertEqual(romano_a_decimal('IX'), 9)
    
    def test_10(self):
        self.assertEqual(romano_a_decimal('X'), 10)

    def test_13(self):
        self.assertEqual(romano_a_decimal('XIII'), 13)

    def test_14(self):
        self.assertEqual(romano_a_decimal('XIV'), 14)
                         
    def test_15(self):
        self.assertEqual(romano_a_decimal('XV'), 15)

    def test_19(self):
        self.assertEqual(romano_a_decimal('XIX'), 19)

if _name_ == '_main_':
    while True:
        romano = input('Ingrese un numero romano: ')
        if romano == '':
            print("No ingresaste nada")
        romano = romano.upper()
        print(romano_a_decimal(romano))