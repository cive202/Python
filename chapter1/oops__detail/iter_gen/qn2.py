'''
Write a Python generator function batch_reader(data, batch_size) that yields data in fixed-size batches. 
Demonstrate its use on a list of 20 records.
'''


def batch_reader(data, batch_size):
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]


records = [f"record_{i}" for i in range(1, 21)]
batchsize = 5
for i, batch_data in enumerate(batch_reader(records, 5), start=1):
    print(f"{i} is {batch}")


def batch_data(data, batch_size):
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]
        # data[0:5]
        # data[5-10]
