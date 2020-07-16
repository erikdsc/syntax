import sys
import re

def highlight(regexes, color_themes, text, print_output=False):
    """
    Applies colors from the color_themes-file to the substrings in the input
    text that matches the regexes in the regexes-file.
    Input:
        regexes (dict): a dictionary with regexes mapped to their names
        color_themes (dict): a dictionary with colors mapped to their names
        file (string): a text file that can be colored
        print_output (bool): will print the string if true.

        NB: Names in regexes and color_themes must match!
            This function expects the files to have a certain format!
    Output:
        The specified text in string-format with the desired colors
    """
    #Building the text with colors from scratch in a new string
    coloredText = ""
    #building a list of all regexes
    first_matches = {}
    for key in regexes.keys():
        try:
            first_matches[key] = re.search(regexes[key], text, re.MULTILINE).start(0)
        except AttributeError: pass
    #keeps count of place in text
    position = 0
    remove_from_dict = []
    while first_matches:
        #Updates the indexes for the syntaxes
        for key in first_matches:
            if first_matches[key] <= position:
                try:
                    first_matches[key] = re.search(regexes[key], text[position:], re.MULTILINE).start(0) + position
                except:
                    remove_from_dict.append(key)
        #Removing syntaxes that have no matches
        for reg in remove_from_dict:
            first_matches.pop(reg)
            remove_from_dict.remove(reg)
        try:
            #Adds regex matches with their associated colors to the new string
            key = min(first_matches, key=first_matches.get)
            match = re.search(regexes[key], text[position:], re.MULTILINE)
            coloredText += text[position:position+match.start(0)]
            coloredText += "\033[{}m".format(color_themes[key])
            coloredText += text[position+match.start(0) : position+match.end(0)] + "\033[0m"
            position += match.end(0)
        #key = min() will reach ValueError when the function has exhausted all 
        #the syntaxes. This except-clause will terminate the function
        except ValueError:
            coloredText += text[position:]
            if (print_output): print(coloredText)
            return coloredText
    
#if the file is being run as main
if __name__ == "__main__":
    if len(sys.argv) == 4:
        syntax_file = open(sys.argv[1], "r")
        theme_file = open(sys.argv[2], "r")
        source_file = open(sys.argv[3], "r")
        text = source_file.read()
        source_file.close()
        syntax = {} #Matches name with syntax
        theme = {} #Matches name with theme

        #iterating through the syntax_file and maps regex to name
        # in the syntax-dictionary
        for line in syntax_file:
            # "#" marks the end of syntax, and the beginning of comments
            if line[0] == "#":
                break
            regex = re.findall(r"^\"(.*)\"", line)
            name = re.findall(r"\": (.*)", line)
            syntax[name[0]] = regex[0]
        syntax_file.close()

        #iterating through the syntax_file and maps regex to name
        # in the theme-dictionary
        for line in theme_file:
            if line[0] == "#":
                break
            line = line.strip()
            linesplit = re.split(": ", line)
            theme[linesplit[0]] = linesplit[1]
        theme_file.close()

        #running the function
        highlight(syntax, theme, text, print_output=True)

    else: #print to make troubleshooting easier
        print("NB: Need three arguments! (syntax_file, theme_file and" +
        " source_file)")
