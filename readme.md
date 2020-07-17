Highlighter.py:
	python3 highlighter.py regex_file color_themes source_text 

grep.py
	python3 grep.py textfile regexes .. [--highlight] [--line_number]
	python3 grep.py demo.py  "#.*" self alive import --highlight --line_number





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
