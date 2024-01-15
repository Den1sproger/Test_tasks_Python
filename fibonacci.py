

def find_sum(top: int) -> int:
    sequence = [3, 4]      # starting with 3 and 4
    next_element = sum(sequence[-2:])
    even_values_sum = sum([i for i in sequence if i % 2 == 0])   # start sum

    while next_element <= top:
        if next_element % 2 == 0:
            even_values_sum += next_element
    
        sequence.append(next_element)
        next_element = sum(sequence[-2:])

    return even_values_sum



if __name__ == '__main__':
    print(find_sum(7_000_000))