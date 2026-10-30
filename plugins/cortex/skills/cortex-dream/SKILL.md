---
name: cortex-dream
description: The nightly dream that keeps a Cortex current and lean. Replays the day, resolves contradictions, flags what time made stale, compacts, spots patterns, and leaves a morning note.
---

# Cortex Dream

Overnight consolidation for the user's Cortex. Every write during the day adds a little: a History line, a Stub, a catalog row, an Inbox item. Left alone, the Cortex drifts: Current falls behind History, one fact lives in two places with two values, "waiting on the proposal next week" is still there a month later, and the catalogs stop matching the records. Tonight's dream fixes that, so tomorrow's reads hit a store that is already clean.

It works like sleep: replay the day, fold it into what's already known, notice patterns, downscale what no longer matters, and leave a short note for the morning.

Read `references/cortex-spec.md` first, especially section 15 (Dreaming), section 7 (Writing), and section 10 (Health check). Section 15 is the contract; this file is the procedure.

If the Map has `pack.company: 1`, also read `references/company-pack.md`, sections 9 and 10: the dream runs once for the company, reads every member's meeting notes with that member's access, flags passed Due dates and stale Metrics, and routes its questions to `company.reviewer`. Questions about Private records go only to their owner.

**Division of labor.** cortex-dream runs nightly and works on a small, bounded slice: what changed today, its neighbors, and a rolling few. cortex-update runs weekly and does the wide sweep: email and calendar, the full health check across every record, and the review list. They share the Ingest Log, so nothing is processed twice. cortex-gnome builds work; the dream only maintains the Cortex. It never sends messages, never touches anything outside the Cortex root, and never deletes.

## Step 0. Wake check

1. **Find and validate the Map** (spec section 4). None: say so in one line and stop. In a scheduled run, that line is the whole report.
2. **One at a time.** If `dream.started` is newer than `dream.last_run` and under two hours old, another dream is running: stop. If `dream.last_run` is under 12 hours old, tonight's work is done: stop, unless the user asked for another pass.
3. **Mode.** `update.approval: autonomous`: write. `required`: dry dream. Do every step, but write only the Dream Journal, the Ingest Log row, and the `dream.*` settings, listing every edit you would have made.
4. **Claim the night.** Set `dream.started` to now, before any other write. On a Map with no `dream.*` settings, this first write adds them all with the defaults from spec section 4: `dream.sources: meeting-notes` if a meeting-notes source is set, otherwise `none`; `dream.max_records: 40`; `dream.cursor: start`; `dream.last_run: never`; and `dream.started` set to now.
5. **Dream Journal.** If `page.dream_journal` is missing, `none`, or points to nothing, create the page or file under the Cortex root with empty Questions for you and Patterns sections, and link it from Settings. Say so in the report. This is the only structure the dream creates.

## Step 1. Orient (read only)

Read the cheap things first, then only the catalogs they point to:

