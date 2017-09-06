class Induk :
	def __init__(self, a, b) :
		self._a = a
		self._b = b

	def test(self) :
		print self._a


records = [1, "Hello", Induk]

print type(records[0]) # class <int>
print type(records[1]) # class <str>
print type(records[2]) # class <classobj>
print records.__len__()

records = [
		[1, 'Master C/C++',['Data Lain']],
		[2, 'Master Java'],
		[3, 'Master PHP'],
		[4, 'Master Javascript']
	]

print records[0][2][0] # data lain

records.append("5") # apped data
print records[4] #5
                 
records.insert(1,"Insert 2") # jika menggunakan insert kita bisa menyisipkan kedalam index
print records

# operator slice :
a = [10,20,30,40,50]
b = [10,20,30,40,50]
print a[:2] # [10,20]
print b[2:] # [30,40,50]
     
# melibatkan asterisk
# ternyata syntax error ini tidak bisa di catch karena script masih tahap parse
# jadi exception tidak akan bisa tertangkap
# https://stackoverflow.com/questions/25049498/failed-to-catch-syntax-error-python
karyawan = ['agus','budi','imam','wisnu','indra']       
try :
	nama1, nama2, *namalain = karyawan
	print nama1
	print nama2
	print namalain
except SyntaxError :
	print "Not supported in python 2.7"
else : # aksi jika tidak terjadi eksepsi
	print "Error tidak terdeteksi"

"""
untuk metode selengkapnya bisa di lihat disini https://docs.python.org/3/tutorial/datastructures.html
"""
