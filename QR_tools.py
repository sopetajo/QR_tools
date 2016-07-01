#!/usr/bin/python

# sudo apt-get install libzbar-dev
# pip install pyqrcode
# pip install qrtools

import pyqrcode
import qrtools.qrtools as qtools


def print_qr_data(filepath):
	qr = qtools.QR()
	qr.decode(filepath)
	print(qr.data)


print_qr_data("qr_test.png")
