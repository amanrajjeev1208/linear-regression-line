import matplotlib.pyplot as plt
import sys
import numpy as np

#***************************************************************************
#**********************GENERAL PURPOSE FUNCTIONS****************************
#***************************************************************************

def get_cords(datapoints):
	x_cord = []
	y_cord = []
	for item in datapoints:
		x_cord.append(item[0])
		y_cord.append(item[1])
	return x_cord, y_cord

def calc_mean(datapoints):
	x_mean = y_mean = 0
	for item in datapoints:
		x_mean += item[0]
		y_mean += item[1]
	x_mean = x_mean / 6
	y_mean = y_mean / 6
	return x_mean, y_mean

def gen_calc_1(datapoints, x_mean, y_mean):
	sx_sqr = sy_sqr = sxy = 0
	for item in datapoints:
		temp =  item[0] - x_mean
		temp1 = item[1] - y_mean
		sx_sqr += temp * temp
		sy_sqr += temp1 * temp1
		sxy += temp * temp1
	sx_sqr = sx_sqr / 6
	sy_sqr = sy_sqr / 6
	sxy = sxy / 6
	return sx_sqr, sy_sqr, sxy

def gen_calc_2(x_mean, y_mean, sx_sqr, sy_sqr, sxy):
	b = sxy / sx_sqr
	a = y_mean - (b * x_mean)
	r = sxy / ((sx_sqr ** 0.5) * (sy_sqr ** 0.5))
	r_sqr = r * r
	E = 6 * sy_sqr * (1 - r_sqr)
	return a, b, r, r_sqr, E

def gen_calc_3(datapoints, a, b):
	y_hat = []
	e = []
	sum_e = sum_e_sqr = 0
	for item in datapoints:
		y_hat.append(a + (b * item[0]))
	#Printing y_hat
	for i in range(0, len(y_hat)):
		print("y" + str(i + 1) + "_hat = ", y_hat[i])
		e.append(-1 * (y_hat[i] - datapoints[i][1]))
	print()
	#printing e and calculating sum_e and sum_e_sqr
	for i in range(0, len(e)):
		print("e" + str(i + 1) + " = ", e[i])
		sum_e += e[i]
		sum_e_sqr += e[i] * e[i]
	print()
	print("sum_e = ", sum_e)
	print("sum_e_sqr = ", sum_e_sqr)
	print()
	return y_hat, e, sum_e, sum_e_sqr

def check_e(sum_e_sqr, E):
	sum_e_sqr = round(sum_e_sqr, 5)
	E = round(E, 5)
	if (sum_e_sqr - E) == 0:
		print("The summation of all the values of e is 0")
		print()
	else:
		print("The summation of all the values of e is not 0")
		sys.exit(0)

def plot_graph(x_cord, y_cord, reg_line, a, b):
	plt.scatter(x_cord, y_cord, color= "green", marker= ".", s=30)
	plt.xlabel('x - axis')
	plt.ylabel('y - axis')
	plt.title('Regression Line Graph')
	x = np.linspace(0, 20, 100)
	y = a + (b * x)
	plt.plot(x, y)
	plt.show()

def print_result(x_cord, y_cord, x_mean, y_mean, sx_sqr, sy_sqr, sxy, a, b, r, r_sqr, E):
	print()
	print("x_cord = ", x_cord)
	print("y_cord = ", y_cord)
	print("x_mean = ", x_mean)
	print("y_mean = ", y_mean)
	print("sx_sqr = ", sx_sqr)
	print("sy_sqr = ", sy_sqr)
	print("sxy = ", sxy)
	print("a = ", a)
	print("b = ", b)
	print("r = ", r)
	print("r_sqr = ", r_sqr)
	print("E = ", E)
	print()

#***************************************************************************
#****************************THE MAIN FUNCTION******************************
#***************************************************************************

def main():
	
	#Given Datapoints
	datapoints = [(2, 2),(4, 6),(5, 4),(7, 8),(8, 10),(10, 12)]

	#get the X and Y cordinates
	x_cord, y_cord = get_cords(datapoints)

	#Calculating the mean of X and Y co-ordinates
	x_mean, y_mean = calc_mean(datapoints)

	#Calculating the Sx^2, Sy^2, Sxy
	sx_sqr, sy_sqr, sxy = gen_calc_1(datapoints, x_mean, y_mean)

	#Calculating a, b, r, r^2 and E
	a, b, r, r_sqr, E = gen_calc_2(x_mean, y_mean, sx_sqr, sy_sqr, sxy)

	#Printing the result values obtained till now
	print_result(x_cord, y_cord, x_mean, y_mean, sx_sqr, sy_sqr, sxy, a, b, r, r_sqr, E)

	#Equation of regression line
	reg_line = "y = " + str(a) + " + " + str(b) + "x"
	print("Equation of regression line: ", reg_line)
	print()

	#Calculating the y_hat for each x and storing in a list, calculating e, sum_e and sum_e_sqr
	y_hat, e, sum_e, sum_e_sqr = gen_calc_3(datapoints, a, b)

	#check if sum of all values of e is 0 or not
	check_e(sum_e_sqr, E)

	option = input("Do you want to see the graph of the datapoints and the regression line? Reply with the Y or N.")
	if option == 'Y':
		plot_graph(x_cord, y_cord, reg_line, a, b)
	else:
		sys.exit(0)


#***************************************************************************
#****************************DRIVER CODE************************************
#***************************************************************************

if __name__ == '__main__':
	main()  # calling main function

