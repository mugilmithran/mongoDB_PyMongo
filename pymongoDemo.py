#Step 1 - Install and import pymongo
#pymongo consists tools or function use to interact with MongoDB database
import pymongo

#Step 2 - Create mongodb client
#Python PyMongo MongoClient allows Developers to establish a connection between 
#their Python application and MongoDB to manage data in a NoSQL Database
#MongoClient is class 
#Client is an instance
conn_str = "mongodb+srv://USERname:Password@cluster0.kg23ucg.mongodb.net/?retryWrites=true&w=majority"
try:
	client = pymongo.MongoClient(conn_str)
except Exception:
	print("Error:" + Exception)

#Step 3: Create a db
myDb = client["Firstdb"]

#print (client.list_database_names())
     
#Step 4: Create a collection
myCollection = myDb["Firstdb"]


#Step 5: Create a document/ record
myDoc = {
		"id_":0,
		"name":"Queens",
		"message":"This is pymong demo"
	}



#insert the document
myCollection.insert_one(myDoc)

#insert many

myDoc1 = {
		"id_":0,
		"name":"College1",
		"message":"This is pymong demo1"
	}
#myCollection.insert_one([myDoc, myDoc1])

#find one record
results = myCollection.find_one({"name":"Queens"})


#find many records  record
#results = myCollection.find({})
results = myCollection.find({"name":"Queens"})

print(results)

for result in results:
		#print(result)
		print(result["_id"])

#delete one record
results_del = myCollection.delete_one({"_id":0})
#delete many record
results_del = myCollection.delete_many({"_id":0})

#update one
result_update = myCollection.update_one({"_id":5},{"$set":{"name":"Queen"}})

res_count = myCollection.count_documents({})
print(res_count)
