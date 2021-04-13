class Painting:
    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year


paint = Painting(input(), input(), input())
print(f'"{paint.title}" by {paint.artist} ({paint.year}) hangs in the Louvre.')
