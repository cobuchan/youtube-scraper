# PRD Schema for Moonshot Ideas

This schema is designed for extracting buildable projects from YouTube transcripts. It's opinionated.

## Core Principle

Influencers ramble. They bury good ideas in 20 minutes of filler. Our job is to extract the **one buildable thing** and make it concrete enough to execute.

## Schema Fields

### 1. Source (metadata)
```json
{
  "source": {
    "video_url": "string",
    "video_title": "string",
    "channel": "string",
    "publish_date": "YYYY-MM-DD",
    "transcript_method": "auto|manual|summary"
  }
}
```

### 2. Idea (one sentence)
What are we building? If you can't say it in one sentence, you don't understand it yet.

```json
{
  "idea": "A CLI tool that converts YouTube transcripts into structured PRDs"
}
```

### 3. Problem
What pain does this solve? Who has this pain? How do they cope today?

```json
{
  "problem": {
    "pain": "string - the actual problem",
    "who_has_it": "string - specific persona",
    "current_solution": "string - how they cope today"
  }
}
```

### 4. Value Proposition
Why would someone use this instead of the current solution?

```json
{
  "value_prop": "string - one sentence, focused on outcome"
}
```

### 5. MVP Scope
The smallest thing we can build to prove this works. NOT the full vision. The first shippable version.

```json
{
  "mvp": {
    "description": "string - what it does",
    "not_included": ["string - explicitly out of scope"],
    "success_metric": "string - how we know it works"
  }
}
```

### 6. User Stories
Actionable, specific, sized. P0 = must have for MVP. P1 = nice to have. P2 = future.

```json
{
  "stories": [
    {
      "id": "STORY-001",
      "as_a": "string - user type",
      "i_want": "string - action",
      "so_that": "string - benefit",
      "acceptance_criteria": ["string"],
      "priority": "P0|P1|P2",
      "size": "S|M|L|XL"
    }
  ]
}
```

### 7. Technical Notes
Rough technical approach. Not a design doc, just enough to know it's feasible.

```json
{
  "technical": {
    "likely_stack": "string - rough guess",
    "key_challenges": ["string"],
    "dependencies": ["string - APIs, data, etc"]
  }
}
```

### 8. Risks
What could kill this? Be honest.

```json
{
  "risks": [
    {
      "risk": "string",
      "likelihood": "low|medium|high",
      "mitigation": "string"
    }
  ]
}
```

### 9. Tech Stack Fit
How well does this translate to Claude Code + our stack?

```json
{
  "tech_fit": {
    "score": "1-10",
    "primary_stack": "string - e.g., Next.js + Supabase",
    "buildable_in_days": true|false,
    "ai_leverage": "none|light|heavy",
    "notes": "string"
  }
}
```

**Scoring guide:**
- 9-10: Perfect fit. Web app, API integrations, data processing.
- 7-8: Good fit. Minor friction (e.g., mobile, real-time).
- 5-6: Possible but stretching. Hardware, heavy ML, marketplaces.
- 1-4: Poor fit. Physical, regulatory, heavy capital.

---

### 10. Viability Assessment
My honest take on whether this is worth building.

```json
{
  "viability": {
    "score": "1-10",
    "reasoning": "string",
    "recommendation": "build|pass|needs_research"
  }
}
```

---

## Full JSON Template

```json
{
  "source": {
    "video_url": "",
    "video_title": "",
    "channel": "",
    "publish_date": "",
    "transcript_method": ""
  },
  "idea": "",
  "problem": {
    "pain": "",
    "who_has_it": "",
    "current_solution": ""
  },
  "value_prop": "",
  "mvp": {
    "description": "",
    "not_included": [],
    "success_metric": ""
  },
  "stories": [],
  "technical": {
    "likely_stack": "",
    "key_challenges": [],
    "dependencies": []
  },
  "risks": [],
  "tech_fit": {
    "score": 0,
    "primary_stack": "",
    "buildable_in_days": false,
    "ai_leverage": "",
    "notes": ""
  },
  "viability": {
    "score": 0,
    "reasoning": "",
    "recommendation": ""
  }
}
```

---

*This schema is a starting point. It will evolve as we learn what works.*
