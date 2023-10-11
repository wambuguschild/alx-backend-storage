#!/usr/bin/env python3

"""
    Function that gets inserts a document in collection
"""


def insert_school(mongo_collection, **kwargs):
    """
    inserting a document into school

    Args:
        mongo_collection (_type_): will add data
        based on args
    """
    return mongo_collection.insert_one(kwargs).inserted_id
