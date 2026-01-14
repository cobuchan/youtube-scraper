# Scratchpad - YouTube Moonshot Program

## Background and Motivation

**What this is:** An idea-to-execution pipeline. We scrape YouTube/podcast transcripts from trusted sources and convert them into:
1. **Moonshot Ideas** → PRD with stories → New projects
2. **Strategy Intel** → Synopsis + recommendations → Apply to existing projects

**Partner model:** Coordinator is Co-CEO with full agency. Opinionated, forceful, outcome-focused.

**Tech stack fit:** Claude Code, Next.js, React, Vercel, Supabase, Firebase.

## Key Decisions

1. **Dual pipeline** — Moonshot Ideas (PRDs) vs Strategy Intel (synopses)
2. **Source funnels** — Tier 1 (Koerner, Isenberg), Tier 2 (Whittemore, Willison, Swyx, Lenny)
3. **Tech stack filtering** — Score ideas on Claude Code buildability
4. **Automation approach** — RSS feeds + script (planned, not built yet)
5. **Audio transcription** — Need to install Whisper for podcast-only content

## High-level Task Breakdown

### Phase 1: Core Infrastructure ✓
- [x] Project setup, git repo
- [x] Dual pipeline (PRD + Strategy skills)
- [x] Source funnels document (6 sources)
- [x] Tech stack fit criteria in PRD schema

### Phase 2: Validation ✓
- [x] First strategy intel: Neil Patel marketing trends
- [x] First moonshot PRD: Free Vertical CRM (Koerner/Cannon)
- [x] Pipeline tested end-to-end

### Phase 3: Tooling (NEXT)
- [ ] Install Whisper for audio transcription (podcast-only episodes)
- [ ] RSS fetch script (`scripts/fetch-new.py`)
- [ ] Processed tracking (`data/processed.json`)
- [ ] Session start workflow

## Completed Work

### Strategy Intel
- **Neil Patel - 8 Marketing Trends 2026** → `docs/strategy/8-marketing-trends-2026/`
  - Key tactics: ManyChat on-platform capture, AI validation, live content, multi-language

### Moonshot PRDs
- **Free Vertical CRM** → `docs/prds/free-vertical-crm.md`
  - Source: Koerner/Cannon "Stupid Simple Apps" interview
  - Idea: Free CRM for vertical (dentists, etc.), monetize via payment processing
  - Viability: 7/10, Tech fit: 8/10
  - Key insight: "Sell it before you have it"

## Pending Work

### Episode 264 (Koerner)
- Title: "Companies Are Panic Paying for This Skill"
- Status: Only on Apple Podcasts (no YouTube version found)
- Blocker: Need Whisper installed to transcribe audio
- Likely topic: Facebook ads or AI skills (based on related DOAC interview)

### Automation Script
- Design complete (RSS + fetch + route + inbox)
- Not yet built — user said hold off, do manually first

## Current Session Summary

**Date**: 2026-01-14

**What we accomplished:**
- Full project setup from scratch
- Source funnels with 6 trusted sources
- Dual pipeline (ideas vs strategy) validated
- First strategy intel processed (Neil Patel)
- First moonshot PRD created (Free Vertical CRM)
- Discovered Apple Podcasts needs Whisper for transcription

**Blockers:**
- Whisper not installed — can't transcribe podcast-only episodes

**Next session should:**
1. Install Whisper: `pip install openai-whisper`
2. Transcribe Episode 264 (Koerner - panic paying skill)
3. Consider building RSS automation script
4. Process more videos from trusted sources

## Lessons Learned This Session

- Apple Podcasts = audio only, need Whisper for transcription
- YouTube videos can be removed (ToS) — always handle gracefully
- Some podcast episodes aren't on YouTube yet — need audio fallback
- Pre-sell validation ("sell before you build") is a key pattern from Will Cannon

## Quick Links

- **PRD Schema**: `docs/prd-schema.md`
- **Sources**: `docs/sources.md`
- **Strategy Intel**: `docs/strategy/`
- **PRDs**: `docs/prds/`
- **Skills**: `skills/`

## Respawn Command

```bash
cd /Users/cobuchan/Projects/youtube && claude
```

**Respawn prompt:**
> Read scratchpad.md and continue where we left off. First priority: install Whisper (`pip install openai-whisper`) so we can transcribe podcast episodes. Then process Episode 264 from Koerner. After that, discuss whether to build the RSS automation or process more videos manually.
