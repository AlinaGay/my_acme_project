import random
for v in ['!'] + [' '.join(random.choice(['*', '*', '^', '^', '@', '+']) * i) for i in range(1, 20, 1)] \
                                          + ['|', '|', '[___]']:
    print('{:~^37}'.format(v))  