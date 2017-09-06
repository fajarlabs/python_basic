import sys 
print ("python version ",sys.version)

class Bapak :
	def __init__(self, nama) : # setiap methode harus ada parameter "self" sebagai bagian dari class tersebut
		self.__nama = nama

	def getNama(self) :
		return self.__nama

class Ibu :
	def __init__(self, nama) : # setiap methode harus ada parameter "self" sebagai bagian dari class tersebut
		self.__nama = nama

	def getNama(self) :
		return self.__nama		

obj = Bapak("Bapak") 	
print(obj.getNama())

class Anak(Bapak,Ibu) :
	def __init__(self):
		Ibu.__init__(self,"HELLO IBU")
		Bapak.__init__(self,"HELLO BAPAK")
		pass

obj = Anak()
# yang terpanggil hello bapak, atau argument turunan class paling kiri
print obj.getNama()




'''
Developer pada umumnya memberi underscore 2x untuk private. 
Contoh __var untuk private dan underscore 1x _var untuk protected
'''

''' Mmembuat atribute private '''
class PersegiPanjang :
	def __init__(self, p, l) :
		"""
		Ini otomatis digenerate secara internal oleh python
		menjadi _PersegiPanjang__panjang dan _PersegiPanjang__lebar
		"""
		self.__panjang = p 
		self.__lebar = l 

	"""
	dibawah anotasi @property berarti hanya sebagai read-only
	jika mencoba di set akan terjadi error, tapi jika menggunakan python 2.7
	tidak terjadi apa-apa
	"""
	@property
	def panjang(self) :
		return self.__panjang

	@property
	def lebar(self) :
		return self.__lebar

	"""
	Property setter
	"""
	@panjang.setter
	def panjang(self, p) :
		self.__panjang = p

	@lebar.setter
	def panjang(self, l) :
		self.__lebar = l

	def setvalue(self, p, l) :
		self.__panjang = p 
		self.__lebar = l 

	def getpanjang(self) :
		return self.__panjang 

	def getlebar(self) :
		return self.__lebar

	def hitung(self) :
		return self.__panjang * self.__lebar

obj = PersegiPanjang(4,5)
print "Dictionary : ",obj.__dict__ # untuk melihat properti private
print "getPanjang() : ",obj.getpanjang()
print "getLebar() : ",obj.getlebar()
print "hitung() : ",obj.hitung()
print "getLebar : ",obj.getlebar()
print "panjang : ",obj.panjang
print "set panjang = 20"
obj.panjang = 20
print "getPanjang() : ",obj.getpanjang()
print "panjang : ",obj.panjang

''' membuat kelas abstrak '''
from abc import ABCMeta, abstractmethod

'''
class HitungPersegiPanjang(metaclass=ABCMeta) :
	# metode abstract
	@abstractmethod
	def luas(self) :
		pass #tidak memiliki implementasi

obj = HitungPersegiPanjang()
'''

''' contoh overload operator '''
class Lingkaran :
	def __init__(self, r) :
		self.__jarijari = r 

	#overload operator == (equals)
	def __eq__(self, objek) :
		return self.__jarijari == objek.__jarijari

	#overload operator != (not equals)
	def __ne__(self, objek) :
		return self.__jarijari != objek.__jarijari

	#overload operator < (less than)
	def __lt__(self, objek) :
		return self.__jarijari < objek.__jarijari

	#overload operator > (greather than)
	def __gt__(self, objek) :
		return self.__jarijari > objek.__jarijari

	#overload operator >= (greather equals)
	def __ge__(self, objek) :
		return self.__jarijari >= objek.__jarijari

	#overload operator <= (less equals)
	def __le__(self, objek) :
		return self.__jarijari <= objek.__jarijari

obj = Lingkaran(5)
obj2 = Lingkaran(6)

if(obj == obj2) :
	print "Same class"
else :
	print "Not same" # result Not Same

if(obj2 > obj) :
	print "Yes greater"
else :
	print "No greater" # result equals


class ContohMetodeStatic :
	@staticmethod
	def tambah(a,b) : # tanpa self
		return a+b

print "Hasil fungsi tambah static : %i " % ContohMetodeStatic.tambah(5,5)

	