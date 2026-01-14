# Skill: Transcript to PRD

Convert a YouTube transcript into a structured PRD for a moonshot project.

## When to Use

When you have a YouTube transcript (pasted or from file) and need to extract a buildable project idea.

## Input

A transcript. Can be:
- Pasted directly in conversation
- Read from a file
- Auto-generated captions (messy but complete)
- Manual captions (cleaner but sometimes summarized)

## Process

### Step 1: Scan for the Core Idea

Most videos bury the actual idea. Look for:
- "Someone should build..." / "There should be a..."
- "The opportunity here is..."
- "What if there was..."
- "I wish someone would..."
- Problems described without solutions (you infer the product)

**Be aggressive about filtering.** If there's no buildable idea, say so. Not every video produces a project.

### Step 2: Validate It's Buildable

Ask:
- Can this be built by a small team in weeks, not years?
- Is the core value prop clear?
- Is there a plausible first customer?

If no to any of these, note it in viability and recommend "pass" or "needs_research."

### Step 3: Extract Problem/Solution

From the rambling, identify:
- The pain point (specific, not vague)
- Who has this pain (persona, not "everyone")
- Current workaround (there's always one)
- Why current workaround sucks

### Step 4: Define MVP Ruthlessly

The influencer will describe a grand vision. Ignore most of it. Find the **smallest thing** that proves the concept.

- What's the one feature that delivers core value?
- What can we cut and still ship something useful?
- What's the success metric? (Be specific: "5 users complete X" not "people like it")

### Step 5: Write Stories

Only P0 stories for MVP. P1/P2 can be brief placeholders.

Each story must be:
- Specific enough to implement
- Small enough to estimate (S/M/L, not XL)
- Testable (clear acceptance criteria)

### Step 6: Assess Viability Honestly

Score 1-10 with real reasoning. Don't be polite.

- 1-3: Don't build this
- 4-6: Maybe, needs more research
- 7-10: Worth building

Factors:
- Is the problem real?
- Is the solution differentiated?
- Can we build it quickly?
- Is there a path to users?

## Output

Produce TWO outputs:

### 1. Human-Readable PRD (Markdown)

Put in `docs/prds/[idea-slug].md`

### 2. Machine-Readable PRD (JSON)

Put in `docs/prds/[idea-slug].json`

Schema is defined in `docs/prd-schema.md`

---

## Example Usage

**User:** Here's a transcript from a video about AI tools: [paste transcript]

**Claude:**
1. Reads transcript
2. Identifies core idea (or says there isn't one)
3. Produces PRD in both formats
4. Gives honest viability assessment

---

## Anti-Patterns

- **Don't invent ideas.** If the transcript doesn't have a buildable idea, say so.
- **Don't be generous.** If the idea is vague or bad, rate it low.
- **Don't scope creep.** MVP is small. Resist adding features.
- **Don't assume technical feasibility.** Flag unknowns as risks.
