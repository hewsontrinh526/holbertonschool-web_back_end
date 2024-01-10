#!/usr/bin/env python3
"""
A script that provides some stats about Nginx logs stored in MongoDB and the
top 10 of the most present IPs in the collection nginx of the database logs
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("localhost", 27017)
    db = client.logs
    collection = db.nginx
    docs = collection.count_documents({})

    print("{} logs".format(docs))
    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        count = collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))
        filter_path = {"method": "GET", "path": "/status"}

    print("{} status check".format(collection.count_documents(filter_path)))
    print("IPs:")

    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]

    ips = collection.aggregate(pipeline)

    for ip in ips:
        print("\t{}: {}".format(ip.get("_id"), ip.get("count")))
