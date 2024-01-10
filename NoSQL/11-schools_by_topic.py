#!/usr/bin/env python3
"""
A function that returns the list of school having a specific topic
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic
    """
    return mongo_collection.find({"topics": topic})
