from pymongo import MongoClient


def get_mongo_client(username, password, clustername, clusterlink, clientname):
    # Initializing connection for mongodb
    connection_string = f"mongodb+srv://{username}:{password}@{clustername}.{clusterlink}.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(connection_string)
    return client[clientname]

def update_document(collection, document):
    try:
        collection.update_one({"name": document['name']}, {"$set": document}, upsert=True)
        return True
    except Exception as ex:
        print(ex)
        return False
