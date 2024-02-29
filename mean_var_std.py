import numpy

# Read the dimensions of the array
N, M = map(int, input().split())

# Read the elements of the array
my_array = numpy.array([input().split() for _ in range(N)], int)

print(numpy.mean(my_array, axis = 1))
print(numpy.var(my_array, axis = 0))
print(numpy.std(my_array, axis = None))