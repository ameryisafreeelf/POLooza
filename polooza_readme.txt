# POLooza
Team project for Real-Time Big Data Analytics Course at NYU, Summer19.

POLooza analyzes the most important words - and, by extension, topics - posted on the social media site reddit in terms of how they track with the success or failure of a U.S. presidential candidate. To perform this analysis, we cleaned a large number of posts pulled from Reddit using Hadoop MapReduce. The scripts to pull the data are in the pull_reddit_data folder. The scripts to clean and profile the data are in the clean_and_profile folder.

We also wrote MapReduce code to match those posts that mentioned a presidential candidate to whether that candidate had won an election, the latter pulled from the MIT Election dataset from 1976-2016 (https://electionlab.mit.edu/data). We wrote a MapReduce implementation of tf-idf featurization of words and used those features to fit a logistic regression model to the target value of whether the mentioned candidate had won an election. We analyzed the coefficient magnitudes of the fitted logistic regression to determine those words that served as the best predictors of electoral success. Code for the above is in the featurize_and_analyze folder.

 
