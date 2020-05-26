Extract:
    Originally i was attempting to find data on UFO sightings but it was formatted weird and I couldnt pull any of the indexes. So i decided to change my subject and go into Video Game sales and trends. The files i extracted from Kaggle and Data.World were in the form of CSV files and a zip file i had to convert. The Data sets that i gathered were formated similarly providing easy access to the keys and indexes.

Transform: 
    Most of the data was formatted correctly but i was having trouble with the Year of Release on the 2nd data set because the coloumns astype was float instead of integer. When i tried to convert the astype using the pandas code it gave me an error due to NaN or inf values. With the help of Greg, we were able to figure out what values were appearing at NaN or inf. I left out alot of the coloumns having to do with rating for indavidual games as well as split an index Number of Owners, into Min Owners and Max Owners.

Load:
Loading was simple and straight forward. I created a new database in my PGadmin4 and was able to successfully upload all t