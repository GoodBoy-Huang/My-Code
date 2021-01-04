import unittest
from Survey import AnonymousSurvey

class Test_AnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""
    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.stored_response("english")

        self.assertIn("english",my_survey.responses)

    def test_store_three_response(self):
        """测试三个答案会被妥善存储"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ["english","spanish","mandarin"]
        for response in responses:
            my_survey.stored_response(response)

        for response in responses:
            self.assertIn(response,my_survey.responses)

unittest.main()

