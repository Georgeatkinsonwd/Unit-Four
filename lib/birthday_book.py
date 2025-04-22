# File: birthday_book.py
from datetime import datetime
from dateutil.relativedelta import relativedelta

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
        upcoming_birthdays = {}
        NOW = datetime.now()
        thirty_days_from_now = NOW+relativedelta(days=+30)
        people = [*self.friends]
        for person in people:
            birthday = datetime.strptime(self.friends[person]["Birthdate"], "%d-%m-%Y")
            if birthday.month < NOW.month:
                next_birthday = birthday.replace(year=NOW.year + 1)
            else:
                next_birthday = birthday.replace(year=NOW.year)
            if NOW <= next_birthday <= thirty_days_from_now:
                upcoming_birthdays.update({person: self.friends[person]})
        return upcoming_birthdays


    def ages_upcoming_birthdays(self):
        # returns name and age for each person with an upcoming birthday that month. 
        ages_of_upcoming = []
        upcoming_birthdays = self.upcoming_birthdays()
        people = [*upcoming_birthdays]
        NOW = datetime.now()
        for person in people:
            birthday = datetime.strptime(self.friends[person]["Birthdate"], "%d-%m-%Y")
            difference = relativedelta(NOW, birthday)
            age = difference.years + 1
            ages_of_upcoming.append((person, age))
        return ages_of_upcoming

    def mark_sent(self,name):
        # returns nothing but changes sent to sent current year. 
        self.friends[name]["Last Sent"] = datetime.now().year


    def check_if_sent(self, name):
        # Finds name and checks if sent this year. 
        if self.friends[name]["Last Sent"] == datetime.now().year:
            return True
        else:
            return False