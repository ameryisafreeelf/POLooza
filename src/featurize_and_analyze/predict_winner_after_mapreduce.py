#!/anaconda3/bin/python
"""
After big data is reduced through MapReduce functions,
perform smaller data analysis locally.

@author: crain
"""

import pandas as pd
import numpy as np

from sklearn import metrics
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from imblearn.under_sampling import RandomUnderSampler

REDDIT_FILENAMES = ['politics.csv',
 'PoliticalDiscussion.csv',
 'worldnews.csv',
 'all_reddit.csv',
 'conservative.csv',
 'bluemidterm2018.csv',
 'Economics.csv',
 'PoliticalHumor.csv',
 'reddit.csv',
 'Libertarian.csv',
 'TheDonald.csv',
 'democrats.csv',
 'LateStageCapitalism.csv',
 'neoliberal.csv',
 'Liberal.csv',
 'anarcho_capitalism.csv',
 'worldpolitics.csv',
 'socialism.csv',
 'SandersForPresident.csv',
 'progressive.csv',
 'news.csv']

ELECTION_FILENAMES = ['1976-2016-president.csv']#, '1976-2018-senate.csv',
#                      '1976-2018-house.csv']

def aggregate_csvs(prefix, filenames, new_col_name=None):
    dfs = [pd.read_csv(prefix + filename, low_memory=False) for filename in filenames]
    if new_col_name:
        for filename, df in zip(filenames, dfs):
            df[new_col_name] = filename[:-4]
    combined_data = np.vstack((dfs[0].values, dfs[1].values))
    for df in dfs[2:]:
        combined_data = np.vstack((combined_data, df.values))
    combined_data = pd.DataFrame(combined_data, columns=dfs[0].columns)
    return combined_data

def utc_to_year(num_seconds):
    try:
        year = 1970 + (float(num_seconds) // 31556926)
    except:
        return 0
    return 0 if np.isnan(year) else int(year)

def get_winners(df):
    signatures = [str(y) + str(s) for y, s in zip(df.year, df.state)]
    is_winner = np.zeros(df.shape[0])
    current_signature = signatures[0]
    current_max = -1
    for i, (signature, votes) in enumerate(zip(signatures, df.candidatevotes)):
        if current_signature == signature:
            if current_max < votes:
                idx_max = i
                current_max = votes
        else:
            is_winner[idx_max] = 1
            current_signature = signature
            idx_max = i
            current_max = votes
    is_winner[idx_max] = 1
    return is_winner

reddit_df = aggregate_csvs('Data/', REDDIT_FILENAMES, 'subreddit')
reddit_df = reddit_df[[type(t) == str for t in reddit_df.text]]
reddit_df['year'] = [utc_to_year(s) for s in reddit_df.time.values]
#reddit_df = reddit_df[np.where(reddit_df.year.values != 0)]

election_df = pd.read_csv('election_data/1976-2016-president.csv', low_memory=False)
election_df = election_df[[type(c) == str for c in election_df.candidate]]
candidate_is_winner = get_winners(election_df)
election_df['is_winner'] = candidate_is_winner

candidate_strs = [c.lower().replace('"', '').replace(',', '')
                 for c in election_df.candidate]

#candidate_strs = [' '.join(c.lower().replace('"', '').replace(',', '').split())
#                 + '\tis_winner: {}'.format(w)
#                 for w, c in zip(election_df.is_winner, election_df.candidate)]

reddit_df['is_winner'] = np.full(reddit_df.shape[0], -1)
for i, text in enumerate(reddit_df.text):
    for word in text.lower().split():
        for j, candidate_str in enumerate(candidate_strs):
            if candidate_str != 'other' and word in candidate_str.split():
                reddit_df.is_winner[i] = candidate_is_winner[j]


tfidf_model = TfidfVectorizer().fit(reddit_df.text)
tfidf_data = tfidf_model.transform(reddit_df.text)

winner_word_dict = {}
for i, s in enumerate(candidate_strs):
    for word in s.split():
        winner_word_dict[word] = max(0, candidate_is_winner[i])
tfidf_vocabulary = list(tfidf_model.vocabulary_)
winner_vocabulary = {}

for v in tfidf_vocabulary:
    try:
        winner_vocabulary[v] = winner_word_dict[v]
    except:
        winner_vocabulary[v] = -1
winner_values = np.full(tfidf_data.shape[1], -1) #
for v in tfidf_vocabulary: #
    winner_values[tfidf_model.vocabulary_[v]] = winner_vocabulary[v] #
#winner_values = [winner_vocabulary[v] for v in winner_vocabulary]


relevant_columns = np.where(np.asarray(winner_values) != -1)
where_to_check_nonzeros = tfidf_data[:, relevant_columns[0]].sum(axis=1)
where_to_check_nonzeros = [z.item(0) for z in where_to_check_nonzeros]
data_with_winners = pd.DataFrame(reddit_df.values[np.where(where_to_check_nonzeros)[0]],
                                 columns=reddit_df.columns)
zero_columns = np.where(np.asarray(winner_values) == 0)[0]
ones_columns = np.where(np.asarray(winner_values) == 1)[0]

tfidf_data_with_labels = tfidf_data[np.where(where_to_check_nonzeros)[0]]
did_win = [z.item(0) for z in (tfidf_data_with_labels[:, ones_columns]).sum(axis=1)]
winner_labels = np.zeros(data_with_winners.shape[0])
winner_labels[np.where(did_win)[0]] = 1

word_from_idx = {}
for v in tfidf_model.vocabulary_:
    word_from_idx[tfidf_model.vocabulary_[v]] = v

#reddit_df.to_csv('reddit_data_big.csv', sep='~')

#winner_data = np.vstack(())
#winner_df.to_csv('winner_df.csv', sep='\t')

data_with_winners['is_winner'] = winner_labels

lgr = LogisticRegression(solver='liblinear', dual=True)

x, y = tfidf_data_with_labels, winner_labels

x_train, x_test, y_train, y_test = train_test_split(
    x, y, random_state=0)

#x_train, y_train = RandomUnderSampler(random_state=0).fit_sample(
#    x_train, y_train)

lgr.fit(x, y)

impt_words = []
impt_word_tfidf = []
largest_coefs = np.argsort(lgr.coef_)[0]
i = 0
j = -1
while i < 50:
    j += 1
    word = word_from_idx[largest_coefs[j]]
    if word not in winner_word_dict and len(word) > 3:
        impt_words.append(word)
        impt_word_tfidf.append(lgr.coef_[0][largest_coefs[j]])
        i += 1

pd.DataFrame(np.reshape([impt_words, impt_word_tfidf], (50,2)),
             columns=['Word', 'Coef']).to_csv('losing_word_data.csv')