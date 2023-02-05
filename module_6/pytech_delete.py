from pymongo import MongoClient
 
url = "mongodb+srv://admin:admin@cluster0.7vyzi7i.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech
 
students = db.students
 
student_list = students.find({})

print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")


for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

new_doc = {
    "student_id": "1010",
    "first_name": "Leather",
    "last_name": "Face"
}

new_doc_id = students.insert_one(new_doc).inserted_id

print("\n  -- INSERT STATEMENTS --")
print("  Inserted student record into the students collection with document_id " + str(new_doc_id))

student_new_doc = students.find_one({"student_id": "1010"})

print("\n  -- DISPLAYING STUDENT TEST DOC -- ")
print("  Student ID: " + student_new_doc["student_id"] + "\n  First Name: " + student_new_doc["first_name"] + "\n  Last Name: " + student_new_doc["last_name"] + "\n")

deleted_student_new_doc = students.delete_one({"student_id": "1010"})
 
revised_student_list = students.find({})
 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in revised_student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

input("\n  End of program, press the Enter key to continue...")
