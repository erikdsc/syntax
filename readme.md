# syntax
This repository consists of three parts.  
The first one, highlighter.py, has a function that colors text in the shell based on the specified regexes and color themes.  
The second one, grep.py, is supposed to work almost the same as the standard grep function in bash. It takes a text and one or more regexes,
  and finds all the places in the text that matches the regex.  
The third one, diff.py, is supposed to work almost the same as the standard diff function in bash. It takes two texts as input and will try to find
  out how the first text was modified into the second text.  

## Highlighting
The highlighter.py file has a function called highlight that can be used to color texts in the terminal. The function requires a dictionary that maps names with a regex, and then another dictionary that maps the same names to a color, the third argument is the text to color. This is explained further in the docstring of the function.

The highlighting function can also be used directly by calling the file containing it:  
	`python3 highlighter.py <regex_file> <color_file> <source_text_file>`  
	
An example for this can be the command below, where a dummy Python file is colored based on Python syntax:  
	`python3 highlighter.py python.syntax python.theme demo.py`    

#### regex_file
It's important to know that the regex- and theme files need to be in a specific format. 
The regex file has to have n consecutive number of lines containing a regex mapped to a name.
A regex should be represented like this:  
	`<regex>: <name>`  
The regex in itself has to be within quotation marks. There can be no empty lines, random spaces or other things like that. 
After all the regex-name pairs have been written, a hashtag should be written on the line following the last regex pair to signal that the script should stop looking for more regexes. Anything written below the hashtag will not be read by the script, so it is a good place to comment the regexes. An example for how to write this file can be found in the python.syntax file.  
	
#### color_file
The color file also has very strict rules for the formatting. The rules for the regex_file also applies here: there can be no empty lines or random spaces, and the file should have a hashtag to terminate the script after the colors are read. A color can be represented like this:  
	`<name>: <color>`  
The name must match a name from the regex file. The colors in themselves must be written like \<attribute>;\<color>, more on this can be found here: https://misc.flogisoft.com/bash/tip_colors_and_formatting#attributes_combination
	
## Grep
This is supposed to work almost like the grep function in bash. The grep.py file has a function, grep, that takes a text and a regex as input. It will return all the lines that contain the regex.   
The grep function can be used by calling the file in the terminal like this:  
	`python3 grep.py <textfile> <regex1> [<regex2> .. <regexN>] [--highlight] [--line_number]`  
An example that uses the dummy file:  
	`python3 grep.py demo.py  "#.*" self alive import --highlight --line_number`  
The highlight flag will color the regexes in the output and the line_number flag will write the line number in the file for each line that has the regex.


## Diff






### temp
Running the code:
Task 1:
Run with python3 highlighter.py <syntaxfile> <themefile> <sourcefile>

Task 2:
You can run the demo with "python3 highlighter.py python.syntax python.theme demo.py"

Task 3:
Decided to go for Java. Did only implement 10 different syntaxes
Run the demo with "python3 highlighter.py favorite_language.syntax favorite_language.theme demo.java"

Task 4:
Run demo with for example: "python3 grep.py -filename demo.py -regex "#.*" self alive import class --highlight True"

Task 5:
Couldn't think of a good way to make use of regular expressions, so I didn't apply it in this task.
Run demo with "python3 diff.py difftest1.txt difftest2.txt difftestchanges.txt"
or "python3 diff.py difftest1.txt difftest2.txt"
The last argument is optional and provides a file to write into. Will print in terminal instead if not provided

Task 6:
Run demo with "python3 highlighter.py diff.syntax diff.theme difftestchanges.txt"

## To do:
Make the formatting for regex- and color files less cumbersome
