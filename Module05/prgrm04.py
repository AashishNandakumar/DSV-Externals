# Annotated line graph with an image background
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# load the image
img = Image.open("plots/pf.jpg")

# create the plot and set the background
_, ax = plt.subplots(figsize=(10, 6))
ax.imshow(img)

# create data for line plot
x = np.array([100, 200, 300])
y = np.array([100, 200, 300])

# plot the line and add markers
ax.plot(x, y, color="blue", linewidth=2, marker="o")

# add annotations
ax.annotate("(100, 100)", xy=(100, 100))
ax.annotate("(200, 200)", xy=(200, 200))
ax.annotate("(300, 300)", xy=(300, 300))

# set the title and labels
ax.set_title("Annotated Line graph with Image")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")

# adjust the plot layout and display
plt.tight_layout()
plt.show()
