class MemoryModule:
    def __init__(self):
        self.storage = {}

    def remember(self, key, value):
        self.storage[key] = value

    def recall(self, key):
        return self.storage.get(key)

