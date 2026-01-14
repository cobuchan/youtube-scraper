# YouTube Moonshot Program — PRD

## Overview

An idea-to-execution pipeline that converts YouTube content from trusted sources into actionable outputs:

1. **Moonshot Ideas** — "Someone should build X" → PRD with user stories → Spawn new projects
2. **Strategy Intel** — Marketing, growth, distribution tactics → Synopsis + recommendations → Apply to existing projects

## Goals

- Surface buildable software opportunities from high-signal sources
- Filter for Claude Code / our tech stack compatibility
- Reduce time from "heard an idea" to "shipping MVP"
- Build institutional knowledge through strategy intel

## Non-Goals

- Not a general YouTube archiver
- Not for entertainment content
- Not for ideas requiring heavy capital, physical products, or large teams

## Target Users

Primary: The two of us (Co-CEOs of this moonshot factory)

## Core Features

### 1. Transcript Extraction
- Input: YouTube URL
- Process: yt-dlp extracts auto-generated or manual captions
- Output: Clean text transcript

### 2. Content Routing
Automatically classify videos:
- **Moonshot** — Contains "someone should build," business ideas, product opportunities
- **Strategy** — Marketing tactics, growth frameworks, distribution channels, AI capabilities

### 3. Moonshot Pipeline
```
Transcript → PRD Extraction → User Stories → JSON Export
```
Output: `docs/prds/[slug].md` + `docs/prds/[slug].json`

Includes:
- Problem/solution extraction
- MVP scoping
- User stories with acceptance criteria
- Tech stack fit score (1-10)
- Viability assessment

### 4. Strategy Pipeline
```
Transcript → Synopsis → Recommendations → Priority Actions
```
Output: `docs/strategy/[slug]/synopsis.md` + `transcript.txt`

Includes:
- Key tactics extracted
- Applicability matrix (SaaS, e-commerce, etc.)
- Prioritized recommendations
- Signal-to-noise assessment

### 5. Source Funnels (Implemented)
Trusted sources organized by tier:
- **Tier 1 (Ideas):** Chris Koerner, Greg Isenberg
- **Tier 2 (Strategy + Technical):** Nathaniel Whittemore, Simon Willison, Swyx, Lenny Rachitsky

### 6. Auto-Fetch & Inbox (Planned)
```
Session Start → Fetch RSS from sources → Filter new videos →
Extract transcripts → Route to pipeline → Present in inbox
```
Components:
- `scripts/fetch-new.py` — RSS fetch + transcript extraction
- `data/processed.json` — Track what's been processed
- `docs/inbox/` — Unprocessed findings await review

---

## User Stories

### Transcript Processing

#### STORY-001: Extract transcript from URL
**As a** user
**I want to** provide a YouTube URL and get a clean transcript
**So that** I can process it through the pipeline

**Acceptance Criteria:**
- [x] Accepts YouTube URL in any format
- [x] Extracts auto-generated or manual captions
- [x] Cleans VTT formatting to plain text
- [x] Returns video metadata (title, channel, date)

**Priority:** P0
**Status:** Complete

---

#### STORY-002: Route content to correct pipeline
**As a** user
**I want** Claude to automatically determine if a video is a moonshot idea or strategy intel
**So that** it gets processed appropriately

**Acceptance Criteria:**
- [x] Analyzes transcript content
- [x] Routes to PRD pipeline if contains buildable ideas
- [x] Routes to Strategy pipeline if contains tactics/frameworks
- [x] Clearly communicates routing decision

**Priority:** P0
**Status:** Complete

---

### Moonshot Pipeline

#### STORY-003: Generate PRD from transcript
**As a** user
**I want to** convert a "moonshot idea" transcript into a structured PRD
**So that** I can evaluate and potentially build it

**Acceptance Criteria:**
- [x] Extracts core idea (one sentence)
- [x] Identifies problem/solution
- [x] Defines MVP scope ruthlessly
- [x] Generates user stories with acceptance criteria
- [x] Scores tech stack fit (1-10)
- [x] Provides honest viability assessment
- [ ] Outputs both Markdown and JSON formats

**Priority:** P0
**Status:** Skill built, not yet tested with real moonshot video

---

### Strategy Pipeline

#### STORY-004: Generate synopsis from transcript
**As a** user
**I want to** convert a strategy/tactics video into actionable recommendations
**So that** I can apply insights to existing projects

**Acceptance Criteria:**
- [x] Extracts specific tactics (not vague advice)
- [x] Creates applicability matrix
- [x] Prioritizes recommendations (High/Medium/Low)
- [x] Provides honest signal-to-noise assessment
- [x] Stores transcript for reference

**Priority:** P0
**Status:** Complete (tested with Neil Patel video)

---

### Automation

#### STORY-005: Auto-fetch new videos from sources
**As a** user
**I want** new videos from trusted sources to be automatically fetched
**So that** I see fresh opportunities when I start a session

**Acceptance Criteria:**
- [ ] Fetches RSS feeds from all Tier 1/2 sources
- [ ] Filters for videos not yet processed
- [ ] Extracts transcripts automatically
- [ ] Routes through appropriate pipeline
- [ ] Presents summary in inbox

**Priority:** P1
**Status:** Planned (not yet built)

---

#### STORY-006: Track processed videos
**As a** user
**I want** the system to remember what's been processed
**So that** I don't see duplicates

**Acceptance Criteria:**
- [ ] Maintains `data/processed.json` with video IDs
- [ ] Checks before processing new videos
- [ ] Allows manual reset if needed

**Priority:** P1
**Status:** Planned

---

## Technical Requirements

### Dependencies
- `yt-dlp` — Transcript extraction
- Python 3.x — Scripting
- Claude Code — Processing and analysis

### Data Schema
See `docs/prd-schema.md` for full JSON schema

### File Structure
```
youtube/
├── scripts/
│   └── fetch-new.py      # RSS fetch automation
├── data/
│   └── processed.json    # Tracking
├── docs/
│   ├── prds/             # Moonshot PRDs
│   ├── strategy/         # Strategy synopses
│   ├── inbox/            # Unprocessed findings
│   ├── prd-schema.md     # JSON schema
│   └── sources.md        # Source funnels
└── skills/
    ├── transcript-to-prd.md
    └── transcript-to-strategy.md
```

---

## Open Questions

1. Should we add a "confidence score" to routing decisions?
2. How often should auto-fetch run? Session start only, or scheduled?
3. Do we need a web UI eventually, or is CLI + docs sufficient?

---

*Last updated: 2026-01-14*
