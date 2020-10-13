# import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt

data = pd.read_csv("C:/Users/g_m/Desktop/Programming/analysis/admittance.csv")
data.head()
data.describe()
print('hello world!')
# import os
# print(os.getcwd())
#
# path = 'c:\\Users\\g_m\\desktop\\programming\\analysis\\'
#
# files = []
# # r=root, d=directories, f = files
# for r, d, f in os.walk(path):
#     for file in f:
#         if '.csv' in file:
#             files.append(os.path.join(r, file))
#
# for f in files:
#     print(f)
#
# print(str(files[5]))
