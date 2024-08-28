#!/usr/bin/env python3
"""
Module for updating topics of a school document in MongoDB.
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates all topics of a school document based on the name.

    :param mongo_collection: pymongo collection object
    :param name: string, the school name to update
    :param topics: list of strings, the list of topics approached in the school
    """
    mongo_collection.update_many(
        { "name": name },
        { "$set": { "topics": topics } }
    )
