

def unique_values(func):
    def wrapper(*args, **kwargs):
        values = func(*args, **kwargs)
        return list(set(values))

    return wrapper

@unique_values
def get_values():
    return a
a=[]

b = int (input ("Введите размер массива:"))
for i in range (b):
    a.append (int (input ()))

print(get_values())
