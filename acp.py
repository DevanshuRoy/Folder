def generate_fibonacci(input):
    i1 = 0
    i2 = 1
    sequence = [i1, i2]

    while input > 2:
        next_num = i1 + i2
        sequence.append(next_num)
        i1 = i2
        i2 = next_num
        input -= 1
    
    return sequence

input = int(input("Enter number of Fibonacci numbers you want to generate: "))

if input <= 0:
    print("Invalid input. Number cannot be 0 or negative")
    
else:
    fibonacci_sequence = generate_fibonacci(input)
    print("The Fibonacci sequence is:", fibonacci_sequence)
