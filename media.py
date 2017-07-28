
class Movie():
    ''' This class provides a way to store movie related information '''
    movies = []

    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

        # url for wikipedia page
        self.wikipage_url = "https://en.wikipedia.org/wiki/" + movie_title.replace(" ", "_")

        Movie.movies.append(self)
