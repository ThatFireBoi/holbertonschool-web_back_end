#!/usr/bin/env python3
"""Improve 12-log_stats.py by adding the top 10 of the most present IPs
in the collection nginx of the database logs"""

from pymongo import MongoClient


def log_stats():
    """Print some stats about Nginx logs in MongoDB"""
    client = MongoClient('mongodb://localhost:27017')
    logs_collection = client.logs.nginx
    print("{} logs".format(logs_collection.count_documents({})))
    print("Methods:")
    print("\tmethod GET: {}".
          format(logs_collection.count_documents({"method": "GET"})))
    print("\tmethod POST: {}".
          format(logs_collection.count_documents({"method": "POST"})))
    print("\tmethod PUT: {}".
          format(logs_collection.count_documents({"method": "PUT"})))
    print("\tmethod PATCH: {}".
          format(logs_collection.count_documents({"method": "PATCH"})))
    print("\tmethod DELETE: {}".
          format(logs_collection.count_documents({"method": "DELETE"})))
    print("{} status check".
          format(logs_collection.count_documents({"method": "GET",
                                                  "path": "/status"})))
    print("IPs:")
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    ips = logs_collection.aggregate(pipeline)
    for ip in ips:
        print("\t{}: {}".format(ip.get("_id"), ip.get("count")))
    print("{} status check".
          format(logs_collection.count_documents({"method": "GET",
                                                  "path": "/status"})))
