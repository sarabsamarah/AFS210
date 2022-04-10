class HashTable:
    def __init__(self) -> None:
        self.size = 10
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashfunction(self,key):
        # Insert your hashing function code
        return key % self.size 

    def rehash(self,key):
        # Insert your secondary hashing function code
    return key // self.size
    def put(self,key,data):
        # Insert your code here to store key and data 
    hashvalue = self.hashfunction(key,self.size)
    if self.slots[hashvalue] == key: #update value
    def get(self,key):
        # Insert your code here to get data by key

    def __getitem__ (self,key):
        return self.get(key)

    def __setitem__ (self,key,data):
        self.put(key,data)


H = HashTable()
H[69] = 'A'
H[66] = 'B'
H[80] = 'C'
H[35] = 'D'
H[18] = 'E'




print (H.slots)
# Store remaining input data

# print the slot values

# print the data values

# print the value for key 52

