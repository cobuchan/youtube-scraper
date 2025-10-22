# YouTube Scraper Project

## Background and Motivation

Building a Python-based CLI tool to scrape YouTube video content including:
- Video metadata (title, description, views, likes, upload date, channel info)
- Transcripts/captions
- Comments

Output will be in JSON format. Tool will process one video at a time (max 45 minutes duration).

The tool will use the YouTube Data API v3 (requires API key) for reliable, official access to YouTube data.

## Key Challenges and Analysis

1. **API Key Setup**: User needs to obtain YouTube Data API key from Google Cloud Console
2. **API Quota Limits**: YouTube Data API has daily quotas (default 10,000 units/day)
   - Reading video details: ~1-3 units
   - Reading comments: ~1 unit per request
   - Should be sufficient for moderate use
3. **Transcript Access**: YouTube API doesn't provide transcripts directly; will need `youtube-transcript-api` library
4. **Comment Pagination**: Videos may have thousands of comments; need to handle pagination
5. **Error Handling**: Handle various edge cases:
   - Invalid URLs
   - Private/deleted videos
   - Videos without captions
   - Videos with disabled comments
   - API quota exceeded
6. **Environment Security**: API key must be stored in `.env` file (never committed)

## High-level Task Breakdown

### Task 1: Setup Project Structure & Dependencies
**Success Criteria:**
- Python virtual environment created
- `requirements.txt` with all dependencies (google-api-python-client, youtube-transcript-api, python-dotenv)
- `.env.example` file created (template for API key)
- `.gitignore` configured to exclude `.env` files
- `README.md` with basic project description

### Task 2: Provide YouTube API Key Setup Instructions
**Success Criteria:**
- Clear step-by-step instructions in README for obtaining YouTube Data API v3 key
- Instructions for creating `.env` file with API key
- User confirms API key obtained and configured

### Task 3: Implement Core Video Metadata Scraper
**Success Criteria:**
- Function to extract video ID from YouTube URL
- Function to fetch video metadata using YouTube Data API:
  - Title
  - Description
  - View count
  - Like count
  - Upload date
  - Channel name & ID
  - Duration
  - Category
- Proper error handling for invalid URLs and API errors
- Unit test coverage for URL parsing

### Task 4: Implement Transcript Scraper
**Success Criteria:**
- Function to fetch video transcript using `youtube-transcript-api`
- Handle multiple caption languages (prefer English, fallback to auto-generated)
- Error handling for videos without captions
- Include timestamps in transcript data

### Task 5: Implement Comments Scraper
**Success Criteria:**
- Function to fetch top-level comments
- Handle comment pagination (fetch all comments or configurable limit)
- Include comment metadata:
  - Author name
  - Comment text
  - Like count
  - Published date
  - Reply count
- Error handling for videos with disabled comments

### Task 6: Build CLI Interface
**Success Criteria:**
- Clean CLI using `argparse` or `click`
- Required argument: YouTube video URL
- Optional flags:
  - `--output` / `-o`: Specify output file path (default: `{video_id}_data.json`)
  - `--no-comments`: Skip comments
  - `--no-transcript`: Skip transcript
  - `--comment-limit`: Limit number of comments (default: 100)
- Display progress indicators during scraping
- Helpful error messages

### Task 7: Implement JSON Output Formatter
**Success Criteria:**
- Structured JSON output with sections:
  - `metadata`
  - `transcript`
  - `comments`
- Pretty-printed JSON (indented, readable)
- Include scrape timestamp
- Handle missing data gracefully (null/empty arrays)

### Task 8: Testing & Documentation
**Success Criteria:**
- Manual test with real YouTube video (user performs)
- README includes:
  - Installation instructions
  - API key setup guide
  - Usage examples
  - Expected output format example
  - Troubleshooting section
- Debug output (console logs showing progress)
- All edge cases documented in Lessons

## Project Status Board

