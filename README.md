# DELACRUZ_2ECE-B_ECE2112_PA3

# **Programming Assignment 3**  
---  
## **Python Data Analysis using Pandas**

This assignment uses the `pandas` library in Python to load, explore, and extract specific data from a CSV file containing information about different car models. All code was written and tested in a Jupyter Notebook and later converted to a `.py` script for submission.

---

## **Problem 1**

### **a) Load the dataset**
Start by importing pandas and loading the CSV file into a DataFrame called `cars`.

import pandas as pd
car_data = pd.read_csv("cars.csv")
car_data

### **b) View the first and last five rows**
To get a quick look at both the beginning and end of the dataset, combine the first 5 and last 5 rows into one display.

print("Here are the first and last 5 rows:")
sample_rows = pd.concat([car_data.iloc[:5], car_data.iloc[-5:]])
sample_rows

### **c) Convert notebook to a Python script**
Once finished, the notebook is converted into a Python script using the following command:
!jupyter nbconvert --to script "DelaCruz_PA3_P1.ipynb"

## **Problem 2**
This problem continues using the cars dataset from Problem 1.

import pandas as pd
cars = pd.read_csv('cars.csv')
cars

### **a) Show the first 5 rows using only odd-numbered columns**
Here, we select only the columns in odd-numbered positions (starting from index 0) and then display the first 5 rows from those columns.

odd_columns = cars.iloc[:, ::2]
top_odd_columns = odd_columns.head()
odd_columns
top_odd_columns

### **b) Locate the row where the model is ‘Mazda RX4’**
To pull up the entire row for a specific car model:

cars.loc[cars['Model'] == 'Mazda RX4']

### **c) Find the number of cylinders for ‘Camaro Z28’**
We access the 'cyl' column specifically for the Camaro Z28 and print out the result.

cmro_cyl = cars.loc[cars['Model'] == 'Camaro Z28', 'cyl'].values[0]
print("Camaro Z28 has", cmro_cyl, "cylinders")

### **d) Show the gear and cylinder info for 3 specific car models**
We filter out only the necessary columns (Model, cyl, gear) for the cars: Mazda RX4 Wag, Ford Pantera L, and Honda Civic.

Mzda = cars.loc[cars["Model"] == 'Mazda RX4 Wag', ['Model', 'cyl', 'gear']]
Frd = cars.loc[cars["Model"] == 'Ford Pantera L', ['Model', 'cyl', 'gear']]
Hnda = cars.loc[cars["Model"] == 'Honda Civic', ['Model', 'cyl', 'gear']]

print("Here’s the number of gears and cylinders for these cars:")
pd.concat([Mzda, Frd, Hnda])

### **e) Convert this second notebook into a Python script**
After completing the notebook, it's also converted into a .py script:
!jupyter nbconvert --to script "DelaCruz_PA3_P2.ipynb"
