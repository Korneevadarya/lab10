def calculate_a_recursive(i):
    if i == 0 or i == 1:
        return 1
    else:
        return calculate_a_recursive(i-2) + (calculate_a_recursive(i-1)/(2**(i-1)))
