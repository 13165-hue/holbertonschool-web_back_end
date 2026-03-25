#!/usr/bin/env python3
"""List all documents in a collection"""


def list_all(mongo_collection):
    """Returns list of all documents in a collection"""
    documents = list(mongo_collection.find())
    if not documents:
        return []
    return documents
