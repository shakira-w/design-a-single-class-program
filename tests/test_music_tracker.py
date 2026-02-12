from lib.music_tracker import MusicTracker

def test_initially_playlist_is_empty():
    music_tracker = MusicTracker()
    assert music_tracker.playlist == {}

def test_music_is_added_to_playlist_dictionary():
    music_tracker = MusicTracker()
    artist = "Taylor Swift"
    song_name = "Blank Space"
    music_tracker.add_music(artist, song_name)
    result = music_tracker.playlist
    assert result == {"Taylor Swift": "Blank Space"}

def test_list_playlist_returns_list_artists_song_names():
    music_tracker = MusicTracker()
    music_tracker.add_music("Justin Beiber", "Sorry")
    music_tracker.add_music("SZA", "Kill Bill")
    music_tracker.add_music("Taylor Swift", "Blank Space")
    result = music_tracker.see_playlist()
    assert result == [("Justin Beiber", "Sorry"), ("SZA", "Kill Bill"), ("Taylor Swift", "Blank Space")]