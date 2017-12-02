#/usr/bin/jython
# -*- coding: utf-8 -*-

import re
@outputSchema("result:tuple(sender:chararray,words:{(id:int,word:chararray)})")
def customParser(line):
	if line is not None:
		mssgLine = line.split(' - ')
		if len(mssgLine) > 1:
			mssgPart = mssgLine[1]
			sender_n_mssg = mssgPart.split(':')
			len_of_sender_n_mssg = len(sender_n_mssg)
			if(len_of_sender_n_mssg > 1):
				sender = sender_n_mssg[0]
				mssg = sender_n_mssg[1]
				words = []
				mwords = mssg.split(' ')
				for index, word in enumerate(mwords):
					words.append((index,word))
				return (sender,words)
		# line = unicode(line,'utf-8')
		# line = line.decode('utf-8','ignore').rstrip().encode("utf-8")
		# return line
		# line = line.encode('unicode_escape')
		# return line
	# 	emoji_pattern = re.compile("["
	# 	        u"\U0001F600-\U0001F64F"  # emoticons
	# 	        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
	# 	        u"\U0001F680-\U0001F6FF"  # transport & map symbols
	# 	        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
	# 	                           "]+", flags=re.UNICODE)
	# 	line = emoji_pattern.sub(r'', line) # no emoji

		# line = "".join(c for c in line if isinstance( c, ( int, long ) ) is False and ord(c) >= 0 and ord(c) <= 127)		
		# no_of_words_in_mssg = len(mssg.split(' '))
		# dateRegex = re.compile(r'\d+/\d+/\d+')
		# matchedDate = re.search(dateRegex,line)
		# if matchedDate is not None:
		# 	grp = matchedDate.group()
		# 	return grp