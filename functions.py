def my_function(a):
    if a < 0:
        return "Cannot do this on a negative number."
    x = a + 5
    y = a - 5
    return x, y


first_answer, second_answer = my_function(2)

print(first_answer)
print(second_answer)

print(x)
print(x[0])
print(x[1])