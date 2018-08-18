The goal of this project is to automate timestamp interpolation while combining FocusVision transcripts.

The folder "OSX" contains the original version of the script, meant for use from the terminal. The folder "windows" contains a version meant for general distribution.

to-do:
	-add optional ability to estimate first and last timestamps if they are NTs
	-fix the weird newline removal issue


ideas to improve interpolation accuracy:
	-omitting respondent/moderator IDs and timestamps from the character count
	-counting non-phonetic characters differently: inaudible/crosstalk tags, punctuation, digraphs (this list is only a beginning)
	-extrapolating speaking rates from speech without NTs for single-respondent transcripts or transcripts with respondent IDs
