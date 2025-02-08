###### strategy
# 1. Use advanced search to learn the searching language
# 2. Use chatgpt to quickly populate dictionaries based on different types of searches
# 3. Copy the url from an example query e.g., hashtag queries and then have chatgpt populate a url dictionary
# 4. Do this for all types of search
# 5. combine into one url dictionary for reference and looping

###### HASHTAG SEARCHES AND URLS ######
# Description: This file contains the search queries for hashtags of target
hashtag_queries = {
    "hashtag_2015": "(#cityandguilds) until:2015-12-31 since:2015-01-01",
    "hashtag_2016": "(#cityandguilds) until:2016-12-31 since:2016-01-01",
    "hashtag_2017": "(#cityandguilds) until:2017-12-31 since:2017-01-01",
    "hashtag_2018": "(#cityandguilds) until:2018-12-31 since:2018-01-01",
    "hashtag_2019": "(#cityandguilds) until:2019-12-31 since:2019-01-01",
    "hashtag_2020": "(#cityandguilds) until:2020-12-31 since:2020-01-01",
    "hashtag_2021": "(#cityandguilds) until:2021-12-31 since:2021-01-01",
    "hashtag_2022": "(#cityandguilds) until:2022-12-31 since:2022-01-01",
    "hashtag_2023": "(#cityandguilds) until:2023-12-31 since:2023-01-01",
    "hashtag_2024": "(#cityandguilds) until:2024-12-31 since:2024-01-01",
    "hashtag_2025": "(#cityandguilds) until:2025-12-31 since:2025-01-01",
}

hashtag_urls = {
    "hashtag_2015": "https://x.com/search?q=(%23cityandguilds)%20until%3A2015-12-31%20since%3A2015-01-01&src=typed_query&f=top",
    "hashtag_2016": "https://x.com/search?q=(%23cityandguilds)%20until%3A2016-12-31%20since%3A2016-01-01&src=typed_query&f=top",
    "hashtag_2017": "https://x.com/search?q=(%23cityandguilds)%20until%3A2017-12-31%20since%3A2017-01-01&src=typed_query&f=top",
    "hashtag_2018": "https://x.com/search?q=(%23cityandguilds)%20until%3A2018-12-31%20since%3A2018-01-01&src=typed_query&f=top",
    "hashtag_2019": "https://x.com/search?q=(%23cityandguilds)%20until%3A2019-12-31%20since%3A2019-01-01&src=typed_query&f=top",
    "hashtag_2020": "https://x.com/search?q=(%23cityandguilds)%20until%3A2020-12-31%20since%3A2020-01-01&src=typed_query&f=top",
    "hashtag_2021": "https://x.com/search?q=(%23cityandguilds)%20until%3A2021-12-31%20since%3A2021-01-01&src=typed_query&f=top",
    "hashtag_2022": "https://x.com/search?q=(%23cityandguilds)%20until%3A2022-12-31%20since%3A2022-01-01&src=typed_query&f=top",
    "hashtag_2023": "https://x.com/search?q=(%23cityandguilds)%20until%3A2023-12-31%20since%3A2023-01-01&src=typed_query&f=top",
    "hashtag_2024": "https://x.com/search?q=(%23cityandguilds)%20until%3A2024-12-31%20since%3A2024-01-01&src=typed_query&f=top",
    "hashtag_2025": "https://x.com/search?q=(%23cityandguilds)%20until%3A2025-12-31%20since%3A2025-01-01&src=typed_query&f=top",
}

###### FROM SEARCHES AND URLS ######
# Description: This file contains the search queries for tweets from target
from_queries = {
    "from_2015": "(from:cityandguilds) until:2015-12-31 since:2015-01-01",
    "from_2016": "(from:cityandguilds) until:2016-12-31 since:2016-01-01",
    "from_2017": "(from:cityandguilds) until:2017-12-31 since:2017-01-01",
    "from_2018": "(from:cityandguilds) until:2018-12-31 since:2018-01-01",
    "from_2019": "(from:cityandguilds) until:2019-12-31 since:2019-01-01",
    "from_2020": "(from:cityandguilds) until:2020-12-31 since:2020-01-01",
    "from_2021": "(from:cityandguilds) until:2021-12-31 since:2021-01-01",
    "from_2022": "(from:cityandguilds) until:2022-12-31 since:2022-01-01",
    "from_2023": "(from:cityandguilds) until:2023-12-31 since:2023-01-01",
    "from_2024": "(from:cityandguilds) until:2024-12-31 since:2024-01-01",
    "from_2025": "(from:cityandguilds) until:2025-12-31 since:2025-01-01",
}

