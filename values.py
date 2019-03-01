"""
THIS FILE IS USED TO GENERATE A LATEX-FORMATTED TABLE OF VALUES FROM EULERS METHOD
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

col1 = eulers(41, .18)
col2 = eulers(41, .23)
col3 = eulers(41, .25)
col4 = eulers(41, .30)

latex_table_string = ''

for i in range(len(col1)):
	latex_table_string += str(i) + ' & '
	latex_table_string += str(round(col1[i],3)) + ' & '
	latex_table_string += str(round(col2[i],3)) + ' & '
	latex_table_string += str(round(col3[i],3)) + ' & '
	latex_table_string += str(round(col4[i],3)) + ' \\\\\n'

print(latex_table_string)