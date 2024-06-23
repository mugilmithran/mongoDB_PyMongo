import pymongo

conn_str = "mongodb+srv://mugilmithran01:mithran1698@cluster0.cfxmvyc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

try:
    client = pymongo.MongoClient(conn_str)
except Exception:
    print("Error:" + Exception)

myDb = client["mydatabase"]

myCollection = myDb["sample"]

# myCollection.insert_many([
#    { "_id": 100, "sku": "abc123", "description": "Single line description." },
#    { "_id": 101, "sku": "abc789", "description": "First line\nSecond line" },
#    { "_id": 102, "sku": "xyz456", "description": "Many spaces before     line" },
#    { "_id": 103, "sku": "xyz789", "description": "Multiple\nline description" },
#    { "_id": 104, "sku": "Abc789", "description": "SKU starts with A" }
# ])

# result = myCollection.find({"sku": {"$regex": "789$"}})

# result = myCollection.find({"sku": {"$regex": "^Abc"}})

result = myCollection.find({"description": {"$regex": "S"}})


for document in result:
    print(document)