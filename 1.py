#coba run ke python

import json

with open('1.json') as data:

    bdata = json.loads(data.read())

    print "Nama \t: %s" % bdata['nama']
    print "Umur \t: %s" % bdata['umur']
    print "Alamat\t: %s" % bdata['alamat']

    print "Hobi\t:"
    for hobi in bdata['hobi']:
        print "\t %s" % (hobi)

    print "Pendidikan\t:"
    for pend in bdata['riwayatPendidikan']:
        print "\t %s" % (pend['namaSekolah'])



