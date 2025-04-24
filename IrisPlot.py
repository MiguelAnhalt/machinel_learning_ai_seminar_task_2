######################################################################
#                                                                    #
# Task 2.1: Understanding the Iris Data Set ML problem               #
# The goal is to familiarize yourself with the terminology used in ML#  
# Please review the Iris dataset and answer the following questions: #
# What are the labels?                                               #
# -- What are the features?                                          #
# -- How could I know use this data to create a supervised learning  #
# python program?                                                    #   
# -- What is / are the targets for the above scenario in one         #
# sentence?                                                          #    
# Task 2.2: Visualizing the Iris dataset                             #
# Create a python application “IrisPlot.py”. Make use of the Iris.csv# 
# file to load data and create plots to visualize the Iris dataset.  #
# Make a single plot each time that shows the data for all three     #
# species at once, in different colours.                             #
# Libraries allowed:                                                 #
# Matplotlib                                                         #
# NumPy                                                              #
# Pandas                                                             #
# The Plots:                                                         #
# Plot 1: The relationship between sepal width and length of the     #
# three classes of flowers.                                          #
# Plot 2: The relationship between petal width and length of three   #
# classes of flowers.                                                #
#                                                                    #
#                                                                    #
# Author: Miguel Angel Lopez Mejia                                   #
######################################################################

# region Libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import logging
# endregion

# Basic configuration
logging.basicConfig(level=logging.INFO)  # Sets the level to INFO and above

# Create a logger
logger = logging.getLogger(__name__)  # __name__ gives the module name

# region IrisDataset
class IrisDataset:
    """Loads and analyzes the Iris dataset.

    Attributes:
        path (str): The file path to the Iris dataset CSV file.
    """

    def __init__(self, path):
        """Initializes with the file path.

        Args:
            path (str): The path to the CSV file.
        """        
        self.path = path

    def analyze_df(self):
        """Loads the CSV into a DataFrame and prints basic info.

        Prints the head, info, columns, and unique labels of the DataFrame.
        """        

        self.df = pd.read_csv(self.path)

        logger.info(self.df.head(10))
        logger.info("--------------------------------------------------------------------------------------------")
        logger.info(self.df.info())
        logger.info("--------------------------------------------------------------------------------------------")
        logger.info(f"The dataset contains {len(self.df.columns)} columns and they are: \n {[column for column in np.array(self.df.columns) ] }")

        self.labels = self.df["Species"].unique()
        logger.info("--------------------------------------------------------------------------------------------")
        logger.info(f"The labels are:\n {self.labels}")
        logger.info("--------------------------------------------------------------------------------------------")


    def clean_df(self):
        """Removes 'Id' and 'Species' columns to get features.

        Updates the DataFrame by dropping specified columns and prints the remaining features.
        """        
        self.df_columns = self.df.drop(['Id','Species'],axis=1)
        logger.info(f"The features are:\n {np.array( self.df_columns.columns)} ")

    def plot_sepal_width_vs_sepal_length(self):
        """Plots sepal width against sepal length for each species.

        Generates a scatter plot visualizing the relationship between sepal width and length, colored by species.
        """
        plt.figure(1)
        for species in self.labels:
            subset = self.df[self.df['Species'] == species]
            plt.scatter(subset['SepalWidthCm'], subset['SepalLengthCm'],label=species)
        plt.xlabel('Sepal Width in Cm')
        plt.ylabel('Sepal Length in Cm')
        plt.legend(title='Species', loc='upper left', bbox_to_anchor= (1, 1))
        plt.title('Relation between Sepal width and length')
        plt.grid(True)
        
    def plot_setal_width_vs_setal_length(self):
        """Plots petal width against petal length for each species.

        Generates a scatter plot showing the relationship between petal width and length, differentiated by species.
        """        
        plt.figure(2)
        for species in self.labels:
            subset = self.df[self.df['Species'] == species]
            plt.scatter(subset['PetalWidthCm'], subset['PetalLengthCm'],label=species)
        plt.xlabel('Petal Width in Cm')
        plt.ylabel('Petal Length in Cm')
        plt.legend(title='Species', loc='upper left', bbox_to_anchor= (1, 1))
        plt.title('Relation between Petal width and length')
        plt.grid(True)
        plt.show()             
#endregion   

#region Implementation
def main():
    path = 'Iris.csv'
    iris_task = IrisDataset(path)

    iris_task.analyze_df()
    iris_task.clean_df()
    iris_task.plot_sepal_width_vs_sepal_length()
    iris_task.plot_setal_width_vs_setal_length()

if __name__ == "__main__":
    main()
#endregion     