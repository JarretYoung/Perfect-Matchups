# Perfect-Matchups
You and your friends are playing this new mobile video game called Diabro Immoral Gacha (DIG). The game revolves around building a team of M characters to compete with other teams in a tournament. You aimed to be the very best, like no one ever was in the game.
Thus, you have done your research into past tournaments in preparation for the biggest tournament. You aim to nd the best performing team composition against the other teams. You are however dealing with a large amount of tournament results. Unlike other competitors, you are able to process this data efficiently using sorting algorithms (counting and radix)
you have learnt.
For this task, I have written a Python function called **analyze(results, roster, score)** which will perform an analysis on the tournament results

The main algirithms included in this project:
- **Counting Sort**
- **Radix Sort**

Main function is **analyze(results, roster, score)** where: 
  - Input **results** is a lists of lists denoted by **[team1, team2, score]** where:
    - **team1** and **team2** are uppercase strings
    - **score** is an integer value in the range of 0 to 100 inclusive
    - Example input: [['EAE', 'BCA', 85], ['EEE', 'BDB', 17], ['EAD', 'ECD', 21], ['ECA', 'CDE', 13], ['CDA', 'ABA', 76], ['BEA', 'CEC', 79], ['EAE', 'CED', 8], ['CBE', 'CEA', 68]]
  
  - Input **score** is an integer value in the range of 0 to 100 inclusive
  
  - Output is a list of two values denoted by **[top10matches, searchedmatches]** where:
    - **top10matches** is a list of 10 matches with the highest score
    - **searchedmatches** is a list of matches with the same score as **score**
