import media
import fresh_tomatoes

"""this file, movies instances are defined to be stored in Movie class """
# instance 1
naruto = media.Movie("The Last: Naruto the Movie",
                     "1:30 hour",
                     """two years since the 4th Ninja World War,
                        another threat surfaces!""",
                     "https://upload.wikimedia.org/wikipedia/en/0/0c/TheLastNarutomovie.jpg",  # noqa
                     "https://www.youtube.com/watch?v=tA3yE4_t6SY"
                     )

# instance 2
spritied_away = media.Movie("Siprited Away",
                            "2:00 hours",
                            """Stubborn and spoiled 10-year-old Chihiro Ogino
                            where strange things occured to her and her parents
                            in their way to a  new house""",
                            "https://vignette.wikia.nocookie.net/studio-ghibli/images/4/4a/Spirited_Away_%28Amerikansk_DVD%29.jpg/revision/latest?cb=20140116135457",  # noqa
                            "https://www.youtube.com/watch?v=ByXuk9QqQkk")

# instance 3
black_butler = media.Movie("Black Butler: Book of Atlantic",
                           "1:00 hour",
                           """The Earl Phantomhive and his butler Sebastian
                              face another mysterious case on a ship""",
                           "https://myanimelist.cdn-dena.com/images/anime/9/85792.jpg",  # noqa
                           "https://www.youtube.com/watch?v=YFRGd6DMtjs")

# instance 4
monester_university = media.Movie("Monester University",
                                  "1:45 hour",
                                  """Mike Wazowski (Billy Crystal) has
                                  dreamed of becoming a Scarer.
                                  To make his dream a reality,
                                  he enrolls at Monsters University""",
                                  "http://t1.gstatic.com/images?q=tbn:ANd9GcRwIJWk6sSJtE5FNXg1pK4lFu5tbeIvi81BKV2SG4wTA1lWfrMH",  # noqa
                                  "https://www.youtube.com/watch?v=QxrQ6BaijAY"  # noqa
                                  )
# instance 5
big_hero_6 = media.Movie("Big Hero 6",
                         "1:30 hour",
                         """Robotics prodigy Hiro (Ryan Potter)
                         lives in the city of San Fransokyo
                         with a robot whose sole purpose is
                         to take care of people. When a devastating
                         turn of events throws Hiro into
                         the middle of a dangerous plot""",
                         "http://t2.gstatic.com/images?q=tbn:ANd9GcQzyu98HxFhB68UKqRKSrTKknXHI-gtSTAAX0CGiKBM980CFhI1",  # noqa
                         "https://www.youtube.com/watch?v=z3biFxZIJOQ")

# store the instances in array
movies = [
    naruto,
    spritied_away,
    black_butler,
    monester_university,
    big_hero_6
    ]
# show the movies in the webpage from the array
fresh_tomatoes.open_movies_page(movies)
