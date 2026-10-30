---
name: strategy-digest
description: Reads the user's strategy documents (plans, OKRs, board and pitch decks, personas, GTM, brand) and condenses them into the Strategy page of their Cortex. Rerun when a doc changes.
---

# Strategy Digest

Pull the durable strategy out of the user's documents and leave the noise behind. The result is a Strategy page every other skill can rely on.

Read `references/cortex-spec.md` first, then find and validate the Cortex Map (spec section 4). If there isn't one, offer cortex-setup and stop. Writes follow the Writing protocol in spec section 7.

If the Map has `pack.company: 1`, also read `references/company-pack.md`: Strategy lives in the Exec space, and nothing from a strategy document goes to the Company space unless the CEO says so.

## Step 1. Find the documents

- If the user named or attached documents, use those.
- Otherwise open `sources.strategy_folder` in `sources.documents`. If that's `none`, ask which folder holds their strategy docs and offer to save it to the Map's Settings.
- List what you found and the type of each doc. Check the Ingest Log: skip any doc already logged unless it changed since (newer modified date) or the user says re-digest.

## Step 2. Extract by document type

- **Strategic plans and OKRs:** the thesis, the bets, the metrics and targets, the time horizon.
- **Board decks:** the narrative, the numbers that matter, the risks named, what was asked of the board.
- **Pitch decks:** positioning, the problem, the ICP, differentiation, traction, the raise.
- **Personas:** each persona's role, goals, pains, buying triggers, objections.
- **Sales, marketing, brand:** the messaging, the GTM motion, the channels, the brand pillars and voice.

Write each summary in the user's words, not the deck's marketing language. Two to ten lines per doc. Keep the durable substance, drop the filler.

## Step 3. Write to the Strategy page

- One section per document, titled "[Doc name], [date of the doc]". If a section for that doc exists, replace it in place. Never duplicate it, and never delete other sections.
- At the top, write or refresh the **Strategy Summary**, a dozen lines at most: positioning, ICP and personas, GTM motion, targets, brand pillars.

## Step 4. Flag problems

Flag conflicts, stale numbers, and gaps. If two documents disagree (different targets, different ICP), say so and ask which is current. Don't resolve a conflict yourself.

## Step 5. Route what isn't strategy

If a document names a clear decision ("we are dropping the SMB tier") or an initiative, offer to add it to Decisions or Initiatives per spec section 7, with its catalog row. Offer only; don't write those without a yes.

## Step 6. Log and report

Add one Ingest Log row per document: Source = doc name, Type Strategy, Date Ingested today, What Changed = "Strategy section added" or "replaced".

Update the Strategy line in the Map's Freshness section with today's date.

Report:

- What you digested and what you skipped
- Conflicts and gaps that need an answer
- The three things in the strategy that should most shape day-to-day priorities

To rerun: drop a new or updated doc in the strategy folder and run strategy-digest again.
