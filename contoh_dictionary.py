# dictionary dibuat menggunakan kurung kurawal {} setiap anggota berupa pasangan key-value
d = {1:10,2:20,3:30,4:40,5:50}

print d.__len__()

try :
	print d.get(1) #cara 1
	print d[1] #cara 2
except KeyError :
	print "Key tidak ditemukan"

try :
	# dictionary bisa dari type apa saja
	karyawan = {
		'nip' : 'NIP-10001',
		'nama' : 'Fajar',
		'gaji' : 15000000
	}

	# menambah dictionary
	karyawan['alamat'] = 'Kota Depok'

	# hapus isi 
	del karyawan['nama']

	# ganti isi
	karyawan['nama'] = 'Fajar Rizky'

	print karyawan['nip']
	print karyawan.get('nama')
	print karyawan
except KeyError :
	print "Key tidak ditemukan"