import unittest
import caja_blanca 

class TestCajaBlanca(unittest.TestCase):
    def test_calculate_GCF(self):
        self.assertEqual(caja_blanca.calculate_GCF(2,3),5)
        self.assertEqual(caja_blanca.calculate_GCF(-1,1),0)
        self.assertEqual(caja_blanca.calculate_GCF(-1,-1),-2)
    
    def test_greates_num(self):
        self.assertEqual(caja_blanca.greatest_num(2,3),5)
        self.assertEqual(caja_blanca.greatest_num(-1,1),0)
        self.assertEqual(caja_blanca.greatest_num(-1,-1),-2)


if __name__ == '__main__':
    unittest.main()
