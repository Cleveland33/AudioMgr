class Album:
    id = 0
    title = '' 
    genre = '' 
    artist = '' 
    release_year = 0 
    price = 0.0 
    album_art = '' 
    related_artist = '' 
    record_label = ''

    songs = []

    def __init__(self, id, title, genre, artist, release_year, price, album_art, related_artist, record_label):
        self.id = id
        self.title = title
        self.genre = genre
        self.artist = artist
        self.release_year = release_year
        self.price = price
        self.album_art = album_art        
        self.related_artist = related_artist
        self.record_label = record_label
        self.songs = []

    def __str__(self):
        return self.title + "|" + self.artist

    def add_song(self, song):
        self.songs.append(song)
        
