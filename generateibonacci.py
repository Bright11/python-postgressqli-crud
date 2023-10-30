def generate(n):
    fibonacci = []
    a, b = 0, 1
    for _ in range(n):
        fibonacci.append(a)
        a, b = b, a + b

    print("printting gerated number:")
    for number in fibonacci:
        print(number, end=" ")

# Example of  usage:
number_of_terms = 10  # generated numbers
generate(number_of_terms)
