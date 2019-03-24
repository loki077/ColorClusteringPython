import matplotlib.pyplot as plt
import numpy as np
 
X = np.zeros(shape=(100,100))

for y in xrange(0, 100):	
		for x in xrange(0, 100):
			if x < 50 :
				X[x, y] = 255
			else:
				X[x, y] = 0

# X = np.random.random((100, 100)) # sample 2D array
plt.imshow(X, cmap="gray")
plt.show()