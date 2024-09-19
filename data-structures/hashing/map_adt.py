from typing import List

def load_factor(hash_table):
    size = len(hash_table)
    occupy_count = 0
    for item in hash_table:
        if item is not None:
            occupy_count += 1
    if size != 0:
        return occupy_count / size

class HashTable:
    def __init__(self) -> None:
        self.size = 11
        self.slots: List[int | None] = [None] * self.size
        self.data: List[int | str | None] = [None] * self.size

    def put(self, key: int, data: int | str):
        hash_v = self.hash_function(key, self.size)
        print(hash_v)

        if self.slots[hash_v] is None:
            self.slots[hash_v] = key
            self.data[hash_v] = data
        else:
            if self.slots[hash_v] == key:
                self.data[hash_v] = data
            else:
                position = self.rehash(hash_v, self.size)
                print(position)
                while self.slots[position] is not None and position != hash_v:
                    position = self.rehash(position, self.size)
                    print(position, hash_v, self.slots[position] )
                if position != hash_v:
                    self.slots[position] = key
                    self.data[position] = data

    def get(self, key):
        start_pos = self.hash_function(key, self.size)

        if self.slots[start_pos] == key:
            return self.data[start_pos]
        else:
            rehash = self.rehash(start_pos, self.size)
            while self.slots[rehash] != key and rehash != start_pos:
                rehash = self.rehash(rehash, self.size)
            if rehash != start_pos: 
                return self.data[rehash]


    def rehash(self, key: int, size: int) -> int:
        return (key + 1) % size

    def hash_function(self, key: int, size: int) -> int:
        return key % size

    def __repr__(self) -> str:
        return f"{self.slots}\n{self.data}"

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def load_factor(self):
        size = len(self.slots)
        occupy_count = 0
        for item in self.slots:
            if item is not None:
                occupy_count += 1
        if size != 0:
            return occupy_count / size


if __name__ == "__main__":
    ht = HashTable()

    ht[54] = "cat"

    ht[26] = "dog"

    ht[93] = "lion"

    ht[17] = "tiger"

    ht[77] = "bird"

    ht[31] = "cow"

    ht[44] = "goat"

    ht[55] = "pig"

    ht[20] = "chicken"

    # ht[2] = "apple"
    # ht[24] = "apple jouce"
    # print(ht[24])
    print(ht[26])
    print("debug")
    ht[26] = 'applejeuice'
    print(ht[26])
    print(ht)
    print(ht.load_factor())
