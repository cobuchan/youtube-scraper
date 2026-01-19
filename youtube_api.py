"""
YouTube Data API v3 wrapper for fetching video metadata and comments.
"""

import os
from typing import Dict, List, Optional
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dotenv import load_dotenv
from colorama import Fore, Style

# Load environment variables
load_dotenv()


class YouTubeAPIClient:
    """
    Wrapper for YouTube Data API v3.
    
    Handles authentication and provides methods for fetching video data.
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize YouTube API client.
        
        Args:
            api_key: YouTube Data API key (defaults to YOUTUBE_API_KEY env var)
        """
        self.api_key = api_key or os.getenv('YOUTUBE_API_KEY')
        
        if not self.api_key:
            raise ValueError(
                "YouTube API key not found. "
                "Set YOUTUBE_API_KEY in .env file or pass api_key parameter."
            )
        
        try:
            self.youtube = build('youtube', 'v3', developerKey=self.api_key)
            print(f"{Fore.GREEN}✓ YouTube API client initialized{Style.RESET_ALL}")
        except Exception as e:
            raise RuntimeError(f"Failed to initialize YouTube API client: {e}")
    
    def get_video_metadata(self, video_id: str) -> Dict:
        """
        Fetch comprehensive metadata for a YouTube video.
        
        Args:
            video_id: YouTube video ID
            
        Returns:
            Dictionary containing video metadata
            
        Raises:
            HttpError: If API request fails
            ValueError: If video not found or is private
        """
        try:
            print(f"{Fore.CYAN}📊 Fetching video metadata...{Style.RESET_ALL}")
            
            request = self.youtube.videos().list(
                part='snippet,contentDetails,statistics,status',
                id=video_id
            )
            response = request.execute()
            
            if not response.get('items'):
                raise ValueError(f"Video not found or is private: {video_id}")
            
            video_data = response['items'][0]
            snippet = video_data.get('snippet', {})
            content_details = video_data.get('contentDetails', {})
            statistics = video_data.get('statistics', {})
            status = video_data.get('status', {})
            
            metadata = {
                'video_id': video_id,
                'title': snippet.get('title'),
                'description': snippet.get('description'),
                'channel_id': snippet.get('channelId'),
                'channel_title': snippet.get('channelTitle'),
                'published_at': snippet.get('publishedAt'),
                'duration': content_details.get('duration'),
                'dimension': content_details.get('dimension'),
                'definition': content_details.get('definition'),
                'caption': content_details.get('caption'),
                'licensed_content': content_details.get('licensedContent'),
                'category_id': snippet.get('categoryId'),
                'tags': snippet.get('tags', []),
                'view_count': int(statistics.get('viewCount', 0)),
                'like_count': int(statistics.get('likeCount', 0)),
                'comment_count': int(statistics.get('commentCount', 0)),
                'privacy_status': status.get('privacyStatus'),
                'embeddable': status.get('embeddable'),
                'thumbnail_url': snippet.get('thumbnails', {}).get('high', {}).get('url'),
            }
            
            print(f"{Fore.GREEN}✓ Metadata fetched: {metadata['title'][:50]}...{Style.RESET_ALL}")
            return metadata
            
        except HttpError as e:
            if e.resp.status == 403:
                raise ValueError(
                    "API quota exceeded or invalid API key. "
                    "Check your API key and quota at "
                    "https://console.cloud.google.com/apis/dashboard"
                )
            elif e.resp.status == 404:
                raise ValueError(f"Video not found: {video_id}")
            else:
                raise RuntimeError(f"YouTube API error: {e}")
    
    def get_comments(
        self, 
        video_id: str, 
        max_results: int = 100,
        order: str = 'relevance'
    ) -> List[Dict]:
        """
        Fetch comments for a YouTube video.
        
        Args:
            video_id: YouTube video ID
            max_results: Maximum number of comments to fetch
            order: Sort order ('time', 'relevance')
            
        Returns:
            List of comment dictionaries
            
        Raises:
            HttpError: If API request fails
            ValueError: If comments are disabled
        """
        try:
            print(f"{Fore.CYAN}💬 Fetching comments (limit: {max_results})...{Style.RESET_ALL}")
            
            comments = []
            request = self.youtube.commentThreads().list(
                part='snippet',
                videoId=video_id,
                maxResults=min(max_results, 100),  # API limit per request
                order=order,
                textFormat='plainText'
            )
            
            while request and len(comments) < max_results:
                response = request.execute()
                
                for item in response.get('items', []):
                    if len(comments) >= max_results:
                        break
                    
                    top_comment = item['snippet']['topLevelComment']['snippet']
                    comment_data = {
                        'comment_id': item['id'],
                        'author': top_comment.get('authorDisplayName'),
                        'author_channel_id': top_comment.get('authorChannelId', {}).get('value'),
                        'text': top_comment.get('textDisplay'),
                        'like_count': top_comment.get('likeCount', 0),
                        'published_at': top_comment.get('publishedAt'),
                        'updated_at': top_comment.get('updatedAt'),
                        'reply_count': item['snippet'].get('totalReplyCount', 0),
                    }
                    comments.append(comment_data)
                
                # Get next page if available and we need more comments
                if len(comments) < max_results and 'nextPageToken' in response:
                    request = self.youtube.commentThreads().list(
                        part='snippet',
                        videoId=video_id,
                        maxResults=min(max_results - len(comments), 100),
                        order=order,
                        textFormat='plainText',
                        pageToken=response['nextPageToken']
                    )
                else:
                    request = None
            
            print(f"{Fore.GREEN}✓ Fetched {len(comments)} comments{Style.RESET_ALL}")
            return comments
            
        except HttpError as e:
            if e.resp.status == 403:
                # Comments might be disabled
                print(f"{Fore.YELLOW}⚠ Comments are disabled for this video{Style.RESET_ALL}")
                return []
            else:
                raise RuntimeError(f"Error fetching comments: {e}")
    
    def get_channel_info(self, channel_id: str) -> Dict:
        """
        Fetch channel information.
        
        Args:
            channel_id: YouTube channel ID
            
        Returns:
            Dictionary containing channel information
        """
        try:
            request = self.youtube.channels().list(
                part='snippet,statistics',
                id=channel_id
            )
            response = request.execute()
            
            if not response.get('items'):
                return {}
            
            channel = response['items'][0]
            snippet = channel.get('snippet', {})
            statistics = channel.get('statistics', {})
            
            return {
                'channel_id': channel_id,
                'title': snippet.get('title'),
                'description': snippet.get('description'),
                'subscriber_count': int(statistics.get('subscriberCount', 0)),
                'video_count': int(statistics.get('videoCount', 0)),
                'view_count': int(statistics.get('viewCount', 0)),
                'thumbnail_url': snippet.get('thumbnails', {}).get('high', {}).get('url'),
            }
        except HttpError:
            return {}

