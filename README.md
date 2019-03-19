# FV Times


The goal of this project is to automate timestamp interpolation while combining FocusVision transcripts.


The directory "OSX" contains the original version of the script, meant for use from the terminal. The directory "windows" contains a version meant for general distribution.


to-do:

	-add optional ability to estimate first and last timestamps if they are NTs

	-fix the newline issue
ideas to improve interpolation accuracy:

	-omitting respondent/moderator IDs and timestamps from the character count
	
	-counting non-phonetic characters differently: inaudible/crosstalk tags, punctuation, etc.

	-it's probably good enough as it is, for the most part
