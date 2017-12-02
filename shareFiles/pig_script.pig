REGISTER /opt/pig-0.17.0/lib/piggybank.jar;

raw_data = LOAD '/home/piggyBoi/sample_log' USING org.apache.pig.piggybank.storage.apachelog.CombinedLogLoader() AS (ipaddr: chararray, logname: chararray, temp0: chararray,time: chararray, temp1: chararray, temp3: chararray, temp4: chararray, temp5: int, temp6: int, page_link: chararray, temp7: chararray);

grpd_by_page = Group raw_data by page_link;

page_hits = FOREACH grpd_by_page GENERATE flatten($0), COUNT($1) as page_count;

STORE page_hits INTO 'parsed_log';

/*
ordrd_list = ORDER page_hits BY page_count DESC;

Top_page = LIMIT ordrd_list 1;

store Top_page into 'top_page_res' using PigStorage(',');

DEFINE DATE_EXTRACT org.apache.pig.piggybank.evaluation.util.apachelogparser.DateExtractor('dd/MMM/yyyy:HH:mm:ss Z','d/M/y');

grpd = GROUP raw_data BY DATE_EXTRACT(time);

hits_per_day = foreach grpd generate flatten($0),COUNT($1);

store hits_per_day into 'hits_per_day' using PigStorage(',');*/