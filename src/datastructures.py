
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # Fill this method and update the return
        if member.age > 0:
            new_member = {
                "id": self._generateId(),
                "first_name": member.first_name,
                "last_name": self.last_name,
                "age": member.age,
                "lucky_numbers": member.lucky_numbers
            }

            self._members.append(new_member)
            return "A NEW MEMBER WAS ADDED SUCCESSEFULLY"
        return "A MEMBER'S AGE MUST BE GREATER THAN ZERO!"

    def update_member(self, id, member):
        for family_member in self._members:
            if family_member["id"] == id and member.age > 0:
                family_member["first_name"] = member.first_name
                family_member["age"] = member.age
                family_member["lucky_numbers"] = member.lucky_numbers
                return "MEMBER UPDATED SUCCESSEFULLY"
            
            return "NO FAMILY MEMBER WITH THAT ID WAS FOUND OR THE MEMBER'S AGE MUST BE GREATER THAN ZERO!"

    def delete_member(self, id):
        # fill this method and update the return
        self._members = list(filter(lambda m: m["id"] != id, self._members))


    def get_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member["id"] == id:
                return {
                    "id": member["id"],
                    "first_name": member["first_name"],
                    "last_name": member["last_name"],
                    "age": member["age"],
                    "lucky_numbers": member["lucky_numbers"]
                }

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
    
    
class Person:

    def __init__(self, first_name: str, age: int, lucky_numbers: list[int]):
        self.first_name = first_name
        self.age = age
        self.lucky_numbers = lucky_numbers