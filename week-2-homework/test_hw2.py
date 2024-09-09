import unittest
from hw2 import Profile, Activity, Post, Message, User



class TestProfile(unittest.TestCase):
    """Test cases for the Profile class."""
    def setUp(self):
        """Create profile to test on"""
        self.profile = Profile("leoapagano", "password$%", "Leo Pagano", "leo@leoapagano.com")
    
    def test_create_profile(self):
        """Test that profile's information was saved successfully in the last step."""
        self.assertEqual(self.profile.username, "leoapagano")
        self.assertEqual(self.profile.password, "password$%")
        self.assertEqual(self.profile.screen_name, "Leo Pagano")
        self.assertEqual(self.profile.email, "leo@leoapagano.com")

    def test_modify_profile(self):
        """Test profile modification API"""
        # Test screen name changing
        self.profile.modify_profile(screen_name="Not Leo Pagano")
        self.assertEqual(self.profile.screen_name, "Not Leo Pagano")

        # Test simultaneous email/password change
        self.profile.modify_profile(email="homework2@leoapagano.com", password="MyNewPassword#!")
        self.assertEqual(self.profile.email, "homework2@leoapagano.com")
        self.assertEqual(self.profile.password, "MyNewPassword#!")



class TestActivity(unittest.TestCase):
    """Test cases for the Activity class."""
    def setUp(self):
        """Create activity to test on"""
        self.user = User("la1440", "password", "Leo P.", "leoapagano@gmail.com")
        self.activity = Activity(self.user, "Activity Content - world hello")

    def test_create_activity(self):
        """Test that activity's information was saved successfully in the last step."""
        self.assertEqual(self.activity.user, self.user)
        self.assertEqual(self.activity.content, "Activity Content - world hello")

    def test_activity_string(self):
        """Test that Activity's __str__ method works properly."""
        self.assertEqual(str(self.activity), "Activity - User: la1440, Content: Activity Content - world hello")



class TestPost(unittest.TestCase):
    """Test cases for the Post class."""

    def setUp(self):
        """Create post to test on"""
        self.post = Post("lpagano1144", "This is a post by user lpagano1144.")
       
    def test_create_post(self):
        """Test that post's information was saved successfully in the last step."""
        self.assertEqual(self.post.user, "lpagano1144")
        self.assertEqual(self.post.content, "This is a post by user lpagano1144.")



class TestMessage(unittest.TestCase):
    """Test cases for the Message class."""

    def setUp(self):
        """Create message to test on"""
        self.message = Message("lpagano1144", "This is a post by user lpagano1144.", "therecipient")
       
    def test_create_post(self):
        """Test that message's information was saved successfully in the last step."""
        self.assertEqual(self.message.user, "lpagano1144")
        self.assertEqual(self.message.content, "This is a post by user lpagano1144.")
        self.assertEqual(self.message.receiver, "therecipient")



class TestUser(unittest.TestCase):
    """Test cases for the User class."""
    
    def setUp(self):
        """Create user to test on"""
        self.user = User("user1", "password1", "User One", "user1@example.com")

    def test_create_user(self):
        """Test that user's information was saved successfully in the last step."""
        self.assertEqual(self.user.username, "user1")
        self.assertEqual(self.user.password, "password1")
        self.assertEqual(self.user.screen_name, "User One")
        self.assertEqual(self.user.email, "user1@example.com")

    def test_create_post(self):
        """Test creating a post for a user."""
        post = self.user.create_post("Test Post Content")
        # Check if the post is added to the user's posts list
        self.assertIn(post, self.user.posts)
        # Check if the user is correct
        self.assertEqual(post.user, self.user)
        # Check if the content of the post is correct
        self.assertEqual(post.content, "Test Post Content")
    


if __name__ == "__main__":
    unittest.main()

