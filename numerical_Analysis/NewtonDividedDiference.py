#python2.7
# -*- coding: utf-8 -*-

"""
Franco Gil

Interpolation exercise
"""

import numpy as np 								      # __version__ 1.15.0
import matplotlib.pyplot as plt 				# __version__ 2.2.2

def f_x( x, d ):
	return ( 1 / 1 + ( (5*x/d+1)**2 ) )

def N_d_d_a(n, x=None, fx=None):
	"""
	Newtons's Divided-Difference algorithim 3.2
	Numerial Analysis Burden-Faires 9th Ed. ~ pag. 126 
	"""
	F=np.zeros( (n,n), dtype='float32' )
	for i in range(n):
		F[i][0] = fx[i]					#filling 1st row with fx( xn )
	for i in range(n):
		for j in range(i, n-1):
			if j >= i and j < n-1:
				"""
				modified
				"""
				F[j+1][i+1] = (F[j+1][i] - F[j][i]) / (x[j+1]-x[j-i])
				#print (j+1,i), '-', (j,i) , '/' , (j+1), '-', (j-i)
	return F

def f2( v, r, pt, n): 
	"""
	Building interpolation polonomial (function 2)
	Input order:
		diag., x_n, point, P_n degree
	"""
	out=v[0]
	ac=1
	for i in range(n-1):
		#print  v[i+1], '*',r[i], '+', pt,  '\n'
		#print ac, '*', v[i+1]
		ac*=(pt-r[i])
		out+=ac*v[i+1]
	return out

if __name__ == '__main__':
	d, size = 6, [4, 7, 10]						      # id, nodes lenght
	for node in range(len(size)):						# temporary hack
		n=size[node] 							            # test
		x=np.arange(-(d+1), (d+2) )
		x=x[0:n]								              # modified length
		y=f_x(x, d)  							            # numpy's ufunc over arrays
		#y = map(lambda x: ( 1 / 1 + ( (5*x/d+1)**2 ) ), x)
		z=N_d_d_a(n, x, y)
		diag=z.diagonal()						          # coefficients for Newton
		zn=[]
		for i in range(n):
			w=f2(diag, x, x[i], n) 				      # diag., x_n, point, P_n degree
			zn.append(w)
		diff=[]
		for i in range(n):
			diff.append( y[i]-zn[i] )
		print 'ID#: ', d, ' node#: ', n, '\n'
		print 'Matrix\n', z 				          # matrix
		c=y[:n]
		"""
		print '\n f(x)\n\n', y[0:n]
		print '\n P(x)\n\n', zn	#interpolating points
		print '\n f(x)-P(x)\n\n', diff	
		"""
		print '\nInformation about points\n'
		print '{:>1} {:>5} {:>15}'.format('f(x)', 'P(x)', 'f(x)-P(x)')	
		for i in range(n):
			print '{:>2} {:>3} {:>13}'.format(c[i], zn[i],diff[i])		
		print '\nEND\n\n'
		plt.style.use('seaborn-whitegrid')
		fig, ax = plt.subplots() 				        # pag 90 matplotlib doc
		ax = plt.axes()
		ax.plot(x, y, color='c', marker='o', label='Original')
		ax.plot(x, zn, '--', color='r', marker='o', label='Interpolation')
		ax.plot(x, diff, color = 'b', marker='o', label='f_x - P_x')
		plt.title("Interpolation by Newton's Divided-Difference method.")
		plt.legend()
		#plt.show()
		cad='HomeWork.1.ci.'+str(d)+'.node.'+str(n)
		fig.savefig(cad+'.png', dpi=150)			  # dpi=1080
