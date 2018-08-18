#! /usr/bin/env python3
#
# interpolate.py - interpolates [NEEDS TIME] values based on surrounding
# timestamps for plaintext FV transcripts
#
# by Aaron Cogbill: acogbill@focusfwd.com



import sys, re


def main(arg):
    transcript = open(arg,encoding='cp1252',errors='ignore')
    text = transcript.readlines()
    transcript.close()

    # identify lines with timestamps and index them in a list
    stampRE=re.compile(r'((\[(\d{2}):(\d{2}):(\d{2})\])|\[NEEDS TIME\])')
    timestamps=[]
    for line in range(len(text)):
        stampsearch=stampRE.search(text[line])
        if stampsearch != None:
            hours=stampsearch.group(3)
            minutes=stampsearch.group(4)
            seconds=stampsearch.group(5)
            timestamps.append((line,hours,minutes,seconds))
    
    # extract the subset containing NTs and index in a list
    needstimes=[]
    for index in range(len(timestamps)):
        if timestamps[index][1]==None:
            needstimes.append(index)

   # warnings: first and last stamps cannot be NTs
    if needstimes[0]==0:
        quit('Error: first timestamp NEEDS TIME.')
    if needstimes[-1]==len(timestamps)-1:
        quit('Error: last timestamp NEEDS TIME.')

    # interpolate NTs
    for index in needstimes:

        # a. find numeric stamps before and after the NT
        m = index-1
        n = index+1
        while timestamps[m][1]==None:
            m += -1
        while timestamps[n][1]==None:
            n += 1
    
        # b. convert numeric timestamps to seconds
        prev_stamp_sec = stampToSeconds(timestamps[m])
        next_stamp_sec = stampToSeconds(timestamps[n])
        difference = next_stamp_sec - prev_stamp_sec
        
        # c. interpolate the NT in seconds
        prev_char = countChar(timestamps[m][0]+1,timestamps[index][0]-1,text)
        next_char = countChar(timestamps[index][0]+1,timestamps[n][0]-1,text)
        weight = prev_char/(prev_char+next_char)

        interpolation = int(prev_stamp_sec + difference*weight)
        
        # d. convert the NT back to string '[hh:mm:ss]'
        NT_string=stampToString(secondsToStamp(interpolation))
        
        # e. replace each NT where it belongs
        line_no=timestamps[index][0]
        text[line_no]=NT_string
        
    # join the lines into one string
    interpolated_text = ''.join(text)
    interpolated_text.strip()
 
    # write the string to a new file - 'originalfilename ck0.txt'
    argparts = arg.split('.')
    argparts[-2] += ' ck0'
    newname = '.'.join(argparts)
    interpolated_file = open(newname,'w')
    interpolated_file.write(interpolated_text)
    interpolated_file.close()
    print('Wrote version ck0.')
    

def stampToSeconds(stamp):
    # converts a tuple (linenumber, hh, mm, ss) to seconds
    # (int, str, str, str) in, integer out
    
    hours,minutes,seconds=stamp[1:]
    totalsec=int(seconds) + 60*int(minutes) + 3600*int(hours)
    
    return totalsec


def secondsToStamp(seconds):
    # converts seconds to a tuple (h, m, s)
    # integer in, tuple of integers out
    
    hours=seconds//3600
    hremainder=seconds%3600
    minutes=hremainder//60
    mremainder=hremainder%60
    seconds=mremainder
    
    return (hours,minutes,seconds)


def stampToString(hms):
    # converts a timestamp tuple (h, m, s) to seconds
    # tuple of integers in, integer out
    
    hours=str(hms[0]).rjust(2,'0')
    minutes=str(hms[1]).rjust(2,'0')
    seconds=str(hms[2]).rjust(2,'0')
    string='['+':'.join([hours,minutes,seconds])+']\n'
    
    return string


def countChar(startline,stopline,text):
    # counts the number of characters in a text broken over multiple lines
    
    string=''.join(text[startline:stopline])
    
    return len(string)

main(sys.argv[1])
