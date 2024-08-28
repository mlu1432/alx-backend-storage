#!/usr/bin/env python3
"""
Module for inserting a new document in a MongoDB collection.
"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a MongoDB collection based on kwargs.

    :param mongo_collection: pymongo collection object
    :param kwargs: dictionary of values to insert as a new document
    :return: the _id of the inserted document
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
