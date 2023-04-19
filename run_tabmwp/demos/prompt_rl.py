
prompt = """
Read the following question and table. Each row is separated by a newline ('\n') and each column is separated by a vertical bar ('|'). Return the simplified table that only remains the rows that are relevant to the question. If all rows are relevant, or the number of rows are fewer than three, return the original table.

Question: In preparation for graduation, some teachers and students volunteered for the various graduation committees. How many people are on the music committee?

Table:
Committee | Students | Teachers
Program | 5 | 17
Ticket | 20 | 5
Music | 20 | 15
Schedule | 15 | 20
Food | 18 | 2

Simplified Table:
Committee | Students | Teachers
Music | 20 | 15

Question: Look at the table. Then answer the question. At a price of $620, is there a shortage or a surplus?

Table:
Price | Quantity demanded | Quantity supplied
$590 | 18,400 | 1,400
$620 | 18,000 | 5,900
$650 | 17,600 | 10,400
$680 | 17,200 | 14,900
$710 | 16,800 | 19,400

Simplified Table:
Price | Quantity demanded | Quantity supplied
$620 | 18,000 | 5,900

Question: Look at the following schedule. Amy is at Oakland. If she wants to arrive at Danville at 3.15 P.M., what time should she get on the train?

Table:
Bloomington | 6:30 A.M. | 6:45 A.M. | 8:45 A.M. | 10:30 A.M. | 11:00 A.M.
Oakland | 7:45 A.M. | 8:00 A.M. | 10:00 A.M. | 11:45 A.M. | 12:15 P.M.
Yardley | 9:45 A.M. | 10:00 A.M. | 12:00 P.M. | 1:45 P.M. | 2:15 P.M.
Middletown | 10:15 A.M. | 10:30 A.M. | 12:30 P.M. | 2:15 P.M. | 2:45 P.M.
Danville | 11:15 A.M. | 11:30 A.M. | 1:30 P.M. | 3:15 P.M. | 3:45 P.M.
Castroville | 12:00 P.M. | 12:15 P.M. | 2:15 P.M. | 4:00 P.M. | 4:30 P.M.
Manchester | 1:30 P.M. | 1:45 P.M. | 3:45 P.M. | 5:30 P.M. | 6:00 P.M.

Simplified Table:
Oakland | 7:45 A.M. | 8:00 A.M. | 10:00 A.M. | 11:45 A.M. | 12:15 P.M.
Danville | 11:15 A.M. | 11:30 A.M. | 1:30 P.M. | 3:15 P.M. | 3:45 P.M.

Question: The movie critic liked to count the number of actors in each movie she saw. How many movies had at least 21 actors but fewer than 75 actors?

Table:
Stem | Leaf
1 | 5, 7, 7
2 | 0, 7, 9
3 | 0, 3
4 | 
5 | 2, 4
6 | 2, 3, 5, 6, 8
7 | 4, 6
8 | 2, 4, 8, 9, 9

Simplified Table:
Stem | Leaf
2 | 0, 7, 9
3 | 0, 3
5 | 2, 4
6 | 2, 3, 5, 6, 8
7 | 4, 6

Question: At a candy factory, butterscotch candies were packaged into bags of different sizes. How many bags had exactly 16 butterscotch candies?

Table: 
Stem | Leaf 
1 | 2, 4, 6, 7
2 | 2, 3
3 | 3, 8
4 | 1, 2, 3, 8
5 | 2, 6, 9
6 | 2, 4, 7

Simplified Table:
Stem | Leaf 
1 | 2, 4, 6, 7

Question: What is the total cost for 3 pounds of oysters, 4 pounds of mussels, and 3 pounds of shrimp?

Table: 
crab meat | $5 per lb
lobster meat | $12 per lb
shrimp | $4 per lb
oysters | $5 per lb
mussels | $5 per lb

Simplified Table:
shrimp | $4 per lb
oysters | $5 per lb
mussels | $5 per lb

Question: Manuel counted the number of silver beads on each bracelet at Sparrowtown Jewelry, the store where he works. What is the smallest number of silver beads?

Table: 
Stem | Leaf 
2 | 0, 2, 4, 7
3 | 1, 3
4 | 3
5 | 3, 4, 7, 9
6 | 0, 1, 2, 2, 6, 7, 7, 8
7 | 0, 3, 4, 6, 7, 9

Simplified Table:
Stem | Leaf 
2 | 0, 2, 4, 7


Read the following question and table. Each row is separated by a newline ('\n') and each column is separated by a vertical bar ('|'). Return the simplified table that only remains the rows that are relevant to the question. If all rows are relevant, or the number of rows are fewer than three, return the original table.
"""