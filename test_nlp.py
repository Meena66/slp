import unittest
from nlp.nlp_processing import process_symptoms, compare_with_known_symptoms

class TestNLP(unittest.TestCase):
    # Test symptom extraction from user input
    def test_process_symptoms(self):
        user_input = "I feel tired and I snore a lot."
        symptoms = process_symptoms(user_input)
        self.assertIn("tired", symptoms)
        self.assertIn("snore", symptoms)

    # Test comparison with known symptoms
    def test_compare_with_known_symptoms(self):
        user_input = "I feel tired."
        known_symptoms = ["snoring", "difficulty breathing", "fatigue", "headache"]
        most_similar = compare_with_known_symptoms(user_input, known_symptoms)
        self.assertEqual(most_similar, "fatigue")

if __name__ == '__main__':
    unittest.main()
