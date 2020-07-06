# PyBer Analysis Report

## Challenge Overview
The C.E.O. of PyBer ride sharing has given me the following tasks to :

 * Technical Analysis Deliverable 1:Create a DataFrame that summarizes the key metrics for the ride-sharing data by city type.
 * Technical Analysis Deliverable 2: Create a multiple-line chart, with one line for each city type, that shows the sum of the fares for each week.
 * Delivering Results: A written report of your results, saved in a README.md document on your GitHub repository

## *Resources*

  * Data Source:
     * city_data.csv
     * ride_data.csv
  
  * Software: Python 3.7.6, Anaconda 4.8.3, Jupyter Notebook 6.0.3

## Background and Results

### Purpose
The purpose of this analysis is to create a dataframe summarizes the key metrics for the ride-sharing data by city type and toplot the sum of the fares for each city type that will show the relationship between each city type and total fare for each week.


### Technical Analysis

#### Technical Analysis 1:
* Create the summary DataFrame, following these steps:
  * From the merged DataFrame get the total rides, total drivers, and total fares for each city type using the groupby() function on the city type.
  * Calculate the average fare per ride and the average fare per driver for each city type.

* To format the summary DataFrame, follow these steps:
  * Delete the index name.
  * Create the summary DataFrame with the appropriate columns, and apply formatting where appropriate.
 
#### Technical Analysis 2:
1. Rename columns 
2. Set the index to the Date column.
3. Create a  DataFrame, for fares, and include only the City Type and Fare columns using the copy() method on the merged DataFrame.
4. Set the index to the datetime data type.
    * Check to make sure the index is a datetime data type by using the info() method on the DataFrame.
5. Calculate the sum() of fares by the type of city and date using groupby() to create a Series.
6. Convert the groupby Series into a DataFrame.
7. Reset the index, then create a pivot table DataFrame with the Date as the index and columns = 'City Type'. The Fare for each Date should appear in each row.
8. Create a new DataFrame from the pivot table DataFrame on the given dates, '2019-01-01':'2019-04-28', using loc.
9. Create a new DataFrame by setting the DataFrame you created in Step 8 with resample() in weekly bins, and calculate the sum() of the fares for each week in the resampled data.
10. Using the object-oriented interface method, plot the DataFrame you created in Step 9 using the df.plot() function.
### Results

The table below shows the summary of the key metrics which are the toral rides, total drivers, total fares, average fare per ride and average fare per driver for the ride-sharing data by city type.
![Pyber Summary Table](https://github.com/soijebor/PyBer_Analysis/blob/master/Analysis/pyber_summary_data.png)
The chart shows the relationship between each city type and fare between January to April 2019 weekly.
![Multiple line chart of the dataframe](https://github.com/soijebor/PyBer_Analysis/blob/master/Analysis/Fig8.png)

### Summary
In conclusion, from both technical analysis we can see that the urabn cities have the highest fare prices and the rural citites have the lowest fare prices betweeen January to April 2019

## Challenges Encountered and Overcome

### Challenges and Difficulties Encountered
The challenge i encountered was finding the total drivers and i overcame it by realizing the city data contains the number of drivers for each city type, when you merge this data with the ride data it will add up the driver count based on rides. So, the merged data has a driver count based on city and rides. In this case i used the city data dataframe to get the total drivers.

### Technical Analyses Used
 From the city data DataFrame i got the total drivers for each city type using the groupby() function on the city type and sum() function.
 
## Recommendations and Next Steps

### Recommendations for Future Analysis
My recommendation is to find the
### Additional Analysis 1

* Description of Approach
  * Show the trend between No. drivers by city type weekly
* Technical Steps
1. Create a  DataFrame, for No. Drivers, and include only the City Type and No. Drivers columns using the copy() method on the merged DataFrame.
2. Set the index to the datetime data type.
    * Check to make sure the index is a datetime data type by using the info() method on the DataFrame.
3. Calculate the sum() of No. Drivers by the type of city and date using groupby() to create a Series.
4. Convert the groupby Series into a DataFrame.
5. Reset the index, then create a pivot table DataFrame with the Date as the index and columns = 'City Type'. The Fare for each Date should appear in each row.
6. Create a new DataFrame from the pivot table DataFrame on the given dates, '2019-01-01':'2019-04-28', using loc.
7. Create a new DataFrame by setting the DataFrame you created in Step 6 with resample() in weekly bins, and calculate the sum() of the No. Drivers for each week in the resampled data.
8. Using the object-oriented interface method, plot the DataFrame you created in Step 7 using the df.plot() function.

### Additional Analysis 2

* Description of Approach
  * Build percentage of rides by city type pie chart
* Technical Steps
1. Get the percentage of rides by city type using groupby() and sum() function from the mrged dataframe from the analysis performed in the challenge
2.Using the object-oriented interface method, plot the percentage of rides by city type pie chart using plt.subplot 
