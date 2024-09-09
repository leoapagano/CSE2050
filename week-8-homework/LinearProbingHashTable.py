from UniqueLinkedList import UniqueLinkedList

class LinearProbingHashTable:
    def __init__(self, MINBUCKETS=2, MINLOADFACTOR=0.1, MAXLOADFACTOR=0.75):
        """Constructor for the LinearProbingHashTable class.
        MINBUCKETS defaults to 2, MINLOADFACTOR defaults to 0.1, and MAXLOADFACTOR defaults to 0.75.
        O(1) time complexity."""
        if MAXLOADFACTOR >= 1:
            raise ValueError
        else:
            self._min_buckets = self.buckets = MINBUCKETS
            self.min_lf = MINLOADFACTOR
            self.max_lf = MAXLOADFACTOR
            self._L = [None for i in range(self.buckets)]
            self._len = 0


    def __len__(self):
        """Built-in length dunder method for the LinearProbingHashTable class."""
        return self._len
    

    def __setitem__(self, key, value):
        """Built-in index setting method for the LinearProbingHashTable class."""
        bucket_idx = hash(key) % self.buckets
        for i in range(self.buckets):
            current_idx = (bucket_idx + i) % self.buckets

            # Set empty item
            if self._L[current_idx] in (None, -1):
                # update list
                self._L[current_idx] = (key, value)
                self._len += 1
                # attempt to rehash
                self._rehash()
                return

            # Set existing item
            elif self._L[current_idx][0] == key:
                # update list
                self._L[current_idx] = (key, value)
                return
                
        # entire thing is full??? somehow
        raise RuntimeError(f"it's over 9000! (the hash table overflowed - check that it's rehashing properly)")


    def __getitem__(self, key):
        """Built in single-item selection method for the LinearProbingHashTable class."""
        bucket_idx = hash(key) % self.buckets
        for i in range(self.buckets):
            current_idx = (bucket_idx + i) % self.buckets
            if self._L[current_idx] not in (None, -1):
                if self._L[current_idx][0] == key:
                    # caught
                    return self._L[current_idx][1]
                
        # not caught
        raise KeyError(f"{key} not found in hash table")


    def __contains__(self, key):
        """Built-in membership testing dunder method for the LinearProbingHashTable class."""
        bucket_idx = hash(key) % self.buckets
        for i in range(self.buckets):
            current_idx = (bucket_idx + i) % self.buckets

            # Emptied slot - stop
            if self._L[current_idx] == -1:
                return False
            
            # Non-empty slot
            elif self._L[current_idx] is not None:
                if self._L[current_idx][0] == key:
                    # caught
                    return True
                
            # Ignore empty (None) slots
                
        # not caught
        return False


    def pop(self, key):
        """Remove an item {key} and its value from a LPHT. Returns the aforementioned value."""
        bucket_idx = hash(key) % self.buckets
        for i in range(self.buckets):
            current_idx = (bucket_idx + i) % self.buckets
            if self._L[current_idx] not in (None, -1):
                if self._L[current_idx][0] == key:
                    # caught
                    val = self._L[current_idx][1]
                    self._len -= 1
                    self._L[current_idx] = -1
                    self._rehash()
                    return val
                
        # not caught
        raise KeyError(f"{key} not found in hash table")


    def get_loadfactor(self):
        """Determine the load factor of a LinearProbingHashTable object."""
        return self._len / self.buckets
    

    def _rehash(self):
        """Rehashes the hashtable only if its current load factor is above MAXLOADFACTOR or below MINLOADFACTOR."""
        current_lf = self.get_loadfactor()

        # Which way to go? Update number of buckets
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
        self._new_L = [None for i in range(self.buckets)]

        # Add each existing bucket item to new bucket list
        for bucket in self._L:
            # Only readd non-empty buckets
            if bucket not in (None, -1):
                # Get basic info
                key, value = bucket[0], bucket[1]
                new_item_idx = hash(key) % self.buckets

                # Look for new position
                for i in range(self.buckets):
                    current_idx = (new_item_idx + i) % self.buckets
                    # Set empty item
                    if self._new_L[current_idx] is None: self._new_L[current_idx] = (key, value); break
            
        # Remap self._L
        self._L = self._new_L

    def __repr__(self):
        s = "\n"
        for idx, i in enumerate(self._L):
            if i is None:
                s += f"Slot {idx}: EMPTY\n"
            elif i == -1:
                s += f"Slot {idx}: EMPTIED\n"
            else:
                s += f"Slot {idx}: {i}\n"
        return s