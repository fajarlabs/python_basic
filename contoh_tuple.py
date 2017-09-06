# dengan menggunakan tuple maka elemen tidak dapat ditambah modifikasi atau dikurangi
t = (10,20,30,40,50)
print type(t)
print t[0]

try :
	t[0] = 100
except TypeError as e :
	''' informasi error menyatakan bahwa tidak mendukung perubahan item '''
	print "Terjadi error : %s" % str(e) 

''' mencari index di tuple '''
print "nilai 20 berada di index %i " % int(t.index(20))

''' selengkapnya bisa baca disini https://www.programiz.com/python-programming/methods/tuple '''