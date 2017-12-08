from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im = Image.open('pinkie.png')
print(im.size)

fig = plt.figure()

data = np.array(im.getdata()).reshape(im.size[0],im.size[1],3)


ax_red = fig.add_subplot(1,3,1)
ax_green = fig.add_subplot(1,3,2)
ax_blue = fig.add_subplot(1,3,3)


ax_red.imshow(data[:,:,0],cmap='gray')
ax_green.imshow(data[:,:,1],cmap='gray')
ax_blue.imshow(data[:,:,2],cmap='gray')

plt.savefig("color-breakdown.png")
