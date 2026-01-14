# Coordinator — Project-Specific Lessons

Lessons learned on the YouTube Moonshot Program. These are context-specific insights, not universal patterns.

## Lessons

### Technical

- **2026-01-14**: yt-dlp transcript extraction works well. VTT format needs cleaning (timestamps, duplicates). Python script cleaner than bash pipes for this.
- **2026-01-14**: YouTube videos can be removed (ToS violations) — always handle gracefully, don't assume URLs work.

### Process

- **2026-01-14**: Dual pipeline (Ideas vs Strategy) emerged naturally from first video. Neil Patel video wasn't moonshot material but had strategy value — don't discard, route correctly.
- **2026-01-14**: User provides unstructured input ("add Lenny's") — my job is to keep docs organized. PRD, sources, scratchpad must stay clean even when conversation is messy.
- **2026-01-14**: Build infrastructure (pipelines, schemas) before automation. Validate workflow manually first, automate second.

### Ideas & Filtering

- **2026-01-14**: Not every video produces a moonshot. Marketing advice videos (Neil Patel style) are strategy intel, not ideas. Be honest about classification.
- **2026-01-14**: Tech stack fit filter is critical. Skip physical products, marketplaces, heavy-capital ideas. Prioritize "buildable in days with Claude Code."

### PRD Generation

- **2026-01-14**: PRD skill built but not yet tested on actual moonshot video. First real test pending.

### Sources

- **2026-01-14**: Six sources covers full lifecycle: ideas (Koerner, Isenberg), technical (Willison, Swyx), growth (Lenny), landscape (Whittemore). Gap was technical depth — Willison/Swyx filled it.

### Tooling

- **2026-01-14**: Apple Podcasts = audio only, no transcripts. Need Whisper (`pip install openai-whisper`) to transcribe. YouTube preferred when available (has auto-captions).
- **2026-01-14**: Some podcast episodes aren't on YouTube (or removed for ToS). Need audio transcription fallback.

---

*Updated continuously during project work.*
