import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("iris")

# create a basic density plot
sns.kdeplot(data=df, x="sepal_width")

plt.title("density plot of sepal width")
plt.show()
