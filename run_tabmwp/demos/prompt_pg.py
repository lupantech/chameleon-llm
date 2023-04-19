
prompt_choice ="""
Read the following table and then write Python code to answer a question:

Price | Quantity demanded | Quantity supplied
$895 | 21,000 | 3,400
$945 | 17,200 | 7,400
$995 | 13,400 | 11,400
$1,045 | 9,600 | 15,400
$1,095 | 5,800 | 19,400

Look at the table. Then answer the question. At a price of $995, is there a shortage or a surplus? Please select from the following options: ['shortage', 'surplus'].

# Python Code, return 'ans'. Make sure that 'ans' is a string selected from the options in the question
quantity_demanded_at_price_955 = 13400
quantity_supplied_at_price_955 = 11400
if quantity_demanded_at_price_955 > quantity_supplied_at_price_955:
    ans = 'shortage'
else:
    ans = 'surplus'

Read the following table regarding Ferry fares and then write Python code to answer a question:

Ferry | Bicycle | Car
Ocracoke | $3 | $15
Fauntleroy-Vashon | $5 | $15

For an economics project, Abby determined the cost of ferry rides for bicycles and cars. Which charges more for a bicycle, the Ocracoke ferry or the Fauntleroy-Vashon ferry? Please select from the following options: ['Ocracoke', 'Fauntleroy-Vashon'].

# Python Code, return 'ans'. Make sure that 'ans' is a string selected from the options in the question
bicycle_cost_ocracoke = 3
bicycle_cost_fauntleroy_vashon = 5
if bicycle_cost_ocracoke > bicycle_cost_fauntleroy_vashon:
    ans = 'Ocracoke'
else:
    ans = 'Fauntleroy-Vashon'
    
Read the following table and then write Python code to answer a question:

toy guitar | $32.42
toy piano | $10.55
model railroad set | $65.51
toy rocket | $80.93
chess board | $15.76

Cody has $49.50. Does he have enough to buy a toy guitar and a chess board? Please select from the following options: ['yes', 'no'].

# Python Code, return 'ans'. Make sure that 'ans' is a string selected from the options in the question
toy_guitar_price = 32.42
chess_board_price = 15.76
total_money = 49.50
if total_money > toy_guitar_price + chess_board_price:
    ans = 'yes'
else:
    ans = 'no'

Read the following table regarding Train schedule and then write Python code to answer a question:

Location | Arrive | Depart
Richmond | 8:05 A.M. | 8:10 A.M.
Weston | 9:00 A.M. | 9:15 A.M.
Fairview | 10:15 A.M. | 10:25 A.M.
Newton | 11:15 A.M. | 11:30 A.M.
Milford | 12:35 P.M. | 12:45 P.M.
Greenpoint | 1:45 P.M. | 1:55 P.M.
Georgetown | 2:35 P.M. | 2:40 P.M.

Look at the following schedule. When does the train arrive at Milford? Please select from the following options: ['12:35 P.M.', '10:15 A.M.', '2:35 P.M.', '8:05 A.M.'].

# Python Code, return 'ans'. Make sure that 'ans' is a string selected from the options in the question
schedule = {
   'Richmond': '8:05 A.M.',
   'Weston': '9:00 A.M.',
   'Fairview': '10:15 A.M.',
   'Newton': '11:15 A.M.',
   'Milford': '12:35 P.M.',
   'Greenpoint': '1:45 P.M.',
   'Georgetown': '2:35 P.M.'
}
ans = schedule['Milford']
"""

prompt_free ="""
Read the following table regarding Coin collections and then write Python code to answer a question:

Name | Number of coins
Shelby | 81
Oliver | 84
Jamal | 78
Vince | 81
Abby | 79
Farid | 77
Tara | 85
Krysta | 83

Some friends discussed the sizes of their coin collections. What is the mean of the numbers?

# Python Code, return 'ans'. Make sure that 'ans' is a number
number_of_coins_for_different_person = [81, 84, 78, 81, 79, 77, 85, 83]
ans = sum(number_of_coins_for_different_person) / len(number_of_coins_for_different_person)

Read the following table regarding Cans of food collected and then write Python code to answer a question:

Name | Number of cans of food
Martin | 18
Cole | 11
Todd | 24
Jasper | 4
Alan | 22
Percy | 18
Bridget | 6

Martin's class recorded how many cans of food each student collected for their canned food drive. What is the median of the numbers?

# Python Code, return 'ans'. Make sure that 'ans' is a number
cans = [18, 11, 24, 4, 22, 18, 6]
cans = sorted(cans)
middle1 = (len(cans) - 1) // 2
middle2 = len(cans) // 2
ans = (cans[middle1] + cans[middle2]) / 2

Read the following table regarding Number of houses sold and then write Python code to answer a question:

Town | Number of houses sold
Seaside | 900
Summerfield | 600
Oakdale | 550
Greenwood | 370
Fairview | 440
Other | 420

A real estate agent evaluated the number of houses sold this year in each town in Washington County. What fraction of houses sold in Washington County were in Greenwood? Simplify your answer.

# Python Code, return 'ans'. Make sure that 'ans' is a number
houses_sold = [900, 600, 550, 370, 440, 420]
houses_sold_in_Stamford = houses_sold[3]
total_houses_sold = sum(houses_sold)
ans = houses_sold_in_Stamford / total_houses_sold

Read the following table regarding Bricks per building and then write Python code to answer a question:

Stem | Leaf 
2 | 5, 7, 8
3 | 
4 | 
5 | 8
6 | 8
7 | 7
8 | 1, 1, 9
9 | 0

The architecture student counted the number of bricks in each building in his neighborhood. How many buildings have at least 20 bricks but fewer than 70 bricks? (Unit: buildings)

# Python Code, return 'ans'. Make sure that 'ans' is a number
stem_leaf = {2: [5, 7, 8], 3: [], 4: [], 5: [8], 6: [8], 7: [7], 8: [1, 1, 9], 9: [0]}
ans = 0
for stem in stem_leaf.keys():
    for leaf in stem_leaf[stem]:
        if 20 <= stem * 10 + leaf <= 70:
            ans += 1
"""



