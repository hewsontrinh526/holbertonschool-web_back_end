#!/usr/bin/env python3
"""
A function that lists all documents in a collection
"""
import pymongo


def list_all(mongo_collection):
    """
    Returns an empty list if no document in the collection
    """
    return mongo_collection.find()