from_urls = {
    "from_2015": "https://x.com/search?q=(from%3Acityandguilds)%20until%3A2015-12-31%20since%3A2015-01-01&src=typed_query&f=top",
    "from_2016": "https://x.com/search?q=(from%3Acityandguilds)%20until%3A2016-12-31%20since%3A2016-01-01&src=typed_query&f=top",
    "from_2017": "https://x.com/search?q=(from%3Acityandguilds)%20until%3A2017-12-31%20since%3A2017-01-01&src=typed_query&f=top",
    "from_2018": "https://x.com/search?q=(from%3Acityandguilds)%20until%3A2018-12-31%20since%3A2018-01-01&src=typed_query&f=top",
    "from_2019": "https://x.com/search?q=(from%3Acityandguilds)%20until%3A2019-12-31%20since%3A2019-01-01&src=typed_query&f=top",
    "from_2020": "https://x.com/search?q=(from%3Acityandguilds)%20until%3A2020-12-31%20since%3A2020-01-01&src=typed_query&f=top",
    "from_2021": "https://x.com/search?q=(from%3Acityandguilds)%20until%3A2021-12-31%20since%3A2021-01-01&src=typed_query&f=top",
    "from_2022": "https://x.com/search?q=(from%3Acityandguilds)%20until%3A2022-12-31%20since%3A2022-01-01&src=typed_query&f=top",
    "from_2023": "https://x.com/search?q=(from%3Acityandguilds)%20until%3A2023-12-31%20since%3A2023-01-01&src=typed_query&f=top",
    "from_2024": "https://x.com/search?q=(from%3Acityandguilds)%20until%3A2024-12-31%20since%3A2024-01-01&src=typed_query&f=top",
    "from_2025": "https://x.com/search?q=(from%3Acityandguilds)%20until%3A2025-12-31%20since%3A2025-01-01&src=typed_query&f=top",
}

###### MENTION SEARCHES AND URLS ######
# Description: This file contains the search queries for tweets mentioning target
mention_queries = {
    "mention_2015": "(@cityandguilds) until:2015-12-31 since:2015-01-01",
    "mention_2016": "(@cityandguilds) until:2016-12-31 since:2016-01-01",
    "mention_2017": "(@cityandguilds) until:2017-12-31 since:2017-01-01",
    "mention_2018": "(@cityandguilds) until:2018-12-31 since:2018-01-01",
    "mention_2019": "(@cityandguilds) until:2019-12-31 since:2019-01-01",
    "mention_2020": "(@cityandguilds) until:2020-12-31 since:2020-01-01",
    "mention_2021": "(@cityandguilds) until:2021-12-31 since:2021-01-01",
    "mention_2022": "(@cityandguilds) until:2022-12-31 since:2022-01-01",
    "mention_2023": "(@cityandguilds) until:2023-12-31 since:2023-01-01",
    "mention_2024": "(@cityandguilds) until:2024-12-31 since:2024-01-01",
    "mention_2025": "(@cityandguilds) until:2025-12-31 since:2025-01-01",
}

