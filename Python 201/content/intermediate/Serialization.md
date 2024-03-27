### Serialization
Process of translating Data Structures or Objects into a format to store/transmit and later de-serialized.

```python
import pickle
dict = {'a':100,'b':300,'c':888}
for key, val in dict.items():
    print(key,val)
# a 100
# b 300
# c 888

serialized = pickle.dumps(dict)
print(serialized)
# b'\x80\x04\x95\x19\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x01a\x94Kd\x8c\x01b\x94M,\x01\x8c\x01c\x94Mx\x03u.'

de_serialized = pickle.loads(serialized)
print(de_serialized)
# {'a': 100, 'b': 300, 'c': 888}

for key, val in de_serialized.items():
    print(key,val)
# a 100
# b 300
# c 888
```

Save the data to disk and read data from disk.
We are storing the atribute of objects (not objects themselves).
lambda functions and generators are harder to serialize.
``` python
data =  {'a'=76543,'b'=3456}
with open("serialized.pickle", 'wb') as handle: #write bytes
    pickle.dump(data, handle)

with open("serialized.pickle", 'rb') as handle: #read bytes
    file_data = pickle.load(data, handle)

print(file_data)
```
