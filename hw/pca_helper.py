import numpy as np
from sklearn.preprocessing import StandardScaler

X = np.array([[.2,-.3],[-1.1,2],[1,-2.2],[.5,-1],[-.6,1]])
mean = np.array([0,-.1])
centered = X - mean
print(f'centered data: \n{centered}')

m = X.shape[0]
cov_matrix = 1/m * np.dot(centered.T, centered)
print(f'covariance: \n{cov_matrix}')

eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
print(f'centered data: \n{eigenvalues}')
print(f'centered data: \n{eigenvectors}')

sorted_indices = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[sorted_indices]
eigenvectors = eigenvectors[:, sorted_indices]

first_pc = eigenvectors[:, 0]
print(f'first_pc: \n{first_pc}')

X_transformed = np.dot(centered, first_pc)
print(f'X_transformed: \n{X_transformed}')

variance = (eigenvalues[0] / np.sum(eigenvalues)) * 100
print(f'variance: \n{variance}')

# centered data: 
# [[ 0.2 -0.2]
#  [-1.1  2.1]
#  [ 1.  -2.1]
#  [ 0.5 -0.9]
#  [-0.6  1.1]]
# covariance:
# [[ 0.572 -1.112]
#  [-1.112  2.176]]
# centered data:
# [0.00296098 2.74503902]
# centered data:
# [[-0.89021285  0.45554483]
#  [-0.45554483 -0.89021285]]
# first_pc:
# [ 0.45554483 -0.89021285]
# X_transformed:
# [ 0.26915153 -2.37054629  2.3249918   1.02896397 -1.25256103]
# variance:
# 99.89224971091342