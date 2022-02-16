import json


class Employee:

    def edetails(self):
        var = {
            "subjects": {
                "science": 85,
                "physics": 90

            }
        }
        with open("jsonAssignment.json", "w") as p:
            json.dump(var, p)


class Department(Employee):

    def dDetails(self):
        super()

        f = open('jsonAssignment.json', 'r')

        data = json.load(f)

        print(data)


object = Department()

object.dDetails()

# print(object.dDetails())
