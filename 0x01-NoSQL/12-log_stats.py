#!/usr/bin/env python3

""" getting logs"""
from pymongo import MongoClient


def log_stats():
    """ log stats"""
    client = MongoClient('mongodb://localhost:27017')

    db = client.logs
    collection = db.nginx

    total_logs = collection.count_documents({})

    print(f"{total_logs} logs")
    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"    method {method}: {count}")

    specific_method = "GET"
    specific_path = "/status"
    specific_count = collection.count_documents(
        {"method": specific_method, "path": specific_path})
    print(f"{specific_count} status check")


if __name__ == "__main__":
    log_stats()
