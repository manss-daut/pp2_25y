def solve(nheads, nlegs):
    chickenheads = nheads
    rabbitheads  = 0
    while chickenheads >= 0 :
        calc = (chickenheads * 2) + (rabbitheads * 4)
        if calc == nlegs and chickenheads + rabbitheads == nheads:
            return chickenheads, rabbitheads
        else:
            chickenheads -= 1
            rabbitheads += 1
result = solve(35, 94)
print("Chicken and Rabbits amount: ")
print(result)