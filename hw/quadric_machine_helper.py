def quadric_helper(x, y):
    print(f'(x, y) is: ({x}, {y})')
    print(f'xy is: {round(x*y,2)}')
    print(f'xx is: {round(x*x,2)}')
    print(f'yy is: {round(y*y,2)}')
    print('-----')

quadric_helper(0,.4)
quadric_helper(-.1,1.2)
quadric_helper(.5,.8)
