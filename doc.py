def expo(num=2,pow=2):
    """
    this function returns exponential value.
    num defaults to 2 and pow defaults to 2
    """
    return num ** pow


print(expo(2,3))
print(expo(3))
print(expo(4))
print(expo())

print(expo(pow=5,num=10))

print(expo.__doc__)
