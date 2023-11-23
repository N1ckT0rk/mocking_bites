from lib.secret_diary import *
from lib.diary import *

def test_diary_entry_is_locked_by_default():
    entry = Diary("This is some contents")
    secret_diary = SecretDiary(entry)
    assert secret_diary.locked == True

def test_unlock_unlocks_the_diary_entry():
    entry = Diary("This is some contents")
    secret_diary = SecretDiary(entry)
    secret_diary.unlock()
    assert secret_diary.locked == False

def test_lock_locks_the_diary_after_unlocking():
    entry = Diary("This is some contents")
    secret_diary = SecretDiary(entry)
    secret_diary.unlock()
    secret_diary.lock()
    assert secret_diary.locked == True

def test_read_returns_message_if_diary_locked():
    entry = Diary("This is some contents")
    secret_diary = SecretDiary(entry)
    assert secret_diary.read() == "Go Away!"

def test_read_returns_contents_if_diary_unlocked():
    entry = Diary("This is some contents")
    secret_diary = SecretDiary(entry)
    secret_diary.unlock()
    assert secret_diary.read() == "This is some contents"


