class MusicTracker():
    def __init__(self):
        self.playlist = {}

    def add_music(self, artist, song_name):
        self.playlist.update({artist: song_name})

    def see_playlist(self):
        return list(self.playlist.items())