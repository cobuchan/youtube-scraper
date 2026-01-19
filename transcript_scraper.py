"""
YouTube transcript/caption scraper using youtube-transcript-api.
Updated for youtube-transcript-api v1.2.3+
"""

from typing import List, Dict, Optional
from youtube_transcript_api import YouTubeTranscriptApi
from colorama import Fore, Style


class TranscriptScraper:
    """
    Handles fetching and formatting YouTube video transcripts.
    """
    
    def __init__(self):
        """Initialize the transcript API client."""
        self.api = YouTubeTranscriptApi()
    
    def get_transcript(
        self,
        video_id: str,
        languages: Optional[List[str]] = None
    ) -> Dict:
        """
        Fetch transcript/captions for a YouTube video.
        
        Args:
            video_id: YouTube video ID
            languages: Preferred languages list (defaults to ['en'])
            
        Returns:
            Dictionary containing transcript data and metadata
            
        Raises:
            TranscriptsDisabled: If video has no transcripts
            NoTranscriptFound: If requested language not available
            VideoUnavailable: If video doesn't exist
        """
        if languages is None:
            languages = ['en']
        
        try:
            print(f"{Fore.CYAN}📝 Fetching transcript...{Style.RESET_ALL}")
            
            # Fetch transcript using new API (v1.2.3+)
            try:
                # Get transcript data - new API returns list of transcript snippets
                transcript_data = self.api.fetch(video_id, languages=languages)
                
                # Get available transcripts info
                available_transcripts = self.api.list(video_id)
                
                # Determine if auto-generated based on available transcripts
                is_auto_generated = True
                language = 'English'
                language_code = 'en'
                
                if available_transcripts:
                    # Get info about the transcript we're using
                    for trans in available_transcripts:
                        if trans.language_code in languages or trans.language_code == 'en':
                            is_auto_generated = trans.is_generated
                            language = trans.language
                            language_code = trans.language_code
                            break
                
                if is_auto_generated:
                    print(f"{Fore.YELLOW}⚠ Using auto-generated transcript ({language}){Style.RESET_ALL}")
                else:
                    print(f"{Fore.GREEN}✓ Found manual transcript ({language}){Style.RESET_ALL}")
                
            except Exception as e:
                # If preferred language fails, try default
                print(f"{Fore.YELLOW}⚠ Preferred language not found, trying default...{Style.RESET_ALL}")
                transcript_data = self.api.fetch(video_id)
                language = 'Unknown'
                language_code = 'unknown'
                is_auto_generated = True
            
            # Convert transcript data to dict format
            # New API returns FetchedTranscriptSnippet objects with .text, .start, .duration
            transcript_list = []
            for entry in transcript_data:
                transcript_list.append({
                    'text': entry.text,
                    'start': entry.start,
                    'duration': entry.duration
                })
            
            # Format the transcript
            full_text = ' '.join([entry['text'] for entry in transcript_list])
            
            result = {
                'available': True,
                'language': language,
                'language_code': language_code,
                'is_auto_generated': is_auto_generated,
                'transcript': transcript_list,  # List of {text, start, duration}
                'full_text': full_text,
                'entry_count': len(transcript_list),
                'duration_seconds': sum(entry['duration'] for entry in transcript_list)
            }
            
            print(f"{Fore.GREEN}✓ Transcript fetched: {len(transcript_list)} entries{Style.RESET_ALL}")
            return result
            
        except Exception as e:
            error_msg = str(e).lower()
            
            if 'disabled' in error_msg or 'not available' in error_msg:
                print(f"{Fore.YELLOW}⚠ Transcripts are disabled or unavailable for this video{Style.RESET_ALL}")
                return {
                    'available': False,
                    'reason': 'Transcripts disabled or unavailable',
                    'transcript': [],
                    'full_text': ''
                }
            
            print(f"{Fore.RED}✗ Error fetching transcript: {e}{Style.RESET_ALL}")
            return {
                'available': False,
                'reason': f'Error: {str(e)}',
                'transcript': [],
                'full_text': ''
            }
    
    def get_available_transcripts(self, video_id: str) -> List[Dict]:
        """
        List all available transcripts for a video.
        
        Args:
            video_id: YouTube video ID
            
        Returns:
            List of available transcript information
        """
        try:
            transcript_list = self.api.list(video_id)
            available = []
            
            for transcript in transcript_list:
                available.append({
                    'language': transcript.language,
                    'language_code': transcript.language_code,
                    'is_generated': transcript.is_generated,
                    'is_translatable': transcript.is_translatable
                })
            
            return available
        except:
            return []

