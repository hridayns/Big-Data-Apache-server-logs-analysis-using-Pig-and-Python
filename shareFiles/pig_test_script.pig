REGISTER /opt/pig-0.17.0/lib/piggybank.jar;
REGISTER  'script.py' using jython as myfuncs;

raw_data = LOAD '/home/piggyBoi/chat1.txt' USING PigStorage('\n') AS (line:chararray);

data = FOREACH raw_data GENERATE FLATTEN(myfuncs.customParser(line));

/*grp_by_sender = GROUP data BY sender;*/

grp_by_word_id = GROUP data BY result::words.id;

STORE grp_by_word_id INTO 'parsed_chat';
