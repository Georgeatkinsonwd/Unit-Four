# File: birthday_book.py
from datetime import datetime

class BirthdayBook:
    def __init__(self):
        self.friends = {}
        # Going to have a dictionary with names as key and value as nested dictionary which contains birthdate and if card sent. 
        pass

    def add(self, name, birthdate):
        if not isinstance(name, str) or not isinstance(birthdate, str):
            raise Exception("Birthday book only accepts strings as arguments")
        try: 
            datetime.strptime(birthdate, "%d-%m-%Y")
        except ValueError:
            raise ValueError("Birthdate must be format DD-MM-YYYY")
        self.friends.update({name: {"Birthdate": birthdate, "Last Sent": None}})

    def view_friends(self):
        return self.friends        
        
    def edit_birthdate(self,name, new_date):
        if not isinstance(name, str) or not isinstance(new_date, str):
            raise Exception("Arguments must be strings")
        try: 
            datetime.strptime(new_date, "%d-%m-%Y")
        except ValueError:
            raise ValueError("Birthdate must be format DD-MM-YYYY")
        try:
            self.friends[name]["Birthdate"] = new_date
        except KeyError:
            raise Exception("Name not in birthday book")


        
    def edit_name(self,name, newName):
        self.friends.update({newName: self.friends[name]})
        self.friends.pop(name)

    def upcoming_birthdays(self):
        # returns list of birthdays for upcoming month 
        pass

    def ages_upcoming_birthdays(self):
        # returns name and age for each person with an upcoming birthday that month. 
        pass

    def mark_sent(self,name):
        # returns nothing but changes sent to sent current year. 
        pass

    def check_if_sent(self, name):
        # Finds name and checks if sent this year. 
        pass