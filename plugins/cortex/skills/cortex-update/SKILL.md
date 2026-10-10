---
name: cortex-update
description: Keeps the user's Cortex current and clean. Scans recent meetings, email, and calendar, updates records in place, triages the Inbox, and runs the health check. Built to run weekly.
---

# Cortex Update

Keep the Cortex current and clean. Scan every connected source from the look-back window, update records in place, triage the Inbox, run the health check, and refresh the Map's Synthesis and Freshness. Safe to repeat: the Ingest Log guarantees each source is processed once. For a single document, use add-to-cortex.

Read `references/cortex-spec.md` first. Every write follows the Writing protocol in section 7.

## Step 1. Load the Map

Find and validate the Cortex Map (spec section 4). If there isn't one, say so and stop. In a scheduled run there's no one to run setup, so just report it.

Settings it uses: `update.lookback_days` (default 7), `update.approval`, `health.stale_after_days` (default 60).

- `autonomous`: apply edits and report.
- `required`: show the edit list and wait for approval.
- Scheduled runs need `autonomous`. If this is a scheduled run and the Map says `required`, build the edit list, write nothing, and report that approval is needed.

## Step 2. Pull new sources

In parallel, for the look-back window:

| Source | What to pull |
| --- | --- |
| Meeting notes | Every meeting in the window |
| Email | Threads with strategic signal: new relationships, decisions, initiative changes. Skip routine operations, newsletters, receipts, and automated mail |
| Calendar | Events that signal a new relationship or commitment |

Drop every source already in the Ingest Log. If a source is unavailable, note it in one line and continue.

## Step 3. Extract and route

From each new source, keep only what stays true for weeks or months. Route each item with the Map's Routing rules, including extension collections.

| What changed | Typical home |
| --- | --- |
| A person they now deal with, or whose role or context shifted | People |
| An initiative that started, shifted, stalled, or finished | Initiatives |
| A decision made, or a question that opened or closed | Decisions |
| A durable fact about the business or their role | Standing Context |

## Step 4. Build the edit list

For each item, resolve identity through the Glossary and catalogs (spec section 7, step 5):

- **People:** new (Active); context changed (update, History line); relationship paused or ended (Dormant or Archived).
- **Initiatives:** new (Active, with Next Action and Blocker if known); shifted (update in place); finished or dropped (Done or Dropped).
- **Decisions:** new (Decided or Open, Date today); reversed or replaced (old one Reversed or Superseded, new one with Supersedes).
- **Standing Context:** surgical edits only.
- **Unclear match or no clear home:** Inbox, with candidates.
- **New category:** Inbox plus a proposal in the report. Never create a collection in an autonomous run.

## Step 5. Approval gate

`required`: show every create, update, supersede, and Inbox item. Write nothing until approved. `autonomous`: continue.

## Step 6. Apply

Re-read each record right before changing it. Write the record and its catalog row together. Add Glossary rows for new key names while there's room. Log one Ingest Log row per source processed.

## Step 7. Triage the Inbox

Read the Inbox catalog. For each New item:

- Clear home and a clear match (or clearly new): file it per spec section 7, set the item to Filed with a note of where it went.
- Noise or duplicate: Discarded, with a one-line reason.
- Still unclear: leave it New and list it in the report with the question that would settle it.

In `required` mode, include triage in the approval list.

## Step 8. Health check

Run every check in spec section 10. Fix what's safe: catalog drift, missing Summaries, Map size. Report the rest: stale records, alias collisions, unregistered collections, broken pointers. Log one Ingest Log row, Type Health Check.

## Step 9. Refresh the Map

- **Freshness:** last processed date per source, record counts, Inbox count, today's date.
- **Synthesis:** if the week shifted the big picture, rewrite the paragraph. Otherwise leave it.

Don't change the Map's structure here. If a new collection or broken pointer needs it, recommend cortex-map.

## Step 10. Report

A short table or a tight paragraph:

- Sources scanned, and skipped as already ingested
- Records created, updated, superseded
- Inbox: filed, discarded, waiting (with the questions)
- Health: fixed, and what needs the user (stale records, likely duplicates)
- Sources that were unavailable
