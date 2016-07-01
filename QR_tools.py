#!/usr/bin/python

# sudo apt-get install libzbar-dev
# pip install pypng
# pip install pyqrcode
# pip install qrtools

import pyqrcode
import qrtools.qrtools as qtools


def print_qr_data(filepath):
	qr = qtools.QR()
	qr.decode(filepath)
	print(qr.data)


qr = pyqrcode.create("Sopetajo")
qr.png("qr_test.png", scale=6)
print_qr_data("qr_test.png")
