data = {
    'one':1,
    'two':2,
    'four':4,
    'three':3
}

sort_dict = {key:val for key,val in sorted(data.items(),key= lambda x : x[1]) }
print(sort_dict)
