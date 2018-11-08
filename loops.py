my_list = [5, 6, 7, 8]

for whatevs in my_list:
    print('whatevs', whatevs)

for idx, whatevs in enumerate(my_list):
    print('idx', idx)
    print('whatevs', whatevs)

for idx in range(4):
    print(idx)

for idx in range(len(my_list)):
    print(idx)

num = 0
while num < 10:
    print(num)
    num += 1