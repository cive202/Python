class Movie:

    def __init__(self, title, rating):
        self.title = title
        self._rating = rating

    @property
    def rating(self):
        print("Calling the getter...")
        return self._rating

    @rating.setter
    def rating(self, new_rating):
        if isinstance(new_rating, float) and 1.0 < new_rating < 5.0:
            print("Calling the setter...")
            self._rating = new_rating
            print("The new rating is", self._rating)
        else:
            print("Please enter a valid rating.")


favorite_movie = Movie("Titanic", 4.3)
print(favorite_movie.rating)

favorite_movie.rating = 3.4
