# 1) Замыкание, отбирающее только уникальные значения из переданных:

def unique_values(func):
    def wrapper(*args, **kwargs):
        values = func(*args, **kwargs)
        return list(set(values))

    return wrapper

@unique_values
def get_values():
    return a
a=[]
