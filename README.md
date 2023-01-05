# expenses_checker
This is a very simple python project that let you go through your expenses, put them in buckets, and the show you how much you expended in each bucketi

You can run in this simple way:
  python3 expenses_checker.py

You need a file called "data.csv" with all your expenses.
Each field should be divided by the delimeter ","
One expense per line
The first row should have the headers

When run it will ask for which one is the Memo field and which one is the Amount field
For example:

Write which field is the Memo?
dict_keys(['Number', 'Date', 'Account', 'Amount', 'Subcategory', 'Memo'])
Memo
Write which field is the Amount?
dict_keys(['Number', 'Date', 'Account', 'Amount', 'Subcategory', 'Memo'])
Amount

If a trasaction without any bucket association is found (extremely common the first time you run it), the program asks for indications.
For example

This type of memo couldn't be found = 
transact 22209536    GERMANY	ON 25 SEP ATM	
What bucket should it belong to?
['0 FOOD', '1 MAKESPACE', '2 DANCING', '3 DRINKS', '4 TRAVEL', '5 MUM PENSION', '6 INVESTMENTS', '7 RENT', '8 DELIVERY FOOD', '9 UNKNOWN', '10 GOING OUT', '11 VIRGIN', '12 CLOTHES', '13 SALARY', '14 PATREON', '15 MEDICINES']
Input the index of the bucket you want to use: 10
You choose 10 GOING OUT are you sure? (y/n) y
What text should be associated to this memo? transact 22209536    GERMANY	ON 25 SEP ATM


The buskets available are 

['0 FOOD', '1 MAKESPACE', '2 DANCING', '3 DRINKS', '4 TRAVEL', '5 MUM PENSION', '6 INVESTMENTS', '7 RENT', '8 DELIVERY FOOD', '9 UNKNOWN', '10 GOING OUT', '11 VIRGIN', '12 CLOTHES', '13 SALARY', '14 PATREON', '15 MEDICINES']


Which you can change from code

Enjoy!

