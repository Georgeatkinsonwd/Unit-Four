# File: test_birthday_book.py
import pytest
from lib.birthday_book import BirthdayBook

# Given an empty birthday book 
# self.friends returns an empty dictionary {}

def test_empty_birthdaybook_returns_empty_dict():
    birthday_book = BirthdayBook()
    assert birthday_book.friends == {}

# Given the addBirthday method, 
# adds a name and a birthday and last sent as None to self.friends. 

def test_add_adds_friend_dictionary_to_self_friends():
    birthday_book = BirthdayBook()
    birthday_book.add("Adam", "10-10-2010")
    assert birthday_book.view_friends() == {"Adam": 
                                            {"Birthdate": "10-10-2010", 
                                             "Last Sent": None
                                             }
                                            }
    
    #addBirthday method raises an error if name is not a string, 
def test_add_raises_error_if_name_or_birthday_not_string():
    birthday_book = BirthdayBook()
    with pytest.raises(Exception) as e:
        birthday_book.add(26, "10-10-2010")
    error_msg = str(e.value)

    assert error_msg == "Birthday book only accepts strings as arguments"

    with pytest.raises(Exception) as e:
        birthday_book.add("Adam", 2025)
    error_msg = str(e.value)

    assert error_msg == "Birthday book only accepts strings as arguments"
    
#add_birthday raises error if birthday not correct format
def test_add_raises_error_if_birthday_not_correct_format():
    birthday_book = BirthdayBook()
    with pytest.raises(ValueError) as vale:
        birthday_book.add("Adam", "10-10-20")
    error_msg = str(vale.value)
    assert error_msg == "Birthdate must be format DD-MM-YYYY"

# Given editBirthday, changes birthday date to new date. 
def test_edit_birthdate_changes_birthdate():
    birthday_book = BirthdayBook()
    birthday_book.add("Adam", "10-10-2010")
    birthday_book.edit_birthdate("Adam", "20-10-2010")

    assert birthday_book.friends["Adam"]["Birthdate"] == "20-10-2010"

#Given editBirthday, returns an error if name is not found 
def test_edit_birthdate_error_if_name_not_found():
    birthday_book = BirthdayBook()
    birthday_book.add("Adam", "10-10-2010")
    with pytest.raises(Exception) as e:
        birthday_book.edit_birthdate("Tom", "20-10-2010")
    error_msg = str(e.value)

    assert error_msg == "Name not in birthday book"

# Given editBirthday eturns an error if name is not a string
def test_edit_birthdate_error_if_name_or_newdate_not_string():
    birthday_book = BirthdayBook()
    birthday_book.add("Adam", "10-10-2010")
    with pytest.raises(Exception) as e:
        birthday_book.edit_birthdate(56, "20-10-2010")
    error_msg = str(e.value)

    assert error_msg == "Arguments must be strings"

    with pytest.raises(Exception) as e:
        birthday_book.edit_birthdate("Adam", 2025)
    error_msg = str(e.value)

    assert error_msg == "Arguments must be strings"

# Given edit birthdate returns error if birthday not correct format 
def test_edit_birthdate_error_if_newdate_wrong_format():
    birthday_book = BirthdayBook()
    birthday_book.add("Adam", "10-10-2010")
    with pytest.raises(ValueError) as e:
        birthday_book.edit_birthdate("Adam", "20-10-10")
    error_msg = str(e.value)

    assert error_msg == "Birthdate must be format DD-MM-YYYY"

# Given editName , changes name to the new name 
def test_edit_name_changes_to_new_name():
    birthday_book = BirthdayBook()
    birthday_book.add("Adam", "10-10-2010")
    birthday_book.edit_name("Adam", "Tom")

    assert birthday_book.friends.get("Tom") == {"Birthdate": "10-10-2010", 
                                             "Last Sent": None
                                             }
                                            
    
    assert birthday_book.friends.get("Adam") == None

"""
given upcomingBirthdays
returns list of all birthdays coming up this month. 
"""
def test_upcoming_birthdays_lists_birthdays_in_next_month():
    birthday_book = BirthdayBook()
    birthday_book.add("Adam", "18-04-2010")
    birthday_book.add("Anna", "10-05-1999")
    birthday_book.add("Aidan", "15-06-2010")
    
    assert birthday_book.upcoming_birthdays() == {"Adam": 
                                            {"Birthdate": "18-04-2010", 
                                             "Last Sent": None
                                             },
                                             "Anna": 
                                            {"Birthdate": "10-05-1999", 
                                             "Last Sent": None
                                             }}
    
def test_ages_for_upcoming():
    birthday_book = BirthdayBook()
    birthday_book.add("Adam", "18-04-2010")
    birthday_book.add("Anna", "10-05-1999")
    birthday_book.add("Aidan", "15-06-2010")

    assert birthday_book.ages_upcoming_birthdays() == [("Adam", 15), ("Anna", 26)]

def test_ages_for_check_if_sent():
    birthday_book = BirthdayBook()
    birthday_book.add("Adam", "16-04-2010")
    birthday_book.add("Anna", "10-05-1999")
    birthday_book.add("Aidan", "15-06-2010")
    birthday_book.mark_sent("Adam")

    assert birthday_book.check_if_sent("Adam") == True