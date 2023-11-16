#import luas
from luas.persegi import luas as kotak
from luas.lingkaran import luas as lingkaran
from luas.segitiga import luas as segitiga

#import volume
from volume.bola import volume as bola
from volume.kerucut import volume as kerucut
from volume.kubik import volume as kubik

#panggil fungsi luas
print(lingkaran(21))
print(kotak(10))
print(segitiga(10,12))

#panggil fungsi volume
print(bola(10))
print(kerucut(12,14))
print(kubik(10,10,10))