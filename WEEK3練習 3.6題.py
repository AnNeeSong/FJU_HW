
"""0502訓詁學課堂實作3-6
"""6. 印星星(三):

def print_star():
    n = 5 
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))
    for i in range(n - 2, -1, -1):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))

print_star()
