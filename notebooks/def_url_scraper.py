from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import time
import os
import pandas as pd

"""
    Scrapes tweets from a specified Twitter profile.

    This function automates the login process and retrieves tweets dynamically,
    extracting relevant metadata such as tweet URLs, timestamps, engagement metrics,
    hashtags, mentions, and links.

    The function is designed as part of a project for a charity organization 
    focused on improving the experiences of young people and students in the UK.
    By analyzing tweet data, we aim to better understand conversations and trends 
    that impact their growth and opportunities. Do not use this script for malicious purposes.

    Args:
        target_url (str): The URL of the Twitter profile to scrape.
        env_suffix (str): The suffix used to retrieve the correct environment variables
                          for login credentials (e.g., 'MAIN', '2015').

    Returns:
        pd.DataFrame: A DataFrame containing extracted tweet data.
"""


def url_scraper(target_url, env_suffix):
    # Load environment variables
    load_dotenv()
    EMAIL = os.getenv(f"EMAIL_{env_suffix}")
    USERNAME = os.getenv(f"USERNAME_{env_suffix}")
    PASSWORD = os.getenv("PASSWORD")

    if not EMAIL or not USERNAME or not PASSWORD:
        raise ValueError("Twitter credentials are not set. Check your .env file!")

    # Setup Chrome WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # Open Twitter Login Page
        driver.get("https://x.com/login")

        # Wait for username field
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "text"))
        )

        # Enter Email (First Login Step)
        username_input = driver.find_element(By.NAME, "text")
        username_input.send_keys(EMAIL)
        username_input.send_keys(Keys.RETURN)

        # Handle extra login prompt
        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.NAME, "text"))
            )
            second_input = driver.find_element(By.NAME, "text")
            second_input.send_keys(USERNAME)
            second_input.send_keys(Keys.RETURN)
        except:
            print("No second login prompt detected, proceeding...")

        # Wait for Password field
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )

        # Enter Password
        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys(PASSWORD)
        password_input.send_keys(Keys.RETURN)

        # Wait for homepage to load
        time.sleep(5)

        # Go to the target Twitter profile
        driver.get(target_url)

        # Ensure tweets load fully before proceeding
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "article"))
        )

        # Initialize an empty DataFrame to store tweets dynamically
        tweet_df = pd.DataFrame(columns=["Tweet URL", "Created At", "Text"])

        # Scroll dynamically until 20 seconds have passed without new tweets
        SCROLL_PAUSE_TIME = 5  # Buffer time after each scroll
        prev_tweets_count = 0
        max_wait_time = 60  # Reduced for testing
        start_time = time.time()

        while True:
            # Scroll down by a larger amount
            driver.execute_script("window.scrollBy(0, 3000);")
            time.sleep(SCROLL_PAUSE_TIME)

            # Extract tweets so far
            soup = BeautifulSoup(driver.page_source, "html.parser")
            tweets = soup.find_all("article")

            new_tweet_data = []
            for tweet in tweets:
                try:
                    # Extract the first <a> tag that contains '/status/'
                    tweet_link_tag = tweet.find(
                        "a", href=lambda href: href and "/status/" in href
                    )
                    tweet_url = (
                        f"https://x.com{tweet_link_tag['href']}"
                        if tweet_link_tag
                        else None
                    )

                    # Extract tweet creation time
                    date_tag = tweet.find("time")
                    created_at = date_tag["datetime"] if date_tag else "Unknown"

                    # Extract Tweet ID
                    tweet_id = tweet.get("data-tweet-id", "Unknown")

                    # Likes, Retweets, Replies
                    likes_tag = tweet.find("div", {"data-testid": "like"})
                    likes = likes_tag.get_text(strip=True) if likes_tag else "Unknown"

                    retweets_tag = tweet.find("div", {"data-testid": "retweet"})
                    retweets = (
                        retweets_tag.get_text(strip=True) if retweets_tag else "Unknown"
                    )

                    replies_tag = tweet.find("div", {"data-testid": "reply"})
                    replies = (
                        replies_tag.get_text(strip=True) if replies_tag else "Unknown"
                    )

                    # Hashtags & Mentions
                    hashtags = [
                        tag.get_text(strip=True)
                        for tag in tweet.find_all("a")
                        if "#" in tag.get_text()
                    ]
                    mentions = [
                        tag.get_text(strip=True)
                        for tag in tweet.find_all("a")
                        if "@" in tag.get_text()
                    ]

                    # URLs in tweet
                    urls = [
                        tag.get("href", "Unknown")
                        for tag in tweet.find_all("a")
                        if "http" in tag.get("href", "")
                    ]

                    # Extract tweet text
                    tweet_text = (
                        tweet.find("div", {"lang": True}).get_text(strip=True)
                        if tweet.find("div", {"lang": True})
                        else "Unknown"
                    )

                    # Only add the tweet if it's not already in the DataFrame
                    if tweet_url and tweet_url not in tweet_df["Tweet URL"].values:
                        new_tweet_data.append(
                            {
                                "Tweet URL": tweet_url,
                                "Created At": created_at,
                                "Text": tweet_text,
                                "Tweet ID": tweet_id,
                                "Likes": likes,
                                "Retweets": retweets,
                                "Replies": replies,
                                "Hashtags": ", ".join(hashtags),
                                "Mentions": ", ".join(mentions),
                                "URLs": ", ".join(urls),
                            }
                        )
                except Exception as e:
                    print(f"Error extracting tweet: {e}")
                    continue

            # Convert new tweets to a DataFrame
            new_tweet_df = pd.DataFrame(new_tweet_data)

            # Append new tweets to the existing DataFrame
            if not new_tweet_df.empty:
                tweet_df = pd.concat([tweet_df, new_tweet_df], ignore_index=True)

            # Check if new tweets were loaded
            if len(tweet_df) == prev_tweets_count:
                elapsed_time = time.time() - start_time
                if elapsed_time >= max_wait_time:
                    print("No new tweets for 20 seconds. Stopping scrolling.")
                    break
            else:
                start_time = time.time()

            prev_tweets_count = len(tweet_df)

        return tweet_df

    finally:
        driver.quit()


#### Example Usage ####
# Define the target profile URL
target_url = "https://x.com/cityandguilds"

# Run the scraper
tweets_df = url_scraper(target_url, env_suffix="MAIN")
