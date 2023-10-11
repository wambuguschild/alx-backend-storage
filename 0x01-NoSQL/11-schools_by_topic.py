#!/usr/bin/env python3

"""
filtering schools by topic
"""


def schools_by_topic(mongo_collection, topic):
    """  filter the schools by topic"""
    return mongo_collection.find({"topics": topic})
