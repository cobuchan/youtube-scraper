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
- **Isenberg/James - Claude Code Local SEO** → `docs/strategy/claude-code-local-seo/`
  - Key tactics: Boring business arbitrage, SEO audit via ultrathink, location pages, Figma→Anima→Claude workflow

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

**Date**: 2026-01-14 (Session 2)

**What we accomplished:**
- Second strategy intel: Isenberg/James "Claude Code Local SEO" → `docs/strategy/claude-code-local-seo/`
- Created `docs/patterns.md` — institutional knowledge for pattern recognition across sources
- Updated INDEX.md with new docs
- Identified key patterns: Boring Business Arbitrage, Free Product + Adjacent Monetization, Vertical Focus

**Patterns identified so far:**
- Free Product + Adjacent Monetization (Koerner/Cannon)
- Boring Business Arbitrage (Isenberg/James)
- Vertical Focus > Horizontal Features (Koerner/Cannon)
- Claude Code Sweet Spot (Isenberg/James)
- Good SEO = Good GEO (Isenberg/James)

**Blockers:**
- Whisper not installed — can't transcribe podcast-only episodes

**Next session should:**
1. Process more YouTube videos from Tier 1/2 sources
2. Continue building patterns.md as we process content
3. Consider installing Whisper when podcast-only content is needed
4. Watch for: pricing strategies, growth channels beyond SEO, team scaling patterns

## Lessons Learned This Session

- Apple Podcasts = audio only, need Whisper for transcription
- YouTube videos can be removed (ToS) — always handle gracefully
- Some podcast episodes aren't on YouTube yet — need audio fallback
- Pre-sell validation ("sell before you build") is a key pattern from Will Cannon
- VTT transcripts need Python cleaning (timestamps, duplicates) — bash pipes insufficient
- Pattern recognition across sources is distinct from individual PRDs/strategy — hence patterns.md
- Strategy intel is immediately applicable (SEO tactics) while moonshots need more validation

## Quick Links

- **PRD Schema**: `docs/prd-schema.md`
- **Sources**: `docs/sources.md`
- **Patterns**: `docs/patterns.md`
- **Strategy Intel**: `docs/strategy/`
- **PRDs**: `docs/prds/`
- **Skills**: `skills/`

## Respawn Prompt

```
You are the Coordinator for the YouTube Moonshot project.

Read in order:
1. ~/.claude/CLAUDE.md — Global rules
2. ~/.claude/coordinator.md — Your identity and operating model
3. ~/Projects/youtube/scratchpad.md — Current state
4. ~/Projects/youtube/CLAUDE.md — Project rules

MACHINE CONTEXT: This project exists ONLY on the laptop (MacBook Air).
It is NOT on the Mac Mini. All work happens here.

STEP 0 — Sync repo:
Run `git pull origin main` before doing anything else. This laptop may be behind
the Mac Mini. Resolve any conflicts before proceeding.

FIRST TASK — Project Modernization:
Bring this project into the unified Claude Code infrastructure system.

1. CLAUDE.md audit:
   - Ensure it exists and inherits from ~/.claude/CLAUDE.md
   - Add Quick Links table and project-specific rules
   - Document skill-based pipeline patterns (transcript extraction, PRD generation)
   - Current CLAUDE.md exists but lacks inheritance declaration and skill documentation

2. Scratchpad audit:
   - Ensure all 8 mandatory sections
   - Document Phase 3 status and pipeline progress
   - Current scratchpad has most sections but last session was 2026-01-14

3. Project-level configuration:
   - No project-level MCPs needed
   - Verify global infrastructure access (especially skills)
   - Note: skills/ directory has transcript-to-prd.md and transcript-to-strategy.md

4. Report: Update scratchpad with modernization completion status

AFTER MODERNIZATION — Resume Phase 3 Pipeline Work:
- Phase 1 (Core Infrastructure) and Phase 2 (Validation) are complete
- Phase 3 (Tooling) is next: Whisper install, RSS fetch script, processed tracking
- Blocker: Whisper needed for podcast-only episodes (e.g., Koerner Episode 264)
- Immediate value: Process more YouTube videos from Tier 1/2 sources
  (Koerner, Isenberg, Whittemore, Willison, Swyx, Lenny — see docs/sources.md)
- Continue building docs/patterns.md as cross-source themes emerge
- Current output: 2 strategy intels, 1 moonshot PRD, 5 identified patterns
- Watch for pattern gaps: pricing strategies, growth channels beyond SEO,
  team scaling, exit patterns
```
