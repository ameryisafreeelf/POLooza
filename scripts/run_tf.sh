#!/bin/bash
hadoop jar $hstream -D mapreduce.job.reduces=1 \
-files hdfs://dumbo/user/ajc867/ooza/tf_mapper.py,hdfs://dumbo/user/ajc867/ooza/tf_reducer.py \
-mapper "python tf_mapper.py" -reducer "python tf_reducer.py" \
-input /user/ajc867/ooza/reddit_tab.tsv \
-output /user/ajc867/ooza/tf_out

