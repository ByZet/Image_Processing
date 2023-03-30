import random
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

A, B, C, D, E = [random.choices(range(8), k=5) for _ in range(5)]

liste_matrix = [A,B,C,D,E]
M = np.array(liste_matrix)

print("A = ",A)
print(M)

liste_0 = [num for sublist in liste_matrix for num in sublist if num == 0]
liste_1 = [num for sublist in liste_matrix for num in sublist if num == 1]
liste_2 = [num for sublist in liste_matrix for num in sublist if num == 2]
liste_3 = [num for sublist in liste_matrix for num in sublist if num == 3]
liste_4 = [num for sublist in liste_matrix for num in sublist if num == 4]
liste_5 = [num for sublist in liste_matrix for num in sublist if num == 5]
liste_6 = [num for sublist in liste_matrix for num in sublist if num == 6]
liste_7 = [num for sublist in liste_matrix for num in sublist if num == 7]

liste_dict = {'0': liste_0, '1': liste_1, '2': liste_2, '3': liste_3, '4': liste_4, '5': liste_5, '6': liste_6, '7': liste_7}

plt.plot(list(liste_dict.keys()), [len(liste_dict[k]) for k in liste_dict])
plt.xlabel('Sayılar')
plt.ylabel('Frekans')
plt.title('Liste Frekansları')
plt.show()

df = pd.DataFrame(M)
sns.heatmap(df, annot=True, cmap='Blues')
plt.show()
