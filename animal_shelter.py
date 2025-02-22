from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        
        USER = 'aacuser'
        PASS = 'aacuser'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31506
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            result = self.collection.insert_one(data)  # Insert data into the collection
            return True if result.inserted_id else False  # Return True if successful, else False
        else:
            raise Exception("Nothing to create, Parameter is empty")

# Create method to implement the R in CRUD.
    def read(self, query):
        if query is None:
            return []
        else:
            cursor = self.collection.find(query)  # Query documents based on the provided query
            result = list(cursor) # Convert cursor to list of documents
            return result
    
    def update(self, query, new_data):
        if query is None or new_data is None:
            raise exception("Parameters cannot be empty")
            
        result = self.collection.update_one(query, {'$set': new_data})  # updates a single document that mathces the query if any
        
        if result.matched_count > 0:
            return result.modified_count    # Return True if document is updated
        return False    # Return False if no document matched the query
    
    def delete(self, query):
        if query is None:
            raise exception("nothing to delete, Parameter is empty")
            
        result = self.collection.delete_one(query)    #Deletes a single document that matches the query if any
        
        if result.deleted_count > 0:
            return result.deleted_count    # Returns True if the document is deleted
        return False    # Returns False if no document is deleted
        