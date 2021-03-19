import unittest
from simplemsisdn import SimpleMSISDN, IncorrectMsisdnData


class Test_Simple_MSISDN(unittest.TestCase):

    def setUp(self):
        self.msisdn = SimpleMSISDN(country_code='380',
                                   national_destination_code='33',
                                   subscriber_number='7629567')

    def test_str(self):
        self.assertEqual(str(self.msisdn), '+380-33-7629567')

    def test_repr(self):
        self.assertEqual(repr(self.msisdn), '380337629567')

    def test_throws_absent(self):
        with self.assertRaises(IncorrectMsisdnData):
            a = SimpleMSISDN()
            
    def test_class_detection_is_functional(self):
        self.assertEqual('REGULAR', self.msisdn.number_grade)


if __name__ == '__main__':
    unittest.main()
