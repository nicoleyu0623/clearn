class HashTable:
    def __init__(self):
        self._table = [None]*10000  #storage is fixed

    def store(self,string):
        """Input a string that's stored in
        the table."""
        idx = self._calculate_hash_value(string)
        if idx != -1:
            if self._table[idx]: # element already exists
                self._table[idx].append(string)
            else:
                self._table[idx] = [string]

    def lookup(self,string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        idx = self._calculate_hash_value(string)
        if self._table[idx]:
            if string in self._table[idx]:   # this check adds robustness for lookups
                return idx
        return -1


    def _calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        if len(string) == 0:
            return 0                    # 0th index for empty string
        return ord(string[0])*100+ord(string[1])

