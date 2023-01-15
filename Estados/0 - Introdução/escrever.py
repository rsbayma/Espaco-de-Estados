#
def dispmat(self,A):
    cols = ''.join(['r']*A.shape[1])
    str = r'\left[\begin{array}{' + cols + r'}'
    (m,n) = A.shape
    for i in range(m):
      for j in range(n):
        if j<n-1:
          str = str + '{:.3}'.format(A[i][j]) + '&'
        else:
          str = str + '{:.3}'.format(A[i][j]) + r'\\'
    return str + r'\end{array}\right]'


''' def dispss(self,A,B,C,D):
    str1 = r'\dot{\mathbf{x}} = ' + self.dispmat(A) + r'\mathbf{x}'
    str1 = str1 + '+' + self.dispmat(B) + r'\mathbf{u}'
    str2 = r'\mathbf{y} = ' + self.dispmat(C) + r'\mathbf{x}'
    str2 = str2 + self.dispmat(D) + r'\mathbf{u}'
    return [str1,str2]
'''

'''import numpy as np
n = np.random.randint(4,6)
p = np.random.randint(1,4)
q = np.random.randint(1,4)

A = np.random.randn(n,n)
B = np.random.randn(n,p)
C = np.random.randn(q,n)
D = np.random.randn(q,p)

print(dispss(A,B,C,D))'''
