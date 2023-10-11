#!/usr/bin/env python3

"""
updating a document using pymongo
"""


def update_topics(mongo_collection, name, topics):
    """
    updates the topics

    Args:
        mongo_collection (_type_): _description_
        name (_type_): _description_
        topics (_type_): _description_
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
