import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.core.window.expanding import Any
import seaborn as sns

np.random.seed(42)
n = 1000

data = {
    "Age": np.random.normal(35, 15, n).astype(int),
    "Marital_Status": np.random.choice(
        ["Single", "Married", "Divorced"],
        n,
    ),
    "Gender": np.random.choice(
        ["Male", "Female", "Other"],
        n,
        p=[0.49, 0.49, 0.02],
    ),
    "Income": np.random.lognormal(10, 1, n).astype(int),
    "Education_Level": np.random.choice(
        ["High School", "Bachelor", "Master", "PhD"],
        n,
    ),
    "Location": np.random.choice(
        ["Downtown", "Suburb", "Rural"],
        n,
    ),
    "Year": np.random.choice(
        range(2015, 2025),
        n,
    ),
}


df = pd.DataFrame(data)


def create_plot(
    plot_type: str,
    x: Any,
    y: Any = None,
    title: str = "",
    xlabel: str = "",
    ylabel: str = "",
) -> None:
    """
    Creates and stores a plot for the given parameters

    Parameters:
        plot_type (str): The plot types required
        x (Any): The x-axis parameter
        y (Any): The y-axis parameter
        title (str): The title of the plot,
        xlabel (str): The x-axis label for the plot
        ylabel (str): The y-axis label for the plot

    Returns:
        None
    """
    plt.figure(figsize=(10, 6))

    if plot_type == "histogram":
        plt.hist(x, bins=20, edgecolor="black")
    elif plot_type == "bar":
        x.value_counts().plot(kind="bar")
        # plt.bar(x, y)
    elif plot_type == "pie":
        x.value_counts().plot(kind="pie", autopct="%1.1f%%")
        # plt.pie(x)
    elif plot_type == "box":
        plt.boxplot(x)
    elif plot_type == "scatter":
        plt.scatter(x, y, alpha=0.5)
    # ! tricky
    elif plot_type == "line":
        x.groupby(y).mean().plot(kind="line", marker="o")
        # plt.plot(x, y)
    elif plot_type == "violin":
        sns.violinplot(x=x)
    # ! tricky
    elif plot_type == "heatmap":
        ct = pd.crosstab(x, y)
        sns.heatmap(ct, annot=True, fmt="d", cmap="YlGnBu")
    # ! tricky
    elif plot_type == "area":
        pivot_data = pd.pivot_table(
            df, values="Age", index="Year", columns="Location", aggfunc="count"
        )
        pivot_data.plot(kind="area", stacked=True)

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.savefig(f"plots/{plot_type}_plot.png")
    plt.close()


# create_plot(
#     plot_type="histogram",
#     x=df["Age"],
#     title="Distribution of Ages",
#     xlabel="Age",
#     ylabel="frequency",
# )

# create_plot(
#     plot_type="bar",
#     x=df["Marital_Status"],
#     title="Marital Status distribution",
#     xlabel="Marital Status",
#     ylabel="Count",
# )

# create_plot(
#     plot_type="pie",
#     x=df["Gender"],
#     title="Gender Distribution",
# )

# create_plot(
#     plot_type="box",
#     x=df["Income"],
#     title="Income Distribution",
#     ylabel="Income",
# )

# create_plot(
#     plot_type="scatter",
#     x=df["Education_Level"],
#     y=df["Income"],
#     title="Education Level vs Income",
#     xlabel="Education Level",
#     ylabel="Income",
# )

# create_plot(
#     plot_type="line",
#     x=df["Age"],
#     y=df["Year"],
#     title="Average age over time",
#     xlabel="Year",
#     ylabel="Average Age",
# )

# create_plot(
#     plot_type="violin",
#     x=df["Education_Level"],
#     title="Education Level Distribution",
#     xlabel="Education Level",
#     ylabel="Density",
# )

# create_plot(
#     plot_type="heatmap",
#     x=df["Education_Level"],
#     y=df["Marital_Status"],
#     title="Education Level vs Marital Status",
# )

create_plot(
    plot_type="area",
    x=df["Location"],
    y=df["Year"],
    title="Population by Location Over Time",
    xlabel="Year",
    ylabel="Population",
)
