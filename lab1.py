import numpy as np
b = 0.007
arr = np.array([
  [1.0,5.5,16.0],
  [4.5,2.0,12.1],
  [8.0,1.0,13.5],
  [1.0,4.0,11.9],
  [5.0,5.5,20.9],
  [0.0,4.5,14.0],
  [1.0,6.0,17.4],
  [5.0,1.0,9.1],
  [2.0,4.5,17.3],
  [5.5,4.0,17.6],
  [6.5,0.0,11.0],
  [0.5,8.0,19.0],
  [3.0,7.0,21.0],
  [6.0,5.5,21.4],
  [1.5,2.5,10.4]])
n = np.shape(arr)[0]
arr0 = arr.T
#копировать присвоением низя, только b=a.copy()
# но если копировать часть?
x = arr0[0] #x = arr[:,0]
w = arr0[1] #w = arr[:,1]
y = arr0[2]


# ex1
Fx = np.sum(np.cos(x)**2)/2
# ex2
Fxwb = np.sum(np.dot(x,w))+b
# ex3
t = [0]*n
for i in range(n):
  t[i] = x[i]*w[i]+b

Loss = np.sum((y-t)**2)
print (Loss)
# ex5
import matplotlib.pyplot as plt
#x = np.arange (0.1 , 10.0 , 0.01) #определенный шаг
x = np.linspace (0.1, 10.0, 100) #количество точек
fig, ax = plt.subplots()
ax.plot(x,1/x)
plt.show ()
