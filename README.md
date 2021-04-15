# VoterFraud2020
VoterFraud2020 is a multi-modal Twitter dataset with 7.6M tweets and 25.6M retweets from 2.6M users related to voter fraud claims.

- [The Associated Paper on arXiv](https://arxiv.org/abs/2101.08210)
- [voterfraud2020.io](http://voterfraud2020.io), interactive web application for exploring the dataset
- [Figshare dataset publication](https://doi.org/10.6084/m9.figshare.13571084) with digital object identifier (DOI) **10.6084/m9.figshare.13571084**
- [github/sTechLab/VoterFraud2020-analysis](https://github.com/sTechLab/VoterFraud2020-analysis), the code behind the data analysis
  
*coming soon*
- github/sTechLab/twitter-stream, the twitter streaming code
<!-- - [github/sTechLab/twitter-stream](https://github.com/sTechLab/twitter-stream), the twitter streaming code -->

### Table of contents
- [VoterFraud2020](#voterfraud2020)
    - [Table of contents](#table-of-contents)
- [Hydrating the data](#hydrating-the-data)
    - [Hydrating using Hydrator (GUI)](#hydrating-using-hydrator-gui)
    - [Hydrating using Twarc (CLI, python 3)](#hydrating-using-twarc-cli-python-3)
- [Data description](#data-description)
  - [Tweets (7.6M)](#tweets-76m)
  - [Retweets (25.6M)](#retweets-256m)
  - [Users (2.6M)](#users-26m)
  - [Images](#images)
  - [URLs](#urls)
  - [Youtube Videos](#youtube-videos)


<img src="https://storage.googleapis.com/voter-fraud-2020/img/logo-ct-jacobs-transparent.png" alt="CT Jacobs" width="250px">

# Hydrating the data
The tweets and user objects in the dataset can be hydrated using [Twarc](https://github.com/DocNow/twarc) or [Hydrator](https://github.com/DocNow/hydrator).

**Note:** tweets from suspended users will not be available for hydration. We believe it's in the [public interest](https://www.propublica.org/article/why-we-published-parler-users-videos-capitol-attack) to make these tweets available. We will share those tweets with published academic researchers; email us for details. 

### Hydrating using [Hydrator](https://github.com/DocNow/hydrator) (GUI)
Navigate to the [Hydrator github repository](https://github.com/DocNow/hydrator) and follow the instructions for installation in their README.
To use the GUI, tweet IDs must first be extracted to a tweet id file from the CSVs in this repository.

### Hydrating using [Twarc](https://github.com/DocNow/twarc) (CLI, python 3)
First install Twarc and tqdm
```
pip3 install twarc tqdm
```

Configure Twarc with your Twitter API tokens (note you must [apply](https://developer.twitter.com/en/apply-for-access) for a Twitter developer account first in order to obtain the needed tokens). You can also configure the API tokens in the script, if unable to configure through CLI. 
```
twarc configure
```

Run the script. The hydrated Tweets will be stored in the same folder as the Tweet-ID file, and is saved as a compressed jsonl file
```
python3 hydrate.py
```

*This guide was inspired by the [#Election2020 Dataset Repository](https://github.com/echen102/us-pres-elections-2020#how-to-hydrate)*.

# Data description
The columns in the data are described below. See [the paper](https://arxiv.org/abs/2101.08210)
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
| user_active_status                | The active status of the tweet's author (as of January 10th). Values: 'active', 'suspended', 'deleted' (not found)  |
| retweet_count_metadata            | The number of retweets the tweet has received according to the tweet object's metadata (as of December 16th). |
| quote_count_metadata              | The number of quotes the tweet has received according to the tweet object's metadata (as of December 16th).  |
| retweet_count_by_community_X      | The number of retweets the tweet received from users in community X (X=0-4). |
| quote_count_by_community_X        | The number of quotes the tweet received from users in community X (X=0-4).  |
| retweet_count_by_suspended_users  | The number of retweets the tweet received from suspended users.  |
| quote_count_by_suspended_users    | The number of quotes the tweet received from suspended users.  |

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
| user_active_status                        | The active status of the user (as of January 10th). Values: 'active', 'suspended', 'deleted' (not found) |
| closeness_centrality_detractor_cluster    | Normalized closeness centrality of the top 10,000 users in the detractor cluster (computed using [Networkit](https://networkit.github.io/dev-docs/python_api/centrality.html#networkit.centrality.TopCloseness)).  |
| closeness_centrality_promoter_cluster     | Normalized closeness centrality of the top 10,000 users in the promoter cluster (computed using [Networkit](https://networkit.github.io/dev-docs/python_api/centrality.html#networkit.centrality.TopCloseness)). |
| retweet_count_by_community_X              | Aggregated count of the retweets the user received from other users in community X (X=0-4). |
| quote_count_by_community_X                | Aggregated count of the quotes the user received from other users in community X (X=0-4).  |
| retweet_count_by_suspended_users          | Aggregated count of the retweets the user received from suspended users.  |
| quote_count_by_suspended_users            | Aggregated count of the quotes the user received from suspended users.  |

## Images
Total count: 167,696

- [images.csv](data/images.csv)

The image perceptual hash values were calculated using the [ImageHash python package](https://github.com/JohannesBuchner/imagehash).

| Data Column                       | Description |
| -------------                     | ------------- |
| unique_id                         | Unique identifier of the image. |
| tweet_id                          | The ID of the tweet that contained the image.  |
| a_hash                            | The [Average hash](https://www.hackerfactor.com/blog/index.php?/archives/432-Looks-Like-It.html) of the image. |
| p_hash                            | The [Perceptive hash](https://www.hackerfactor.com/blog/index.php?/archives/432-Looks-Like-It.html) of the image.  |
| w_hash                            | The [Wavelet hash](https://fullstackml.com/wavelet-image-hash-in-python-3504fdd282b5) of the image.  |

## URLs
- [urls.csv](data/urls.csv)

| Data Column                       | Description |
| -------------                     | ------------- |
| url                               | The URL. |
| domain                            | The domain of the URL. |
| tweet_count                       | Aggregated count of the tweets that contained the URL.  |
| retweet_count_metadata            | Aggregated count of the retweets that tweets containing the URL received according to the tweet object's metadata (as of December 16th). |
| quote_count_metadata              | Aggregated count of the quotes that tweets containing the URL received according to the tweet object's metadata (as of December 16th).  |
| tweet_count_by_community_X        | Aggregated count of tweets that contained the URL by users in community X (X=0-4). |
| retweet_count_by_community_X      | Aggregated count of the retweets that tweets containing the URL received from users in community X (X=0-4). |
| quote_count_by_community_X        | Aggregated count of the quotes that tweets containing the URL received from users in community X (X=0-4).  |
| tweet_count_by_suspended_users        | Aggregated count of tweets that contained the URL by suspended users. |
| retweet_count_by_suspended_users  | Aggregated count of the retweets that tweets containing the URL received from suspended users.  |
| quote_count_by_suspended_users    | Aggregated count of the quotes that tweets containing the URL received from suspended users.  |

## Youtube Videos
- [youtube_videos.csv](data/youtube_videos.csv)

| Data Column                       | Description |
| -------------                     | ------------- |
| video_id                          | ID of the Youtube video.  |
| video_title                       | Title of the video (as of January 1st). |
| channel_id                        | Channel ID of the channel where the video was posted.  |
| channel_title                     | Channel title of the channel where the video was posted (as of January 1st).  |
| published_at                      | Timestamp of when the video was published. |
| tweet_count                       | Aggregated count of the tweets that contained the video.  |
| retweet_count_metadata            | Aggregated count of the retweets that tweets containing the video received according to the tweet object's metadata (as of December 16th). |
| quote_count_metadata              | Aggregated count of the quotes that tweets containing the video received according to the tweet object's metadata (as of December 16th).  |
| tweet_count_by_community_X        | Aggregated count of tweets that contained the video by users in community X (X=0-4). |
| retweet_count_by_community_X      | Aggregated count of the retweets that tweets containing the video received from users in community X (X=0-4). |
| quote_count_by_community_X        | Aggregated count of the quotes that tweets containing the video received from users in community X (X=0-4).  |
| tweet_count_by_community_X        | Aggregated count of tweets that contained the video by suspended users. |
| retweet_count_by_suspended_users  | Aggregated count of the retweets that tweets containing the video received from suspended users.  |
| quote_count_by_suspended_users    | Aggregated count of the quotes that tweets containing the video received from suspended users.  |
