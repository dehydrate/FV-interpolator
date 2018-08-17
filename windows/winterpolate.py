#! python3
# winterpolate.py - a script to interpolate FV needs times values
# by Aaron Cogbill acogbill@focusfwd.com


import sys, re, os
inspect = False

def main(arg):
    transcript = open(arg, encoding='cp1252', errors='ignore')
    text = transcript.readlines()

    # 1. identify lines with timestamps and index them in a list
    stampRE=re.compile(r'((\[(\d{2}):(\d{2}):(\d{2})\])|\[NEEDS TIME\])')
    timestamps=[]
    for line in range(len(text)):
        stampsearch=stampRE.search(text[line])
        if stampsearch != None:
            hours=stampsearch.group(3)
            minutes=stampsearch.group(4)
            seconds=stampsearch.group(5)
            timestamps.append((line,hours,minutes,seconds))
    
    # 2. identify lines with NT timestamps and index in a list
    needstimes=[]
    for index in range(len(timestamps)):
        if timestamps[index][1]==None:
            needstimes.append(index)

    # 3. interpolate NTs
    for index in needstimes:

        # 3a. find numeric stamps before and after the NT
        m = index-1
        n = index+1
        while timestamps[m][1]==None:
            m += -1
        while timestamps[n][1]==None:
            n += 1
    
        # 3b. convert numeric timestamps to seconds
        prev_stamp_sec = stampToSeconds(timestamps[m])
        next_stamp_sec = stampToSeconds(timestamps[n])
        difference = next_stamp_sec - prev_stamp_sec
        
        # 3c. interpolate the NT in seconds
        prev_char = countChar(m,index,text)
        next_char = countChar(index,n,text)
        weight = prev_char/(prev_char+next_char)

        interpolation = int(prev_stamp_sec + difference*weight)
        
        # 3d. convert the NT back to string '[hh:mm:ss]'
        NT_string=stampToString(secondsToStamp(interpolation))
        if inspect:
            NT_string = r'**'+NT_string
        # 3e. replace each NT where it belongs
        line_no=timestamps[index][0]
        text[line_no]=NT_string
        
    # join the lines into one string
    interpolated_text = ''.join(text)
    
    # write the string to a new file - 'originalfilename ck0.txt'
    argparts = arg.split('.')
    argparts[-2] += ' ck0'
    newname = '.'.join(argparts)
    interpolated_file = open(newname,'w')
    interpolated_file.write(interpolated_text)
    interpolated_file.close()
    print('Wrote ck0.')
    

def stampToSeconds(stamp):
    hours,minutes,seconds=stamp[1:]
    totalsec=int(seconds) + 60*int(minutes) + 3600 * int(hours)
    return totalsec


def secondsToStamp(seconds):
    hours=seconds//3600
    hremainder=seconds%3600
    minutes=hremainder//60
    mremainder=hremainder%60
    seconds=mremainder
    return (hours,minutes,seconds)


def stampToString(stamp):
    hours=str(stamp[0]).rjust(2,'0')
    minutes=str(stamp[1]).rjust(2,'0')
    seconds=str(stamp[2]).rjust(2,'0')
    string='['+':'.join([hours,minutes,seconds])+']\n'
    return string


def countChar(startline,stopline,text):
    string=''.join(text[startline:stopline+1])
    return len(string)


try:
    if len(sys.argv) == 2:
        main(sys.argv[1])
    elif len(sys.argv) == 3 and sys.argv[1] == '-c':
        arg=sys.argv[2]
        inspect = True
        main(sys.argv[2])
    elif len(sys.argv) == 1:
        raise Exception()
    else:
        print('Syntax:\npy winterpolate.py "filename", OR\npy winterpolate.py -c "filename"')
except:
    for file in os.listdir():
        if file != 'winterpolate.py' and 'ck0' not in file:
            main(file)
