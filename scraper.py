#!/usr/bin/env python3
"""
YouTube Video Scraper - CLI Tool

Scrapes YouTube videos for metadata, transcripts, and comments.
Outputs data in JSON format.
"""

import sys
import json
import os
from datetime import datetime
from typing import Optional
import click
from colorama import Fore, Style, init

from youtube_utils import extract_video_id, validate_video_id, format_duration
from youtube_api import YouTubeAPIClient
from transcript_scraper import TranscriptScraper

# Initialize colorama for cross-platform colored output
init(autoreset=True)


class YouTubeScraper:
    """
    Main scraper class that coordinates metadata, transcript, and comment scraping.
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the scraper.
        
        Args:
            api_key: YouTube Data API key (optional, defaults to .env)
        """
        self.api_client = YouTubeAPIClient(api_key)
        self.transcript_scraper = TranscriptScraper()
    
    def scrape_video(
        self,
        url: str,
        include_comments: bool = True,
        include_transcript: bool = True,
        comment_limit: int = 100
    ) -> dict:
        """
        Scrape all data for a YouTube video.
        
        Args:
            url: YouTube video URL
            include_comments: Whether to fetch comments
            include_transcript: Whether to fetch transcript
            comment_limit: Maximum number of comments to fetch
            
        Returns:
            Dictionary containing all scraped data
        """
        print(f"\n{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}YouTube Video Scraper{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}\n")
        
        # Extract and validate video ID
        try:
            video_id = extract_video_id(url)
            print(f"{Fore.GREEN}✓ Video ID extracted: {video_id}{Style.RESET_ALL}")
            
            if not validate_video_id(video_id):
                raise ValueError(f"Invalid video ID format: {video_id}")
        except ValueError as e:
            print(f"{Fore.RED}✗ Error: {e}{Style.RESET_ALL}")
            raise
        
        # Initialize result structure
        result = {
            'scrape_info': {
                'scraped_at': datetime.utcnow().isoformat() + 'Z',
                'video_url': f"https://www.youtube.com/watch?v={video_id}",
                'video_id': video_id
            },
            'metadata': None,
            'transcript': None,
            'comments': None,
            'errors': []
        }
        
        # Fetch metadata
        try:
            metadata = self.api_client.get_video_metadata(video_id)
            
            # Add formatted duration
            if metadata.get('duration'):
                duration_info = format_duration(metadata['duration'])
                metadata['duration_formatted'] = duration_info['formatted']
                metadata['duration_seconds'] = duration_info['total_seconds']
            
            result['metadata'] = metadata
            
        except Exception as e:
            error_msg = f"Failed to fetch metadata: {str(e)}"
            print(f"{Fore.RED}✗ {error_msg}{Style.RESET_ALL}")
            result['errors'].append(error_msg)
            # If metadata fails, we can't continue
            return result
        
        # Fetch transcript
        if include_transcript:
            try:
                transcript_data = self.transcript_scraper.get_transcript(video_id)
                result['transcript'] = transcript_data
            except Exception as e:
                error_msg = f"Failed to fetch transcript: {str(e)}"
                print(f"{Fore.YELLOW}⚠ {error_msg}{Style.RESET_ALL}")
                result['errors'].append(error_msg)
                result['transcript'] = {'available': False, 'reason': str(e)}
        
        # Fetch comments
        if include_comments:
            try:
                comments = self.api_client.get_comments(video_id, max_results=comment_limit)
                result['comments'] = {
                    'total_fetched': len(comments),
                    'limit': comment_limit,
                    'items': comments
                }
            except Exception as e:
                error_msg = f"Failed to fetch comments: {str(e)}"
                print(f"{Fore.YELLOW}⚠ {error_msg}{Style.RESET_ALL}")
                result['errors'].append(error_msg)
                result['comments'] = {'total_fetched': 0, 'items': []}
        
        return result


def save_json(data: dict, output_path: str) -> None:
    """
    Save data to JSON file with pretty formatting.
    
    Args:
        data: Data to save
        output_path: Path to output file
    """
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"\n{Fore.GREEN}✓ Data saved to: {output_path}{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Fore.RED}✗ Error saving file: {e}{Style.RESET_ALL}")
        raise


@click.command()
@click.argument('url')
@click.option(
    '--output', '-o',
    default=None,
    help='Output JSON file path (default: {video_id}_data.json)'
)
@click.option(
    '--no-comments',
    is_flag=True,
    help='Skip fetching comments'
)
@click.option(
    '--no-transcript',
    is_flag=True,
    help='Skip fetching transcript'
)
@click.option(
    '--comment-limit',
    default=100,
    type=int,
    help='Maximum number of comments to fetch (default: 100)'
)
@click.option(
    '--api-key',
    default=None,
    envvar='YOUTUBE_API_KEY',
    help='YouTube Data API key (or set YOUTUBE_API_KEY env var)'
)
def main(url, output, no_comments, no_transcript, comment_limit, api_key):
    """
    YouTube Video Scraper - Extract metadata, transcripts, and comments.
    
    \b
    Examples:
        python scraper.py https://www.youtube.com/watch?v=dQw4w9WgXcQ
        python scraper.py https://youtu.be/dQw4w9WgXcQ -o output.json
        python scraper.py URL --no-comments --comment-limit 50
    """
    try:
        # Initialize scraper
        scraper = YouTubeScraper(api_key=api_key)
        
        # Scrape video
        data = scraper.scrape_video(
            url=url,
            include_comments=not no_comments,
            include_transcript=not no_transcript,
            comment_limit=comment_limit
        )
        
        # Determine output path
        if output is None:
            video_id = data['scrape_info']['video_id']
            output = f"{video_id}_data.json"
        
        # Save to file
        save_json(data, output)
        
        # Print summary
        print(f"\n{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Scraping Summary{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
        
        if data.get('metadata'):
            print(f"Title: {data['metadata']['title']}")
            print(f"Channel: {data['metadata']['channel_title']}")
            print(f"Views: {data['metadata']['view_count']:,}")
            print(f"Likes: {data['metadata']['like_count']:,}")
            
            if data['metadata'].get('duration_formatted'):
                print(f"Duration: {data['metadata']['duration_formatted']}")
        
        if data.get('transcript'):
            if data['transcript'].get('available'):
                print(f"Transcript: ✓ ({data['transcript']['entry_count']} entries)")
            else:
                print(f"Transcript: ✗ ({data['transcript'].get('reason', 'N/A')})")
        
        if data.get('comments'):
            print(f"Comments: {data['comments']['total_fetched']} fetched")
        
        if data.get('errors'):
            print(f"\n{Fore.YELLOW}Warnings/Errors: {len(data['errors'])}{Style.RESET_ALL}")
            for error in data['errors']:
                print(f"  - {error}")
        
        print(f"\n{Fore.GREEN}✓ Scraping complete!{Style.RESET_ALL}\n")
        
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Scraping cancelled by user{Style.RESET_ALL}")
        sys.exit(1)
    except Exception as e:
        print(f"\n{Fore.RED}✗ Fatal error: {e}{Style.RESET_ALL}")
        sys.exit(1)


if __name__ == '__main__':
    main()

