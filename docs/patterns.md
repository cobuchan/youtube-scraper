# Patterns — Institutional Knowledge

This document captures meta-learning across all processed content. Not individual ideas or tactics, but **recurring patterns** that improve our ability to evaluate future opportunities.

Updated continuously as we process more sources.

---

## Business Model Patterns

### Free Product + Adjacent Monetization
**Sources:** Koerner/Cannon (Free Vertical CRM)

Give away the core product, monetize through adjacent services with higher margins.
- Free CRM → monetize via payment processing (2.9% on every transaction)
- Free scheduling → monetize via SMS/email marketing
- Free invoicing → monetize via financing/factoring

**Why it works:** Removes acquisition friction, creates lock-in, captures transaction flow.

**Red flags:** Only works if adjacent service has real margin. Don't give away the product if you're just hoping for upsells.

---

### Boring Business Arbitrage
**Sources:** Isenberg/James (Local SEO)

Use modern AI tooling to dominate industries with unsophisticated competition.
- Local service businesses (HVAC, plumbing, mobile repair)
- Competitors have 10-15 year old websites
- Basic Claude Code SEO work outperforms months of traditional agency work

**Why it works:** Arbitrage = your skills vs. their skills. AI-savvy operators crush legacy operators.

**Red flags:** Low barriers mean others will catch up. Build moats (reviews, relationships, brand) fast.

---

### Vertical Focus > Horizontal Features
**Sources:** Koerner/Cannon (Free Vertical CRM)

A mediocre product for one vertical beats a good product for everyone.
- "CRM for dentists" > "CRM for small businesses"
- Vertical focus enables: specific language, targeted marketing, word-of-mouth in tight communities

**Why it works:** Specialists always beat generalists in their niche. Marketing is cheaper and more effective.

**Red flags:** Market size ceiling. Plan expansion path to adjacent verticals.

---

## Tech Stack Patterns

### Claude Code Sweet Spot
**Sources:** Isenberg/James (Local SEO), general observation

Claude Code excels at:
- Website builds (especially with Figma → Anima → React workflow)
- SEO audits and fixes (technical, on-page, content)
- Local/location page generation at scale
- Parallel sub-agents for research/audit tasks

Claude Code struggles with (inferred):
- Real-time systems, complex state management
- Heavy integrations with external APIs
- Anything requiring persistent backend infrastructure beyond Vercel/Supabase

**Buildable in days:** Marketing sites, lead gen, local business sites, content sites, simple SaaS
**Needs more time:** Marketplaces, complex workflows, multi-tenant systems

---

### The Boring Stack
**Sources:** Isenberg/James (Local SEO)

Repeatable stack for local/lead-gen businesses:
```
Figma (design) → Anima (export) → Claude Code (build) → GitHub (version) → Vercel (deploy)
```

Add-ons:
- Google Business Profile (local presence)
- PageSpeed Insights → Claude Code feedback loop
- llms.txt for GEO

---

## Evaluation Heuristics

### Skip These
- **Marketplaces** — chicken-and-egg problem, heavy ops, low margin per transaction
- **Physical products** — inventory, shipping, returns, capital requirements
- **Heavy capital** — anything needing $100K+ before revenue
- **Regulated industries** — healthcare, finance, legal (unless you have domain expertise)

### Prioritize These
- **Buildable in days** — Can Claude Code ship an MVP in <1 week?
- **Clear monetization** — Do you know how you'll charge on day 1?
- **Unsophisticated competition** — Are incumbents running 15-year-old websites?
- **Transaction flow** — Can you insert yourself into money movement?
- **Vertical focus** — Is there a specific audience you can own?

### Questions to Ask Every Idea
1. Who pays, and why would they pay you instead of alternatives?
2. Can I build an MVP with Claude Code in under a week?
3. What's the moat after 12 months?
4. Is competition sophisticated or asleep?
5. Can I validate before building? (Pre-sell, landing page, etc.)

---

## Source Tendencies

Understanding each source's biases helps calibrate their advice.

### Chris Koerner (Tier 1 - Ideas)
- **Strength:** Practical, revenue-focused, boring business expertise
- **Bias:** Loves service businesses, mobile home parks, cash flow plays
- **Watch for:** May underweight tech risk, overweight operational complexity

### Greg Isenberg (Tier 1 - Ideas)
- **Strength:** Product intuition, startup patterns, community building
- **Bias:** Loves communities, AI tools, "startup ideas" framing
- **Watch for:** May overweight novelty, underweight execution difficulty

### James "The Boring Marketer" (Guest)
- **Strength:** SEO deep expertise, Claude Code tactical knowledge
- **Bias:** Very SEO-focused, may oversimplify non-SEO success factors
- **Watch for:** SEO-centric worldview

*(More sources to be added as processed)*

---

## Emerging Themes

Themes appearing across multiple sources — not yet full patterns, but worth tracking.

### "Sell Before You Build"
- Koerner/Cannon: "Get 3 dentists to pay before writing code"
- Validates demand, de-risks development
- Counter: Some products need demos to sell

### "AGI Hedge / Barbell Strategy"
- Isenberg/James: Physical services as hedge against digital disruption
- One side: SaaS, digital, AI-native
- Other side: Boring businesses with physical moats
- Open question: Is this real risk management or overthinking?

### "Good SEO = Good GEO"
- No secret sauce for LLM optimization
- Same fundamentals: clean tech, meta tags, topical authority, links, reviews
- Add llms.txt but don't expect magic

---

## Pattern Gaps

Things we haven't seen patterns for yet — watch for these in future content.

- **Pricing strategies** — How to price vertical SaaS, service businesses
- **Growth channels beyond SEO** — Paid, partnerships, virality
- **Team scaling** — When to hire, what roles first
- **Exit patterns** — What makes these businesses acquirable

---

*Last updated: 2026-01-14*
*Sources processed: 2 (Koerner/Cannon Free CRM, Isenberg/James Local SEO)*
