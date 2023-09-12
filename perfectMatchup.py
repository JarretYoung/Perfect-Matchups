"""                                            +
Unit: FIT2004 - Algorithms and Data Structures +
---------------------------------------------- +
Assignment 1                                   +
Submission Date: 19 - 8 - 2022                 +
---------------------------------------------- +
Student Name:   Garret Yong Shern Min          +
Student ID:     31862616                       +
Student Email:  gyon0004@student.monash.edu    +
______________________________________________ +
"""
import math


def counting_sort_int(int_list, col, index):
    """
    This is a specialised counting sort algorithm that sorts integers in a list (of lists) while maintaining its order.
    - First a bucket list with 11 spaces for 10 numbers (0-9) and one padded number
    - The frequency of each number (and pad) in the selected column is calculated (achieved using number//10^column % 10)
    - Iterate through all the numbers in bucket list to find the frequency of each number to insert into the output
        - When the frequency is found (>0) then the integer list would be iterated through until a match is found
            - The match in the integer list is removed and inserted into the output list
    - After all the characters is inserted back into the output list, return the output list

    :Input:
        :param int_list:    Is the list of lists with numbers in a specific index
        :param col:         Is the column that is being analysed
        :param index:       Is the index of the integer in the list of lists to be analysed and sorted

    :return: output_list:   Is a list of the "sorted" list based on the current column (index)

    Time complexity:
        Worst: O(N)
    Space complexity:
        Aux: O(MN)
    """
    # Finding the largest number in list
    largest_num = int_list[0][index]  # Time: O(1)
    for matches in int_list:  # Time: O(N)
        if matches[index] > largest_num:  # Time: O(1)
            largest_num = matches[index]  # Time: O(1)

    # Initialising bucket
    bucket_list = [0] * 11

    # Counting the frequency of numbers
    for matches in int_list:
        num_in_specified_column = -1
        if matches[index] == 0:
            if col < 1:
                num_in_specified_column = 0
        else:
            if col < (math.floor(math.log10(matches[index]))+1):
                num_in_specified_column = ((matches[index])//10 ** col) % 10
        bucket_list[num_in_specified_column+1] = bucket_list[num_in_specified_column+1] + 1

    # Prepping output
    output_list = []
    for i in range(0, len(bucket_list)):
        # Letter to be inserted based on index of bucket
        insert_number = i -1
        frequency = bucket_list[i]
        # Index used to traverse the input (to find a matching letter)
        traverse_string_list_index = 0

        # Keep inserting items of this alphabet until reach frequency
        while frequency != 0:
            # Default the number at 0 (padding number) and increment based on the current number in column
            number = -1
            if int_list[traverse_string_list_index][index] != 0:
                if col < (math.floor(math.log10(int_list[traverse_string_list_index][index])) + 1):

                    number = ((int_list[traverse_string_list_index][index]) //10**col)%10
            else:
                if col < 1:
                    number = 0
            # If matching letters then remove from old list (input) and into new list (output)
            if number == insert_number:
                output_list.append(int_list[traverse_string_list_index])
                int_list.pop(traverse_string_list_index)
                # Decrement the frequency to be able to terminate loop
                frequency -= 1
            else:
                # Increment traversing index to signal for next string
                traverse_string_list_index += 1
    return output_list


def counting_sort_string(string_list, column):
    """
    This is a counting sort algorithm that sorts characters in a list while maintaining its order.
    - First a bucket list with 27 spaces for 26 letters and one padded letter
    - The frequency of each letter (and pad) is calculated
    - Iterate through all the letters in bucket list to find the frequency of each letter to insert into the output
        - When the frequency is found (>0) then the string list would be iterated through until a match is found
            - The letter in the string list is removed and inserted into the output list
    - After all the characters is inserted back into the output list, return the output list

    :Input:
        :param string_list: Is the list of characters to be sorted
        :param column:      Is the current column (index) being analysed

    :return: output_list:   Is a list of the "sorted" list based on the current column (index)

    Time complexity:
        Worst: O(M)
    Space complexity:
        Aux: O(M)
    """
    number_of_letters_in_alphabet = 26  # Time: O(1)
    code_for_A = ord('A')  # Time: O(1)

    # Initialising bucket
    bucket_list = [0] * (number_of_letters_in_alphabet + 1)  # Add 1 for padded number | Time: O(1)  Space: O(1)

    # Counting the frequency of letters
    for word in string_list:  # Time: O(M)
        letter_worth = 0  # Time: O(1)
        if column < len(word):  # Time: O(1)
            letter_worth = ord(word[column]) - code_for_A + 1  # Time: O(1)
        bucket_list[letter_worth] += 1  # Time: O(1)

    # Prepping output
    output_list = []  # Space: O(M)
    for i in range(0, len(bucket_list)):  # Time: O(1)
        # Letter to be inserted based on index of bucket
        insert_letter = i  # Time: O(1)
        frequency = bucket_list[i]  # Time: O(1)
        # Index used to traverse the input (to find a matching letter)
        traverse_string_list_index = 0  # Space: O(1)

        # Keep inserting items of this alphabet until reach frequency
        while frequency != 0:
            # Default the letter at 0 (padding letter) and increment based on the current letter in column
            letter = 0  # Time: O(1)
            if column < len(string_list[traverse_string_list_index]):  # Time: O(1)
                letter = ord(string_list[traverse_string_list_index][column]) - code_for_A + 1  # Time: O(1)

            # If matching letters then remove from old list (input) and into new list (output)
            if letter == insert_letter:  # Time: O(1)
                output_list.append(string_list[traverse_string_list_index])  # Time: O(1)
                string_list.pop(traverse_string_list_index)  # Time: O(1)
                # Decrement the frequency to be able to terminate loop
                frequency -= 1  # Time: O(1)
            else:
                # Increment traversing index to signal for next string
                traverse_string_list_index += 1  # Time: O(1)

    return output_list  # Time: O(1)


def counting_sort_team(team_list, column, team):
    """
    This is a counting sort algorithm that sorts a list of lists for a selected index while maintaining its order.
    In the context of this assignment, it sorts the matches based on the selected team (team1 and team2) columns.

    - First a bucket list with 27 spaces for 26 letters and one padded letter
    - The frequency of each letter (and pad) is calculated by accessing the column of the selected team (team1/team2) of each match
    - Iterate through all the letters in bucket list to find the frequency of each letter to insert into the output
        - When the frequency is found (>0) then the string list would be iterated through until a match is found
            - The match in the team list is removed and inserted into the output_list
    - After all the matches is inserted back into the output list, return the output list

    :Input:
        :param team_list:   Is the list of lists of results of all the matches
        :param column:      Is the current column (index) being analysed
        :param team:        Is the current team column (team1/team2) that is being analysed

    :return: output_list:   Is a list of the "sorted" list based on the current column (index)

    Time complexity:
        Worst: O(N)
    Space complexity:
        Aux: O(MN)
    """
    number_of_letters_in_alphabet = 26
    code_for_A = ord('A')

    # Initialising bucket
    bucket_list = [0] * (number_of_letters_in_alphabet + 1)  # Add 1 for padded number

    # Counting the frequency of letters
    for match in team_list:
        letter_worth = 0
        if column < len(match[team]):
            letter_worth = ord(match[team][column]) - code_for_A + 1
        bucket_list[letter_worth] += 1

    # Prepping output
    output_list = []
    for i in range(len(bucket_list)-1,-1,-1):
        # Letter to be inserted based on index of bucket
        insert_letter = i
        frequency = bucket_list[i]
        # Index used to traverse the input (to find a matching letter)
        traverse_string_list_index = 0

        # Keep inserting items of this alphabet until reach frequency
        while frequency != 0:
            # Default the letter at 0 (padding letter) and increment based on the current letter in column
            letter = 0
            if column < len(team_list[traverse_string_list_index][team]):
                letter = ord(team_list[traverse_string_list_index][team][column]) - code_for_A + 1

            # If matching letters then remove from old list (input) and into new list (output)
            if letter == insert_letter:
                output_list.append(team_list[traverse_string_list_index])
                team_list.pop(traverse_string_list_index)
                # Decrement the frequency to be able to terminate loop
                frequency -= 1
            else:
                # Increment traversing index to signal for next string
                traverse_string_list_index += 1

    return output_list


def radix_sort_int(int_list, index):
    """
    This method utilises the counting sort (counting_sort_int) iteratively to ensure that all the indexes are being
    iterated through

    :Input:
        :param int_list:    Is the list of lists of results of all the matches
        :param index:       Is the index of the list of lists that needs to be analysed

    :return: output_list:   Is a sorted list of lists based on the score (Ascending)

    Time complexity:
        Worst: O(N)
    Space complexity:
        Aux: O(MN)
    """
    longest_num_len = 0
    for team in int_list:
        if team[index] != 0:
            if math.floor(math.log10(team[index]))+1 > longest_num_len:
                longest_num_len = math.floor(math.log10(team[index])) +1
        else:
            if 1 > longest_num_len:
                longest_num_len = 1

    for column in range(0, longest_num_len):  # O(M)
        int_list = counting_sort_int(int_list, column, index)

    return int_list


def radix_sort_team(team_list, team):
    """
        This method utilises the counting sort (counting_sort_team) iteratively to ensure that all the indexes are being
        iterated through

        :Input:
            :param team_list:       Is the list of lists of results of all the matches
            :param team:            Is the current team column (team1/team2) that is being analysed

        :return: output_list:       Is a sorted list of lists based on the teams (Descending)

        Time complexity:
            Worst: O(MN)
        Space complexity:
            Aux: O(MN)
    """
    team -= 1 # This is to fit for indexing (team 1 = index 0)

    # Screening for longest length of team composition
    longest_team_comp = 0
    for match in team_list:
        if len(match[team]) > longest_team_comp:
            longest_team_comp = len(match[team])

    # Iterate for every available column to achieve sort
    for column in range(longest_team_comp -1, -1, -1):
        team_list = counting_sort_team(team_list, column, team)

    return team_list


def radix_sort_string(string_list):
    """
    This method utilises the counting sort (counting_sort_string) iteratively to ensure that all the indexes are being
    iterated through

    :Input:
        :param string_list: Is the list of strings (or char) to be sorted

    :return: output_list:       Is a sorted list of strings/char (Ascending)

    Time complexity:
        Worst: O(M)
    Space complexity:
        Aux: O(M)
    """
    # Screening for longest length of string
    longest_str_len = 0
    for word in string_list:
        if len(word) > longest_str_len:
            longest_str_len = len(word)

    # Iterate for every available column to achieve sort
    for column in range(longest_str_len -1, -1, -1):  # O(M)
        string_list = counting_sort_string(string_list, column)

    return string_list



def analyze(results, roster, score):
    """
    The purpose of this method is to return the top 10 scoring matches and the matches that scored the closest to the
    "score" input.

    This was achieved by the following steps:
        - Sorting the composition of each individual team to get a cleaner data set.
            e.g. ABA -> AAB
        - The invert of all matches would be created to ensure all the matches were mirrored.
            e.g. [AAB,BBB,30] will produce [BBB,AAB,70]
        - The results would be sorted starting from the lowest importance to ensure that the list is properly sorted
            - Sorting based on Team2
            - Sorting based on Team1
            - Sorting based on score
            This by inverting the process we ensure that the sorting of the highest importance would not be affected by
            sorting of the lower importance. On the other hand, the sorting of the lower importance has to be affected
            by the sorting of higher importance
        - The results would be iterated from the top (end of the list where the score is the highest) to find the top 10
          results
            - After the top 10 is found, append it into an output list
        - Finally the match(es) with scores closest to the input "score" will be looked for. This is achieved by:-
            - Finding if the score is too high (there should be no output as there is no next highest)
                - Append findings into output list
            - If the score is within the results, iterate backwards through the list
                - If a matching score exists, iterate through the list for all other matching scores
                - If no matching score exists, continue probing until a lower score is found and probe forward to find
                  the next highest score(s)
                - Append findings into output list
        - Return the output list in the form of the form [ [y] , [z] ] where y is 10 top scoring matches and z is
          the list of matches that contain the scores closest to the input "score"

    :Input:
        :param results: Is a list of lists e.g.[[x1,y1,z1],[x2,y2,z2],[x3,y3,z3]] where x and y is team composition and
                        z is the score scored by team x against team y
        :param roster:  Is the possible composition of team (A=1 ... Z=26) that is allowed
        :param score:   Is the score that needs to be searched for (if not found then find the next largest)

    :return output:     Is a list of lists of lists in the form [ [y] , [z] ] where y is 10 top scoring matches and z is
                        the list of matches that contain the scores closest to the input "score"

    Time complexity:
        Worst: O(MN)
    Space complexity:
        Aux: O(MN)
    """

    # Auxiliary space complexity for output = O(1)
    output = []

    # Sorting the Composition | e.g. ABA -> AAB
    # Time complexity of chunk = O(NM)
    # Auxiliary space complexity of chunk = 0
    for matches in results:  # Time: O(N)
        for team in range(0, 1+1):  # Time: O(2)
            character_list = list(matches[team])  # Time: O(M)
            matches[team] = ''.join(radix_sort_string(character_list))  # .join is Time: O(M)

    # Finding and appending inverse of each match | e.g. [AAB,BBB,30] will produce [BBB,AAB,70]
    # Time complexity of chunk = O(N)
    # Auxiliary space complexity of chunk = O(N)
    for matches in range(len(results)):  # Time: O(N)
        temp_match = [results[matches][1], results[matches][0], 100-results[matches][2]]  # Time: O(1)
        results.append(temp_match)  # Time: O(1)

    # Sorting based on team 2
    # Time complexity of chunk = O(MN)
    # Auxiliary space complexity of chunk = O(N)
    results = radix_sort_team(results, 2)

    # Sorting based on team 1
    # Time complexity of chunk = O(MN)
    # Auxiliary space complexity of chunk = O(N)
    results = radix_sort_team(results, 1)

    # Sorting based on the score
    # Time complexity of chunk = O(MN)
    # Auxiliary space complexity of chunk = O(N)
    results = radix_sort_int(results, 2)  # 2 is the index of the score

    # Obtaining top 10
    # Time complexity of chunk = O(MN)
    # Auxiliary space complexity of chunk = O(1)
    top_10 = []  # Space: O(1)
    top_10_index_counter = len(results) - 1  # Time: O(1)
    while (len(top_10) < 10) and (top_10_index_counter != -1):  # Time: O(N)
        if len(top_10) == 0:  # Time: O(1)
            top_10.append(results[top_10_index_counter])  # Time: O(1)
        else:
            if top_10[-1] == results[top_10_index_counter]:  # Time: O(M)
                pass  # Time: O(1)
            else:
                top_10.append(results[top_10_index_counter])  # Time: O(1)
        top_10_index_counter -= 1  # Time: O(1)
    output.append(top_10)  # Time: O(1)

    # Obtaining next largest
    # Time complexity of chunk = O(MN)
    # Auxiliary space complexity of chunk = O(MN)
    # This is a temporary array to store the output for the closest scores to input "score"
    next_largest_output = []
    # This is a variable to track if a valid score is found
    found = -1
    # This is the index / counter to control the while loop
    matches = len(results) -1
    # Checking to see if the input "score" is valid (the are numbers above it)
    # If not valid then append an empty list to the output and return immediately
    if score > results[-1][2]:
        output.append(next_largest_output)
        return output
    # Iterate through the results backwards to find the next highest
    while matches > -1:
        # If there is a matching score,
        # Iterate until all matches with matching score is found and added into next_largest_output
        if results[matches][2] == score:
            # Note the valid score
            found = score
            if len(next_largest_output) == 0:
                next_largest_output.append(results[matches])
            else:
                if results[matches] != next_largest_output[-1]:
                    next_largest_output.append(results[matches])
        # If there is a score smaller than input "score" and no valid score has been found
        # and the current match being analysed is not at the end of the list of results
        if (results[matches][2] < score) and (found == -1) and (matches < (len(results) - 1)):
            # Note the valid score
            found = results[matches + 1][2]
            # Append the previous match (since found smaller score than input "score", the prev score must be larger)
            next_largest_output.append(results[matches + 1])
            # Exit while loop
            break
        # Else if there is a score smaller than input "score" and no valid score has been found
        # and current match is at end of the list of results, ignore
        elif (results[matches][2] < score) and (found == -1) and (matches == (len(results) - 1)):
            found = -2
        matches -= 1
    # If a valid score is found that is not equal to input "score", then iterate forward until all matches of similar
    # scores to the next highest would be added to next_largest_output
    if (found != -1) and (matches > 0):
        valid = True
        while valid and ((matches+1) != len(results)):
            matches += 1
            if results[matches][2] == found:
                if results[matches] != next_largest_output[-1]:
                    next_largest_output.append(results[matches])
            else:
                valid = False
        # Invert the list to ensure that the stability (sorting of the scores are maintained)
        next_largest_output_inverted = next_largest_output[::-1]
        # Appending the now properly sorted next_largest_output to the output
        output.append(next_largest_output_inverted)
        # return output to end execution
        return output
    # If the next-largest_output is empty after iterating through results (meaning all matches have higher score than
    # input "score") then identify and note the score of the last match to iterate through and iterate forwards to find
    # all the scores with similar score the one noted
    if len(next_largest_output) == 0:
        found = results[0][2]
        valid = True
        index = 0
        next_largest_output.append(results[0])
        while valid and index < len(results):
            index += 1
            if results[index][2] == found:
                if results[index][2] != next_largest_output[-1]:
                    next_largest_output.append(results[index])
            else:
                valid = False
        # Invert the list to ensure that the stability (sorting of the scores are maintained)
        next_largest_output_inverted = next_largest_output[::-1]
        # Appending the now properly sorted next_largest_output to the output
        output.append(next_largest_output_inverted)
        # return output to end execution
        return output

    # Finally, return output
    output.append(next_largest_output)
    return output  # Time: O(1)






