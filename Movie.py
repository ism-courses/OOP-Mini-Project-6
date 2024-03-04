class Movie:
    def __init__(self,title,rating):
        self.title = title
        # below is a non-public attribute
        self._rating = rating
