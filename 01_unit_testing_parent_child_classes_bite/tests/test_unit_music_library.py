from lib.music_library import *
from unittest.mock import Mock

# Test music library returns empty list if no instances
def test_music_library_for_empty_list():
    myLibrary = MusicLibrary()
    assert myLibrary.tracks == []

# # Test add function adds a track to the tracks list
def test_add_adds_track_to_list_with_mocks():
    myLibrary = MusicLibrary()
    fake_track_1 = Mock()
    myLibrary.add(fake_track_1)
    assert myLibrary.tracks == [fake_track_1]

# Test search function returns the track if it keyword matches
# artist or title
def test_add_adds_track_to_list_with_mocks():
    myLibrary = MusicLibrary()
    fake_track_1 = Mock()
    fake_track_1.matches.return_value = True
    myLibrary.add(fake_track_1)
    assert myLibrary.search("hello") == [fake_track_1]


