# Moonshot PRD: Free Vertical CRM + Ancillary Services

## Source

| Field | Value |
|-------|-------|
| Video | ["Stupid Simple" Apps Are Making Millions While You Overthink](https://www.youtube.com/watch?v=bH_coG-2ASo) |
| Channel | The Koerner Office (Chris Koerner) |
| Guest | Will Cannon (UpLead, Signaturley) |
| Date | 2024-12-19 |
| Duration | ~50 min |

---

## Idea (One Sentence)

Give away a best-in-class CRM for a specific vertical (dentists, chiropractors, barbers, etc.) for FREE, and monetize through white-labeled credit card processing, payroll, and health insurance services.

---

## Problem

| Field | Description |
|-------|-------------|
| **Pain** | Small business owners pay $100-500/month for generic CRMs (HubSpot, Salesforce, etc.) that aren't built for their industry. They also use multiple vendors for payments, payroll, insurance — each taking a cut. |
| **Who Has It** | Solo practitioners and small service businesses: dentists, chiropractors, barbers, HVAC, plumbers, etc. |
| **Current Solution** | Pay for generic CRM + separate payment processor + separate payroll + separate insurance. Or use nothing and manage manually. |

---

## Value Proposition

"Your entire business operating system — CRM, scheduling, invoicing, payments — for $0/month. We make money when you make money (through payment processing), not by charging you rent on software."

---

## MVP Scope

**What it does:**
- Industry-specific CRM (white-label Go High Level or similar)
- Appointment scheduling
- Client communication (email, SMS)
- Invoicing + payment collection (via white-labeled processor)
- Basic reporting

**What's NOT included in MVP:**
- Custom-built CRM (use white-label)
- Payroll integration (Phase 2)
- Health insurance (Phase 2)
- Multiple verticals (pick ONE)

**Success Metric:**
- 10 paying merchants processing $50K+/month within 90 days
- At 1% margin on processing = $5K/month revenue

---

## User Stories

### STORY-001: Sign up and onboard
**As a** small business owner (e.g., dentist)
**I want to** sign up for a free CRM built for my industry
**So that** I can manage my business without paying SaaS fees

**Acceptance Criteria:**
- [ ] Sign up with email
- [ ] Industry-specific onboarding flow
- [ ] Import existing client list
- [ ] Connected to payment processor within setup

**Priority:** P0
**Size:** M

---

### STORY-002: Schedule appointments
**As a** service provider
**I want to** let clients book appointments online
**So that** I don't have to manage scheduling manually

**Acceptance Criteria:**
- [ ] Embeddable booking widget
- [ ] Calendar sync (Google, Outlook)
- [ ] Automated reminders (email/SMS)

**Priority:** P0
**Size:** M

---

### STORY-003: Invoice and collect payment
**As a** business owner
**I want to** send invoices and collect payment in-app
**So that** I get paid faster and everything is tracked

**Acceptance Criteria:**
- [ ] Create invoice from client record
- [ ] Client pays via credit card
- [ ] Payment recorded automatically
- [ ] Funds deposited to my bank account

**Priority:** P0
**Size:** L

---

### STORY-004: Process payments (white-label)
**As the** platform operator
**I want to** white-label a payment processor
**So that** I earn margin on every transaction without building payments infrastructure

**Acceptance Criteria:**
- [ ] Integrated white-label processor (Stripe Connect, Finix, etc.)
- [ ] Standard 2.9% + $0.30 pricing to merchant
- [ ] 0.5-1% margin to platform
- [ ] Compliant onboarding (KYC)

**Priority:** P0
**Size:** L

---

## Technical Requirements

### Likely Stack

| Component | Option |
|-----------|--------|
| **CRM Platform** | Go High Level (white-label) OR custom Next.js + Supabase |
| **Payment Processing** | Stripe Connect, Finix, or white-label provider |
| **Auth** | Supabase Auth or Firebase |
| **Hosting** | Vercel |
| **SMS/Email** | Twilio, SendGrid (or GHL built-in) |

### Key Challenges

1. **Payment processor onboarding** — KYC/compliance for sub-merchants
2. **Industry-specific customization** — Each vertical has different workflows
3. **Margin compression** — Payment processing margins are thin
4. **Switching costs** — Getting merchants to move payment processing

### Dependencies

- White-label payment processor partner
- Go High Level agency account ($297-497/month) OR dev time for custom

---

## Risks

| Risk | Likelihood | Mitigation |
|------|------------|------------|
| Merchants don't want to switch payment processors | HIGH | Target new businesses or those unhappy with current processor. Offer onboarding help. |
| Margins too thin to be profitable | MEDIUM | Volume is key. Also upsell payroll/insurance in Phase 2. |
| Go High Level changes terms | MEDIUM | Build with extraction in mind. Could migrate to custom later. |
| Compliance issues with payments | LOW | Use established white-label provider with built-in compliance. |

---

## Tech Stack Fit

| Field | Assessment |
|-------|------------|
| **Score** | 8/10 |
| **Primary Stack** | Next.js + Supabase + Stripe Connect (or GHL white-label) |
| **Buildable in Days** | Yes (with GHL). Weeks if custom. |
| **AI Leverage** | Light — could add AI scheduling, client communication |
| **Notes** | Perfect fit for our stack. GHL shortcut gets to market fast. Custom build has more upside but more work. |

---

## Viability Assessment

| Field | Assessment |
|-------|------------|
| **Score** | 7/10 |
| **Reasoning** | Model is proven (Squarespace, Toast, etc. do this). Main risk is sales — you need to convince merchants to switch processors. Will Cannon did this successfully twice. Key insight: don't compete on software features, compete on "it's free." |
| **Recommendation** | **BUILD** — Start with ONE vertical. Use GHL to get to market fast. Validate payment processing revenue model before building custom. |

---

## Key Insights from Interview

1. **"Sell it before you have it"** — Cold email/pre-sell before building
2. **"Stupid simple wins"** — Signaturley beat DocuSign by being radically simpler
3. **"Acquiring customers profitably is the moat"** — Features can be copied, distribution can't
4. **"Go window shopping on BizBuySell"** — Free market research on proven models
5. **"$10K/month is life-changing for 99% of people"** — Don't need massive scale

---

## Next Actions

1. **Pick a vertical** — Dentists? Chiropractors? HVAC?
2. **Pre-sell test** — Cold email 100 businesses in that vertical with the offer
3. **If interest** — Set up GHL agency account, white-label processor
4. **Launch MVP** — First 10 merchants

---

*Processed: 2026-01-14*
