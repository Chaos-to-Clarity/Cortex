# Coordination

Cortex is a team's context layer, so several people may each run a gnome over the same context. Each gnome belongs to one owner and one scheduled task. They share one home, one queue, and one Manifesto, and they coordinate through the Gnome Registry, Gnome Runs, and claims on Gnome Jobs.

None of the backends offer real locks, so this is a lease-and-claim protocol with a re-read. It prevents duplicate work in practice; the brief reports any collision it catches.

## Check-in (run Step 1)

1. **Open the run.** Create a Gnome Runs row: Status Running, Started and Heartbeat now.
2. **Read the Registry.** Note every Active gnome: name, owner, lanes, schedule.
3. **Read every Running run** (other than this one).
   - Heartbeat within `coord.lease_minutes` (default 90): that gnome is live. Note it.
   - Heartbeat older than the lease: mark that run Abandoned, and release its claims (every job it Claimed or was Building goes back to Queued, Note "released from abandoned run <run>"). Log both in this run's Coordination note.
4. **Release stale claims** from runs that ended without checking out (Failed runs, crashed sessions): any job still Claimed or Building whose Run isn't Running goes back to Queued, with a Note.
5. **Same gnome, two runs.** If another live run belongs to this same gnome (a double-fired task, or a manual run during a scheduled one), the earlier Started wins. If that's the other run, close this one as Skipped, "another run of this gnome is live", and stop.

## Lanes

Each Registry row lists Lanes: the areas that gnome builds in by default. Lanes are how gnomes agree on who builds what before anyone claims anything.

- A job in another live or scheduled gnome's lane belongs to that gnome. Leave it, unless that gnome won't run in the next 24 hours (Paused, Retired, or its schedule skips tomorrow) and the job has been Queued for over a day. Then take it and say so in the brief.
- A job in no one's lane, or in several, is open to whichever gnome claims it first.
- A job with For Gnome set belongs to that gnome.
- An owner's own tags go to their own gnome first.

## Claiming (run Step 4)

Claims are append-only: each gnome creates its own claim row and never edits another gnome's. Two gnomes can't overwrite each other, and every claim stays visible on re-read.

1. **Dedupe Key.** Give the job a stable key from its source, so two gnomes reach the same key for the same work:
   - Task tool item: `<tool>:<item id>`, for example `asana:1209938452`
   - Cortex record: `cortex:<collection>:<record name>:<field>:<YYYY-MM-DD>`, for example `cortex:initiatives:Q4 Board Prep:next-action:2026-10-12`
   - Meeting commitment: `<meetings tool>:<meeting id>:<short slug>`
   - Email thread: `<email tool>:thread:<thread id>:<short slug>`
   - Calendar event (prep): `<calendar>:event:<event id>`
   - Chat message: `<chat tool>:<channel>:<message id>`
   - Idea inbox entry: `<tool>:<page, file, or entry id>`
   - Repo issue or PR: `github:<owner>/<repo>#<number>`
   - Revision of a job: `revision:<parent job id>`; ship step: `ship:<parent job id>`
   - Queued row with no outside source: its own row id
2. **Look for live work** with the same key: any job or claim row that is Claimed or Building under a Running run, or is Ready, Shipped, or Needs Decision.
   - Claimed or Building under a live run: don't build. Log it as Yielded in this run's Coordination note.
   - Ready, Shipped, or Needs Decision: done or waiting on a person. Don't rebuild it; a Revision job is the way to redo work.
   - Claimed or Building under a run that isn't Running (Done, Failed, Abandoned): stale. Treat it as unclaimed, and set that claim row to Skipped, "stale claim released".
3. **Create a claim row** (`gnome-spec.md`, Claim rows): Parent the job, same Dedupe Key, Claimed By this gnome, Claimed At now, Run this run.
4. **Re-read every claim row** with that key. The earliest Claimed At under a live run wins; ties go to the alphabetically first gnome name. Lost: set your own claim row to Yielded and move on. Won: set the job itself to Claimed, with Claimed By and Run.
5. **Re-check before acting.** Just before setting a job to Building, and again just before any ship step, re-read the claim rows and this run's own row:
   - Another claim now wins: stop, save nothing over theirs, set yours to Yielded.
   - This run has been marked Abandoned (another gnome thought the heartbeat expired): stop building immediately, set the job back to Queued with Note "lease lost", record it in the brief, and finish the run without claiming anything else.
6. **Heartbeat.** Refresh this run's Heartbeat after each claim and each job. A long build refreshes it at least every 30 minutes, so its lease never expires while it works.

## Check-out (run Steps 7 and 8)

- Every claim this run holds ends in a final status: Ready, Needs Decision, Shipped, Failed, or Skipped. A claim that's still Claimed at the end (out of budget) goes back to Queued.
- Close the run: Done, Ended, Harvest End.
- The brief's Coordination note lists other live gnomes, anything yielded, and anything released from an abandoned run.

## When gnomes disagree

Two gnomes may read the same context and want different things from it. That isn't a collision as long as the Dedupe Keys differ. When two outputs from different gnomes conflict (two decks for the same meeting, two PRs touching the same file), the second gnome to notice marks its job Needs Decision with a link to the other and lets the owners pick. Neither gnome deletes or overwrites the other's work.
