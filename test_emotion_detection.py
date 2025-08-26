import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_happy(self):
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_disgust(self):
        result = emotion_detector("I am disgusted by this")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sad(self):
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear(self):
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')

    def test_anger(self):
        result = emotion_detector("I hate working long hours")
        self.assertEqual(result['dominant_emotion'], 'anger')

if __name__ == '__main__':
    unittest.main()
