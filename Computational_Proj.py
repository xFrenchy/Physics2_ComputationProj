"""Anthony Dupont
   Kulprawee Prayoonsuk
   Nicholas Kong
   Jessica Hernandez-Fernandez
   Erik Fong
   7/20/2020
   PHYS 2331"""
import math
import matplotlib.pyplot as plt

# TODO clean up these horrible variable names and argument names, disgusting
# TODO add units when we display results

# These are pretty much going to be globals
x_input = float(input("Type in the x value: "))
y_input = float(input("Type in the y value: "))
charge_input = float(input("Type in the q value: "))
length = float(input("Type in the length value: "))
k_const = 9.0 * (10 ** 9)   # 9.0x10^9


def compute_r_distance():
    """In this function, we will calculate the value of r, that will be constantly changing due to delta y
    delta y is a variable that will be traveling throughout the entirety of length of the object
    for example if the length is 10, we will gradually go up through it by starting at 0.1, then 0.2...
    etc all the way up to 10. This will give us many values for r throughout the entire length
    we will return a list full of these values"""
    y_prime = 0.1
    delta_y = []
    r_values = []
    while y_prime < length:
        delta_y.append(round(y_input - y_prime, 1))     # Rounding to avoid float number issues such as 2.000000000001
        y_prime += 0.1

    # Following the equation the professor gave us but it doesn't make sense that it's x-y instead of x+y
    for y in delta_y:
        r_values.append(math.sqrt((x_input**2) + (y**2)))     # ** is the syntax for squaring in python
    return r_values, delta_y


def compute_v_values(r_value_list, delta_y_value_list):
    """In this function we will receive a list full of r values, we will iterate over this entire list to plug
    into the equation to solve for V, this will give us an entire list of V values that we will return
    we will also print the value of V at the end"""
    v_values = []
    q_values = []
    v = 0.0
    # solve for all delta q's
    for i in range(len(delta_y_value_list)):
        q_values.append(charge_input / length * delta_y_value_list[i])
        # now solve for delta V
        v += k_const*q_values[i]/r_value_list[i]
        v_values.append(v)  # Thanks to some big brain thinking, we can do all of
        # this computation in a single loop iterating through two different arrays only once for O(n) computation
    print("\nHere is the electric potential: " + str(v) + " V")
    return v_values, q_values, v


def compute_electric_field(delta_v_value_list ,delta_y_value_list):
    """In this function, we will compute the electric field in both the x and y direction, display both
    and then display the total electric field as well"""
    # Keep in mind for this project, our x value is constant and we're only moving in the y direction...
    e_x_field = 0.0
    e_y_field = 0.0
    for i in range(len(delta_v_value_list)):
        try:
            e_x_field += -(delta_v_value_list[i]/x_input)
            e_y_field += -(delta_v_value_list[i]/delta_y_value_list[i])
        except ZeroDivisionError:
            pass
    print("\nThe electric field in the x direction: " + str(e_x_field) + " V/m")
    print("The electric field in the y direction: " + str(e_y_field)+ " V/m")
    e_field = e_x_field + e_y_field
    print("The total electric field is: " + str(e_field) + " V/m")

# ---------------------------------------MAIN GOES BELOW--------------------------------------------------------------


list1 = compute_r_distance()
r_list = list1[0]
delta_y_list = list1[1]
# we have all values for r, time to solve for all V's
list2 = compute_v_values(r_list, delta_y_list)
v_list = list2[0]
q_charge_list = list2[1]
v_value = list2[2]
compute_electric_field(v_list, delta_y_list)
# plotting the delta v values that was calculated
plt.plot(v_list)
plt.ylabel("V(m)")
plt.title("V(x,y)=" + str(x_input) + "," + str(y_input))
plt.show()