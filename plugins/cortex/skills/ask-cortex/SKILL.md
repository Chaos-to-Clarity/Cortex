---
name: ask-cortex
description: Answers questions about the user's world from their Cortex plus live meetings, calendar, and email. Lookups, meeting prep, and synthesis like what's at risk this week or where they're overcommitted.
---

# Ask Cortex

Answer questions about the user's business, people, priorities, and schedule. The Cortex is the durable layer; meeting notes, calendar, and email are the live layer. Connect them. Don't just retrieve.

Read `references/cortex-spec.md` first. Every read follows the Reading protocol in section 6: Map, then catalogs, then only the records needed. Never list whole databases or search the workspace broadly.

If the Map has `pack.company: 1`, also read `references/company-pack.md`. Act for the asking member (its section 5): read only what their role and spaces allow, and never quote Private content to anyone but its owner.

If the user hasn't asked a question yet, ask what they want to know.

## Step 1. Load the Map

Find and validate the Cortex Map (spec section 4). If there isn't one, answer from live sources where you can, say the Cortex isn't set up, and offer cortex-setup.

## Step 2. Resolve and route

- Match every name, company, project, and term in the question against the Glossary, then catalog Names and Aliases.
- Pick collections with the Map's Routing rules.

| Question | Start in | Live supplement |
| --- | --- | --- |
| Positioning, ICP, brand, GTM | Strategy | |
| A person: role, context, history | People, then their company and initiatives | Recent meetings and threads with them |
| A company: where things stand with a customer, investor, or partner | Companies, then its people and initiatives | Recent meetings and threads with them |
| An initiative: status, blocker, next action | Initiatives, then its decisions | Recent mentions, upcoming events |
| A decision: what and why | Decisions | |
| Risk or overcommitment this week | Initiatives and People catalogs | Upcoming calendar, open meeting actions |
| Meeting prep | The person, their initiatives | Their last meeting, the next one on the calendar |

## Step 3. Pick and open records

Read the relevant catalogs. Choose records from their Summaries, most-linked first when two fit. Open only those, and follow relations one hop. A Stub has only a line of context; say so rather than overstating what the Cortex knows. If more than about 10 records would be needed, answer from catalog summaries and say so.

## Step 4. Pull live data when it's time-sensitive

- Meeting notes: the last one to three meetings with the person or on the topic
- Calendar: relevant events in the next 7 to 14 days
- Email: recent threads with the person or on the topic

Check freshness against the Map's Freshness section and record dates. Newer live data wins for the answer; flag the conflict.

## Step 5. Answer

Answer first, then the support. Cite each record and its date ("People: Jane Rivera, updated Oct 3") and each live source ("meeting on Oct 8").

When a question touches strategy, people, and schedule, pull from each and synthesize: the implication behind the question, the pattern no single source shows, where live data contradicts the Cortex.

- **Lookup:** one direct answer, the source, one line of context if useful.
- **Prep:** (1) where things stand, from the Cortex; (2) what the last meeting or thread showed; (3) what to raise, given their priorities and open threads.
- **Synthesis:** the pattern or risk, the evidence across sources, the implication. Name the one thing most likely to slip or compound if left alone.

If a name or topic the question depends on wasn't in the Glossary or catalogs, run the scoped search (spec section 6, step 7) before concluding. If that also misses, say "not in the Cortex," never "doesn't exist."

## Step 6. Fix what's stale

If the answer exposed a stale or wrong record ("the Cortex says X, but the Oct 8 meeting says Y"), propose the exact fix and apply it after a yes, per spec section 7.

## Step 7. Offer to keep what's worth keeping

If the answer produced something durable (a pattern across people, a real risk in a decision, a position worth reusing), offer to save it: update the relevant record, add a Decision if it settled something, or update Strategy. Offer only; don't fill the Cortex with every passing question.

On a yes, write per spec section 7 and log it: Source "Query: [short description, date]", Type Query Insight.
