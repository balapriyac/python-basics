def get_cubes(num):
    cubes = []
    for i in range(num):
        cubes.append(i**3)
    return cubes

def get_cubes(num):
    cubes = [i**3 for i in range(num)]
    return cubes

# get_cubes() function can be rewritten as a generator function get_cubes_gen()
def get_cubes_gen(num):
    for i in range(num):
        yield i**3

cubes_gen = get_cubes_gen(6)
print(cubes_gen)

# >>> from gen_example import get_cubes_gen
# >>> cubes_gen = get_cubes_gen(6)
# >>> next(cubes_gen)
# 0
# >>> next(cubes_gen)
# 1
# >>> next(cubes_gen)
# 8
# >>> next(cubes_gen)
# 27
# >>> next(cubes_gen)
# 64
# >>> next(cubes_gen)
# 125
