
prompt = """
Read the following question and table. Write a textual description of the table. The description should keep the critical information in the table for answering the question. The description should not answer the question.

Question: In preparation for graduation, some teachers and students volunteered for the various graduation committees. How many people are on the music committee?

Table:
Committee | Students | Teachers
Program | 5 | 17
Ticket | 20 | 5
Music | 20 | 15
Schedule | 15 | 20
Food | 18 | 2

Table description: The table shows the number of students and teachers on each of the four graduation committees: Program, Ticket, Music, and Schedule. The Music committee has 20 students and 15 teachers.

Question: Omar has two dogs, Sprinkles and Champ. He is concerned because Sprinkles keeps eating Champ's food. Omar asks their vet how much each dog's weight has changed since their last visit. Which dog's weight has changed the most?

Table:
Dog | Weight change (oz.)
Sprinkles | 5
Champ | -6

Table description: The table shows the weight change of two dogs, Sprinkles and Champ, since their last visit to the vet. Sprinkles' weight has increased by 5 ounces, while Champ's weight has decreased by 6 ounces.

Question: The architecture student counted the number of bricks in each building in his neighborhood. How many buildings have at least 20 bricks but fewer than 70 bricks?

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

Table description: The table shows the number of bricks in the architecture student's neighborhood in each building. The numbers of bricks are 25, 27, 28, 58, 68, 77, 81, 81, 89, and 90.

Question: Alana, an employee at Hong's Convenience Store, looked at the sales of each of its soda products. Which beverage had lower sales on Thursday, Krazy Kola or Fizzy Fun?

Table:
Beverage | Thursday | Friday
Kickin' Coffee | $9 | $18
Brenner's Juices | $5 | $8
Krazy Kola | $13 | $14
Olde Tyme Cola | $17 | $9
Fizzy Fun | $12 | $19

Table description: The table shows the sales of five beverages at Hong's Convenience Store on Thursday and Friday. Krazy Kola had sales of $13 on Thursday, while Fizzy Fun had sales of $12 on Thursday.

Question: Look at the following schedule. Lee just missed the 1.00 P.M. train at Snowy Mountain. What time is the next train?

Table:
Snowy Mountain | 2:30 A.M. | 4:30 A.M. | 1:00 P.M. | 4:00 P.M. | 12:00 A.M.
Comfy Pillows Resort | 3:15 A.M. | 5:15 A.M. | 1:45 P.M. | 4:45 P.M. | 12:45 A.M.
Magician Village | 3:45 A.M. | 5:45 A.M. | 2:15 P.M. | 5:15 P.M. | 1:15 A.M.
Floral Gardens | 4:30 A.M. | 6:30 A.M. | 3:00 P.M. | 6:00 P.M. | 2:00 A.M.

Table description:  The table shows the train schedule from Snowy Mountain to four other destinations: Comfy Pillows Resort, Magician Village, Floral Gardens, and back to Snowy Mountain. The trains depart from Snowy Mountain at 2:30 A.M., 4:30 A.M., 1:00 P.M., 4:00 P.M., and 12:00 A.M.

Question: A researcher recorded the number of cows on each farm in the county. How many farms have at least 4 cows but fewer than 46 cows?

Table:
Stem | Leaf 
0 | 1, 4, 7
1 | 2, 4, 5
2 | 0, 3
4 | 0, 1, 5, 8, 9

Table description: The table shows the number of cows on each farm in the county. The numbers of cows are 1, 4, 7, 12, 14, 15, 20, 23, 40, 41, 45, 48, and 49.

Question: A dietitian noted the number of apples eaten by his clients last week. How many clients ate more than 1 apple last week?

Table:
Apples eaten | Frequency
2 | 12
3 | 4

Table description: The table shows the number of apples eaten by the dietitian's clients last week. There were 12 clients who ate 2 apples and 4 clients who ate 3 apples.

Read the following question and table. Write a textual description of the table. The description should keep the critical information in the table for answering the question. The description should not answer the question.
"""