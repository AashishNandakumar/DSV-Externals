import matplotlib.pyplot as plt
import numpy as np

months = ["January", "February", "March", "April"]
vanilla_sales = [50, 60, 70, 80]
chocolate_sales = [60, 70, 80, 90]
butterscotch_sales = [30, 40, 50, 60]

plt.bar(months, vanilla_sales, label="vanilla", color="lightyellow")
plt.bar(
    months,
    chocolate_sales,
    label="chocolate",
    bottom=np.array(vanilla_sales),
    color="lightgray",
)
plt.bar(
    months,
    butterscotch_sales,
    label="butterscotch",
    bottom=np.array(vanilla_sales) + np.array(chocolate_sales),
    color="lightcoral",
)

plt.xlabel("months")
plt.ylabel("sales")
plt.title("Ice cream flavour sales over different months")
plt.legend()

plt.tight_layout()
plt.show()
