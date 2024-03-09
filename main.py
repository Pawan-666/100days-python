import random
import new_module         # custom module

random_int_no = random.randint(1,10)      # random int
random_float_no = random.random()        # random float between 0,1
random_float_no1 = random.uniform(2.5,9)
print(random_int_no)
print(random_float_no)
print(random_float_no1)

print(new_module.pi)
