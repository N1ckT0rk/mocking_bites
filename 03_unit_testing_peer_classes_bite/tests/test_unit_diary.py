from lib.diary import *

def test_diary_init():
    new_entry = Diary("I am the contents")
    assert new_entry.contents == "I am the contents"

def test_diary_read():
    new_entry = Diary("I am the contents")
    assert new_entry.read() == "I am the contents"