mention_urls = {
    "mention_2015": "https://x.com/search?q=(%40cityandguilds)%20until%3A2015-12-31%20since%3A2015-01-01&src=typed_query&f=top",
    "mention_2016": "https://x.com/search?q=(%40cityandguilds)%20until%3A2016-12-31%20since%3A2016-01-01&src=typed_query&f=top",
    "mention_2017": "https://x.com/search?q=(%40cityandguilds)%20until%3A2017-12-31%20since%3A2017-01-01&src=typed_query&f=top",
    "mention_2018": "https://x.com/search?q=(%40cityandguilds)%20until%3A2018-12-31%20since%3A2018-01-01&src=typed_query&f=top",
    "mention_2019": "https://x.com/search?q=(%40cityandguilds)%20until%3A2019-12-31%20since%3A2019-01-01&src=typed_query&f=top",
    "mention_2020": "https://x.com/search?q=(%40cityandguilds)%20until%3A2020-12-31%20since%3A2020-01-01&src=typed_query&f=top",
    "mention_2021": "https://x.com/search?q=(%40cityandguilds)%20until%3A2021-12-31%20since%3A2021-01-01&src=typed_query&f=top",
    "mention_2022": "https://x.com/search?q=(%40cityandguilds)%20until%3A2022-12-31%20since%3A2022-01-01&src=typed_query&f=top",
    "mention_2023": "https://x.com/search?q=(%40cityandguilds)%20until%3A2023-12-31%20since%3A2023-01-01&src=typed_query&f=top",
    "mention_2024": "https://x.com/search?q=(%40cityandguilds)%20until%3A2024-12-31%20since%3A2024-01-01&src=typed_query&f=top",
    "mention_2025": "https://x.com/search?q=(%40cityandguilds)%20until%3A2025-12-31%20since%3A2025-01-01&src=typed_query&f=top",
}

###### TO SEARCHES AND URLS ######
# Description: This file contains the search queries for tweets to target
to_queries = {
    "to_2015": "(to:cityandguilds) until:2015-12-31 since:2015-01-01",
    "to_2016": "(to:cityandguilds) until:2016-12-31 since:2016-01-01",
    "to_2017": "(to:cityandguilds) until:2017-12-31 since:2017-01-01",
    "to_2018": "(to:cityandguilds) until:2018-12-31 since:2018-01-01",
    "to_2019": "(to:cityandguilds) until:2019-12-31 since:2019-01-01",
    "to_2020": "(to:cityandguilds) until:2020-12-31 since:2020-01-01",
    "to_2021": "(to:cityandguilds) until:2021-12-31 since:2021-01-01",
    "to_2022": "(to:cityandguilds) until:2022-12-31 since:2022-01-01",
    "to_2023": "(to:cityandguilds) until:2023-12-31 since:2023-01-01",
    "to_2024": "(to:cityandguilds) until:2024-12-31 since:2024-01-01",
    "to_2025": "(to:cityandguilds) until:2025-12-31 since:2025-01-01",
}

to_urls = {
    "to_2015": "https://x.com/search?q=(to%3Acityandguilds)%20until%3A2015-12-31%20since%3A2015-01-01&src=typed_query&f=top",
    "to_2016": "https://x.com/search?q=(to%3Acityandguilds)%20until%3A2016-12-31%20since%3A2016-01-01&src=typed_query&f=top",
    "to_2017": "https://x.com/search?q=(to%3Acityandguilds)%20until%3A2017-12-31%20since%3A2017-01-01&src=typed_query&f=top",
    "to_2018": "https://x.com/search?q=(to%3Acityandguilds)%20until%3A2018-12-31%20since%3A2018-01-01&src=typed_query&f=top",
    "to_2019": "https://x.com/search?q=(to%3Acityandguilds)%20until%3A2019-12-31%20since%3A2019-01-01&src=typed_query&f=top",
    "to_2020": "https://x.com/search?q=(to%3Acityandguilds)%20until%3A2020-12-31%20since%3A2020-01-01&src=typed_query&f=top",
    "to_2021": "https://x.com/search?q=(to%3Acityandguilds)%20until%3A2021-12-31%20since%3A2021-01-01&src=typed_query&f=top",
    "to_2022": "https://x.com/search?q=(to%3Acityandguilds)%20until%3A2022-12-31%20since%3A2022-01-01&src=typed_query&f=top",
    "to_2023": "https://x.com/search?q=(to%3Acityandguilds)%20until%3A2023-12-31%20since%3A2023-01-01&src=typed_query&f=top",
    "to_2024": "https://x.com/search?q=(to%3Acityandguilds)%20until%3A2024-12-31%20since%3A2024-01-01&src=typed_query&f=top",
    "to_2025": "https://x.com/search?q=(to%3Acityandguilds)%20until%3A2025-12-31%20since%3A2025-01-01&src=typed_query&f=top",
}

