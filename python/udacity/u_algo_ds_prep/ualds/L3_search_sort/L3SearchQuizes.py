
def factorial_recursive(n):
    if  n <= 1:
        return 1  #base case  with defined exit (danger: infinite recursion)
    else:
        return n*(factorial_recursive(n-1))


def get_fib(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return get_fib(n-1) + get_fib(n-2)

def test_factorial_recursive():
    print("factorial 4:", factorial_recursive(4))

def test_fibonnaci():
    for i in range(8):
        print("fib {0}: {1}".format(i, get_fib(i)))




def main():
    #test_factorial_recursive()
    test_fibonnaci()

if __name__ == '__main__':
        main()



