

## 1. Describe the Problem

As a user
So I don't forget the details
I want to keep a record of friends' names and birthdates

As a user
So I can make edits when I've got dates wrong
I want to be able to update a record by passing in a name and new date

As a user
So I can make edits when people change their name
I want to be able to update a record by passing in an old and a new name

As a user
So I can remember to send birthday cards at the right time
I want to be able to list friends whose birthdays are coming up soon and to whom I need to send a card

As a user
So I can buy age-appropriate birthday cards
I want to calculate the upcoming ages for friends with birthdays

As a user
So I can keep track of cards sent and to be sent
I want to be able to mark a birthday card for a year as "done"

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class BirthdayBook:
    def __init__(self):
        self.friends = {}
        # Going to have a dictionary with names as key and value as nested dictionary which contains birthdate and if card sent. 

    def addBirthday(self, name, birthdate):
        
        
    def editBirthdays(self,name, newDate):

    def editName(self,name, newName):

    def upcomingBirthdays(self):
        # returns list of birthdays for upcoming month 

    def agesUpcomingBirthdays(self):
        # returns name and age for each person with an upcoming birthday that month. 

    def markSent(self,name):
        # returns nothing but changes sent to sent current year. 

    def checkIfSent(self, name):
        # Finds name and checks if sent this year. 


## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

- Given an empty birthday book self.friends returns an empty dictionary {}

- Given the addBirthday method, adds a name and a birthday and last sent as None to self.friends. 

- addBirthday method raises an error if name is not a string, birthday is not the correct format. 

 -Given editBirthday, changes birthday date to new date. 

- Given editBirthday, returns an error if name is not found or not a string and if new date is not correct format. 

- editName returns error if name is not found and new name is not a string. 

given upcomingBirthdays returns list of all birthdays coming up this month. 

agesUpcomingBirthdays returns a list of name and age of upcoming birthdays. 

markSent changes lastSent in relevant person to current year.

markSent throws error if name not found. 

if markSent already contains current year, throw error. 

checkIfSent throws error if name not found. 

checkIfSent returns True if last sent is current year for name entered. 

checkIfSent returns False if it is not the current year 





```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
