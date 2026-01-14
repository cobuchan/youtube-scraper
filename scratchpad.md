# Scratchpad - YouTube Moonshot Program

<!--
INSTRUCTIONS FOR CLAUDE:
- Do not rename sections
- Append instead of deleting prior content (mark outdated content as such)
- Update this file frequently during work sessions
- Add lessons learned immediately when bugs/corrections occur
- Keep under 150 lines; move verbose history to docs/sessions/[topic].md
- Only coordinator writes to this file (subagents report back verbally)
-->

## Background and Motivation

**What this is:** An idea-to-execution pipeline. We scrape YouTube transcripts from trusted sources (AI/business influencers) and convert them into actionable outputs:
1. **Moonshot Ideas** → PRD with stories → New projects
2. **Strategy Intel** → Synopsis + recommendations → Apply to existing projects

**Partner model:** Coordinator is Co-CEO with full agency. Opinionated, forceful, outcome-focused.

**Tech stack fit:** Claude Code, Next.js, React, Vercel, Supabase, Firebase. Prioritize ideas buildable in days.

## Key Decisions

1. **Dual pipeline** — Moonshot Ideas (PRDs) vs Strategy Intel (synopses)
2. **Source funnels** — Tier 1 (Koerner, Isenberg), Tier 2 (Whittemore, Willison, Swyx, Lenny)
3. **Tech stack filtering** — Score ideas on Claude Code buildability
4. **Automation approach** — RSS feeds + script (not full MCP yet)

## High-level Task Breakdown

### Phase 1: Core Infrastructure ✓
- [x] Project setup, git repo
- [x] Dual pipeline (PRD + Strategy skills)
- [x] Source funnels document
- [x] Tech stack fit criteria in PRD schema

### Phase 2: Automation (IN PROGRESS)
- [ ] RSS fetch script (`scripts/fetch-new.py`)
- [ ] Processed tracking (`data/processed.json`)
- [ ] Inbox for unprocessed findings (`docs/inbox/`)
- [ ] Session start workflow

### Phase 3: Refinement (FUTURE)
- [ ] Test with multiple real videos
- [ ] Iterate on PRD extraction quality
- [ ] Consider MCP if script approach limits us

## Project Status Board

### Completed ✓
- [x] Git repo initialized
- [x] Transcript→PRD skill
- [x] Transcript→Strategy skill
- [x] PRD schema with tech stack fit
- [x] Source funnels (6 trusted sources)
- [x] First strategy intel: Neil Patel marketing trends

### In Progress 🔄
- [ ] RSS automation script

### Pending 📋
- [ ] First moonshot PRD (need working video URL)
- [ ] Session start hook

## Current Session

**Date**: 2026-01-14

**Accomplished:**
- Full project setup from scratch
- Dual pipeline design (ideas vs strategy)
- Source funnels with 6 trusted sources
- Processed first video (Neil Patel → strategy intel)
- One dead video URL (removed by YouTube)
- Starting automation build

**Next:**
- Build RSS fetch script
- Test with real channel feeds
- Process first moonshot idea

## Quick Links

- **PRD Schema**: `docs/prd-schema.md`
- **Sources**: `docs/sources.md`
- **Strategy Intel**: `docs/strategy/`
- **PRDs**: `docs/prds/`
- **Inbox**: `docs/inbox/` (pending)
- **Scripts**: `scripts/` (building)
