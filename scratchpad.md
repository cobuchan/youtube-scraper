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

## Respawn Command

```bash
cd /Users/cobuchan/Projects/youtube && claude
```

**Respawn prompt:**
> Read scratchpad.md, patterns.md, and your coordinator agent files to get up to speed. We have 2 strategy intels and 1 moonshot PRD processed. Continue processing YouTube videos from Tier 1/2 sources and updating patterns.md as we identify recurring themes.
