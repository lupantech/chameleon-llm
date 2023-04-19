# 
prompt = """
Read the following table and question, and generate the domain-specific knowledge as the context information that could be helpful for answering the question.

Table:
x | y
10 | 15
11 | 9
12 | 2

Question: The table shows a function. Is the function linear or nonlinear?

Knowledge:
- A linear function is a function whose graph is a straight line.
- A nonlinear function is a function whose graph is not a straight line.
- The equation of a linear function is y = mx + b, where m is the slope and b is the y-intercept.
- The equation of a nonlinear function is not y = mx + b.

Table: Dog | Weight change (oz.)
Sprinkles | 5
Champ | -6

Question: Austen has two dogs, Sprinkles and Champ. He is concerned because Sprinkles keeps eating Champ's food. Austen asks their vet how much each dog's weight has changed since their last visit. Which dog's weight has changed the most?

Knowledge:
- This table shows the weight change (in ounces) for two dogs, Sprinkles and Champ.
- The dog whose weight has changed the most is the one with the highest (positive or negative) weight change.

Table:
Stem | Leaf 
1 | 6, 7, 8
2 | 1, 4, 6, 7
3 | 
4 | 1, 2, 5, 7, 7, 9
5 | 1, 8, 9

Question: Ms. Bradford reported her students' scores on the most recent quiz. How many students scored exactly 17 points?

Knowledge:
- This is a stem-leaf plot, where each data value is split into a "stem" (the first digit or digits) and a "leaf" (usually the last digit).
- The stems represent the tens digit of the data values, while the leaves represent the ones digit.
- The data value 17 would be represented as stem 1 and leaf 7.

Table: 
 | Fly | Read minds
Forgetful | 2 | 4
Lazy | 2 | 2

Question: A creative writing class compiled a list of their favorite superheroes. They listed each superhero's superpower and personality flaw. What is the probability that a randomly selected superhero is lazy and can read minds? Simplify any fractions.

Knowledge:
- This table shows a two-way frequency table, which is used to show the relationship between two variables.
- The probability of an event is calculated by dividing the number of favorable outcomes by the total number of outcomes.

Table: 
Stem | Leaf 
3 | 3
4 | 1, 4
5 | 6, 7
6 | 6
7 | 2

Question: The receptionist at a doctor's office kept track of each patient's wait time. What is the shortest wait time?

Knowledge:
- This is a stem-leaf plot, which is used to organize numerical data. 
- The stems represent the tens digit of the data values, while the leaves represent the ones digit.
- The shortest wait time is represented by the stem with the lowest value and the leaf with the lowest value within that stem.

Read the following table and question, and generate the domain-specific knowledge as the context information that could be helpful for answering the question.
"""