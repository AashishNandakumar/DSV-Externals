# use piechart to visualize the distribution of speakers for major Indian languages
import matplotlib.pyplot as plt

languages = [
    "Hindi",
    "Bengali",
    "Marathi",
    "Telugu",
    "Tamil",
    "Gujarati",
    "Urdu",
    "Kannada",
    "Odia",
    "Malayalam",
]
speakers = [44.0, 8.1, 7.2, 6.9, 6.3, 5.0, 4.5, 3.8, 3.2, 3.2]

# create piechart
plt.figure(figsize=(10, 6))

# populate the piechart
plt.pie(speakers, labels=languages, autopct="%1.1f%%")
plt.title("Distribution of speakers for major Indian languages")

# adjust the layout and display
plt.tight_layout()
plt.show()
