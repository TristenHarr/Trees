# import numpy as np
# import pandas as pd

# # x = pd.DataFrame({0:[1,2,3], 1:[[4,5,6],[1,2,3],[7,8,9]],2:[7,8,9]})
# outside2 = ["A","B"]
# outside = ['G1','G1','G1','G2','G2','G2']
# inside = [1,2,3,1,2,3]
# hier_index = list(zip(outside,inside))
# hier_index = pd.MultiIndex.from_tuples(hier_index)
# df = pd.DataFrame(np.random.randn(6,2),index=hier_index,columns=['A','B'])
# print(df)

root = root=(1,1)
y=[ [[0], [1], [2], [3]],
    [[1], [1], [2], [3]],
    [[2], [4], [5], [6]],
    [[3], [7], [8], [9]]]

print(y[0][0])
