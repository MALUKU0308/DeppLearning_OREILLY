import numpy as np

# 入力(1*2行列)
X = np.array([1,2])
print(X)
# 重み(2*3行列) 
W = np.array([[1,3,5],[2,4,6]])
print(W)
# 出力
Y = np.dot(X,W)
print(Y)

