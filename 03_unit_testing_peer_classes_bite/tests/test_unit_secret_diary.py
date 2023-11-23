from lib.secret_diary import *
from unittest.mock import Mock

def test_diary_entry_is_locked_by_default():
    fake_entry = Mock()
    secret_diary = SecretDiary(fake_entry)
    assert secret_diary.locked == True

def test_unlock_unlocks_the_diary_entry():
    fake_entry = Mock()
    secret_diary = SecretDiary(fake_entry)
    secret_diary.unlock()
    assert secret_diary.locked == False

def test_lock_locks_the_diary_after_unlocking():
    fake_entry = Mock()
    secret_diary = SecretDiary(fake_entry)
    secret_diary.unlock()
    secret_diary.lock()
    assert secret_diary.locked == True

def test_read_returns_message_if_diary_locked():
    fake_entry = Mock()
    secret_diary = SecretDiary(fake_entry)
    assert secret_diary.read() == "Go Away!"

def test_read_returns_contents_if_diary_unlocked():
    fake_entry = Mock()
    fake_entry.read.return_value = "I am contents"
    secret_diary = SecretDiary(fake_entry)
    secret_diary.unlock()
    assert secret_diary.read() == "I am contents"

