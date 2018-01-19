#
# Program, j1
# Author,  CGG
# Date,    8-NOV-2017
# Last modification, 8-NOV-2017
# Place,   BSC
#

import os
import numpy as np
import math
from random import uniform

# Ivan: numbers of times we randomly go to a random position
Ivan = 20
# upper and lower limits of the domains
lower_limit = -3.0
upper_limit =  3.0
# Number_of_tries: is the total ammount of tries to perform
Number_of_tries = 1000
# Random seed
seed = 1234

# DECLARATIONS
v_results = np.linspace(0,Number_of_tries-1,Number_of_tries) # where the results remains
v_xf      = np.linspace(0,Number_of_tries-1,Number_of_tries) # where the xf used remains
v_yf      = np.linspace(0,Number_of_tries-1,Number_of_tries) # where the yf used remains
# xf: is the weight factor from the stocastic algorithm, initial 1 (float) >>>
xf = 1.0
yf = 1.0
xf_old = 1.0
yf_old = 1.0

######################
# HERE IS THE ALGORITM
# the function is:
# Z = 3.0 * (1-X)*(1-X) * np.exp(-(X*X + (Y+1)*(Y+1))) \
#     - 10.0 * (X/5.0 - (X**3) - (Y**5)) * np.exp(-(X*X + Y*Y)) - 1/3.0 * np.exp(-((X+1)*(X+1) + Y*Y))
# later on we have to look if the new "y" performed with the computed "xf" improves the old "y"
# THIS IS THE CORE OF OUR PROGRAM
# agressive hill-climbing implementation
# MORE EXPLORATIVE THAN EXPLOTATIVE
###################################
print 'Hill-Climbing (1+1) launched ... version 8-NOV-2017'
# specific Ivan seed for randint
np.random.seed(seed)
v_crazy = np.random.randint(0,Ivan,Number_of_tries)
# the uniform for xf when crazy Ivan is already active, xf free to to to anywhere!
np.random.seed(seed)
v_uniform = np.random.uniform(lower_limit,upper_limit,Number_of_tries*2)
# general seed for normal
np.random.seed(seed)
v_tweak_top = Number_of_tries*1000*2
v_tweak =np.random.normal(0, (upper_limit-lower_limit)/8 , v_tweak_top)
v_tweak_count = 0
for super_counter in range(0,Number_of_tries):
# crazy Ivan maneuver from time to time to be more explorative!
    crazy = v_crazy[super_counter]
    if crazy == 0:
#       print 'crazy Ivan maneuver'
        xf = v_uniform[super_counter]
        v_xf[super_counter] = xf # SAVING "xf" to be used
        yf = v_uniform[super_counter]
        v_yf[super_counter] = xf # SAVING "xf" to be used
    else:
########################
# cheching lasts results
########################
        if (super_counter > 1):
            if (v_results[super_counter-2] <= v_results[super_counter-1]):
# FATHER REMAINS AS THE NEW CHILD
#               print (v_results[super_counter-2], '<=', v_results[super_counter-1])
#               print ('father remains as the father')
                xf = xf_old
                v_xf[super_counter] = xf # SAVING "xf" to be used
                yf = yf_old
                v_yf[super_counter] = yf # SAVING "yf" to be used
            else:
# CHILD HAS BECOME THE FATHER
                pass # do nothing
#               print (v_results[super_counter-2], '>', v_results[super_counter-1])
#               print ('new child becomes the father')
# we compute positive and negative increments
# customized variance (sigma) for scoring function selected as: (upper_limit-lower_limit)/8,
# divided by 8 to be more explotative!
        tweak_x = v_tweak[v_tweak_count]
        tweak_y = v_tweak[v_tweak_count+1]
        if (v_tweak_count == v_tweak_top-2):
            v_tweak_count = 0
        else:
            v_tweak_count = v_tweak_count + 2
        while (xf+tweak_x > upper_limit) or (xf+tweak_x < lower_limit) or (yf+tweak_y > upper_limit) or (yf+tweak_y < lower_limit):
            tweak_x = v_tweak[v_tweak_count]
            tweak_y = v_tweak[v_tweak_count+1]
            if (v_tweak_count == v_tweak_top-2):
                v_tweak_count = 0
            else:
                v_tweak_count = v_tweak_count + 2
        xf_old = xf     # save OLD "xf" for future use, if necessary
        xf = xf + tweak_x # we compute the NEW "xf"
        v_xf[super_counter] = xf # SAVING "xf" to be used
        yf_old = yf     # save OLD "yf" for future use, if necessary
        yf = yf + tweak_y # we compute the NEW "yf"
        v_yf[super_counter] = xf # SAVING "yf" to be used
# we put the new xf value in the function and compute the child
        X = xf
        Y = yf
        v_results[super_counter] = 3.0 * (1-X)*(1-X) * np.exp(-(X*X + (Y+1)*(Y+1))) \
        - 10.0 * (X/5.0 - (X**3) - (Y**5)) * np.exp(-(X*X + Y*Y)) - 1/3.0 * np.exp(-((X+1)*(X+1) + Y*Y))

# PROGRAM FINISHED
print 'Hill-Climbing finished !'
# v,i = min([(v,i) for i,v in enumerate(y)])
print 'Minimum "z" value is', min(v_results)

#
#
#
import matplotlib.pyplot as plt
#
ax=plt.gca()
ax.set_ylim([-10,10])
plt.plot(v_results,'ro')
plt.show()
#
# stop clausule: raise ValueError(">>> Paramos aqui.")

