# Python-challenge

#PyBank

##Task

Your task is to create a Python script that analyzes the records to calculate each of the following values:

The total number of months included in the dataset
The net total amount of "Profit/Losses" over the entire period
The changes in "Profit/Losses" over the entire period, and then the average of those changes
The greatest increase in profits (date and amount) over the entire period
The greatest decrease in profits (date and amount) over the entire period

##Description

I started the challenge by first determining what each individual task was asking. The first task requesting a return of the total months in the dataset. I used the += operator running through the rows and adding two values together and assigning the final value to a variable. I used the same operator for the next task to determine the net total amount of profit and losses which could be interpreted as income. This time I specified to read the rows as integers to get the correct total amount. To determine the changes in income over the entire period, and then the average of those changes, I first broke the task into two steps; determining the "changes" over the entire period and then the average of those changes. When thinking about change I determined the best way to figure that out would be by subtracting the "Profit/Losses" values over the entire period to get the changes. Then to determine the average of those changes we would have to caculate the sum of the changes and divide it by the total amount of changes. To accomplish this I created blank list to store where the changes would be stored and used that list to determine the average. After determining the average, I rounded to two decimal points to align with the output provided in the challenge instructions. The next part of the challenge asked for the greatest incease in profits both date and amount. You were also asked to determine the greatest decrease in profits. Using the max and min built-in functions to find the smallest and the largest elements in any iterable. I passed over the list I created for total changes to determine these values. Then later in my print statement, using an f-string, I used the index function indexing the list for total changes to the months list that I created earlier to retun the greatest increase and decrease in profits with their corresponding month. Then using f-strings, I printed the financial analysis to the terminal as well as wrote the financial analysis to export as a text file to the correct path. 

##Citations

https://stackoverflow.com/questions/13517080/sum-a-csv-column-in-python - Line 32 of main.py code Pybank
https://stackoverflow.com/questions/59493593/loop-over-csv-rows-and-subtract-current-row-from-previous-row-using-python - Line 42 of main.py code Pybank
https://www.w3schools.com/python/ref_list_index.asp - Reference for indexing a list
https://www.pythontutorial.net/python-basics/python-write-text-file/ - Used this article to learn how to write on the next line when writing the output of a code as a text file
