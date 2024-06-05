#Chapter 6 project
#multi-clipboaard program in python 3

TEXT ={'agree':"""Yes, I agree. that sounds fine to me.""",
       'busy':"""Sorry, can we do this later this week or next week?""",
       'upsell':"""Would you consider making this a monthly donation?"""}

import sys, pyperclip 

if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1] # first command line arg is the keyphrase


if keyphrase in TEXT: #.lower()?
    pyperclip.copy(TEXT[keyphrase])
    print('test for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)

