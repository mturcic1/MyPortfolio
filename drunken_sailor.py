import random
step_num = int(input("Enter number of steps: "))
grid_size = int(input("Enter the size: "))
sailor_num = int(input("Enter number of sailors: "))
iteration = 0
fall_condition = [grid_size//2, grid_size//2]
fallen_sailors = 0
def walking(step_num):
    x = 0
    y = 0
    for i in range(step_num):
        step = random.choice([1, 2, 3, 4])
        if step == 1:
            y = y-1
        elif step == 2:
                y = y+1
        elif step == 3:
            x = x+1
        elif step == 4:
            x = x-1
    return [x,y]


while iteration < sailor_num:
    if walking(step_num) > fall_condition:
        fallen_sailors += 1

    iteration +=1

percentage = round(fallen_sailors/sailor_num*100)
print("Out of "+str(sailor_num)+" drunk sailors, "+str(fallen_sailors)+"("+str(percentage)+"%) fell into the water.")