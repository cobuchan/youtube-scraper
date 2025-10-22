"""
YouTube transcript/caption scraper using youtube-transcript-api.
"""

from typing import List, Dict, Optional
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    TranscriptsDisabled,
    NoTranscriptFound,
    VideoUnavailable
)
from colorama import Fore, Style


class TranscriptScraper:
    """
    Handles fetching and formatting YouTube video transcripts.
    """
    
    @staticmethod
    def get_transcript(
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
            
            # Try to get transcript in preferred languages
            try:
                transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
                
                # Try to find manually created transcript first
                try:
                    transcript = transcript_list.find_manually_created_transcript(languages)
                    is_auto_generated = False
                    print(f"{Fore.GREEN}✓ Found manual transcript ({transcript.language}){Style.RESET_ALL}")
                except:
                    # Fall back to auto-generated
                    transcript = transcript_list.find_generated_transcript(languages)
                    is_auto_generated = True
                    print(f"{Fore.YELLOW}⚠ Using auto-generated transcript ({transcript.language}){Style.RESET_ALL}")
                
                # Fetch the transcript data
                transcript_data = transcript.fetch()
                language = transcript.language
                language_code = transcript.language_code
                
            except NoTranscriptFound:
                # If preferred language not found, get any available transcript
                print(f"{Fore.YELLOW}⚠ Preferred language not found, fetching any available transcript{Style.RESET_ALL}")
                transcript_data = YouTubeTranscriptApi.get_transcript(video_id)
                language = 'Unknown'
                language_code = 'unknown'
                is_auto_generated = True
            
            # Format the transcript
            full_text = ' '.join([entry['text'] for entry in transcript_data])
            
            result = {
                'available': True,
                'language': language,
                'language_code': language_code,
                'is_auto_generated': is_auto_generated,
                'transcript': transcript_data,  # List of {text, start, duration}
                'full_text': full_text,
                'entry_count': len(transcript_data),
                'duration_seconds': sum(entry.get('duration', 0) for entry in transcript_data)
            }
            
            print(f"{Fore.GREEN}✓ Transcript fetched: {len(transcript_data)} entries{Style.RESET_ALL}")
            return result
            
        except TranscriptsDisabled:
            print(f"{Fore.YELLOW}⚠ Transcripts are disabled for this video{Style.RESET_ALL}")
            return {
                'available': False,
                'reason': 'Transcripts disabled',
                'transcript': [],
                'full_text': ''
            }
        
        except NoTranscriptFound:
            print(f"{Fore.YELLOW}⚠ No transcript found for this video{Style.RESET_ALL}")
            return {
                'available': False,
                'reason': 'No transcript available',
                'transcript': [],
                'full_text': ''
            }
        
        except VideoUnavailable:
            print(f"{Fore.RED}✗ Video is unavailable{Style.RESET_ALL}")
            return {
                'available': False,
                'reason': 'Video unavailable',
                'transcript': [],
                'full_text': ''
            }
        
        except Exception as e:
            print(f"{Fore.RED}✗ Error fetching transcript: {e}{Style.RESET_ALL}")
            return {
                'available': False,
                'reason': f'Error: {str(e)}',
                'transcript': [],
                'full_text': ''
            }
    
    @staticmethod
    def get_available_transcripts(video_id: str) -> List[Dict]:
        """
        List all available transcripts for a video.
        
        Args:
            video_id: YouTube video ID
            
        Returns:
            List of available transcript information
        """
        try:
            transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
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

