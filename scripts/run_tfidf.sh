#!/bin/bash
hadoop jar $hstream -D mapreduce.job.reduces=1 \
-files hdfs://dumbo/user/ajc867/ooza/tfidf_mapper.py,hdfs://dumbo/user/ajc867/ooza/tfidf_reducer.py \
-mapper "python tfidf_mapper.py" -reducer "python tfidf_reducer.py" \
-input /user/ajc867/ooza/tfdf_data \
-output /user/ajc867/ooza/tfidf_out

