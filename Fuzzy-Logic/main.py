"""
    This is the main file for Fuzzy Logic based Offloading Decision making.
    Author: Minor Project Group 4(A); 4th Year; B.Tech (CSE)
    Location: PMEC, Berhampur
    Date: 13 January 2022

"""

import numpy as np
import skfuzzy as fuzzy
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Values for the Numpy arange() function
RANGE_START = 0
RANGE_END = 11
RANGE_STEP = 1

# Initializing Antecedents/Inputs
task_size = ctrl.Antecedent(np.arange(RANGE_START, RANGE_END, RANGE_STEP), 'task_size')
net_bandwidth = ctrl.Antecedent(np.arange(RANGE_START, RANGE_END, RANGE_STEP), 'net_bandwidth')
delay = ctrl.Antecedent(np.arange(RANGE_START, RANGE_END, RANGE_STEP), 'delay')

# Initializing Consequent/Outputs
decision = ctrl.Consequent(np.arange(RANGE_START, RANGE_END, RANGE_STEP), 'decision')

# Initializing Membership Functions

# Initializing the Trapezoidal Membership Function for Task Size
task_size['small'] = fuzzy.trapmf(task_size.universe, [0, 0, 2, 4])
task_size['medium'] = fuzzy.trapmf(task_size.universe, [2, 4, 7, 9])
task_size['large'] = fuzzy.trapmf(task_size.universe, [7, 9, 10, 10])

# Initializing the Trapezoidal Membership Function for net_ Bandwidth
net_bandwidth['small'] = fuzzy.trapmf(net_bandwidth.universe, [0, 0, 2, 4])
net_bandwidth['medium'] = fuzzy.trapmf(net_bandwidth.universe, [2, 4, 7, 9])
net_bandwidth['large'] = fuzzy.trapmf(net_bandwidth.universe, [7, 9, 10, 10])

# Initializing the Trapezoidal Membership Function for Delay
delay['small'] = fuzzy.trapmf(delay.universe, [0, 0, 2, 4])
delay['medium'] = fuzzy.trapmf(delay.universe, [2, 4, 7, 9])
delay['large'] = fuzzy.trapmf(delay.universe, [7, 9, 10, 10])

# Initializing the Trapezoidal Membership Function for Decision
decision['local'] = fuzzy.trapmf(decision.universe, [0, 0, 3, 5])
decision['mec'] = fuzzy.trapmf(decision.universe, [3, 5, 10, 10])

# First Rule
rule1 = ctrl.Rule(task_size['small'] & net_bandwidth['small'] & delay['small'], decision['local'])
rule2 = ctrl.Rule(task_size['small'] & net_bandwidth['small'] & delay['medium'], decision['local'])
rule3 = ctrl.Rule(task_size['small'] & net_bandwidth['small'] & delay['large'], decision['local'])

rule4 = ctrl.Rule(task_size['small'] & net_bandwidth['medium'] & delay['small'], decision['local'])
rule5 = ctrl.Rule(task_size['small'] & net_bandwidth['medium'] & delay['medium'], decision['local'])
rule6 = ctrl.Rule(task_size['small'] & net_bandwidth['medium'] & delay['large'], decision['local'])

rule7 = ctrl.Rule(task_size['small'] & net_bandwidth['large'] & delay['small'], decision['local'])
rule8 = ctrl.Rule(task_size['small'] & net_bandwidth['large'] & delay['medium'], decision['local'])
rule9 = ctrl.Rule(task_size['small'] & net_bandwidth['large'] & delay['large'], decision['local'])
# Ending of First rule

# Second Rule
rule10 = ctrl.Rule(task_size['medium'] & net_bandwidth['small'] & delay['small'], decision['local'])
rule11 = ctrl.Rule(task_size['medium'] & net_bandwidth['small'] & delay['medium'], decision['local'])
rule12 = ctrl.Rule(task_size['medium'] & net_bandwidth['small'] & delay['large'], decision['local'])

rule13 = ctrl.Rule(task_size['medium'] & net_bandwidth['medium'] & delay['small'], decision['mec'])
rule14 = ctrl.Rule(task_size['medium'] & net_bandwidth['medium'] & delay['medium'], decision['mec'])
rule15 = ctrl.Rule(task_size['medium'] & net_bandwidth['medium'] & delay['large'], decision['local'])

rule16 = ctrl.Rule(task_size['medium'] & net_bandwidth['large'] & delay['small'], decision['mec'])
rule17 = ctrl.Rule(task_size['medium'] & net_bandwidth['large'] & delay['medium'], decision['mec'])
rule18 = ctrl.Rule(task_size['medium'] & net_bandwidth['large'] & delay['large'], decision['mec'])
# Ending of Second Rule

# Third Rule
rule19 = ctrl.Rule(task_size['large'] & net_bandwidth['small'] & delay['small'], decision['local'])
rule20 = ctrl.Rule(task_size['large'] & net_bandwidth['small'] & delay['medium'], decision['local'])
rule21 = ctrl.Rule(task_size['large'] & net_bandwidth['small'] & delay['large'], decision['local'])

rule22 = ctrl.Rule(task_size['large'] & net_bandwidth['medium'] & delay['small'], decision['mec'])
rule23 = ctrl.Rule(task_size['large'] & net_bandwidth['medium'] & delay['medium'], decision['mec'])
rule24 = ctrl.Rule(task_size['large'] & net_bandwidth['medium'] & delay['large'], decision['local'])

rule25 = ctrl.Rule(task_size['large'] & net_bandwidth['large'] & delay['small'], decision['mec'])
rule26 = ctrl.Rule(task_size['large'] & net_bandwidth['large'] & delay['medium'], decision['mec'])
rule27 = ctrl.Rule(task_size['large'] & net_bandwidth['large'] & delay['large'], decision['mec'])
# Ending of Third Rule

offloading_ctrl = ctrl.ControlSystem(
    [rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
     rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17,
     rule18, rule19, rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27])
offloading = ctrl.ControlSystemSimulation(offloading_ctrl)

# Inputting the value from user
print("-" * 40)
a = float(input("[+] Enter task_size(range between 1 to 10):\t"))
b = float(input("[+] Enter net_bandwidth(range between 1 to 10):\t"))
c = float(input("[+] Enter delay(range between 1 to 10):\t"))
print("-" * 40)

# Assigning the values
offloading.input['task_size'] = a
offloading.input['net_bandwidth'] = b
offloading.input['delay'] = c

# Computing based on Inputs and Rules
offloading.compute()

# Getting the computing value
value = offloading.output['decision']

print(f'\nThe Value of Decision is: {value}')

# Threshold Value for MEC Offloading
THRESHOLD = 4.5

# Making the decision to offload or not
if value >= THRESHOLD:
    print("\n---- Offloading to MEC ----")
else:
    print("\n---- Local Execution ----")

# Plotting the Graphs
task_size.view(sim=offloading)
net_bandwidth.view(sim=offloading)
delay.view(sim=offloading)
decision.view(sim=offloading)

plt.show()
