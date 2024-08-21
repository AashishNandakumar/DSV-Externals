import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset("iris")

sns.pairplot(df, kind="scatter", hue="species")

plt.suptitle("iris dataset correlogram", y=1.02)

plt.show()
