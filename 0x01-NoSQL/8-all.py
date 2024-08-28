#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """


def list_all(mongo_collection):
    """ List all documents in a MongoDB collection

    :param mongo_collection: pymongo collection object
    :return: List of all documents in the collection, or an empty if none found
    """
    return list(mongo_collection.find())