###### HPHRASE SEARCHES AND URLS ######
# Description: This file contains the search queries  tweets with target search phrase
phrase_queries = {
    "phrase_2015": '"city and guilds" until:2015-12-31 since:2015-01-01',
    "phrase_2016": '"city and guilds" until:2016-12-31 since:2016-01-01',
    "phrase_2017": '"city and guilds" until:2017-12-31 since:2017-01-01',
    "phrase_2018": '"city and guilds" until:2018-12-31 since:2018-01-01',
    "phrase_2019": '"city and guilds" until:2019-12-31 since:2019-01-01',
    "phrase_2020": '"city and guilds" until:2020-12-31 since:2020-01-01',
    "phrase_2021": '"city and guilds" until:2021-12-31 since:2021-01-01',
    "phrase_2022": '"city and guilds" until:2022-12-31 since:2022-01-01',
    "phrase_2023": '"city and guilds" until:2023-12-31 since:2023-01-01',
    "phrase_2024": '"city and guilds" until:2024-12-31 since:2024-01-01',
    "phrase_2025": '"city and guilds" until:2025-12-31 since:2025-01-01',
}

phrase_urls = {
    "phrase_2015": "https://x.com/search?q=%22city%20and%20guilds%22%20until%3A2015-12-31%20since%3A2015-01-01&src=typed_query&f=top",
    "phrase_2016": "https://x.com/search?q=%22city%20and%20guilds%22%20until%3A2016-12-31%20since%3A2016-01-01&src=typed_query&f=top",
    "phrase_2017": "https://x.com/search?q=%22city%20and%20guilds%22%20until%3A2017-12-31%20since%3A2017-01-01&src=typed_query&f=top",
    "phrase_2018": "https://x.com/search?q=%22city%20and%20guilds%22%20until%3A2018-12-31%20since%3A2018-01-01&src=typed_query&f=top",
    "phrase_2019": "https://x.com/search?q=%22city%20and%20guilds%22%20until%3A2019-12-31%20since%3A2019-01-01&src=typed_query&f=top",
    "phrase_2020": "https://x.com/search?q=%22city%20and%20guilds%22%20until%3A2020-12-31%20since%3A2020-01-01&src=typed_query&f=top",
    "phrase_2021": "https://x.com/search?q=%22city%20and%20guilds%22%20until%3A2021-12-31%20since%3A2021-01-01&src=typed_query&f=top",
    "phrase_2022": "https://x.com/search?q=%22city%20and%20guilds%22%20until%3A2022-12-31%20since%3A2022-01-01&src=typed_query&f=top",
    "phrase_2023": "https://x.com/search?q=%22city%20and%20guilds%22%20until%3A2023-12-31%20since%3A2023-01-01&src=typed_query&f=top",
    "phrase_2024": "https://x.com/search?q=%22city%20and%20guilds%22%20until%3A2024-12-31%20since%3A2024-01-01&src=typed_query&f=top",
    "phrase_2025": "https://x.com/search?q=%22city%20and%20guilds%22%20until%3A2025-12-31%20since%3A2025-01-01&src=typed_query&f=top",
}


# COMBINE ALL URLS INTO ONE DICTIONARY
all_search_urls = {}

# List of all individual URL dictionaries
url_dictionaries = [hashtag_urls, from_urls, mention_urls, to_urls, phrase_urls]

# Merge dictionaries into one
for url_dict in url_dictionaries:
    all_search_urls.update(url_dict)

# Print to verify
for key, value in all_search_urls.items():
    print(f"{key}: {value}")

# Convert to DataFrame
feeder_df = pd.DataFrame(list(all_search_urls.items()), columns=["tag", "url"])
# Extract year suffix from tag names to feed the env_suffix argument of def page_scraper
feeder_df["env_suffix"] = feeder_df["tag"].str.extract(r"(\d{4})")

# Display the structure of the DataFrame
print(feeder_df.info())
print(feeder_df.head())
print(feeder_df.dtypes)

# Get the absolute path to the workspace root (one level up from the script's directory)
workspace_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Define the output directory at the workspace root
output_dir = os.path.join(workspace_root, "output")

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Define output file path
output_path = os.path.join(output_dir, "feeder_df.csv")
# Save output to CSV
feeder_df.to_csv(output_path, index=False)
