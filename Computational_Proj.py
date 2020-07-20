"""Anthony Dupont
   Katie
   Nicholas Kong
   Jessica
   7/20/2020
   PHYS 2331"""
import math

# TODO clean up these horrible variable names and argument names, disgusting

# These are pretty much going to be globals
x_input = float(input("Type in the x value"))
y_input = float(input("Type in the y value"))
charge = float(input("Type in the q value"))
length = float(input("Type in the length value"))
k_const = 9.0 * (10 ** 9)   # 9.0x10^9

def compute_r_distance():
    """In this function, we will calculate the value of r, that will be constantly changing due to delta y
    delta y is a variable that will be traveling throughout the entirety of length of the object
    for example if the length is 10, we will gradually go up through it by starting at 0.1, then 0.2...
    etc all the way up to 10. This will give us many values for r throughout the entire length
    we will return a list full of these values"""
    index = 0.1
    delta_y = []
    r_values = []
    while index < length:
        delta_y.append(round(index, 1))
        index += 0.1

    # ---CAUTION--- currently this loop will break if the user inputs a Y value that is bigger than X
    for y in delta_y:
        r_values.append(math.sqrt((x_input ** 2) - (y_input - y) ** 2))     # ** is the syntax for squaring in python
    # the very last value of this list is going to be 0 because Ymax - Ymax is just 0
    r_values.pop()
    return r_values, delta_y

def compute_v_values(r_value_list, delta_y_value_list):
    """In this function we will receive a list full of r values, we will iterate over this entire list to plug
    into the equation to solve for V, this will give us an entire list of V values that we will return"""
    v_values = []
    q_values = []
    v = 0.0
    # solve for all delta q's
    for i in range(len(delta_y_value_list)-1):  # we -1 because r_value_list is 1 less total length compared to delta y
        q_values.append(charge/(2*length) * delta_y_value_list[i])   # y is delta y
        # now solve for delta V
        v += k_const*q_values[i]/r_value_list[i]
        v_values.append(v)  # Thanks to some big brain thinking, we can do all of
        # this computation in a single loop iterating through two different arrays only once for O(n) computation
    return v_values, q_values, v

def compute_electric_field(delta_v_value_list ,delta_y_value_list):
    """In this function, we will compute the electric field in both the x and y direction, display both
    and then display the total electric field as well"""
    # Keep in mind for this project, our x value is 0 and we're only moving in the y direction...
    e_field = 0.0
    e_y_field = 0.0
    for i in range(len(delta_v_value_list)):
        e_y_field += -(delta_v_value_list[i]/delta_y_value_list[i])
    print("The electric field in the x direction is 0 since we are not moving in the x direction")
    print("The total electric field and also in the y direction is: ")
    print(e_y_field)

# ---------------------------------------MAIN GOES BELOW--------------------------------------------------------------

list = compute_r_distance()
r_list = list[0]
delta_y_list = list[1]
# we have all values for r, time to solve for all V's
list = compute_v_values(r_list, delta_y_list)
v_list = list[0]
q_charge_list = list[1]
v_value = list[2]
print("Here is the electric potential: ")
print(v_value)
compute_electric_field(v_list, delta_y_list)