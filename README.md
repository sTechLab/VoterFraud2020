# VoterFraud2020
VoterFraud2020 is a multi-modal Twitter dataset with 7.6M tweets and 25.6M retweets related to voter fraud claims.

- [voterfraud2020.io](http://voterfraud2020.io), interactive web application for exploring the dataset
- [Figshare dataset publication](https://doi.org/10.6084/m9.figshare.13571084) with digital object identifier (DOI) **10.6084/m9.figshare.13571084**
  
*coming soon*
- Dataset Paper (PDF) 
- [github/sTechLab/twitter-stream](https://github.com/sTechLab/twitter-stream), the twitter streaming code
- [github/sTechLab/VoterFraud2020-analysis](https://github.com/sTechLab/voter-fraud-analysis), the code behind the data analysis


### Table of contents
- [VoterFraud2020](#voterfraud2020)
    - [Table of contents](#table-of-contents)
- [Hydrating the data](#hydrating-the-data)
- [Data description](#data-description)
  - [Tweets (7.6M)](#tweets-76m)
  - [Retweets (25.6M)](#retweets-256m)
  - [Users (2.6M)](#users-26m)
  - [Images](#images)
  - [URLs](#urls)
  - [Youtube Videos](#youtube-videos)

# Hydrating the data
_To-do_

# Data description
The columns in the data are described below. See the paper (to-do: link to PDF)
 for more details, or explore the [project website](http://voterfraud2020.io) for additional descriptive statistics.
## Tweets (7.6M)

Total count: 7,603,103  
Original tweets: 3,781,524  
Quote tweets: 3,821,579

- [October 2020](data/tweets/2020-10)
- [November 2020](data/tweets/2020-11)
- [December 2020](data/tweets/2020-12)

The tweets are split into daily chunks.

| Data Column                       | Description |
| -------------                     | ------------- |
| tweet_id                          | The ID of the tweet.  |
| user_community                    | The community of the tweet's author in the retweet graph, which is found using the [Infomap community detection algorithm](https://mapequation.github.io/infomap/python/) with default parameters. Values: 0, 1, 2, 3, 4, null  |
| user_active_status                | The active status of the tweet's author (as of January 10th). Values: 'active', 'suspended', 'not-found'  |
| retweet_count_metadata            | The number of retweets the tweet has received according to the tweet object's metadata (as of December 16th). |
| quote_count_metadata              | The number of quotes the tweet has received according to the tweet object's metadata (as of December 16th).  |
| retweet_count_by_community_X      | The number of retweets the tweet received from users in community X (X=0-4). |
| quote_count_by_community_X        | The number of quotes the tweet received from users in community X (X=0-4).  |
| retweet_count_by_suspended_users  | The number of retweets the tweet received from suspended users.  |
| quote_count_by_suspended_users    | The number of quotes the tweet received from users in community X.  |

## Retweets (25.6M)

Total count: 25,566,698

- [October 2020](data/retweets/2020-10)
- [November 2020](data/retweets/2020-11)
- [December 2020](data/retweets/2020-12)

The retweets are split into daily chunks.

| Data Column                       | Description |
| -------------                     | ------------- |
| retweeted_id                      | The ID of the retweeted tweet.|
| user_id                           | The ID of the user that retweeted. |

## Users (2.6M)

Total count: 2,559,018

- [users.csv](data/users/)

The users are split into 5 chunks, sorted by user id (ascending).

| Data Column                               | Description |
| -------------                             | ------------- |
| user_id                                   | The ID of the user. |
| user_community                            | The community of the user in the retweet graph, which is found using the [Infomap community detection algorithm](https://mapequation.github.io/infomap/python/) with default parameters. Values: 0, 1, 2, 3, 4, null |
| user_active_status                        | The active status of the user (as of January 10th). Values: 'active', 'suspended', 'not-found' |
| closeness_centrality_detractor_cluster    | Normalized closeness centrality of the top 10,000 users in the detractor cluster (computed using [Networkit](https://networkit.github.io/dev-docs/python_api/centrality.html#networkit.centrality.TopCloseness)).  |
| closeness_centrality_promoter_cluster     | Normalized closeness centrality of the top 10,000 users in the promoter cluster (computed using [Networkit](https://networkit.github.io/dev-docs/python_api/centrality.html#networkit.centrality.TopCloseness)). |
| retweet_count_by_community_X              | The number of retweets the user received from other users in community X (X=0-4). |
| quote_count_by_community_X                | The number of quotes the user received from other users in community X (X=0-4).  |
| retweet_count_by_suspended_users          | The number of retweets the user received from suspended users.  |
| quote_count_by_suspended_users            | The number of quotes the user received from other users in community X.  |

## Images
- [images.csv](data/images.csv)

| Data Column                       | Description |
| -------------                     | ------------- |
| unique_id                         |   |
| tweet_id                          |   |
| a_hash                            |   |
| p_hash                            |   |
| w_hash                            |   |

## URLs
- [urls.csv](data/urls.csv)

| Data Column                       | Description |
| -------------                     | ------------- |
| url                               |   |
| domain                            |   |
| tweet_count                       |   |
| retweet_count_metadata            |   |
| quote_count_metadata              |   |
| tweet_count_cluster_0             |   |
| retweet_count_cluster_0           |   |
| quote_count_cluster_0             |   |
| tweet_count_cluster_1             |   |
| retweet_count_cluster_1           |   |
| quote_count_cluster_1             |   |
| tweet_count_cluster_2             |   |
| retweet_count_cluster_2           |   |
| quote_count_cluster_2             |   |
| tweet_count_cluster_3             |   |
| retweet_count_cluster_3           |   |
| quote_count_cluster_3             |   |
| tweet_count_cluster_4             |   |
| retweet_count_cluster_4           |   |
| quote_count_cluster_4             |   |
| retweet_count_suspended_users     |   |
| quote_count_suspended_users       |   |

## Youtube Videos
- [youtube_videos.csv](data/images.csv)

| Data Column                       | Description |
| -------------                     | ------------- |
| video_id                          |   |
| video_title                       |   |
| channel_id                        |   |
| channel_title                     |   |
| published_t                       |   |
| retweet_count_metadata            |   |
| quote_count_metadata              |   |
| tweet_count_cluster_0             |   |
| retweet_count_cluster_0           |   |
| quote_count_cluster_0             |   |
| tweet_count_cluster_1             |   |
| retweet_count_cluster_1           |   |
| quote_count_cluster_1             |   |
| tweet_count_cluster_2             |   |
| retweet_count_cluster_2           |   |
| quote_count_cluster_2             |   |
| tweet_count_cluster_3             |   |
| retweet_count_cluster_3           |   |
| quote_count_cluster_3             |   |
| tweet_count_cluster_4             |   |
| retweet_count_cluster_4           |   |
| quote_count_cluster_4             |   |
| retweet_count_suspended_users     |   |
| quote_count_suspended_users       |   |
