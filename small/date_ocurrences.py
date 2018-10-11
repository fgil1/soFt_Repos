# -*- coding: utf-8 -*-
# Developer  : Franco Gil, from an uthopic latin country  :)
# Created Date: September 16 2018
# =============================================================================
# - > DATA in  : https://drive.google.com/open?id=1AAGyy8gml2Gpi6oYI0eGPZlpwMK9jyff
# Description : Using a csv file (full of dates, explaining the submited date of 
# a arvix publication ). To plot the ocurrences in a current date.
# - > DATA out : local
# v.01 lenght of data collected, < 500
# =============================================================================


from collections import Counter
from numpy import * # 1.15.0
import matplotlib.pyplot as plt # 2.2.2
import pandas as pd # 0.23.4
import time
from PIL import Image
from datetime import datetime #  'datetime'
import csv
import sys

def no_blank(w):
	"""
	Delete ' ' at left
	"""
	j=0; back=[]
	while(j < len(w) and w[j].isdigit()==False):
		j+=1
	back=w[j:]
	return back

def filter1():
	"""
	Cleaning the .csv
	"""
	l2=[];	l1=[]; exam=[]; dels=[]
	l2=pd.read_csv('dates.csv', lineterminator='\n', sep='\n', index_col=0)
	# l2 -> <class 'pandas.core.frame.DataFrame'>
	# if not exis an identificartor on the column, index the data like this
	# l2.index.values[0] -> str
	l1=l2.index.values # numpy.ndarray
	#print 'len l1 antes:', len(l1)
	for i in range(len(l1)):
		x=l1[i]
		if len(x) > 28: # 29: 2 dates, 44: 3 dates in one line
			exam.append(x)
			dels.append(i)
			#np.delete(l1, i)
	l1=np.delete(l1, dels)
	#print 'len l1 dsps:', len(l1)
	#print '\n '.join(exam) # muy util
	for k in range(2):
	# ugly cycle to 'clean' data
		for i in range(len(exam)):
			exam[i]=no_blank(exam[i])
			while(len(exam[i])>28):
				get=exam[i].find(';')+1
				a=exam[i][get:]
				exam[i]=exam[i][:get]
				exam.append(a)
	l1=np.append(l1, exam)
	#print 'len l1 normalized: ', len(l1) 
	for i in range(len(l1)):
		l1[i]=no_blank(l1[i])
	#print '\n '.join(l1)
	# next step convert this into an datetime array
	return l1

def to_date(D):
	"""
	Modify the datetime
	in: nn Month, yyyy
	out: datetime(yyy, mm, dd) -> int's
	"""
	if D[1].isspace()==True: # One digiy days.
		d=D[:1]; m=D[2:5]
	else:
		d=D[:2]; m=D[3:6]
	# Years
	k=-1
	while(D[k]!=';'):
		k-=1
	y=D[k-4:k]
	# print d, m, y
	# Mising the breaks like C/C++ :'|
	if(m=='Jan'):
		return datetime(int(y), 1, int(d))

	elif(m=='Feb'):
		return datetime(int(y), 2, int(d))

	elif(m=='Mar'):
		return datetime(int(y), 3, int(d))

	elif(m=='Apr'):
		return datetime(int(y), 4, int(d))

	elif(m=='May'):
		return datetime(int(y), 5, int(d))

	elif(m=='Jun'):
		return datetime(int(y), 6, int(d))

	elif(m=='Jul'):
		return datetime(int(y), 7, int(d))

	elif(m=='Aug'):
		return datetime(int(y), 8, int(d))

	elif(m=='Sep'):
		return datetime(int(y), 9, int(d))

	elif(m=='Oct'):
		return datetime(int(y), 10, int(d))

	elif(m=='Nov'):
		return datetime(int(y), 11, int(d))

	elif(m=='Dec'):
		return datetime(int(y), 12, int(d))

if __name__ == '__main__':	
	"""
	Enter point.
	"""
	D=filter1();
	D2=[]
	for i in range(len(D)):
		D2.append(to_date(D[i]))
	print 'elements procesed', i+1
	D2=sorted(D2)
	D2=Counter(D2)
	v=D2.values()
	k=D2.keys()
	# plotting resul
	ts=pd.Series(v, index=k)
	tl=plt.title('Occurrences of (Data) in 200 titles on CS arxiv submited between JUL-SEP')
	# open the image result in amutomate way
	img=ts.plot(); fig=img.get_figure().savefig('ocurrences.png', dpi=500)
	f=Image.open('ocurrences.png').show()

