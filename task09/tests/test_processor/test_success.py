from tests.test_processor import ProcessorLambdaTestCase


class TestSuccess(ProcessorLambdaTestCase):

    def test_success(self):
        self.assertEqual(True, True)
