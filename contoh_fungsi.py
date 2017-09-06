# tanpa nilai balik
def kali(a,b) :
	print "Hasilnya adalah %d" % (a*b)

# contoh dengan nilai balik
def kali2(a,b) :
	return a * b

print kali2(5,5)

''' cara mengakses global var '''
def testGlobal() :
	global varglobal #gunakan keyword global
	varglobal = "text global"

testGlobal()
print varglobal

''' membuat fungsi dengan parameter default '''
def testDefParameter(a,b,c='Hello'):
	print c

testDefParameter(None,None,"Test")	

''' membuat fungsi yg dapat dipanggil dengan parameter berbeda '''
def testMultiParameter(*args) :
	for i in args :
		print str(i)

testMultiParameter("hello", 4, "KT-0001")






''' fungsi yang dapat dipanggil dengan keyword argument '''
''' menggunakan dua asterisk / bintang '''
def testKeywordArgs(**kwargs) :
	try :
		a = kwargs['a']
		print "a didefinisikan"
	except KeyError :
		print "a tidak didefinisikan"

	try :
		b = kwargs['b']
	except KeyError :
		print "b tidak didefinisikan"

testKeywordArgs(a='Hello')








''' membuat fungsi untuk merubah variabel kedalam bentuk string '''
def namavar(obj, namespace) :
	temp = [k for k in namespace if namespace[k] is obj]
	if len(temp) > 0 :
		return temp[0]
'''
    globals() always returns the dictionary of the module namespace
    locals() always returns a dictionary of the current namespace
    vars() returns either a dictionary of the current namespace (if called with no argument) or the dictionary of the argument.
'''
print "local : ",locals()

myvar = 14
print namavar(myvar, globals()) # myvar 






''' membuat fungsi untuk menurunkan atau menaikan nilai variabel '''
''' Jika di c/c++ menggunakan pointer di python menggunakan perlakuan berbeda '''
def decvar(x) :
	v = namavar(x, globals())
	globals()[v] = globals()[v]-1

decvar(myvar)
print myvar # hasil 13 turun 1 angka







''' membuat fungsi yang bisa mengembalikan nilai lebih dari 1 '''
def multiReturn() :
	return 1,"HELLO",3

a,b,c = multiReturn()
print a,b,c # print a, HELLO, 3






''' membuat fungsi tanpa kunci def '''
test = lambda a,b : a * b 
print test(5,5) # print 25


''' membuat callback fungsi '''
def fungsi_kali(a,b) :
	return a*b

def fungsi_cetak(x) :
	print x

def caller(f, daftar_argument, callback) :
	''' 
	melakukan perhitungan 
	ini juga callback melewatkan fungsi ke parameter tapi dengan cara berbeda
	'''
	hasil = f(*daftar_argument)
	''' menampilkan hasil cetak dengan memanggil fungsi_cetak(x) '''
	callback(hasil)
	
caller(fungsi_kali,(5,10),callback=fungsi_cetak)


''' membuat deskripsi didalam fungsi '''
''' deskripsi ini dituliskan badan kode fungsi ditulis '''
def contohDeskripsi() :
	''' ini adalah contoh deskripsi fungsi '''
	pass

help(contohDeskripsi)
