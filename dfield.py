import matplotlib.pyplot as plt
import numpy as np
import math

"""
THIS FILE IS USED TO DRAW THE DIRECTION FIELD OF THE DIFF EQ AND APPROXIMATION METHOD STEPS ALONG IT
"""

def eulers(n, h, p0=0.1):
	t_vals = [0]
	p_vals = [p0]

	for i in range(n-1):
		t_n = t_vals[-1]
		p_n = p_vals[-1]

		t_vals.append(t_n + h)
		p_vals.append((1+10*h)*p_n - 10*h*p_n**2)
	return p_vals

def runge_kutta(n, h, p_0=0.1):

	f = lambda p: 10*p*(1-p)

	p_vals = [p_0]

	for i in range(n-1):
		p_n = p_vals[-1]
		k1 = h*f(p_n)
		k2 = h*f(p_n + k1/2)
		k3 = h*f(p_n + k2/2)
		k4 = h*f(p_n + k3)

		p_vals.append(p_n + (1/6)*(k1 + k2/2 + k3/2 + k4))
	print(p_vals)
	return p_vals


#h_vals=[0.18, 0.23, 0.25, 0.3]
h_vals = [0.27]
init_vals = [0.1]

dp_dt_str = "10*p*(1-p)"

plane_step = 0.05
arr_len = 0.2

X = np.arange(0, 4.5, plane_step)
Y = np.arange(-0.2, 1.4, plane_step)

V = np.concatenate([np.vstack(10*Y*(1-Y)) for i in range(len(X))], axis=1)
U = np.ones((len(V),len(V[0])))

plt.quiver(X,Y,U,V)


for h in h_vals:
	for init_val in init_vals:
		hx = np.arange(0, 4.5, h)
		hy = np.array(runge_kutta(len(hx), h, init_val))

		plt.plot(hx,hy)

plt.xlabel('t')
plt.ylabel('p')

axes = plt.gca()
axes.set_xlim([0,4])

plt.show()