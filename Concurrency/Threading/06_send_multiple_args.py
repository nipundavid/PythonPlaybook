import concurrent.futures


def multiply_and_add(a, b):
    return a + 2 * b


def multiply_and_add_wrapper(p):
    return multiply_and_add(*p)


if __name__ == "__main__":
    a_list = list(range(0, 20, 1))
    some_b = 2
    args = ((some_a, some_b) for some_a in a_list)

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(multiply_and_add_wrapper, args)

    print(list(results))