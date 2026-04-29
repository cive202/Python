'''
Write a Python class RecordIterator that iterates over a list of patient records and yields one record at a time.
Demonstrate its use in a data science context.
'''


class RecordIterator:

    def __init__(self, list1):
        self.list1 = list1
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.list1):
            record = self[self.index]
            self.index += 1
            return record
        else:
            raise StopIteration


patients = [
    {"id": 1, "name": "Ram", "age": 45, "bp": 120},
    {"id": 2, "name": "Sita", "age": 50, "bp": 140},
    {"id": 3, "name": "Hari", "age": 60, "bp": 135}
]
