from UniqueLinkedList import UniqueLinkedList

class SeparateChainingHashTable:
    def __init__(self, MINBUCKETS=2, MINLOADFACTOR=0.5, MAXLOADFACTOR=1.5):
        """Constructor for the SeparateChainingHashTable class.
        MINBUCKETS defaults to 2, MINLOADFACTOR defaults to 0.5, and MAXLOADFACTOR defaults to 1.5.
        O(1) time complexity."""
        self._min_buckets = self.buckets = MINBUCKETS
        self.min_lf = MINLOADFACTOR
        self.max_lf = MAXLOADFACTOR
        self._L = [UniqueLinkedList() for i in range(self.buckets)]
        self._len = 0

    def __len__(self):
        """Built-in length method for the SeparateChainingHashTable class.
        O(1) time complexity."""
        return self._len
    
    def __setitem__(self, key, value):
        """Built-in index setting method for the SeparateChainingHashTable class.
        O(1) amortized time complexity."""
        bucket_idx = hash(key) % self.buckets
        self._len += (self._L[bucket_idx]).add(key, value)
        self._rehash()

    def __getitem__(self, key):
        """Built-in single-item selection method for the SeparateChainingHashTable class.
        O(1) amortized time complexity."""
        bucket_idx = hash(key) % self.buckets
        return (self._L[bucket_idx]).get(key)

    def __contains__(self, key):
        """Built-in membership testing method for the SeparateChainingHashTable class.
        O(1) amortized time complexity."""
        bucket_idx = hash(key) % self.buckets
        return key in self._L[bucket_idx]

    def pop(self, key):
        """Removes a key from the SeparateChainingHashTable class and returns its corresponding value.
        O(1) amortized time complexity."""
        bucket_idx = hash(key) % self.buckets
        val = (self._L[bucket_idx]).remove(key)
        self._len -= 1
        self._rehash()
        return val 

    def get_loadfactor(self):
        """Returns the load factor for a given instance of the SeparateChainingHashTable class.
        O(1) time complexity."""
        return self._len / self.buckets
    
    def _rehash(self):
        """Rehashes the hashtable only if its current load factor is above MAXLOADFACTOR or below MINLOADFACTOR."""
        current_lf = self.get_loadfactor()

        # Which way to go?
        if current_lf > self.max_lf: # Up
            self.buckets *= 2
        elif self.min_lf > current_lf: # Down
            if (self.buckets // 2) >= self._min_buckets:
                self.buckets = self.buckets // 2
            else:
                return # Done
        else:
            return # Done

        # Build new buckets
        self._new_L = [UniqueLinkedList() for i in range(self.buckets)]

        # Add each existing node to new buckets
        for bucket in self._L:
            for Node in bucket:
                new_bucket_idx = hash(Node[0]) % self.buckets
                (self._new_L[new_bucket_idx]).add(Node[0], Node[1])

        # Remap self._L
        self._L = self._new_L