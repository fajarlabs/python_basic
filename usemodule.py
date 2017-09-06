''' cara 1 '''
'''
import mymodule

def main() :
	a = mymodule.A()
	b = mymodule.B()
	c = mymodule.C()

	a.metode()
	b.metode()
	c.metode()

if __name__ == "__main__" :
	main()
'''

''' cara 2 '''
'''
from mymodule import A,B,C,myvar,myfunc

def main() :
	a = A()
	b = B()
	c = C()

	a.metode()
	b.metode()
	c.metode()
	print myvar  #variable
	print myfunc() #function

if __name__ == "__main__" :
	main()
'''

''' cara 3 '''
''' memecah kedalam folder module '''

# cara 1
from module_terpisah import *

# cara 2 
'''
import os
os.chdir('D:\\fajarlabs\\kerjaan_luar\\PYTHON_SAMPLES')
from module_terpisah import *
'''

def main() :
	print var1
	print var2

	f1()
	f2()

	a = C1()
	b = C2()

	a.m()
	b.m()

if __name__ == '__main__' :
	main()

	