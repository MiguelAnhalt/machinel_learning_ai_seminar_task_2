# Task 2: Understanding and Visualizing the Iris Dataset

This Python script (`IrisPlot.py`) loads the Iris dataset from a CSV file (`Iris.csv`) and generates scatter plots to visualize the relationships between different features for the three species of Iris flowers.

## Author:

Miguel Angel Lopez Mejia

## Libraries Used:

* `pandas`: For reading and manipulating the CSV data into a DataFrame.
* `matplotlib.pyplot`: For creating the scatter plots.
* `numpy`: For numerical operations, particularly when handling array-like data.
* `logging`: For recording information and potential issues during the script execution.

## Class: `IrisDataset`

This class provides methods to load, analyze, and visualize the Iris dataset.

### `__init__(self, path)`

Initializes the `IrisDataset` with the path to the CSV file.

### `analyze_df(self)`

Loads the Iris dataset from the specified CSV path into a pandas DataFrame. It then prints the head, information summary, column names, and unique species labels found in the dataset to the console via the logger.

### `clean_df(self)`

Removes the 'Id' and 'Species' columns from the DataFrame, isolating the features. It then prints the names of the remaining feature columns using the logger.

### `plot_sepal_width_vs_sepal_length(self)`

Generates a scatter plot showing the relationship between 'SepalWidthCm' and 'SepalLengthCm' for each of the three Iris species. Each species is represented by a different color, and a legend is included to identify them. The plot includes axis labels, a title, and a grid.

### `plot_setal_width_vs_setal_length(self)`

Creates a scatter plot illustrating the relationship between 'PetalWidthCm' and 'PetalLengthCm' for the three Iris species, using different colors for each. A legend, axis labels, a title, and a grid are added for clarity. The plot is displayed using `plt.show()`.

## Implementation (`main()` function):

The `main()` function performs the following steps:

1.  Defines the path to the `Iris.csv` file.
2.  Creates an instance of the `IrisDataset` class, passing the file path.
3.  Calls the `analyze_df()` method to load and display basic information about the dataset.
4.  Calls the `clean_df()` method to remove non-feature columns and display the features.
5.  Calls `plot_sepal_width_vs_sepal_length()` to generate and display the first scatter plot.
6.  Calls `plot_setal_width_vs_setal_length()` to generate and display the second scatter plot.

The `if __name__ == "__main__":` block ensures that the `main()` function is executed when the script is run directly.

## Task 2.1: Understanding the Iris Data Set ML problem

Based on the Iris dataset and the script:

* **What are the labels?** The labels are the different species of Iris flowers: 'Iris-setosa', 'Iris-versicolor', and 'Iris-virginica'.

* **What are the features?** The features are the measurements of the flowers: 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', and 'PetalWidthCm'.

* **How could I know use this data to create a supervised learning python program?** This data can be used for supervised learning because it contains labeled examples. Each flower has measurements (features) associated with a specific species (label). A supervised learning program could be trained on this data to learn the relationship between the features and the species, allowing it to predict the species of new, unlabeled Iris flowers based on their measurements.

* **What is / are the targets for the above scenario in one sentence?** The target for a supervised learning program using this data is to predict the Iris species based on the sepal and petal measurements.

## Task 2.2: Visualizing the Iris dataset

The script `IrisPlot.py` directly addresses Task 2.2 by loading the `Iris.csv` file and creating two scatter plots:

* **Plot 1:** Shows the relationship between sepal width and sepal length for all three Iris species, with each species plotted in a different color.
* **Plot 2:** Shows the relationship between petal width and petal length for all three Iris species, again using different colors for each species.

These plots allow for a visual understanding of how the different features vary across the three species.