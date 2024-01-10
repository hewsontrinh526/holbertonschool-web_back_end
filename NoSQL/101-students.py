#!/usr/bin/env python3
"""
A function that returns all students sorted by average score
"""
import pymongo


def top_students(mongo_collection):
    """
    Returns all students stored by average score
    """
    return mongo_collection.aggregate([
        {"$project": {"name": "$name",
                      "averageScore": {"$avg": "$topics.score"}}},
        {"$sort": {"averageScore": -1}}
    ])
