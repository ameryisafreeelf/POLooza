#!/bin/bash
hadoop jar $hstream -D mapreduce.job.reduces=1 \
-files hdfs://dumbo/user/ajc867/ooza/timestamp_to_year_mapper.py,hdfs://dumbo/user/ajc867/ooza/timestamp_to_year_reducer.py \
-mapper "python timestamp_to_year_mapper.py" -reducer "python timestamp_to_year_reducer.py" \
-input /user/ajc867/ooza/reddit_tab.tsv \
-output /user/ajc867/ooza/post_years

