class Song:
    id = 1
    title = ''
    featured_artist = ''
    length_of_track = ''
    written_by = ''

    def __init__(self, id, title, featured_artist, length_of_track, written_by):
        self.id = id
        self.title = title
        self.featured_artist = featured_artist
        self.length_of_track = length_of_track
        self.written_by = written_by