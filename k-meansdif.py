from math import *
#import scipy
#import numpy

def distEuc(a,b):
	s=0
	for i in range(len(a)):
		s+=(a[i]-b[i])**2
	s=round(sqrt(s),4)
	return s

def multiesca(x,a):
	ax=[]
	for i in range(len(x)):
		ax.append(round(x[i]*a,4))
	return ax

def sumvec(a,b):
	s=[]
	for i in range(len(a)):
		s.append(a[i]+b[i])
	return s
	
def dibujaMatriz(M):
	for i in range(len(M)):
		for j in range(len(M[i])):
			print '{0:>3s}'.format(str(M[i][j])),
		print 

def getDistMat(P,C,c,n):
	D=[]
	for i in range(c):
		aux=[]
		for j in range(n):
			d=distEuc(P[j],C[i])
			aux.append(d)
		D.append(aux)
	return D

def getMemMat(D,c,n,m):
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
	return U

def getCenters(P,U,n,m,c):
	C=[]
	for i in range(c):
		aux1,aux2=2*[0],0
		for j in range(n):
			aux1=sumvec(multiesca(P[j],U[i][j]**m),aux1)
			aux2+=U[i][j]**m
		cent=multiesca(aux1,1.0/aux2)
		C.append(cent)
	return C

def KMeans(P,C,m):
	#por el momento haremos la primera iteracion
	D=[]
	c=len(C)
	n=len(P)

	#Matriz de distancias
	D=getDistMat(P,C,c,n)
	print("La Matriz de distancias es:")
	print
	dibujaMatriz(D)
	print

	#matriz de membresia
	U=getMemMat(D,c,n,m)
	print("La Matriz de Membresia es:")
	print
	dibujaMatriz(U)
	print

	#obteniendo los nuevos centros
	Cen=getCenters(P,U,n,m,c)
	print 'los nuevos centros son:'
	print Cen


P=input("Inserte puntos: ")
C=input("Inserte centros: ")
m=input("inserte valor de m: ")
print
KMeans(P,C,m)


