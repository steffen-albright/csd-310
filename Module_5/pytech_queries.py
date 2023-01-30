from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.7vyzi7i.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

students = db.students

docs = students.find({})

for doc in docs:
	print(doc)


doc = students.find_one({"student_id": "1007"})

print(doc["student_id"])
