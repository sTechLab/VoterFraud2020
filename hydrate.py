#!/usr/bin/env python3

#
# This script will walk through all the tweet id files and
# hydrate them with twarc. The line oriented JSON files will
# be placed right next to each tweet id file.
#
# Note: you will need to install twarc, tqdm, and run twarc configure
# from the command line to tell it your Twitter API keys.
#
# Special thanks to Github users echen102, edsu and SamSamhuns for contributing to this file. This file was repurposed from another
# data repository on COVID-19 related tweets : https://github.com/echen102/COVID-19-TweetIDs
#

import gzip
import json
from tqdm import tqdm
from twarc import Twarc
from pathlib import Path

twarc = Twarc()
tweet_data_dirs = ["data/tweets/2020-10", "data/tweets/2020-11", "data/tweets/2020-12"]


def main():
    for tweet_data_dir in tweet_data_dirs:
        for path in Path(tweet_data_dir).iterdir():
            if path.name.endswith(".csv"):
                hydrate(path)

def line_count(filepath):
    """
    Counts number of lines in a file
    """
    i = 0
    with open(filepath, "r") as f:
        for line in f.readlines():
            i += 1
    return i

def extract_tweet_ids(filepath):
    with open(filepath, "r") as f:
        # skip header
        f.readline()
        # Extract ids
        for line in f.readlines():
            yield line[0:line.find(',')]


def hydrate(filepath):
    print("Hydrating {}".format(filepath))

    hydrated_path = filepath.with_suffix(".jsonl.gz")
    if hydrated_path.is_file():
        print("skipping json file already exists: {}".format(hydrated_path))
        return
    print(filepath.name)
    # Subtract header from line count
    num_ids = line_count(filepath) - 1
    print("Hydrating {} tweets".format(num_ids))

    with gzip.open(hydrated_path, "w") as output:
        with tqdm(total=num_ids) as pbar:
            for tweet in twarc.hydrate(extract_tweet_ids(filepath)):
                output.write(json.dumps(tweet).encode("utf8") + b"\n")
                pbar.update(1)


if __name__ == "__main__":
    main()
