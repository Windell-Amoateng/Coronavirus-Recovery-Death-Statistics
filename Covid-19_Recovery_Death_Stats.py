import matplotlib.pyplot as plt

def main():
    countries = [0, 10, 20, 30, 40, 50, 60, 70] # x-coordinates
    totalRecovered = [7.56, 35.894, 15.476, 10.376, 5.847, 10.89, 5.254, 13.87] # y-coordinates
    deaths = [3.763, 10.46, 6.946, 4.876, 2.34, 4.467, 3.34, 5.693] # relates to the line graph

    # Bar Graph
    barWidth = 5
    leftEdge = countries
    height = totalRecovered

    # Line Graph
    heights1 = deaths

    # Constructing Bar Graph
    plt.bar(leftEdge, height, barWidth, color = ("Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet", "Brown"))

    # Customizing xlabel, ylabel, and title for diagram
    plt.xlabel("Countries")
    plt.ylabel("Number of deaths")
    plt.title("Coronavirus Recovery and Death Statistics of Various Countries")

    # Constructing Line Graph and ticks
    plt.plot(countries, heights1, color = ("pink"), marker = "o")
    plt.xticks([0, 10, 20, 30, 40, 50, 60, 70], ["Germany", "USA", "UK", "Italy", "Belgium", "France", "Greece", "Spain"])
    plt.yticks([4, 11, 7, 5, 2, 5, 3, 6], ["3.763", "10.46", "6.946", "4.876", "2.34", "4.467", "3.34", "5.693"])

    # Displaying Completed Graph 
    plt.grid(True)
    plt.show()
main()