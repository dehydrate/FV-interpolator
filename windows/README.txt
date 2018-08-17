winterpolate.py is a Python script to estimate timestamps for all NEEDS TIMES in a FocusVision transcript.


Requirements:
	You must have Python 3 installed.


Running the script by double clicking:
	Make an empty folder and put winterpolate.py in it. Drag a plain text FV transcript into the folder, then double click winterpolate.py.  A new plain text file with "ck0" in the name will appear; this is the interpolated version.


Running the script from the command line:
	syntax: py winterpolate.py your_filename

	You can add the -c flag to leave asterisks before each interpolated timestamp, if you want to run through them after the fact (py witerpolate.py -c your_filename). If winterpolate.py and/or the transcript you want to interpolate are not in your working directory, you'll need to use their absolute or relative paths. Make sure to put your_filename in quotes, since almost all FV transcripts have spaces in their names.
	The interpolated transcript will be saved with "ck0" in the name.


Notes:
	-This script is only meant for use on plain text files.
	-The script can't estimate the first or last timestamp of a transcript. You'll have to fill those in yourself BEFORE doing anything else.
	-Our work login accounts don't have Python installed by default, which is a problem if you work from home. Unless you can get someone to install it for you, you'll have to copy the plain text transcript to your computer and interpolate it there.
	-If I copy/paste an interpolated transcript into the term server, I lose all the line divisions. Check your interpolated transcript on the term server. If you have the same problem, you can get around it by copying/pasting the text of the transcript, rather than the transcript itself.
	-There used to be a text encoding issue that caused the script to stop running or to omit certain characters. I believe it's been resolved, but if you notice Notepad highlighting any spelling errors after running the script, please report the issue (see below).
	-Send any problems to acogbill@focusfwd.com (or Slack me for a faster reply).
