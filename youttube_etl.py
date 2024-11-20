# -*- coding: utf-8 -*-

import pandas as pd
import os
import googleapiclient.discovery

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    # Set up API credentials and service
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyC5lp9noMkJxJpl0aR9EjrXcFZkvpkRVNY"  # Add your API key here

    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=DEVELOPER_KEY)

    # Video ID you want to fetch comments for
    video_id = "q8q3OFFfY6c"

    # Fetch the comment threads for the given video ID
    request = youtube.commentThreads().list(
        part="snippet,replies",  # We need snippet and replies data
        videoId=video_id,
        maxResults=100  # Fetch a max of 100 comments per request
    )
    response = request.execute()

    # Initialize list to hold refined data
    comments_list = []

    # Loop through the response and extract relevant information
    for item in response['items']:
        comment_data = item['snippet']['topLevelComment']['snippet']
        comment_author = comment_data['authorDisplayName']
        comment_text = comment_data['textDisplay']
        like_count = comment_data['likeCount']
        published_at = comment_data['publishedAt']
        # You can also extract reply count if needed
        reply_count = item['snippet']['totalReplyCount']

        # Store extracted data in a dictionary
        refined_comment = {
            'author': comment_author,
            'text': comment_text,
            'like_count': like_count,
            'published_at': published_at,
            'reply_count': reply_count,
            'video_id': video_id  # To associate the comments with the video
        }
        
        comments_list.append(refined_comment)

    # Convert the list of comments into a DataFrame
    df = pd.DataFrame(comments_list)

    # Save the DataFrame to a CSV file
    df.to_csv('s3://de-project2-youtube/youtube_comments.csv', index=False)

    print("Comments saved to youtube_comments.csv")

if __name__ == "__main__":
    main()
