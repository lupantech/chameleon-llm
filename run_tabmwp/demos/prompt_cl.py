
prompt = """
Read the following question and table. Each row is separated by a newline ('\n') and each column is separated by a vertical bar ('|'). Return the simplified table that only remains the columns that are relevant to the question. If all columns are relevant, return the original table.

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
Program | 5 | 17
Ticket | 20 | 5
Music | 20 | 15
Schedule | 15 | 20
Food | 18 | 2

Question: Look at the following schedule. When does Recess end?

Table:
Subject | Begin | End
Recess | 6:15 A.M. | 7:20 A.M.
Orchestra | 7:30 A.M. | 8:40 A.M.
Art | 8:45 A.M. | 9:35 A.M.
Handwriting | 9:45 A.M. | 10:20 A.M.
Gym | 10:30 A.M. | 11:15 A.M.
Choir | 11:20 A.M. | 12:25 P.M.
Science | 12:35 P.M. | 1:35 P.M.
Reading | 1:40 P.M. | 2:50 P.M.

Simplified Table:
Subject | End
Recess | 7:20 A.M.
Orchestra | 8:40 A.M.
Art | 9:35 A.M.
Handwriting | 10:20 A.M.
Gym | 11:15 A.M.
Choir | 12:25 P.M.
Science | 1:35 P.M.
Reading | 2:50 P.M.

Question: Derek's Candies has been studying how much chocolate people have been eating in different countries. Which country consumed the least chocolate per capita in 2002?

Table:
Country | 2002 | 2005
Denmark | 9 | 8
Australia | 4 | 5
Sweden | 8 | 7
Belgium | 8 | 11

Simplified Table:
Country | 2002
Denmark | 9
Australia | 4
Sweden | 8
Belgium | 8

Question: Look at the following schedule. Amy is at Oakland. If she wants to arrive at Danville at 3.15 P.M., what time should she get on the train?

Table:
Oakland | 7:45 A.M. | 8:00 A.M. | 10:00 A.M. | 11:45 A.M. | 12:15 P.M.
Danville | 11:15 A.M. | 11:30 A.M. | 1:30 P.M. | 3:15 P.M. | 3:45 P.M.

Simplified Table:
Oakland | 11:45 A.M.
Danville | 3:15 P.M.

Question: Sixth graders at Campbell Middle School are taught in classes of various sizes. How many more students are in Mr. East's class than Mr. Center's class?

Table:
Teacher | Girls | Boys
Mr. Center | 16 | 10
Miss West | 17 | 20
Mrs. South | 16 | 16
Ms. North | 11 | 9
Mr. East | 12 | 17

Simplified Table:
Teacher | Girls | Boys
Mr. Center | 16 | 10
Mr. East | 12 | 17

Question: A researcher recorded the number of cows on each farm in the county. How many farms have at least 4 cows but fewer than 46 cows?

Table:
Stem | Leaf 
0 | 1, 4, 7
1 | 2, 4, 5
2 | 0, 3
3 | 
4 | 0, 1, 5, 8, 9

Simplified Table:
Stem | Leaf 
0 | 1, 4, 7
1 | 2, 4, 5
2 | 0, 3
3 | 
4 | 0, 1, 5, 8, 9

Read the following question and table. Each row is separated by a newline ('\n') and each column is separated by a vertical bar ('|'). Return the simplified table that only remains the columns that are relevant to the question. If all columns are relevant, return the original table.
"""