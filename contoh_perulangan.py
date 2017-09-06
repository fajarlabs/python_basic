i = 0;

# contoh menggunakan while
while(i < 3) :
	print "cetak while : %d " % i 
	i += 1

# karena do-while di python tidak ada sesuai konsep do-while
# dilakukan dengan seperti ini
i = 0;
while True :
	i += 1
	print "Setup :"
	if(i > 5) :
		break;

# contoh menggunakan range
for i in range(0, 4) :
	print "cetak for : %d " % i

# contoh menggunakan dengan index menurun
for i in range(4, 0, -1) :
	print "cetak for index : %d" % i