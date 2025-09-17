import pandas as pd
import numpy as np
df = pd.DataFrame(np.arange(0, 20).reshape(5, 4))
# print(df)
# print(df[0])
# print(df[1][0])
# print(df[3])


arr = np.array([[1, 2],
                [3, 4]])
arr[0][1]    # -> 2   (row 0, col 1)
arr[0, 1]    # -> 2
 

# print(df[0][1] )     # -> 3   (column label 0, then row label 1)
# print(df.iloc[0, 1]) # -> 2   (row 0, col 1 by position)


df[0][1] != df.iloc[0, 1]  # True


df = pd.read_csv('data.csv', header=0, skipinitialspace=True)  # first row -> column names
# print(df)
# print(df.iloc[1, 2])  # -> 7
# print(df[2][1])       # -> 7    
# print(df.loc[1, 2])       # -> 7

# print(df["COL4"])



import matplotlib.pyplot as plt
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], color = 'blue', marker='o', linestyle='dashed')   # 'ro' means red color, round points
# plt.xlabel('x axis')
# plt.ylabel('y axis')
# plt.title('My first graph')
# plt.savefig('plot.png', bbox_inches='tight')  # save to workspace
# plt.show()

# plt.plot(df["COL1"], df["COL2"], color = 'blue', marker='o', linestyle='dashed')   # 'ro' means red color, round points

# plt.scatter(df["COL1"], df["COL2"], color = 'blue')  


plt.subplot(2, 1, 1,)   # 'ro' means red color, round points
plt.savefig('plot.png', bbox_inches='tight')  # save to workspace
plt.show() 