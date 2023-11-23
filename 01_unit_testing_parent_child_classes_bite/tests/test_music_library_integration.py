from lib.music_library import *
from lib.track import *

# Test music library returns empty list if no instances
def test_music_library_for_empty_list():
    myLibrary = MusicLibrary()
    assert myLibrary.tracks == []

# Test add track adds instance to list
    myLibrary = MusicLibrary()
    track1 = Track("Title1", "Artist1")
    track2 = Track("Title2", "Artist2")
    myLibrary.add(track1)
    myLibrary.add(track2)
    assert myLibrary.tracks == [track1, track2]

# Test search returns a list of instances of a track
# that match the keyword
def test_search_returns_keyword_instances_of_track():
    myLibrary = MusicLibrary()
    track1 = Track("Title1", "Artist1")
    track2 = Track("Title2", "Artist2")
    myLibrary.add(track1)
    myLibrary.add(track2)
    assert myLibrary.search("Artist2") == [track2]


