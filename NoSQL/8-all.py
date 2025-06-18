#!/usr/bin/env python3
def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.
    Returns an empty list if no documents are found.
    """
    return list(mongo_collection.find())