import matplotlib.pyplot as plt

"""
THIS FILE IS USED TO DRAW THE BIFURCATION DIAGRAMS OF EACH METHOD
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
		
	return p_vals

def distinct(l1):
	already_seen = []
	output = []
	for x in l1:
		if x not in already_seen:
			output.append(x)
	return output

h_step = 0.0005
x_lower = 0.15
x_upper = 0.5
dx = x_upper - x_lower
x_count = int(dx//h_step)
x_axis = [x_lower+x*h_step for x in range(x_count)]
vals = [distinct(runge_kutta(400, h)[-40:]) for h in x_axis]

for te, pe in zip(x_axis, vals):
	plt.scatter([te]*len(pe), pe, s=1, c='#4286f4')

plt.xlabel('h')
plt.ylabel('approximate solution')
plt.show()