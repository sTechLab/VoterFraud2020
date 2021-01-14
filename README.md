# VoterFraud2020 Dataset

# Hydrating the data
_To-do_

# Data description

## Tweets

- [October 2020](data/tweets/2020-10)
- [November 2020](data/tweets/2020-11)
- [December 2020](data/tweets/2020-12)

The tweets are split into daily chunks.

| Data Column                       | Description |
| -------------                     | ------------- |
| tweet_id                          |   |
| user_cluster                      |   |
| user_active_status                |   |
| retweet_count_metadata            |   |
| quote_count_metadata              |   |
| retweet_count_cluster_0           |   |
| quote_count_cluster_0             |   |
| retweet_count_cluster_1           |   |
| quote_count_cluster_1             |   |
| retweet_count_cluster_2           |   |
| quote_count_cluster_2             |   |
| retweet_count_cluster_3           |   |
| quote_count_cluster_3             |   |
| retweet_count_cluster_4           |   |
| quote_count_cluster_4             |   |
| retweet_count_suspended_users     |   |
| quote_count_suspended_users       |   |

## Retweets

- [October 2020](data/retweets/2020-10)
- [November 2020](data/retweets/2020-11)
- [December 2020](data/retweets/2020-12)

The retweets are split into daily chunks.

| Data Column                       | Description |
| -------------                     | ------------- |
| retweeted_id                      |   |
| user_id                           |   |

## Users

- [users.csv](data/users/)

The users are split into 5 chunks, sorted by user id (ascending).

| Data Column                       | Description |
| -------------                     | ------------- |
| user_id                           |   |
| cluster                           |   |
| active_status                     |   |
| closeness_centrality_clusters_0   | Closeness centrality ...  |
| closeness_centrality_clusters_1234| Closeness centrality ...  |
| retweet_count_cluster_0           |   |
| quote_count_cluster_0             |   |
| retweet_count_cluster_1           |   |
| quote_count_cluster_1             |   |
| retweet_count_cluster_2           |   |
| quote_count_cluster_2             |   |
| retweet_count_cluster_3           |   |
| quote_count_cluster_3             |   |
| retweet_count_cluster_4           |   |
| quote_count_cluster_4             |   |
| retweet_count_suspended_users     |   |
| quote_count_suspended_users       |   |

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

### Youtube Videos
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
