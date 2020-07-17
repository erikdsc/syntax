import sys
import highlighter as hl
from queue import PriorityQueue

def superdiff(original, modified):
    """
    superdiff uses the function dig to find all non-changed lines, and
    finds the removed and inserted lines based on that.
    Input:
        original (string): a list that is used as to find changes in modified
        modified (string): a list that you want to find changed made in
    Output:
        a string that contains every change that has been made from original
        to modded
    """
    changes = PriorityQueue()
    #Passes the empty list matches into the recursive function
    #the function will append every sequence of non-changed lines it can
    #find. So after dig is called, the list should contain everything that
    #wasn't changed
    matches = []
    dig(original, modded, matches)
    matches.sort() #Needs to be sorted in order to write the changes correctly

    last_match1 = 0
    last_match2 = 0
    #looping through the non-changed sequence of lines. Lines that aren't
    #non-changed will be set as removed if they are only in the origin, and
    #inserted if they are only in the modified file
    #Places every found line into the priorityqueue, with a priority determined
    #by their place in original
    for match in matches:
        #Adding removed rows
        for i in range(last_match1, match[0]):
            changes.put((i, "-: "+original[i]))
        #Adding inserted rows
        for i in range(last_match2, match[2]):
            changes.put((match[0], "+: "+modded[i]))
        #Adding unchanged rows
        for i in range(match[0], match[1]):
            changes.put((i, "0: "+original[i]))
        last_match1 = match[1]
        last_match2 = match[3]
    #Adding the last few lines, the loop over couldn't get the last gap between
    #the last match and the end of the string
    for i in range(last_match1, len(original)):
        changes.put((i, "-: "+original[i]))
    for i in range(last_match2, len(modded)):
        changes.put((i, "+: "+modded[i]))

    #Puts the content of the priority queue into a list
    new_text = []
    while not changes.empty():
        new_text.append(changes.get()[1])
    #returns the list contents as a string, with the newlines added back in
    return "\n".join(new_text)

def dig(original, modded, matches, orgincr=0, modincr=0):
    """
    Uses recursion to find all matching sets of lines.
    The function finds the longest sequence of matching lines, then returns
    that set along with a new function call on the lines before and after
    the set
    Input:
        original (string): the original string
        modded (string): the modded string
        matches (list): a list reference that will contain every set of matching
            lines that are found
        origincr (int): an int increment for the original file that makes up for
            the reduction on indexvalues that comes from slicing lists
        modincr (int): an int increment that serves the same purpose as orgincr,
            but for the modded string
    Output:
        A new function call on the remaining parts of the strings
    """
    #finds the longest matching sequence of lines
    snake = LCS(original, modded, orgincr, modincr)
    #will not make more recursive calls if there are no more matches to be found
    if snake != None:
        matches.append(snake)
        #Splitting the texts at the matching rows:
        orgfront = original[0: snake[0]-orgincr]
        orgback = original[snake[1]-orgincr:-1]
        modfront = modded[0:snake[2]-modincr]
        modback = modded[snake[3]-modincr:-1]
        #Calling this function on the sliced parts:
        if len(orgfront) > 0 and len(orgback) > 0:
            return (dig(orgfront,modfront,matches,orgincr, modincr),
             dig(orgback, modback, matches, snake[1], snake[3]))
        elif len(orgfront) > 0:
            return dig(orgfront,modfront, matches,orgincr, modincr)
        elif len(orgback) > 0:
            return dig(orgback, modback, matches, snake[1], snake[3])

    #making a snake of the longest consecutive matches
def LCS(text1, text2, plus1=0, plus2=0):
    """
    Find the longest matching sequence of lines in two texts
    Input:
        text1: the first text used for comparison
        text2: the second text used for comparison
        plus1: an increment that is added to the return value in text1
        plus2: an increment that is added to the return value in text2
    Output:
        A list containing indexes indicating the start- and end location of
        the longest matching sequence of lines of both texts.
    """
    matches = []
    #maps all matching lines in the text to each other
    for i in range(len(text1)):
        matches.append([])
        for j in range(len(text2)):
            if (text1[i] == text2[j]):
                matches[i].append(j)

    #variables that represent the longest found sequence along with the current
    #sequence being worked on
    text1_start = -1
    text1_end = -1
    text2_start = -1
    text2_end = -1
    current_text1_start = -1
    current_text2_start = -1
    #loops through text1 and finds out where the longest matching sequence
    #starts and ends in both texts
    for i in range(len(text1)):
        for j in matches[i]:
            index1 = i
            index2 = j
            #increments and checks until there's no longer a match
            while (index2 in matches[index1]):
                if (current_text1_start == -1):
                    current_text1_start = index1
                    current_text2_start = index2
                index1 += 1
                index2 += 1
                #prevents the indexes from incrementing too much
                if (index1>=len(text1) or index2>=len(text2)):
                    break
            #overwrites the previous longest sequence found with the current
            if (index1-current_text1_start > text1_end-text1_start):
                text1_start = current_text1_start
                text2_start = current_text2_start
                text1_end = index1
                text2_end = index2
            #resets the first indexes
            current_text1_start = -1
            current_text2_start = -1
    if (text1_start != -1):
        return [text1_start+plus1, text1_end+plus1, text2_start+plus2,
         text2_end+plus2]

#If this file is run as main
if __name__ == "__main__":
    #ensures there are enough arguments passed
    if len(sys.argv) >= 3:

        original = open(sys.argv[1], "r").read().split("\n")
        modded = open(sys.argv[2], "r").read().split("\n")
        diff = superdiff(original, modded)
        if len(sys.argv) == 3:
            #no output file was specified
            regexes = {"added" : "^\+:(?= )", "removed" : "^-:(?= )"}
            colors = {"added" : "0;92", "removed" : "0;91"}
            diff = hl.highlight(regexes, colors, diff, print_output=True)
        else:
            #writes into outputfile
            out_file = open(sys.argv[3], "w+")
            out_file.write(diff)
            out_file.close()
    else:
        print("Needs two file arguments!")