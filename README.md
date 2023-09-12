# Perfect-Matchups
This project is an analysis algorithm that utilises skills based on various Data Structures and Algorithms. 

The main algirithms included in this project:
**- Counting Sort
- Radix Sort**

Main function is **analyze(results, roster, score)** where: 
  - Input **results** is a lists of lists denoted by **[team1, team2, score]** where:
    - **team1** and **team2** are uppercase strings
    - **score** is an integer value in the range of 0 to 100 inclusive
    - Example input: [['EAE', 'BCA', 85], ['EEE', 'BDB', 17], ['EAD', 'ECD', 21], ['ECA', 'CDE', 13], ['CDA', 'ABA', 76], ['BEA', 'CEC', 79], ['EAE', 'CED', 8], ['CBE', 'CEA', 68]]
  
  - Input **score** is an integer value in the range of 0 to 100 inclusive
  
  - Output is a list of two values denoted by **[top10matches, searchedmatches]** where:
    - **top10matches** is a list of 10 matches with the highest score
    - **searchedmatches** is a list of matches with the same score as **score**
