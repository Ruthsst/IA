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
	aux=[]
	ax=()
	for i in range(len(x)):
		aux.append((round(x[i]*a,4),))
		ax+=aux[i]
	return ax

def sumvec(a,b):
	s=[]
	for i in range(len(a)):
		s.append(round(a[i]+b[i],4))
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

def CostFunc(U,D,c,n,m):
	J=0
	for i in range(c):
		JI=0
		for j in range(n):
			JI+=U[i][j]**m*D[i][j]**2
		J+=JI
	return J

def KMeans(P,C,m):
	D=[]
	c=len(C)
	n=len(P)
	Centros=[]
	Centros.append(C)
	for k in range(ite):
		print 'iteracion numero: '+str(k+1)
		print
		#Matriz de distancias
		D=getDistMat(P,Centros[k],c,n)
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
		Centros.append(Cen)
		
		#Calculando la funcion de costo
		print
		J=CostFunc(U,D,c,n,m)
		print 'la Funcion de Costos es: '+str(J)
		#if(k!=0 & distEuc(Centros[k-1][0],Centros[k][0])==0 & distEuc(Centros[k-1][1],Centros[k][1])==0 ):
		#	break
		#print 'los centros nuevos y los anteriores coinciden'
		
	#print Centros

P=input("Inserte puntos: ")
C=input("Inserte centros: ")
m=input("inserte valor de m: ")
ite=input("numero de iteraciones")

print
KMeans(P,C,m)


