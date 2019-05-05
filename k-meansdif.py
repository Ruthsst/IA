from math import *
#import scipy
import numpy

def distEuc(a,b):
	s=0
	for i in range(len(a)):
		s+=(a[i]-b[i])**2
	s=round(sqrt(s),4)
	return s

def dibujaMatriz(M):
	for i in range(len(M)):
		print 
		for j in range(len(M[i])):
			print '{:>3s}'.format(str(M[i][j])),
		print 


def KMeans(P,C,m):
	#por el momento haremos la primera iteracion
	D=[]
	c=len(C)
	n=len(P)
	#calculando Distancias y matriz de distancias
	D=[]
	for i in range(c):
		aux=[]
		for j in range(n):
			d=distEuc(P[j],C[i])
			aux.append(d)
		D.append(aux)
	print("La Matriz de distancias es:")
	print
	dibujaMatriz(D)
	#matriz de membresia
	U=[]
	for i in range(c):
		aux=[]
		for j in range(n):
			aux2=0
			for k in range(c):
				aux2+=(D[i][j]/D[k][j])**(2.0/(m-1))
			u=round(1.0/aux2,4)
			aux.append(u)
		U.append(aux)
	print("La Matriz de Membresia es:")
	print
	dibujaMatriz(U)
	

P=input("Inserte puntos: ")
C=input("Inserte centros: ")
m=input("inserte valor de m: ")
KMeans(P,C,m)
