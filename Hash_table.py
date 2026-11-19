class HashTable:
    # Initializes the underlying storage dictionary for the hash table
    def __init__(self):
        self.collection = {}  # Maps hash values -> nested dicts of {key: value}

    # Generates a hash index by summing the Unicode code points of each character
    def hash(self, string):
        return sum(ord(char) for char in string)  

    # Inserts or updates a key-value pair in the hash table
    def add(self, key, value):
        hashed_key = self.hash(key)                 # Compute hash index for the key
        if hashed_key not in self.collection:
            self.collection[hashed_key] = {}        # Create a bucket if hash doesn't exist yet
        self.collection[hashed_key][key] = value    # Store pair inside the bucket (handles collisions)

    # Removes a key-value pair safely without raising an error if missing
    def remove(self, key):
        hashed_key = self.hash(key)
        # Verify both the hash bucket and the specific key exist
        if hashed_key in self.collection and key in self.collection[hashed_key]:
            del self.collection[hashed_key][key]    # Delete the specific key-value pair
            # Clean up the outer bucket if no colliding keys remain inside it
            if not self.collection[hashed_key]:
                del self.collection[hashed_key]

    # Retrieves the value associated with a given key, or None if not found
    def lookup(self, key):
        hashed_key = self.hash(key)
        # Verify both the hash bucket and the specific key exist before returning
        if hashed_key in self.collection and key in self.collection[hashed_key]:
            return self.collection[hashed_key][key]
        return None
