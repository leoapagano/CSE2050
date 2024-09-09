###############################################################################
# Collaboration                                                               #
# -------------                                                               #
# You can collaborate with up to 3 classmates (for a total of 4 students per  #
# group). If you do so, remember not to share code directly. Discussions are  #
# fine, code sharing is not. Also note that all have to submit individually.  #
#                                                                             #
# Enter any collaborators here:                                               #
# Collaborator 1:                                                             #
# Collaborator 2:                                                             #
# Collaborator 3:                                                             #
###############################################################################
class Profile:
    """Class representing a user's profile."""
    def __init__(self, username, password, screen_name, email):
        """Establish the Profile's username, password, screen name, and email address."""
        self.username = username
        self.password = password
        self.screen_name = screen_name
        self.email = email

    def __str__(self): # Done.
        """Return a string representation of the Profile."""
        return f"Profile - Username: {self.username}, Screen Name: {self.screen_name}, Email: {self.email}"

    def modify_profile(self, password=None, screen_name=None, email=None):
        """Replace any of the profile's values with the given values."""
        if password != None:
            self.password = password
        if screen_name != None:
            self.screen_name = screen_name
        if email != None:
            self.email = email

class Activity:
    """Base class representing an activity."""
    def __init__(self, user, content):
        """Establish the Activity's uploader and its' content."""
        self.user = user
        self.content = content

    def __str__(self):
        """Return a string representation of the Activity."""
        return f"Activity - User: {self.user.profile.username}, Content: {self.content}"


class Post(Activity):
    """Class representing a user's post."""
    def __init__(self, user, content):
        """Create a new Post."""
        super().__init__(user, content)

    def __str__(self):
        """Return a string representation of the Post."""
        return f"Post - {super().__str__()}"
    

class Message(Activity):
    """Class representing a user's message to another user."""
    def __init__(self, user, content, receiver):
        """Initialize a new Message, with a sender, content, and recipient."""
        super().__init__(user, content)
        self.receiver = receiver

    def __str__(self):
        """ Return a string representation of the Message."""
        return f"Message - {super().__str__()}, Receiver: {self.receiver.profile.username}"


class User:
    def __init__(self, username, password, screen_name, email):
        """Create a new User, with a username, password, screen name and email address,
        plus a Profile with that content, an empty list of Posts, and an empty list of Messages."""
        self.username = username
        self.password = password
        self.screen_name = screen_name
        self.email = email
        self.profile = Profile(self.username, self.password, self.screen_name, self.email)
        self.posts = []
        self.messages = []

    def create_post(self, content):
        """Create a new post for the user.
        Args:
            content (str): The content of the post.

        Returns:
            Post: The created post.

        Raises:
            ValueError: If the content of the post is empty.
        """
        if content == "" or content == None:
            raise ValueError
        else:
            currentPost = Post(self, content)
            self.posts.append(currentPost)
            return currentPost

    def send_message(self, receiver, content):
        """Send a message from the user to the specified receiver.

        Args:
            receiver (User): The user receiving the message.
            content (str): The content of the message.

        Returns:
            Message: The created message.

        Raises:
            ValueError: If the receiver ID or message content is empty.
        """
        if content == "" or content == "None" or receiver == "" or receiver == "None":
            raise ValueError
        else:
            currentMessage = Message(self, content, receiver)
            self.messages.append(currentMessage)
            return currentMessage

    def __str__(self):
        """ Return a string representation of the User."""
        return f"User - {self.profile}"

# Example usage:
if __name__ == "__main__":
    user1 = User("user1", "password1", "User One", "user1@example.com")
    user2 = User("user2", "password2", "User Two", "user2@example.com")

    post1 = user1.create_post("This is my first post!")
    message1 = user2.send_message(user1, "Hi User One! How are you?")
    print(post1)
    print(message1)
    user1.profile.modify_profile(email="User1_1@uconn.edu")
    print(user1)
    print(user2)

