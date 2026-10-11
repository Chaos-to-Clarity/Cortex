# Review and learning

Review is where the gnome gets good. Every verdict is a lesson; the Manifesto is where lessons accumulate. A gnome nobody reviews keeps making the same mistakes, so the brief makes reviewing fast and the review makes the next night better.

## Where review happens

- **In the run's own chat** (default). The brief ends with a reply line. The person answers in that chat, and the session continues in review mode.
- **"Review my gnome"** in any chat: load the latest runs with unreviewed jobs.
- **Directly in the Gnome Jobs collection**: a person sets Verdict and Feedback on rows. The next run folds these in (Unattended learning).
- **Email or Slack replies**: only if setup configured a way to read them back. Otherwise the brief points to the chat.

## Review mode

1. **Load.** Find the runs with jobs that are Ready, Needs Decision, or Proposed and have no Verdict, newest run first. Use the Brief No on each job so "keep 2" matches what the person saw.
2. **Parse the reply.** Accept any wording. The shorthand:
   - `2 keep` or `keep 2`: the output is good
   - `2 tweak: <what to change>`: close, needs changes
   - `2 kill: <why>`: not wanted
   - `ship 2`: approved to ship as is
   - `P1 now` / `P1 later` / `P1 never`: answers to proposals
   - A free comment ("decks are too long") is a Manifesto change, not a job verdict
   - Anything not mentioned stays unreviewed. Don't assume silence is a Keep.
3. **Ask once for what's missing.** A Kill or Tweak without a reason: ask why in one short line, because the reason is the lesson. Batch every question into one message.
4. **Write the verdicts** to each job: Verdict, Feedback (their words, verbatim), and:
   - Keep: Ship stays Draft; Status Closed unless they also ship it
   - Tweak: create a Revision job (Queued, Parent = this job, Dedupe Key `revision:<job id>`, Title "Revise: <title>", the feedback in Note), unless one with that key already exists; Status Closed on the original once the revision exists
   - Kill: Status Closed
   - Ship: only from this gnome's owner. Set Ship = Approved to Ship, Approved By, Approved At now, Approved Amount if it spends, and add a line to the run's Grants section with their words. Someone else asking to ship: record it in Feedback and tell them the owner has to approve
   - Proposal now: Answer Do Now, Status Queued, and since a person is present, offer to build it right away
   - Proposal later: Answer Do Next Run, Status Queued
   - Proposal never: Answer Don't, Status Closed
5. **Ship approvals, live.** A person is present, so approved ship steps can run now. Before each, say in one line exactly what will happen ("Merge PR #42 into acme/docs", "Send the draft to Dana at Acme") and do it on a yes. Record Shipped with the link. The guardrails still apply; a Never stays never.
6. **Distill rules** (below). Show the proposed Manifesto changes as a short list and apply the ones confirmed. Set Learned on every job reviewed.
7. **Close.** Update each run's Keep Rate. One line back: what was recorded, what ships, what's queued for tonight.

## Distilling rules

A good rule is one line, specific enough to change tomorrow's output, and in the reviewer's words where possible.

| Feedback | Becomes |
| --- | --- |
| Kill: "not our ICP" on a prospect deck | Skip: "Don't build sales material for companies outside the ICP in Strategy" |
| Tweak: "lead with the ask" on an email | Quality bars > Email: "Put the ask in the first line" |
| Keep on an inferred meeting prep | Inference: "Build prep pages for external first meetings without being asked" |
| P1 never: "don't refactor without an issue" | Inference: "Propose, never build, refactors without an issue" |
| `ship 2` plus "you can always merge docs PRs" | Permissions: "Merge PRs to acme/docs that pass CI and touch only /docs (granted by <name>, <date>)" |

Rules for rules:

- **One lesson, one rule.** If the lesson matches an existing rule, add a confirmation to it ("confirmed 3x") instead of a new line.
- **Contradiction:** the newer rule replaces the older one. Log the change in the Rule log.
- **Scope it** when the feedback is about one gnome, repo, client, or type: "(acme/web)", "(Eric's Gnome only)".
- **Permissions only from the person who can grant them**: the owner of the gnome they apply to, said in a live review, never inferred from a Keep. Scope each one to that owner's gnome, record who granted it and when, and add the grant to the run's Grants section. On the Starter rung, record it but mark it "(active from Trusted)".
- **Never** turn feedback into a rule that weakens `guardrails.md`. If someone asks for that ("just send emails, don't wait"), say which guardrail it hits and offer the nearest thing allowed (for example, a standing permission for one named recipient and one kind of message).
- Every change gets a Rule log line: date, the change, the job it came from.

## Unattended learning (run Step 2)

When people leave verdicts directly in Gnome Jobs, the next run picks them up:

1. Read the "Unlearned verdicts" view, keeping only jobs whose Run belongs to this gnome.
2. Apply each verdict's and answer's effects (Revision jobs with their `revision:` key, Closed, Queued) as in review mode step 4. An Approved to Ship set outside a live review is checked against `guardrails.md` (Approvals); if it fails, it's a request: build nothing new, and ask for a live approval in the brief.
3. Re-read the Manifesto's Provisional section right before writing to it, and only add lines; another gnome may be learning at the same time.
4. Distill rules the same way, but write them to the Manifesto's **Provisional** section, not the main sections. Provisional rules guide tonight's run; the next live review confirms or drops them.
5. Never add a Permission unattended. An Approved to Ship on a job covers that job only.
6. Set Learned. List the provisional rules in the brief's Manifesto section.

## Weekly consolidation

On the first run on or after `manifesto.consolidate_day`:

- Consolidation is done by one gnome per week: the first to run on or after the day, which records "consolidated <date>" in the Rule log. Others see that line and skip it.
- Merge rules that say the same thing; keep the confirmation counts.
- Move Provisional rules confirmed in a review into their sections; drop ones older than 14 days that no review confirmed.
- Compute keep rate by Type over the last 14 days from Gnome Jobs. Note any type under 40% in the brief ("Decks kept 1 of 5; tighten or skip?"). Triage uses these rates as Fit.
- Check the Trust ladder (`setup.md`, Trust ladder): offer to move up a rung if it's earned, move down if the keep rate fell, and apply the no-reviews rule.
- Trim the Rule log to the last 30 days, with one summary line for everything older.
- Keep the Manifesto under `manifesto.max_chars`. If it's over, merge and trim before adding anything.

The consolidation is reported in the brief in one or two lines. If the Manifesto lives in a repo, consolidation opens one pull request with the changes.
