## Week 4 Exercise with Numpy
Use only numpy in these exercises

Exercise 1
Open the file './befkbhalderstatkode.csv'
Turn the csv file into a numpy ndarray with np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)
Using this data:
neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave', 
       5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst', 
       10: 'Amager Vest', 99: 'Udenfor'}
Find out how many people lived in each of the 11 areas in 2015
Make a bar plot to show the size of each city area from the smallest to the largest
Create a boolean mask to find out how many people above 65 years lived in Copenhagen in 2015
How many of those were from the other nordic countries (not dk)
Make a line plot showing the changes of number of people in vesterbro and østerbro from 1992 to 2015