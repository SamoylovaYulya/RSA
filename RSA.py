#!/usr/bin/python
# -*- coding: utf-8 -*-

import bint
import sys
import random



def xgcd(a, b):
	
	if a == bint.bint(0):
		return 0, 1, b

	if b == bint.bint(0):
		return 1, 0, a

	px = bint.bint(0)
	ppx = bint.bint(1)
	py = bint.bint(1)
	ppy = bint.bint(0)

	while b > bint.bint(0):
		q = a / b
		a, b = b, a % b
		x = ppx - q * px
		y = ppy - q * py
		ppx, px = px, x
		ppy, py = py, y

	return ppx, ppy, a


def generate_d(a, b): #вычисляется число d
	while True:
		x, y, g = xgcd(a, b)

		if g != bint.bint(1):
			raise ValueError("Невозможно подобрать такое d, чтобы выполнялось условие d * e mod fi = 1.")
		else:
			z = x % b # chislo d,tolko tut z, no na samom dele eto d :)
			break
	return z

# shifr /deshifr rsa
def rsa(msg, p, q, e):
	fi = (p - bint.bint(1)) * (q - bint.bint(1)) #vichislyaem phi po knizhke shitova) p and q prostie => phi(p)= p - 1 and phi(q)=q-1
	d = generate_d(e, fi) # generim chislo d
	print "\nopen key: {"+str(e)+","+str(p)+"}"
	print "\nclose key: {"+str(d)+","+str(p)+"}"

	msg = bint.bint(str(msg)) 

	modulus = p * q # vichislyaem n = p*q on zhe modul'

	

	if msg > modulus:
		raise ValueError("Неверная длина сообщения") #esli soobshenie > modulya => oshibka 

	

	code = d.powmod(msg, e, modulus) #code = msg^e mod modulus                     # Кодирование

	print "\ncode: "+ str(code)

	decode_msg = d.powmod(code, d, modulus) # decod = code^d mod modulus              # Декодирование


	return decode_msg


def usage():
	print "\nИспользование: python RSA.py msg.txt\n"

	sys.exit(-1)


def main():
	if len(sys.argv) != 2:
		usage()
	try:

		f = open(sys.argv[1])

		msg = int(f.read())

		f.close()
	except IOError:
		print 'no such file',sys.argv[1]
		sys.exit(-1)
	print "\ntext: "+str(msg)
	tmp = bint.bint()

	p = bint.bint(tmp.read("p.txt"))
	q = bint.bint(tmp.read("q.txt"))
	e = bint.bint(tmp.read("e.txt"))

	
	decode_msg = rsa(msg, p, q, e)
	print "\ndecode: "+str(decode_msg)

main()