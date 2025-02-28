total_row = 10
star_repeat = 1
space = ' '
move = 1
sign = '♈'
for i in range(1, total_row + 1):
    print(space * (total_row - move) + sign * star_repeat)
    star_repeat += 2
    move += 1
