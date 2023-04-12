import math
pmtb=5000
pmtk=1000
psdb=600
psdk=100
prdmax=7000
prdmin=2000
xpmt=int(input("Masukan inputan Permintaan : "))
xpsd=int(input("Masukan inputan Persediaan : "))

#fungsi permintaan linear turun
if (xpmt<=pmtk): pmtt=1
elif (xpmt>pmtk and xpmt<pmtb): pmtt=(pmtb-xpmt)/(pmtb-pmtk)
else: pmtt=0
#fungsi permintaan linear naik
if (xpmt<=pmtk): pmtn=0
elif (xpmt>pmtk and xpmt<pmtb): pmtn=(xpmt-pmtk)/(pmtb-pmtk)
else: pmtn=1
#fungsi persediaan sedikit
if (xpsd<=psdk): psds=1
elif(xpsd>psdk and xpsd<psdb): psds=(psdb-xpsd)/(psdb-psdk)
else: psds=0
#fungsi persediaan banyak
if (xpsd<=psdk): psdba=0
elif(xpsd>psdk and xpsd<psdb): psdba=(xpsd-psdk)/(psdb-psdk)
else: psdba=1
#Rule 1
aprd1=min(pmtt,psdba)
z1=prdmax-(aprd1*(prdmax-prdmin))
#Rule 2
aprd2=min(pmtt,psds)
z2=prdmax-(aprd2*(prdmax-prdmin))
#Rule 3
aprd3=min(pmtn,psdba)
z3=(aprd3*(prdmax-prdmin))+prdmin
#Rule 4
aprd4=min(pmtn,psds)
z4=(aprd4*(prdmax-prdmin))+prdmin

z=((aprd1*z1)+(aprd2*z2)+(aprd3*z3)+(aprd4*z4))/(aprd1+aprd2+aprd3+aprd4)
print("Jadi Jumlah Makanan jenis ABC yang harus di produksi dari permintaan ", xpmt," dan persediaan ", xpsd," sebanyak ", math.ceil(z))