- [x] Task 1: Setup Project Structure & Dependencies ✓
- [x] Task 2: Provide YouTube API Key Setup Instructions ✓
- [x] Task 3: Implement Core Video Metadata Scraper ✓
- [x] Task 4: Implement Transcript Scraper ✓
- [x] Task 5: Implement Comments Scraper ✓
- [x] Task 6: Build CLI Interface ✓
- [x] Task 7: Implement JSON Output Formatter ✓
- [ ] Task 8: Testing & Documentation (ready for user testing)

## Current Status / Progress Tracking

**Status**: Tasks 1-7 COMPLETE ✓ - Ready for User Testing (Task 8)

**Completed:**
- ✅ Task 1: Project structure, dependencies, virtual environment
- ✅ Task 2: User configured `.env` file with YouTube API key - verified working
- ✅ Task 3: Core video metadata scraper implemented
  - Created `youtube_utils.py` - URL parsing and video ID extraction
  - Created `youtube_api.py` - YouTube Data API wrapper
  - Supports all metadata fields (title, views, likes, duration, etc.)
  - Duration formatting (ISO 8601 to human-readable)
- ✅ Task 4: Transcript scraper implemented
  - Created `transcript_scraper.py`
  - Supports manual and auto-generated transcripts
  - Multi-language support with fallback
  - Timestamps included in output
- ✅ Task 5: Comments scraper implemented
  - Pagination support for large comment counts
  - Configurable comment limit
  - Handles disabled comments gracefully
- ✅ Task 6: CLI interface built
  - Created `scraper.py` with Click framework
  - Help documentation
  - Options: --output, --no-comments, --no-transcript, --comment-limit
  - Colored terminal output with debug info
- ✅ Task 7: JSON output formatter implemented
  - Structured JSON with sections: scrape_info, metadata, transcript, comments
  - Pretty-printed, indented output
  - Handles missing data gracefully
  - Includes error tracking
- ✅ README updated with complete usage instructions and troubleshooting

**Currently Working On:**
- 🔄 Task 8: Testing & Documentation - awaiting user manual testing

**Git Repository:**
- ✅ Initial commit created with conventional commit message
- ✅ Remote added: https://github.com/cobuchan/youtube-scraper.git
- ✅ Code pushed to GitHub main branch
- Commit: 211c3f1 "feat: initial YouTube scraper implementation"

**Next Steps**: 
- User needs to test with a real YouTube video
- Verify all functionality works correctly
- Address any issues that arise during testing

## Executor's Feedback or Assistance Requests

**Tasks 1-7 Complete - Ready for User Testing:**

All core functionality has been implemented:
- ✅ YouTube URL parsing (supports all formats)
- ✅ Video metadata fetching via YouTube Data API v3
- ✅ Transcript/caption scraping with multi-language support
- ✅ Comment scraping with pagination
- ✅ CLI interface with helpful options
- ✅ JSON output with structured format
- ✅ Error handling for edge cases
- ✅ Debug output with colored terminal messages
- ✅ Complete documentation in README

**Awaiting user manual test with real YouTube video** before marking Task 8 complete.

**Files Created:**
1. `youtube_utils.py` - URL parsing utilities
2. `youtube_api.py` - YouTube Data API wrapper
3. `transcript_scraper.py` - Transcript fetching
4. `scraper.py` - Main CLI application
5. Updated `README.md` with complete usage guide

## Lessons

- User prefers pnpm as package manager for Node.js projects (not applicable here - Python project)
- Never commit `.env` files; always provide `.env.example`
- Include debug output in code for verification
- Conventional commits: feat/*, fix/*, chore/*
- User obtained YouTube API key and configured `.env` successfully
- python-dotenv successfully loads environment variables from `.env` file
- colorama provides cross-platform colored terminal output for better UX
- Click framework provides excellent CLI functionality with built-in help
- YouTube Data API returns ISO 8601 duration format (PT15M33S) - needs parsing
- youtube-transcript-api library works independently of YouTube Data API (no API key needed)
- Structured error handling allows scraper to continue even if one component fails
- Modular design (separate files for utils, API, transcript, main) improves maintainability
- Git repository initialized and pushed to GitHub successfully
- Conventional commit format used: "feat: initial YouTube scraper implementation"

