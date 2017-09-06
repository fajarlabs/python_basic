data = [10,20,30]

try :
	x = data[3]
except IndexError :
	print "Tidak ada di list data"
except (NameError,Exception) as e : # jika menggunakan multi except
	print "Error default"
else : # aksi jika tidak terjadi eksepsi
	print "Error tidak terdeteksi"
finally : # final harus ditaruh di posisi terakhir dan selalu di eksekusi
	print "Final"

