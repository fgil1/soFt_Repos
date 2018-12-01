#python2.7
# -*- coding: utf-8 -*-

"""
Franco Gil

Cubic Spline Interpolation
"""

import numpy as np 								      # __version__ 1.25.0
import matplotlib.pyplot as plt 				# __version__ 2.2.2

def f_x( x, d ):
	return ( 1 / 1 + ( (5*x/d+1)**2 ) )

def cubic_sp( n, x, a):
	"""
	Natural Cubic Spline Interplation Algorithim
	n: size of nodes
	x: source pts to evaluate
	fx: function to interpolate
		fx[1] = a1, ..., fx[n] = an
	From: Numerical Analysis~9th  Algorithim 3.4 pg 150
	"""
	h=np.zeros(n, dtype='float32')
	alp=np.zeros(n, dtype='float32')
	l=np.zeros(n, dtype='float32')
	miu=np.zeros(n, dtype='float32')
	z=np.zeros(n, dtype='float32')
	#
	b=np.zeros(n, dtype='float32')
	c=np.zeros(n, dtype='float32')
	d=np.zeros(n, dtype='float32')
	# step 1
	for i in range(0, n-1):
		h[i]=x[i+1]-x[i]
	# step 2
	for i in range(1, n-1):
		alp[i] = (3/h[i])*(a[i+1]-a[i]) - (3/h[i-1])*(a[i]-a[i-1])
	# step 3
	l[0]=1
	miu[0]=0
	z[0]=0
	# step 4
	for i in range(1, n-1):
		l[i] = 2*(x[i+1]-x[i-1])-(h[i-1]*miu[i-1])
		miu[i] = h[i]/l[i]
		z[i]=(alp[i]-h[i-1]*z[i-1])/l[i]
	# step 5
	l[n-1]=1
	z[n-1]=0
	c[n-1]=0
	# setp 6
	for j in range(n-2, -1, -1):
		c[j] = z[j]-miu[j]*c[j+1]
		b[j] = (a[j+1]-a[j])/h[j] - h[j]*(c[j+1] + 2*c[j])/3 #3.20
		d[j] = (c[j+1] - c[j])/3*h[j]
	# step 7
	return a,b,c,d

def f_2(x, a, b, c, d):
	"""
	x: pt. to interpolate
	a: grade 0 coeficient
	...
	d: grade 3 coeficient

	Out: Evaluate a point x into the Spline interpolation function
	"""
	for i in range(len(b)):
		#if(x >= 0 and x <= 1):
		if(x >= i and x <=i+1 ):	
			t=i
			break
	w=a[i]
	w += b[i]*(x-t)
	w += c[i]*np.power( (x-t), 2 )
	w += d[i]*np.power( (x-t), 3 )
	#print x, i, a[i], b[i], c[i], d[i]
	return  w

if __name__ == '__main__':
	ci, n = 6, [4, 7, 10]
	x=np.arange(-(ci+1), (ci+2))
	fx=f_x(x, ci)							# numpy's ufunc
	for i in range(len(n)):
		#go = 4+1
		#go=7
		go=n[i]
		a,b,c,d = cubic_sp(go, x, fx)
		m=len(b)
		print 'ID#: ', ci, ' ', 'node#: ', go, '\n'
		print 'Coefficient to interpolate.\n'
		print '{:>1} {:>2} {:>4} {:>16} {:>17}'.format('pol.', 'a', 'b', 'c', 'd')	
		for i in range(m):
			print '{:>1} {:>6} {:>16} {:>16} {:>17}'.format(i, a[i],b[i],c[i],d[i])
		w=[]
		for i in range(go):
			w.append( f_2(i,a,b,c,d) )
		diff=fx[:go]-w
		"""
		print '\npts. x\n\n', x 
		print '\nf(x)\n\n', fx
		print '\nf(x)-P(x)\n\n', diff
		"""

		print '\n\nInformation about points\n'
		print '{:>} {:>5} {:>15}'.format('f(x)', 'P(x)', 'f(x)-P(x)')	
		for i in range(m):
			print '{:>2} {:>3} {:>13}'.format(fx[i],w[i],diff[i])

		print '\nEND \n\n'
		plt.style.use('seaborn-whitegrid')
		fig, ax = plt.subplots() 				
		ax = plt.axes()
		ax.plot(x[:go], fx[:go], color='c', marker='o', label='Original')
		ax.plot(x[:go], w, '--', color='r', marker='o', label='Spline')
		ax.plot(x[:go], diff, color = 'b', marker='o', label='f_x - P_x')
		plt.title("Interpolation by Cubic Spline method.")
		plt.legend()
		fig.savefig('CubicSpline.png', dpi=150)			
