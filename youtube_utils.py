"""
YouTube utility functions for URL parsing and video ID extraction.
"""

import re
from urllib.parse import urlparse, parse_qs


def extract_video_id(url: str) -> str:
    """
    Extract YouTube video ID from various URL formats.
    
    Supports:
    - https://www.youtube.com/watch?v=VIDEO_ID
    - https://youtu.be/VIDEO_ID
    - https://www.youtube.com/embed/VIDEO_ID
    - https://www.youtube.com/v/VIDEO_ID
    
    Args:
        url: YouTube URL string
        
    Returns:
        Video ID string
        
    Raises:
        ValueError: If URL is invalid or video ID cannot be extracted
    """
    if not url or not isinstance(url, str):
        raise ValueError("URL must be a non-empty string")
    
    # Remove whitespace
    url = url.strip()
    
    # Pattern 1: youtu.be/VIDEO_ID
    if 'youtu.be/' in url:
        parsed = urlparse(url)
        video_id = parsed.path.lstrip('/')
        # Remove any query parameters or fragments
        video_id = video_id.split('?')[0].split('#')[0]
        if video_id:
            return video_id
    
    # Pattern 2: youtube.com/watch?v=VIDEO_ID
    if 'youtube.com/watch' in url:
        parsed = urlparse(url)
        query_params = parse_qs(parsed.query)
        if 'v' in query_params and query_params['v']:
            return query_params['v'][0]
    
    # Pattern 3: youtube.com/embed/VIDEO_ID
    if 'youtube.com/embed/' in url:
        match = re.search(r'/embed/([a-zA-Z0-9_-]+)', url)
        if match:
            return match.group(1)
    
    # Pattern 4: youtube.com/v/VIDEO_ID
    if 'youtube.com/v/' in url:
        match = re.search(r'/v/([a-zA-Z0-9_-]+)', url)
        if match:
            return match.group(1)
    
    # If nothing matched, raise error
    raise ValueError(f"Could not extract video ID from URL: {url}")


def validate_video_id(video_id: str) -> bool:
    """
    Validate that a string is a valid YouTube video ID format.
    
    YouTube video IDs are typically 11 characters long and contain
    alphanumeric characters, hyphens, and underscores.
    
    Args:
        video_id: String to validate
        
    Returns:
        True if valid, False otherwise
    """
    if not video_id or not isinstance(video_id, str):
        return False
    
    # YouTube video IDs are 11 characters: letters, numbers, -, _
    pattern = r'^[a-zA-Z0-9_-]{11}$'
    return bool(re.match(pattern, video_id))


def format_duration(duration_iso: str) -> dict:
    """
    Convert ISO 8601 duration to human-readable format.
    
    Args:
        duration_iso: ISO 8601 duration string (e.g., "PT15M33S")
        
    Returns:
        Dictionary with hours, minutes, seconds, and formatted string
    """
    # Parse ISO 8601 duration (PT#H#M#S)
    pattern = r'PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?'
    match = re.match(pattern, duration_iso)
    
    if not match:
        return {
            'hours': 0,
            'minutes': 0,
            'seconds': 0,
            'formatted': '0:00'
        }
    
    hours = int(match.group(1) or 0)
    minutes = int(match.group(2) or 0)
    seconds = int(match.group(3) or 0)
    
    # Format as H:MM:SS or M:SS
    if hours > 0:
        formatted = f"{hours}:{minutes:02d}:{seconds:02d}"
    else:
        formatted = f"{minutes}:{seconds:02d}"
    
    return {
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds,
        'formatted': formatted,
        'total_seconds': hours * 3600 + minutes * 60 + seconds
    }

