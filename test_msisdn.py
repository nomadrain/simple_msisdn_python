import unittest
from simplemsisdn import SimpleMSISDN, IncorrectMsisdnData
from fake_msisdn_generator import FakeMsisdnGenerator


class TestSimpleMSISDN(unittest.TestCase):

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
        self.assertEqual('REGULAR', self.msisdn.number_class)

    def test_get_local_only(self):
        self.assertEqual(self.msisdn.get_local_only(), '337629567')

    def test_get_local_only_leading_zero(self):
        self.assertEqual(self.msisdn.get_local_only(leading_zero=True), '0337629567')


class TestFakeMsisdnGenerator(unittest.TestCase):

    def setUp(self):
        self.gn = FakeMsisdnGenerator(
            allowed_country_codes=['111',], allowed_national_destination_codes=['11'], subscriber_number_length=10
        )

    def test_able_to_generate(self):
        """
        If the generator is able to produce TNs
        """
        tn = self.gn.get()
        self.assertIsInstance(tn, SimpleMSISDN)

    def test_number_len(self):
        tn = repr(self.gn.get())
        self.assertEqual(len(tn), 15)

    def test_number_starts_with_cc_and_ndc(self):
        tn = repr(self.gn.get())
        self.assertEqual(tn[0:5], '11111')


if __name__ == '__main__':
    unittest.main()
