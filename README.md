# Python-challenge

# PyBank

## Task

In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will be given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".

Your task is to create a Python script that analyzes the records to calculate each of the following values:

The total number of months included in the dataset

The net total amount of "Profit/Losses" over the entire period

The changes in "Profit/Losses" over the entire period, and then the average of those changes

The greatest increase in profits (date and amount) over the entire period

The greatest decrease in profits (date and amount) over the entire period

## Description

I started the challenge by first determining what each individual task was asking. The first task requesting a return of the total months in the dataset. I set a variable as an integer of zero to store the returned value for total months. Then I used the += operator running through the rows and adding two values together and assigning the final value to a variable. I used the same operator for the next task to determine the net total amount of profit and losses which could be interpreted as income. This time I specified to read the rows as integers to get the correct total amount again, setting a variable to store the data. To determine the changes in income over the entire period, and then the average of those changes, I first broke the task into two steps; determining the "changes" over the entire period and then the average of those changes. When thinking about change, I determined the best way to figure that out would be by subtracting the "Profit/Losses" values over the entire period to get the changes. Then to determine the average of those changes we would have to caculate the sum of the changes and divide it by the total amount of changes. To accomplish this I created blank list to store where the changes would be stored and used that list to determine the average. After determining the average, I rounded to two decimal points to align with the output provided in the challenge instructions. The next part of the challenge asked for the greatest incease in profits both date and amount. You were also asked to determine the greatest decrease in profits. Using the max and min built-in functions to find the smallest and the largest elements in any iterable, I passed over the list I created for total changes to determine these values. Then later in my print statement, using an f-string, and using the index function, I indexed the list for total changes to the months list that I created earlier to return again, using max and min to show the greatest increase and decrease in profits with their corresponding month. Then using f-strings, I printed the financial analysis to the terminal as well as wrote the financial analysis to export as a text file to the correct path.

## References

https://www.w3schools.com/python/ref_list_index.asp 

Reference for indexing a list

https://favtutor.com/blogs/min-max-python 

Reference for max and min functions

https://www.pythontutorial.net/python-basics/python-write-text-file/ 

Referenced to learn how to write on the next line when writing the output of a code as a text file

## Citations

https://stackoverflow.com/questions/13517080/sum-a-csv-column-in-python - Line 32 of main.py code Pybank
https://stackoverflow.com/questions/59493593/loop-over-csv-rows-and-subtract-current-row-from-previous-row-using-python - Line 42 of main.py code Pybank


# Pypoll

## Task
In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process. You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate".

Your task is to create a Python script that analyzes the votes and calculates each of the following values:

The total number of votes cast

A complete list of candidates who received votes

The percentage of votes each candidate won

The total number of votes each candidate won

The winner of the election based on popular vote

## Description

I began this part of the challenge as the last, determined what each individual task was asking. The first task requesting a return of the total votes cast in the dataset. I used the += operator from the first part of Pybank challenge to determine this part as well. For getting the complete list of candiates who received votes, I first accounted for all the candidates in the dataset. After getting all the candidates, using the not in operator, I was able to account for each candidates that received votes. I drew back from a tutoring session I had for a previous challenge where my tutor mentioned that it's a good idea to try and use your code where ever you can for other parts of your problem or task. The previous challenge was requesting to account for the "ticker" in the dataset. My tutor mentioned by setting a variable to 0, and to start counting the value for each of the rows. While adding each candidate who received votes to the new list, I was also accounting for how many votes they earned. I had issues with my print statements I believe due to my indentations so, whenever I completed a task in the challenge I would write my print statement to get the proper output at the end. I would do the same for writing to the text file. To determine the total number of votes each candiate won, I created a blank dictionary and associated the key being the candiates and the value being the votes for each of the candidates. To determine the percentage of the vote each candidate earned I took the total number of votes for each candidate, divided by the total amount of votes as float values and multiplied by 100. Using an f-string I both printed and wrote the list of candidates, the percentage earned for each candidate and the total number of votes earned for each candidate. To determine the winner of the election based on popular vote, I used the votes for each candidate and created a blank variable for the winner's winning count. Using a greater than (>) as a conditional, I could determine who got the most votes get the winner from the candidates list. I then printed the winner to the terminal and wrote the winner to the text file using f-string.

## References

https://www.askpython.com/python/examples/in-and-not-in-operators-in-python - Reference on in and not in operators

https://bobbyhadz.com/blog/python-append-value-to-list-if-not-present - Reference on how to append multiple values to a List if not present

https://thepythonguru.com/python-string-formatting/#:~:text=2f%20are%20called%20as%20format,the%20tuple%20i.e%2012%20and%20%25. - Reference on how to print percentage to three decimal places ":.3F" known as a format specifier.
