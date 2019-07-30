#!/bin/bash
hadoop jar $hstream -D mapreduce.job.reduces=1 \
-files hdfs://dumbo/user/ajc867/ooza/df_mapper.py,hdfs://dumbo/user/ajc867/ooza/df_reducer.py \
-mapper "python df_mapper.py" -reducer "python df_reducer.py" \
-input /user/ajc867/ooza/reddit_tab.tsv \
-output /user/ajc867/ooza/df_out

