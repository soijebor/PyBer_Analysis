# PyBer Analysis Report

## Background and Results

### Purpose
The purpose of this analysis is to create a dataframe summarizes the key metrics for the ride-sharing data by city type.
### Technical Analysis
I analyzed the data by merging the two datasets given and then i got the total ride, total drivers, total fares by using the groupby() function. And then i calculated the average fare per ride and the average fare per driver for each city type. After which i created a summary dataframe and formatted it appropriately
### Results
This table below shows the summary of the key metricswhich are the toral rides, total drivers, total fares, average fare per ride and average fare per driver for the ride-sharing data by city type 
![Pyber Summary Table](https://github.com/soijebor/PyBer_Analysis/blob/master/Images/pyber_summary_data_df.png)
This chart shows the relationship between each city type and fare between January to April 2019 weekly
![Multiple line chart of the dataframe](https://github.com/soijebor/PyBer_Analysis/blob/master/Images/multiple_line_chart_df.png)
### Summary
In conclusion, from both technical analysis we can see that the urabn cities have the highest fare prices and the rural citites have the lowest fare prices betweeen January to April 2019
## Challenges Encountered and Overcome
The challenge i encountered and overcame was finding the total drivers and i overcame it by using the original city data instead of the merged dataset as the merged dataset is counting the driver count multiple times due to the 2 different datasets
### Challenges and Difficulties Encountered
