from math import sqrt
import numpy as np
import scipy.stats as sp
import matplotlib.pyplot as plt

# X ~ B(50, 0.6)
# n = 50, p = 0.6인 이항 분포를 생성하고 누적 분포 함수 그리기
n = 50
p = 0.6
rv_1 = sp.binom(n, p)
x = np.arange(0, 51)
y = rv_1.cdf(x)
plt.plot(x, y)
plt.show()

# X의 확률 분포를 따르는 100개의 표본을 생성하고 각 표본의 평균 구하기
np.random.seed(0)
samples_1 = rv_1.rvs(100)
print(samples_1.mean())

# X의 값이 40이상의 값을 가지는 확률 구하기
print(1 - rv_1.cdf(39))

# 표본 100개에 대한 표본 평균을 구하는 과정을 30회 반복한 후, 표본 평균에 대한 평균과 분산 구하기
np.random.seed(0)
samples_2 = rv_1.rvs((30, 100))
average = samples_2.mean(axis=1).mean()
var = samples_2.mean(axis=1).var()
print(average)
print(var)

# 표본 평균이 따르는 정규 분포를 생성하고 누적 분포 함수 그리기
rv_2 = sp.norm(average, sqrt(var))
x = np.arange(23, 37, 0.1)
y = rv_2.cdf(x)
plt.plot(x, y)
plt.show()

# 표본 평균이 40이상의 값을 가지는 확률 구하기
print(1 - rv_2.cdf(40))
