def array_map(array, func):
    for key,value in enumerate(array):
        array[key] = func(value)
    return array


def array_for(array, func):
    for key,value in enumerate(array):
        func(value,key)

def my_print(*value):
    print(value)

array = ['ll','adsj','asdehfjbe']

array_map(array,len)

key,value = ('name', 'lizhicheng')
print(key,value)
