def vasya(func):

    def wrapper():
        print('Vasya!')
        func()

    return wrapper


def print_hello():
    print('Hello!')

print_hello = vasya(print_hello)

if __name__ == '__main__':
    print_hello()