

from pymongo import MongoClient
 
url = "mongodb+srv://admin:admin@cluster0.7vyzi7i.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech
 
students = db.students
 
student_list = students.find({})

print("\n  students documents from the find() query  ")
 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

Freddie = students.find_one({"student_id": "1007"})

print("\n  student document from the find_one() query  ")

print("  Student ID: " + Freddie["student_id"] + "\n  First Name: " + Freddie["first_name"] + "\n  Last Name: " + Freddie["last_name"] + "\n")

input("\n  End of program, press the Enter key to continue ... ")
