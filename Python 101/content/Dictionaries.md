## Dictionaries {}
Key:value Hashtable data structures.

Does not allow for repeating keys.

`dict = {"key":"value", 0b1:100, "list":[0, 1], 'a':{'b':'c'}}`

dictionary support many objects, including nested dictionaries.

##### initialize an empty dictionary
`dict_empty = {}` or `dict_empty=dict()`
## Methods
#### access elements with key, `dict[key]`
`dict["key"]` __>>>__ 'value'
#### get all keys, `.keys()`
`dict.keys()`
#### get all items, `.items()`
`dict.items()` __>>>__ dict_items([(key, value)])
#### add new key, value pairs, `dict[newkey] = newval`
`dict["newK"] = "newV"`
#### change val, `dict[key] = newval`
`dict["key"] = "newValue:`
#### change val, `.update({key:newval})`
`dict.update({"key":"newValue"})`
#### remove & return item, `.pop(key)`
`dict.pop("key") __>>>__ val
#### remove item, `del dict[key]`
`del dict["key]`
