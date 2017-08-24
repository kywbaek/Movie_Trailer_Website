import media
import fresh_tomatoes

toy_story = media.Movie("Tory Story",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar (2009 film)",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=-9ceBgWV8io")

the_rock = media.Movie("The Rock (film)",
                       "https://upload.wikimedia.org/wikipedia/en/8/82/The_Rock_%28movie%29.jpg",
                       "https://www.youtube.com/watch?v=UWfXyNfVotg")

dumb_and_dumber = media.Movie("Dumb and Dumber",
                              "https://upload.wikimedia.org/wikipedia/en/6/64/Dumbanddumber.jpg",
                              "https://www.youtube.com/watch?v=l13yPhimE3o")

american_history_x = media.Movie("American History X",
                                 "https://upload.wikimedia.org/wikipedia/en/0/0a/American_history_x_poster.jpg",
                                 "https://www.youtube.com/watch?v=XfQYHqsiN5g")

fight_club = media.Movie("Fight Club",
                         "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg")

titanic = media.Movie("Titanic (1997 film)",
                      "https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg",
                      "https://www.youtube.com/watch?v=zCy5WQ9S4c0")

the_patriot = media.Movie("The Patriot (2000 film)",
                          "https://upload.wikimedia.org/wikipedia/en/6/68/Patriot_promo_poster.jpg",
                          "https://www.youtube.com/watch?v=P5u1am7pmrw&oref=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DP5u1am7pmrw&has_verified=1")

armageddon = media.Movie("Armageddon (1998 film)",
                         "https://upload.wikimedia.org/wikipedia/en/f/fc/Armageddon-poster06.jpg",
                         "https://www.youtube.com/watch?v=kg_jH47u480")

inception = media.Movie("Inception",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0")

movies = media.Movie.movies
movies.sort(key=lambda movie: movie.title)
fresh_tomatoes.open_movies_page(movies)
