import re
import argparse
import highlighter as hl

def grep(text, regex, line_number=False):
    """
    Returns all lines containing the regex in a string
    Input:
        text (string): a string that you want to search
        regex (string): a regex you want to find in the string
    Output:
        a string containing all lines that has the regex
    """
    out_text = ""
    for linenum, line in enumerate(text.split("\n")):
        #re.search will return None if no matches are found
        if (re.search(regex, line) != None):
            #adds the line to the output if it contains the regex
            if line_number: out_text += str(linenum + 1) + ":"
            out_text += line +"\n"
    return out_text

if __name__ == "__main__":
    #creating the parser with arguments
    parser = argparse.ArgumentParser("Find lines matching a regex")
    parser.add_argument("filename",
    help="Choose which text file to use")
    parser.add_argument("regex", nargs="+",
    help="Specify the regex(es) to search for")
    parser.add_argument("--highlight", action='store_true',
    help="Flag for highlighting matches")
    parser.add_argument("--line_number", action='store_true',
    help="Flag for specifying the line number of the matches")
    args = parser.parse_args()

    #save the file in the string "text"
    f = open(args.filename, "r")
    text = f.read()
    f.close()

    #Colors to loop through
    colors = ["0;31", "0;32", "0;33", "0;34", "0;35", "0;36"]

    #adds all lines containing regexes to the string grepText
    print("")
    if args.highlight:
        for i in range(len(args.regex)):
            #a is just a placeholder key to match the syntax and theme
            syntax = {"a":args.regex[i]}
            theme = {"a":colors[i%6]}
            print(args.regex[i] + ":")
            hl.highlight(syntax, theme,grep(text, args.regex[i], 
             args.line_number), True)
    else:
        for reg in args.regex:
            print(reg + ": ")
            print(grep(text, reg, args.line_number)+"\n")
