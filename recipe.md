# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

## 2. Design the Class Interface



```python

class MusicTracker():
    def __init__(self):
        self.playlist = {}

    def add_music(self, artist, song_name):
        self.playlist[artist] = song_name

    def see_playlist(self):
        for artist, song_name in self.playlist.items():
            print(f"{artist}: {song_name})
            return list(self.playlist.items())
```

## 3. Create Examples as Tests

"""
initially playlist should return empty {}

"""
def test_initially_playlist_is_empty():
    assert self.playlist == {}

"""
when add_music is called, it stores into the playlist dictionary

"""
def test_music_is_added_to_playlist_dictionary():
    artist = "Taylor Swift"
    song_name = "Blank Space"
    assert self.playlist = {artist: song_name}

"""
when function is called it returns list of artists and song names

"""


``` python
# EXAMPLE

"""
Given a name and a task
#remind reminds the user to do the task
"""
reminder = Reminder("Kay")
reminder.remind_me_to("Walk the dog")
reminder.remind() # => "Walk the dog, Kay!"

"""
Given a name and no task
#remind raises an exception
"""
reminder = Reminder("Kay")
reminder.remind() # raises an error with the message "No task set."

"""
Given a name and an empty task
#remind still reminds the user to do the task, even though it looks odd
"""
reminder = Reminder("Kay")
reminder.remind_me_to("")
reminder.remind() # => ", Kay!"
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._