# YouTube Scraper

A powerful Python CLI tool to scrape YouTube video content including metadata, transcripts, and comments.

## Features

- 📊 **Video Metadata**: Title, description, views, likes, upload date, channel info, duration, category
- 📝 **Transcripts**: Fetch video captions/subtitles with timestamps
- 💬 **Comments**: Scrape comments with pagination support
- 📄 **JSON Output**: Clean, structured JSON export
- 🛡️ **Error Handling**: Graceful handling of private videos, disabled comments, missing captions

## Requirements

- Python 3.8 or higher
- YouTube Data API v3 key (free from Google Cloud Console)

## Installation

### 1. Clone/Navigate to Project Directory

```bash
cd youtube-scrape
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
```

### 3. Activate Virtual Environment

**macOS/Linux:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Set Up YouTube API Key

#### Getting Your API Key

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the **YouTube Data API v3**:
   - Navigate to "APIs & Services" > "Library"
   - Search for "YouTube Data API v3"
   - Click "Enable"
4. Create credentials:
   - Go to "APIs & Services" > "Credentials"
   - Click "Create Credentials" > "API Key"
   - Copy your new API key
5. (Optional but recommended) Restrict your API key:
   - Click on your API key to edit it
   - Under "API restrictions", select "Restrict key"
   - Choose "YouTube Data API v3"
   - Save

#### Configure Your API Key

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and replace `your_api_key_here` with your actual API key:
   ```
   YOUTUBE_API_KEY=AIzaSyD...your_actual_key_here
   ```

⚠️ **NEVER commit your `.env` file to version control!** It's already in `.gitignore`.

## Usage

### Basic Usage

Scrape a YouTube video (fetches metadata, transcript, and comments):

```bash
# Activate virtual environment first
source venv/bin/activate

# Scrape a video
python scraper.py https://www.youtube.com/watch?v=VIDEO_ID
```

### Command Line Options

```bash
# Show help
python scraper.py --help

# Specify output file
python scraper.py URL -o my_output.json

# Skip comments
python scraper.py URL --no-comments

# Skip transcript
python scraper.py URL --no-transcript

# Limit number of comments (default: 100)
python scraper.py URL --comment-limit 50

# Combine options
python scraper.py URL -o output.json --no-comments --comment-limit 200
```

### Supported URL Formats

The scraper supports all standard YouTube URL formats:
- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`
- `https://www.youtube.com/embed/VIDEO_ID`
- `https://www.youtube.com/v/VIDEO_ID`

### Example Output

The scraper creates a JSON file with the following structure:

```json
{
  "scrape_info": {
    "scraped_at": "2025-10-22T12:00:00Z",
    "video_url": "https://www.youtube.com/watch?v=VIDEO_ID",
    "video_id": "VIDEO_ID"
  },
  "metadata": {
    "title": "Video Title",
    "description": "Video description...",
    "channel_title": "Channel Name",
    "view_count": 1000000,
    "like_count": 50000,
    "comment_count": 1000,
    "duration_formatted": "15:33",
    "published_at": "2025-01-01T00:00:00Z",
    ...
  },
  "transcript": {
    "available": true,
    "language": "English",
    "entry_count": 150,
    "full_text": "Complete transcript text...",
    "transcript": [
      {
        "text": "Hello everyone",
        "start": 0.0,
        "duration": 2.5
      },
      ...
    ]
  },
  "comments": {
    "total_fetched": 100,
    "items": [
      {
        "author": "John Doe",
        "text": "Great video!",
        "like_count": 50,
        "published_at": "2025-01-02T00:00:00Z",
        ...
      },
      ...
    ]
  }
}
```

## API Quota Information

The YouTube Data API has a default quota of **10,000 units per day**. Typical costs per video:
- Video metadata: ~1-3 units
- Comments (100): ~1-5 units
- Total per video: ~5-10 units

You can scrape approximately **1,000-2,000 videos per day** with the default quota.

## Project Status

🚧 **Under Development**

Current progress tracked in `.cursor/scratchpad.md`

## Troubleshooting

### API Key Issues
- **Error: "YouTube API key not found"**
  - Ensure your API key is correctly copied to `.env`
  - Make sure the file is named exactly `.env` (not `.env.txt`)
  - Verify the format: `YOUTUBE_API_KEY=your_key_here`

- **Error: "API quota exceeded"**
  - Check your quota at https://console.cloud.google.com/apis/dashboard
  - Default quota is 10,000 units/day
  - Wait until the next day or request a quota increase

- **Error: "Invalid API key"**
  - Verify YouTube Data API v3 is enabled in Google Cloud Console
  - Try creating a new API key
  - Check that there are no extra spaces in your `.env` file

### Transcript Issues
- **"Transcripts are disabled for this video"**
  - The video creator has disabled captions
  - Use `--no-transcript` flag to skip transcript fetching
  
- **"No transcript found"**
  - Some videos don't have captions/subtitles available
  - Auto-generated captions may not be available for all videos
  - Try a different video or use `--no-transcript`

### Comments Issues
- **"Comments are disabled for this video"**
  - The video creator has disabled comments
  - The scraper will continue and save other data
  - Use `--no-comments` flag to skip comment fetching

### Video Issues
- **"Video not found or is private"**
  - Check that the URL is correct
  - Verify the video is public (not private or unlisted)
  - The video may have been deleted

### Common Errors
- **Import errors**: Make sure you activated the virtual environment (`source venv/bin/activate`)
- **Permission denied**: Run `chmod +x scraper.py` to make the script executable
- **JSON decode error**: Check that your `.env` file doesn't have any special characters

## License

MIT License - Free to use and modify

## Development Notes

- Uses conventional commits: `feat/*`, `fix/*`, `chore/*`
- Never commit `.env` files
- Debug output included for verification

