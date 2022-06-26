import random
import numpy as np
import matplotlib.pylab as plt
import pandas as pd
import seaborn as sns
liste = []
deger = 0
A = []
B = []
C = []
D = []
E = []
son = 0
matrix1 = []
while son < 5:
    A.append(random.randint(0,7))
    B.append(random.randint(0,7))
    C.append(random.randint(0,7))
    D.append(random.randint(0,7))
    E.append(random.randint(0,7))
    son +=1
liste_matrix = [A,B,C,D,E]
M = np.array(liste_matrix)    
print("A = ",A)
print(M)

liste_0 = []
liste_1 = []
liste_2 = []
liste_3 = []
liste_4 = []
liste_5 = []
liste_6 = []
liste_7 = []

for i in A:
    while deger < 5:
        if A[deger] == 0:
            liste_0.append(A[deger])
            color = '#808090'
        elif A[deger] ==1 :
            liste_1.append(A[deger])
            color = '#808085'
        elif A[deger] == 2:
            color = '#808080'
            liste_2.append(A[deger])
        elif A[deger] ==3 :
            color = '#808075'
            liste_3.append(A[deger]) 
        elif A[deger] ==4 :
            color = '#808075'
            liste_4.append(A[deger])
        elif A[deger] ==5 :
            color = '#808075'
            liste_5.append(A[deger]) 
        elif A[deger] ==6:
            color = '#808075'
            liste_6.append(A[deger])
        elif A[deger] ==7 :
            color = '#808075'
            liste_7.append(A[deger]) 
        deger += 1
deger = 0

for i in B:
    while deger < 5:
        if B[deger] == 0:
            liste_0.append(B[deger])
            color = '#808090'
        elif B[deger] ==1 :
            liste_1.append(B[deger])
            color = '#808085'
        elif B[deger] == 2:
            color = '#808080'
            liste_2.append(B[deger])
        elif B[deger] ==3 :
            color = '#808075'
            liste_3.append(B[deger]) 
        elif B[deger] ==4 :
            color = '#808075'
            liste_4.append(B[deger])
        elif B[deger] ==5 :
            color = '#808075'
            liste_5.append(B[deger]) 
        elif B[deger] ==6:
            color = '#808075'
            liste_6.append(B[deger])
        elif B[deger] ==7 :
            color = '#808075'
            liste_7.append(B[deger]) 
        deger += 1
deger = 0

for i in C:
    while deger < 5:
        if C[deger] == 0:
            liste_0.append(C[deger])
            color = '#808090'
        elif C[deger] ==1 :
            liste_1.append(C[deger])
            color = '#808085'
        elif C[deger] == 2:
            color = '#808080'
            liste_2.append(C[deger])
        elif C[deger] ==3 :
            color = '#808075'
            liste_3.append(C[deger]) 
        elif C[deger] ==4 :
            color = '#808075'
            liste_4.append(C[deger])
        elif C[deger] ==5 :
            color = '#808075'
            liste_5.append(C[deger]) 
        elif C[deger] ==6:
            color = '#808075'
            liste_6.append(C[deger])
        elif C[deger] ==7 :
            color = '#808075'
            liste_7.append(C[deger]) 
        deger += 1
deger = 0
for i in D:
    while deger < 5:
        if D[deger] == 0:
            liste_0.append(D[deger])
            color = '#808090'
        elif D[deger] ==1 :
            liste_1.append(D[deger])
            color = '#808085'
        elif D[deger] == 2:
            color = '#808080'
            liste_2.append(D[deger])
        elif D[deger] ==3 :
            color = '#808075'
            liste_3.append(D[deger]) 
        elif D[deger] ==4 :
            color = '#808075'
            liste_4.append(D[deger])
        elif D[deger] ==5 :
            color = '#808075'
            liste_5.append(D[deger]) 
        elif D[deger] ==6:
            color = '#808075'
            liste_6.append(D[deger])
        elif D[deger] ==7 :
            color = '#808075'
            liste_7.append(D[deger]) 
        deger += 1
deger = 0


for i in E:
    while deger < 5:
        if E[deger] == 0:
            liste_0.append(E[deger])
            color = '#808090'
        elif E[deger] ==1 :
            liste_1.append(E[deger])
            color = '#808085'
        elif E[deger] == 2:
            color = '#808080'
            liste_2.append(E[deger])
        elif E[deger] ==3 :
            color = '#808075'
            liste_3.append(E[deger]) 
        elif E[deger] ==4 :
            color = '#808075'
            liste_4.append(E[deger])
        elif E[deger] ==5 :
            color = '#808075'
            liste_5.append(E[deger]) 
        elif E[deger] ==6:
            color = '#808075'
            liste_6.append(E[deger])
        elif E[deger] ==7 :
            color = '#808075'
            liste_7.append(E[deger]) 
        deger += 1
deger = 0

print("M = ",type(M))
print(liste_0)
print ("liste1",liste_1)
print(liste_2)
print(liste_3)  
print(liste_4)  
print(liste_5)
print(liste_6)
print(liste_7)

bagil_0 = (len(liste_0)/25)
bagil_1=(len(liste_1)/25)
bagil_2 = (len(liste_2)/25)
bagil_3 = (len(liste_3)/25)
bagil_4 =(len(liste_4)/25)
bagil_5 = (len(liste_5)/25)
bagil_6 = (len(liste_6)/25)
bagil_7 = (len(liste_7)/25)
liste_bagil_0 = [bagil_0]
liste_bagil_1 = [bagil_1]
liste_bagil_2 = [bagil_2]
liste_bagil_3 = [bagil_3]
liste_bagil_4 = [bagil_4]
liste_bagil_5 = [bagil_5]
liste_bagil_6 = [bagil_6]
liste_bagil_7 = [bagil_7]
print("Bağıl=", bagil_1,bagil_2,bagil_3,bagil_4,bagil_5,bagil_6,bagil_7)
y = np.array(8)
x_grafik_1 = liste_0 + liste_1 + liste_2 + liste_3 + liste_4 + liste_5 + liste_6 + liste_7
plt.hist(x_grafik_1, bins = 20,color = 'blue')
plt.show()
y_2 = [0,1,2,3,4,5,6,7]
x_2 =  [bagil_0,bagil_1,bagil_2,bagil_3,bagil_4,bagil_5,bagil_6,bagil_7]
#plt.hist(x_2, y ,color = 'red')

plt.plot(y_2,x_2)
plt.show()
fig2, (resim) = plt.subplots(1)
resim = plt.imshow(M, cmap='gray')
mng = plt.get_current_fig_manager()
fig2.text(0.35, 0.96, '8 Bit', verticalalignment='top', horizontalalignment='left', fontsize=20)
try:mng.window.geometry('500x500+1059+225')
except:pass
try:mng.window.title('Resim')
except:pass
plt.show()
print('Veri matris =  \n',M)
