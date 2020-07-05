# PyBer Analysis Report

## Background and Results

### Purpose
The purpose of this analysis is to create a dataframe summarizes the key metrics for the ride-sharing data by city type and show the sum of the fares for each week.

## *Resources*

  * Data Source:
     * city_data.csv
     * ride_data.csv
  
  * Software: Python 3.7.6, Anaconda 4.8.3, Jupyter Notebook 6.0.3
  
### Technical Analysis

#### Technical Analysis 1:
* Create the summary DataFrame, following these steps:
  * From the merged DataFrame get the total rides, total drivers, and total fares for each city type using the groupby() function on the city type.
  * Calculate the average fare per ride and the average fare per driver for each city type.

* To format the summary DataFrame, follow these steps:
  * Delete the index name.
  * Create the summary DataFrame with the appropriate columns, and apply formatting where appropriate.
 
#### Technical Analysis 2:
1. Rename columns {'city':'City', 'date':'Date','fare':'Fare', 'ride_id': 'Ride Id','driver_count': 'No. Drivers', 'type':'City Type'}.
2. Set the index to the Date column.
3. Create a new DataFrame, for fares, and include only the City Type and Fare columns using the copy() method on the merged DataFrame.
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
![Pyber Summary Table](https://github.com/soijebor/PyBer_Analysis/blob/master/Images/pyber_summary_data_df.png)
The chart shows the relationship between each city type and fare between January to April 2019 weekly.
![Multiple line chart of the dataframe](https://github.com/soijebor/PyBer_Analysis/blob/master/Images/multiple_line_chart_df.png)

### Summary
In conclusion, from both technical analysis we can see that the urabn cities have the highest fare prices and the rural citites have the lowest fare prices betweeen January to April 2019

## Challenges Encountered and Overcome

### Challenges and Difficulties Encountered
The challenge i encountered and overcame was finding the total drivers and i overcame it by using the original city data instead of the merged dataset as the merged dataset is counting the driver count multiple times due to the 2 different datasets

### Technical Analyses Used
![Technical analysis used](https://github.com/soijebor/PyBer_Analysis/blob/master/Images/difficulties_technical_analysis.png)

## Recommendations and Next Steps

### Recommendations for Future Analysis

### Additional Analysis 1

* Description of Approach

* Technical Steps

### Additional Analysis 2

* Description of Approach

* Technical Steps
