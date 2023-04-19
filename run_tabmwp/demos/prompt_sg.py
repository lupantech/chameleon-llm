
prompt_choice = """
Read the following table and then answer a question:

Table:
Price | Quantity demanded | Quantity supplied
$895 | 21,000 | 3,400
$945 | 17,200 | 7,400
$995 | 13,400 | 11,400
$1,045 | 9,600 | 15,400
$1,095 | 5,800 | 19,400

Question: Look at the table. Then answer the question. At a price of $995, is there a shortage or a surplus? Please select from the following options: ['shortage', 'surplus'].

Solution: At the price of $995, the quantity demanded is greater than the quantity supplied. There is not enough of the good or service for sale at that price. So, there is a shortage. The answer is shortage.

Read the following table regarding Ferry fares and then answer a question:

Table:
Ferry | Bicycle | Car
Mukilteu-Clinton | $5 | $7
Seattle-Bremerton | $8 | $12
Ocracoke | $3 | $15
Southport-Fort Fisher | $2 | $5
Fauntleroy-Vashon | $5 | $15

Question: For an economics project, Santiago determined the cost of ferry rides for bicycles and cars. Of the ferries shown, which charges the least for a bicycle? Please select from the following options: ['Ocracoke', 'Mukilteu-Clinton', 'Fauntleroy-Vashon', 'Southport-Fort Fisher'].

Solution: Look at the numbers in the Bicycle column. Find the least number in this column.\n\nThe least number is $2.00, which is in the Southport-Fort Fisher row. The Southport-Fort Fisher ferry charges the least for a bicycle. The answer is Southport-Fort Fisher.

Read the following table and then answer a question:

Table:
toy guitar | $32.42
toy piano | $10.55
model railroad set | $65.51
toy rocket | $80.93
chess board | $15.76

Question: Cody has $49.50. Does he have enough to buy a toy guitar and a chess board? Please select from the following options: ['yes', 'no'].

Solution: Add the price of a toy guitar and the price of a chess board:\n\n$32.42 + $15.76 = $48.18\n\n$48.18 is less than $49.50. Cody does have enough money. The answer is yes.

Read the following table regarding Train schedule and then answer a question:

Table:
Location | Arrive | Depart
Richmond | 8:05 A.M. | 8:10 A.M.
Weston | 9:00 A.M. | 9:15 A.M.
Fairview | 10:15 A.M. | 10:25 A.M.
Newton | 11:15 A.M. | 11:30 A.M.
Milford | 12:35 P.M. | 12:45 P.M.
Greenpoint | 1:45 P.M. | 1:55 P.M.
Georgetown | 2:35 P.M. | 2:40 P.M.

Question: Look at the following schedule. When does the train arrive at Milford? Please select from the following options: ['12:35 P.M.', '10:15 A.M.', '2:35 P.M.', '8:05 A.M.'].

Solution: Find Milford on the schedule. Find the arrival time for Milford.\n\nMilford: 12:35 P. M. The train arrives at Milford at 12:35 P.M. The answer is 12:35 P.M.
"""


prompt_free = """
Read the following table regarding Coin collections and then answer a question:

Table:
Name | Number of coins
Shelby | 81
Oliver | 84
Jamal | 78
Vince | 81
Abby | 79
Farid | 77
Tara | 85
Krysta | 83

Question: Some friends discussed the sizes of their coin collections. What is the mean of the numbers?

Solution: Read the numbers from the table.\n\n81, 84, 78, 81, 79, 77, 85, 83\n\nFirst, count how many numbers are in the group.\n\nThere are 8 numbers.\n\nNow add all the numbers together:\n\n81 + 84 + 78 + 81 + 79 + 77 + 85 + 83 = 648\n\nNow divide the sum by the number of numbers:\n\n648 \u00f7 8 = 81\n\nThe mean is 81. The answer is 81.

Read the following table regarding Cans of food collected and then answer a question:

Table:
Name | Number of cans of food
Martin | 18
Cole | 11
Todd | 24
Jasper | 4
Alan | 22
Percy | 18
Bridget | 6

Question: Martin's class recorded how many cans of food each student collected for their canned food drive. What is the median of the numbers?

Solution: Read the numbers from the table.\n\n18, 11, 24, 4, 22, 18, 6\n\nFirst, arrange the numbers from least to greatest:\n\n4, 6, 11, 18, 18, 22, 24\n\nNow find the number in the middle.\n\n4, 6, 11, 18, 18, 22, 24\n\nThe number in the middle is 18.\n\nThe median is 18. The answer is 18.

Read the following table regarding Number of houses sold and then answer a question:

Table:
Town | Number of houses sold
Seaside | 900
Summerfield | 600
Oakdale | 550
Greenwood | 370
Fairview | 440
Other | 420

Question: A real estate agent evaluated the number of houses sold this year in each town in Washington County. What fraction of houses sold in Washington County were in Greenwood? Simplify your answer.

Solution: Find how many houses were sold in Greenwood.\n\n370\n\nFind how many houses were sold in total.\n\n900 + 600 + 550 + 370 + 440 + 420 = 3,280\n\nDivide 370 by 3,280.\n\n\\frac{370}{3,280}\n\nReduce the fraction.\n\n\\frac{370}{3,280} \u2192 \\frac{37}{328}\n\n\\frac{37}{328} of houses were sold in Greenwood. The answer is 37/328.

Read the following table regarding Bricks per building and then answer a question:

Table:
Stem | Leaf 
2 | 5, 7, 8
3 | 
4 | 
5 | 8
6 | 8
7 | 7
8 | 1, 1, 9
9 | 0

Question: The architecture student counted the number of bricks in each building in his neighborhood. How many buildings have at least 20 bricks but fewer than 70 bricks? (Unit: buildings)

Solution: Count all the leaves in the rows with stems 2, 3, 4, 5, and 6.\n\nYou counted 5 leaves, which are blue in the stem-and-leaf plot above. 5 buildings have at least 20 bricks but fewer than 70 bricks. The answer is 5.
"""