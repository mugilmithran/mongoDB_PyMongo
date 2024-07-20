# Importing necessary modules:
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import os
import pymongo

# Retrieved password from a newly created '.env' file.
password = os.environ.get("MONGODB_PWD")

# Created a mongodb connection string.
conn = f'mongodb+srv://mugilmithran01:{password}@cluster0.cfxmvyc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'

client = pymongo.MongoClient(conn)

# Creating a database named 'students'.
# students = client.students

# Creating a collection named 'details'.
# details = students.details

# Inserting one document to the collection.
# details.insert_one({"Name": "Mugilmithran", "Age": 20, "Course": "Bigdata"})

# # Inserting multiple documents to the collection.
# details.insert_many([{"Name": "Ragul", "Age": 26, "Course": "Bigdata"}, 
#                      {"Name": "Rajeev", "Age": 24, "Course": "Bigdata"}, 
#                      {"Name": "Ramnath", "Age": 22, "Course": "Bigdata"},
#                      {"Name": "Bo", "Age": 30, "Course": "Bigdata"}])

# Updating a document's 'Name' by '_id' from the collection.
# details.update_one({"Name": "Mugilmithran"}, {"$set": {"Name": "Kathiravan"}})

# Deleting a document, which is named as 'Mugilmithran'
# details.delete_one({'Name': 'Mugilmithran'})

#Initializing a document relationship.
# address = {
#     "Street": "Bay street",
#     "Number": 2706,
#     "City": "San francisco",
#     "Country": "Country"
# }

# details.update_one({"Name": "Ragul"}, {"$addToSet": {"address": address}})



