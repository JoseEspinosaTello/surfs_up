# surfs_up
## Overview
W. Avy, is looking to open surf and ice cream shops on the Oahu Island. Before making their finaly decision, the company would like a temperature analysis to determine if the weather in Oahu is beneficial towards surf and ice cream shops. W. Avy would like to compare the temperatures on the island during the months of June and December. These two months will help determine if surf and ice cream shops are sustainable year-round. For this project we have extracted weather data between 2010 - 2017 for the months of June and December from an SQLite database. We used this data to create descriptive statistic which will help our client to make their decision.

## Results

We will analyze the descriptive statistics for each month. 

June Temperatures

![june](https://github.com/JoseEspinosaTello/surfs_up/blob/main/Resources/june.png)

The average temperature over the 8-year period was about 75 degrees, wich is perfect surfing weather. The standard deviation is smaller than the average which tells us there arent many outliers in the data and the temperature is very consistent. The lowest recorder temperature was 64 degrees, in contrast the highest recorded temperature was 85%. The upper percentile sits at 73 degrees and the upper percentile sits at 77 degrees which tells us that we can expect most days to sits around 77 degress or higher. Over the June temperatures looked great and would benefit opening a surf and ice ream shop.

December Temperatures

![dec](https://github.com/JoseEspinosaTello/surfs_up/blob/main/Resources/dec.png)

The December temperature sat about a bit lower than June. The average December temperature was 71 degress which is 3 degrees lower than June. The standard deviation is once again lower than the average which tells us that we can expect the temperatures to sit close to the average range. The minimum temperature camputred was about 8 degress les than June, however the maximum temperature captured was only 2 degrees off sitting at 83 degress. The lower percentile sits at 69 degrees while the upper percentile sits at 74 degrees, telling us that we can expect most of our days in December to sit around the 71 degree average or higher.

## Summary

The temperatures in both June and Decemeber are not very different. December does have some colder days, however they average is about the same. The temperatures for both June and Decemebr are favorable to surf and ice cream shops year round, with December calling for some lower business days. However, temperatures are not the full story when it comes to the islands of Hawaii as we can expect rain year round. Tow additional queries that would benefit the final decision are descriptive statistics for precipitation.

June Precipitation

![june_prcp](https://github.com/JoseEspinosaTello/surfs_up/blob/main/Resources/june_prcp.png)

December Precipitation

![dec_prcp](https://github.com/JoseEspinosaTello/surfs_up/blob/main/Resources/dec_prcp.png)

The statistics tell us that on average Oahu Island gets mor rain during the month of December than June. The standard deviation for both months sits higher than the average this tells us that there are major outliers in the data, and we can expect that most of the data comes from single stormy days rather than a per day average. This theory is supported by our percentils as the 75 percent of our data for the month of December had a .15 inches of rain or higher and .12 for June. Our max values as December had a max of 6.42 inches of rain and June had a max of 4.43 inches of rain, combined with the upper percentiles we can once again assume that most of the rain came from single stormy days that scewed the averages. However, our averages do show that there is a small chance of light rain every day.

In conclusion that data tells us that the temperature is favorable, however, precipitation may be a concern. Overall it may not rain enough to affect the surf, but given our clients past experience with rain, he will have a tough decision to make.   

