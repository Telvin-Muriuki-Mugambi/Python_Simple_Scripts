def fibonacci_sequence(n):

    if n <= 0:
        return []

    sequence = []
    a, b = 0, 1

    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b



    print(sequence)


    return sequence



fibonacci_sequence(10)