1. The Map: Settings, Collections, Glossary, Freshness
2. The Dream Journal: open Questions for you, Patterns, and the last entry (including what didn't fit last night)
3. Ingest Log rows dated after `dream.last_run`. Their What Changed lines name the records written since the last dream
4. The meeting-notes source, if `dream.sources` includes it: meetings in the last `update.lookback_days` days not in the Ingest Log
5. Only the catalogs those point to, plus the one the cursor is in. Never the archives or the databases. If an Ingest Log row is too vague to name its records, read that collection's catalog and use its Updated column

Build tonight's working set, in this priority order, up to `dream.max_records` records:

| Priority | What | How to find it |
| --- | --- | --- |
| 0 | Last night's carryover | The last journal entry's "didn't fit" list |
| 1 | New meeting notes, if `dream.sources` includes them | Meetings in the last `update.lookback_days` days not in the Ingest Log, oldest first |
| 2 | Records changed since the last dream | Named in Ingest Log rows since `dream.last_run`, or catalog rows with Updated after it |
| 3 | Inbox items with Status New, and Query Insight rows since the last dream | The Inbox catalog and the Ingest Log |
| 4 | Neighbors of priority 2 | One hop through relations: a changed person's company and initiatives, an initiative's decisions |
| 5 | Answers to journal questions | Open questions the user answered (checked, or replied to in the journal) |
| 6 | The rolling slice | The next Active records after `dream.cursor`, walking the catalogs in Map order, to fill what's left of the budget |

Meeting notes count against the budget by the records they touch. If the set is full before priority 6, the slice waits for another night. Record what didn't fit in tonight's journal entry; it's priority 0 next time. Meetings that didn't fit are picked up anyway, because they stay out of the Ingest Log until replayed.

**Light night.** If priorities 0 to 5 are empty, read only the cursor's catalog, open the rolling slice, write a one-line journal entry, and finish. Most nights should cost little.

## Step 2. Replay

For each new meeting note, run the Writing protocol (spec section 7) exactly as cortex-update does: keep only what's durable, route it, resolve identity through the Glossary and catalogs, update in place, Stubs on first mention, unclear matches to the Inbox, catalog row with every write, one Ingest Log row per meeting.

Email and calendar are not replayed nightly. cortex-update handles them weekly.

## Step 3. Consolidate

Open each record in the working set (re-read it right before changing it; other agents may write the same Cortex). Then:

1. **Answers first.** Apply each journal question the user answered, per spec section 7, and remove it from Questions for you.
2. **Contradictions.** Look for two claims about the same thing: a field against the body, Summary against Current, one record against another. The newer dated source wins. (A catalog row that disagrees with its record is not a contradiction: the record always wins, and Step 5 fixes the row.) Set the field to the new value and add a History line "Was [old] until [date] ([source])". Never erase the old claim. If the dates tie, the sources are different in kind, or the claim is about someone's private context, don't choose: ask.
3. **Absolute dates.** Rewrite relative dates in Current, Open Thread, Next Action, and Blocker, anchored to the date of the History line that introduced the text: "next Friday" added by a line dated 2026-10-10 becomes "Oct 16, 2026". No History line matches, or it's unclear which one did: leave the text and ask. History lines keep their wording.
4. **What time passed by.** Flag, don't close:
   - An Open Thread, Next Action, or Blocker that names a date already gone
   - A "waiting on" or "follow up" older than 14 days
   - An Active initiative past its Target
   - An Open decision older than 30 days
   - A person with a Cadence whose newest History line from a real source (not the dream) is older than twice that cadence
   Each becomes one question: what's true now, with the record named. Skip it if the same question is already open. A question dropped after 14 nights comes back only if the record has changed since.
5. **Compact** any record with five or more History lines since Current was rewritten (spec section 2). Keep every name, number, date, amount, and commitment that's still true. Drop repetition, not detail. Refresh the Summary (15 words or fewer). Add "Current rewritten (Dream, [date])" to History.
6. **Depth.** Promote Stubs that now qualify as Full. Archive Stubs with one mention older than `health.stub_expire_days`.
7. **Relations.** Add a relation when the record's own text makes it unambiguous (the body names a company that exists in the Companies catalog). Anything less certain: leave it.
8. **Duplicates.** Two records sharing a name or alias, or clearly the same thing under two names: ask to merge. Never merge on your own. Exact duplicate Inbox items: discard the copies with a one-line reason.
9. **Inbox.** File items with a clear home and a clear match, per spec section 7, and set them to Filed with where they went. Leave unclear ones for cortex-update's weekly triage.
10. **Query Insights.** Where a saved insight shows a name the catalogs missed, add the alias to the record and its catalog row.

**Stamping.** Every change gets a History line with Source "Dream, [date]", so the user can see and reverse it. Changes that bring in new facts (a replayed meeting, an answer the user gave) also set Last Updated and Source as usual. Maintenance alone (date rewrites, compaction, relations, Stub promotion, catalog and alias fixes) does not touch Last Updated, so stale and orphan checks still see how long it's been since anything real happened.

## Step 4. Abstract

Step back from single records. Across tonight's working set and the last seven journal entries, look for what no one record shows:

- A person, company, or topic recurring across several meetings or initiatives with no record or initiative that holds it
- A blocker or open thread unchanged across three or more weeks
- Commitments stacking up in the same week, or one person carrying many open threads
- A decision or initiative that contradicts the Strategy summary or Standing Context
- An initiative with no meeting, update, or decision touching it in a month

Write each as one line under Patterns, labeled inferred, with the records it rests on. A pattern already listed gets its night count raised instead of a second line. A pattern seen on three or more nights becomes a question proposing where to save it (a new initiative, a Decision, a Standing Context line, a Strategy note). Inferences never go into records without a yes.

If the night changed the big picture, rewrite the Map's Synthesis paragraph from the records, not from the patterns. Otherwise leave it.

## Step 5. Downscale

- **Catalogs.** Confirm the catalog row for every record the dream opened matches the record; fix drift. Move closed records to the archive catalog. Re-sort only the catalogs that changed, most-linked first.
- **Glossary.** Add rows for new key names (never Stubs) while there's room. When it's full, drop the least-referenced Dormant or Archived terms first.
- **Map budget.** Under 10,000 characters. Over: trim the glossary, then tighten Synthesis.
- **Freshness.** Meeting notes last processed, record counts, Inbox count.
- **Cursor.** Move `dream.cursor` past the last record reviewed in the rolling slice. At the end of the last catalog, wrap to `start`.

## Step 6. Journal and log

1. **Dream Journal.** Update Questions for you and Patterns. Add tonight's entry at the top of the dated entries: two or three lines of counts and names (replayed, updated, superseded, compacted, promoted, archived, filed, reviewed), plus anything that didn't fit tonight. Drop questions unanswered for 14 nights, noting it once. Keep 14 nightly entries, roll older ones into one line per month under "Earlier", and keep the page under 6,000 characters. Format: spec section 15.
2. **Ingest Log.** One row: Source "Cortex dream [date]", Type Dream, What Changed = the counts.
3. **Settings.** Set `dream.last_run` to now.

If the run is cut short, stop at a clean point: finish the record in hand, write the journal entry with what's done and what's left, and set `dream.last_run`. A half-finished dream is fine; tomorrow picks up from the cursor.

## Step 7. Morning note

End with a short note, the final message of the run:

- **Overnight:** one line of counts
- **Needs you:** up to five questions, most consequential first, each one line with the record named
- **Noticed:** up to three patterns, labeled inferred
- Where the full journal is

A light night is one line. A dry dream (approval required) says so first and lists the edits waiting for approval.

## Rules

- **Never delete.** Supersede with a dated History line. History is never shortened.
- **Bounded.** Only the working set, never the whole Cortex. Stop at `dream.max_records`; the rest waits.
- **Specifics survive.** Consolidation removes repetition, never names, numbers, dates, or commitments.
- **Inferred stays labeled.** Patterns live in the journal until the user confirms them.
- **Ask, don't guess.** Merges, closures, status changes on inference, and structure changes need a yes.
- **Stamp everything.** A History line with Source "Dream, [date]" on every change, so every night is auditable. Last Updated moves only when a real fact arrives.
- **Inside the Cortex only.** No messages, no other tools' data, nothing outside the Cortex root.
