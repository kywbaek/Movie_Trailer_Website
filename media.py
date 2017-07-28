
class Movie():
    ''' This class provides a way to store movie related information '''
    movies = []

    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

        Movie.movies.append(self)
