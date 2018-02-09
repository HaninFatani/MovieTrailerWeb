import webbrowser


class Video():

    """A parent class, so the developer can inherit from"""
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration


class Movie(Video):

    """Class to store movies in order to run them in website"""

    def __init__(self, title, duration, storyline, img, trailer):
        Video.__init__(self, title, duration)
        self.title = title
        self.storyline = storyline
        self.poster_image_url = img
        self.trailer_youtube_url = trailer

        # to run the trailer videos in the website
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
