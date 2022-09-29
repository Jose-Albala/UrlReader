from flask import json

# Serialize(e.g print out the object) the File Object to JSON
class File:
    def __init__(self, type, url):
        self.type = type
        self.url = url

    def __iter__(self):
        yield from {
            "type": self.type,
            "url": self.url
        }.items()

    def __str__(self):
        return json.dumps(dict(self))

    def to_json(self):
        return self.__str__()