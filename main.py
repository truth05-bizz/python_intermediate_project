def fun(x=0):
    return x**2

call = fun(6)
print(call)

y = lambda a : a * 5
print(y(5))

x = lambda a, b, c : a + b * (c + 5)
print(x(5, 5, 2))


def myfun(n):
    return lambda y=1 : y * n

mydoubler = myfun(2)
print(mydoubler)
print(mydoubler(5))
print(myfun(5)())
print(myfun(10)(2))


def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for i in range(1):
        for key, value in kwargs.items():
            print(f"{key}: {value}")


shipping_label("Mr",".","Truth", "Mosh",
                street = "123 Fake St.",
                apt = "100",
                city = "Lekki",
                state = "Lagos",
                zip = "54321",
                POB = "1101")


my_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def square(x):
    return x**2

squares = list(map(square, my_number))
print(squares)
    

print(list(map(lambda x: x**2, my_number)))

def even(y):
    return y % 2 == 0

even_numbers = list(filter(even, my_number))
print(even_numbers)


student_data = [("Truth", 96.4), ("John", 55.2), ("Emma", 55.7), ("Matthew", 67.7)]
sorted_data = list(sorted(student_data, key=lambda x: x[1]))
print(sorted_data)



name, *score = input() .strip()
print(name)
print(score)