import pandas as pd

'''
Part 1 - Importing the data

This just includes a a tool that
is a good habit to include. It catches
exceptions (errors) safely rather than having
the code exit abruptly. 

It is not necessary to do this in your answer.
The following is sufficient:
    data = pd.read_csv("PROJECT6.csv")
'''

f = 'PROJECT6.csv'
with open(f, "r") as file:
    try:
        df = pd.read_csv(f) # sets the data to variable name "df"
    except Exception as err:
        print(err)
        exit()

# Part 2 - Getting the average age
mean = df['Age'].mean() # gets the mean of the column named "Age"
rounded = round(mean, 2)
print("The average age of the passengers is ", rounded)

# Part 3 - Cabins
cabins = df.dropna(subset=['Name', 'Cabin']) # drops all missing values for columns: "Name" and "Cabin"

# Part 4 - Exporting to .csv file
df.to_csv('CABINS_P6.csv')

