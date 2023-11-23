from lib.track import *

# Test that init creates new instance with title
# and artist
def test_init_for_title_and_artist():
    track1 = Track("Title1", "Artist1")
    assert track1.title == "Title1"
    assert track1.artist == "Artist1"

# Test matches function returns True if keyword is found in
# title or artist
def test_init_for_title_and_artist():
    track1 = Track("Title1", "Artist1")
    track2 = Track("Title2", "Artist2")
    assert track1.matches("Artist1") == True
    assert track2.matches("Title2") == True


