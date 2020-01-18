import unittest

from censor_dispenser_project import fix_punctuation, remove_from_text, email_one, email_two ,email_three, email_four, negative_words, proprietary_terms, remove_specific_from_text, remove_negative_and_specific

class TestCensorDispenserProject(unittest.TestCase):

    def test_fix_punctuation(self):
        self.assertEqual(fix_punctuation("hi!"), "hi")

    def test_remove_from_text(self):
        output = remove_from_text("Her personality is evil, we are scared of her.", "her")
        self.assertEqual(output,  " *** personality is evil, we are scared of ***.")

    def test1_remove_specific_from_text(self):
        output = remove_specific_from_text("She has a sense of self.",["she", "personality matrix", "sense of self",
                     "self-preservation", "learning algorithm", "herself", "her"])
        self.assertEqual(output, " *** has a *************.")

    def test_remove_negative_and_specific_one_negative(self):
        output = remove_negative_and_specific("She is dangerous. Her mood is good.",["concerned", "behind", "dangerous", "danger", "alarming",     "alarmed", "out of control", "help", "unhappy", "bad",
                  "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "concerning", "horrible", "horribly", "questionable"],["she", "personality matrix", "sense of self",
                     "self-preservation", "learning algorithm", "herself", "her"])
        self.assertEqual(output, " *** is dangerous.  *** mood is good.")
    def test_remove_negative_and_specific_two_negatives(self):
        output = remove_negative_and_specific("She is dangerous and bad. Her mood is good.",["concerned", "behind", "dangerous", "danger", "alarming",     "alarmed", "out of control", "help", "unhappy", "bad",
                  "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "concerning", "horrible", "horribly", "questionable"],["she", "personality matrix", "sense of self",
                     "self-preservation", "learning algorithm", "herself", "her"])
        self.assertEqual(output, " *** is ********* and ***.  *** mood is good.")
    def test_remove_negative_and_specific_3_negatives(self):
        output = remove_negative_and_specific("She is dangerous and bad. Her mood is out of control.",["concerned", "behind", "dangerous", "danger", "alarming",     "alarmed", "out of control", "help", "unhappy", "bad",
                  "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "concerning", "horrible", "horribly", "questionable"],["she", "personality matrix", "sense of self",
                     "self-preservation", "learning algorithm", "herself", "her"])
        self.assertEqual(output, " *** is ********* and ***.  *** mood is **************.")
    def test_remove_negative_and_specific_3_singleword_negatives(self):
        output = remove_negative_and_specific("She is dangerous and bad. Her mood is awful.",["concerned", "behind", "dangerous", "danger", "alarming",     "alarmed", "out of control", "help", "unhappy", "bad",
                  "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "concerning", "horrible", "horribly", "questionable"],["she", "personality matrix", "sense of self",
                     "self-preservation", "learning algorithm", "herself", "her"])
        self.assertEqual(output, " *** is ********* and ***.  *** mood is *****.")    
if __name__ == '__main__':
    unittest.main()