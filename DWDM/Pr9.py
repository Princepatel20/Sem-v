from sklearn import datasets
digits = datasets.load_digits()
dir(digits)
print(digits.images[0])
import matplotlib.pyplot as plt
def plot_multi(i):
nplots = 16
fig = plt.figure(figsize=(15, 15))
for j in range(nplots):
plt.subplot(4, 4, j+1)
plt.imshow(digits.images[i+j], cmap='binary')
plt.title(digits.target[i+j])
plt.axis('off')
plt.show()
plot_multi(0)
