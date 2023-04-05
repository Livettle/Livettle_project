import unittest
from imdb import detect_emotion

class TestEmotionDetection(unittest.TestCase):
    
    def test_detect_emotion(self):
        expected_num_movies = 50
        emotions = ["angry", "disgust", "fear", "happy", "neutral", "sad", "surprise"]
        
        for emotion in emotions:
            movies = detect_emotion(emotion)
            self.assertEqual(len(movies), expected_num_movies, f"Expected {expected_num_movies} movies for emotion '{emotion}', but got {len(movies)} movies instead.")
            
            for movie in movies:
                # Verify that each movie has a valid title
                self.assertTrue(len(movie["title"]) > 0, f"Invalid title '{movie['title']}' for movie in emotion '{emotion}'.")
                
                # Verify that each movie has a valid image URL
                self.assertTrue(movie["image_url"].startswith("https://"), f"Invalid image URL '{movie['image_url']}' for movie '{movie['title']}' in emotion '{emotion}'.")

                import json
from imdb import app
import json
           
if __name__ == '__main__':
    unittest.main()


