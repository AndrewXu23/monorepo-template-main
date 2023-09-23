import unittest
from jsonapi import dumps, loads, CustomJSONEncoder, CustomJSONDecoder, MyClass

class TestJSONAPI(unittest.TestCase):

    def test_custom_encoder(self):
        # Test complex number encoding
        self.assertEqual(dumps(3 + 4j), '{"type": "complex", "real": 3.0, "imag": 4.0}')
        # Test range encoding
        self.assertEqual(dumps(range(5, 10, 2)), '{"type": "range", "start": 5, "stop": 10, "step": 2}')

    def test_custom_decoder(self):
        # Test complex number decoding
        self.assertEqual(loads('{"type": "complex", "real": 3.0, "imag": 4.0}'), 3 + 4j)
        # Test range decoding
        self.assertEqual(loads('{"type": "range", "start": 5, "stop": 10, "step": 2}'), range(5, 10, 2))

    def test_custom_class(self):
        obj = MyClass("hello")
        self.assertEqual(loads(dumps(obj)).attribute, "hello")

    def test_dumps_function(self):
        self.assertIsInstance(dumps(3 + 4j), str)

    def test_loads_function(self):
        self.assertEqual(loads('{"type": "complex", "real": 3.0, "imag": 4.0}'), 3 + 4j)

if __name__ == "__main__":
    unittest.main()

