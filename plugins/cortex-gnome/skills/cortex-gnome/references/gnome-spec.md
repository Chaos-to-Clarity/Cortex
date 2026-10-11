# Cortex Gnome Spec

Where the Gnome keeps its state, what each record looks like, and the settings it runs on. Every mode reads this first.

## 1. The Gnome home

One home per company, shared by every gnome. It holds four things:

| Piece | Kind | What it's for |
| --- | --- | --- |
| **Gnome Registry** | Collection, one row per gnome | Who runs a gnome, when, on what sources, in which lanes, with what settings |
| **Gnome Runs** | Collection (a log), one row per run | Start, heartbeat, end, what was harvested, the brief. The coordination lease lives here |
| **Gnome Jobs** | Collection (a log), one row per piece of work | The queue, the claims, the outputs, the verdicts. Anyone or any skill can add work here |
| **Gnome Manifesto** | Page | The team's rules for what's valuable, what to skip, quality bars, voice, and standing permissions. Grows from feedback |

Plus a **Gnome Workspace**: wherever built outputs are stored for review (a page or folder; code goes to branches and pull requests in the target repos instead).

**With a Cortex**, the home is a page or folder named "Cortex Gnome" under the Cortex parent, and the three collections are registered on the Cortex Map as added collections (Cortex spec section 2) with these Routing lines:

- Find it: "What the gnome did, is doing, or was asked to do → Gnome Jobs, then Gnome Runs"
- File it: "Work for the gnome to do overnight → Gnome Jobs (Status Queued)"

Gnome Runs and Gnome Jobs are logs, like the Ingest Log: no catalog, no Current and History body, read through saved views. The Registry is small enough that it doesn't need a catalog either.

**Without a Cortex**, the home is a standalone page or folder named "Cortex Gnome" in whatever tool the team chose (Notion, Google Drive, Obsidian, a local folder, a repo). Same pieces, same fields.

### Finding it

1. The scheduled task's prompt names the home link and the gnome name. Use them. No searching.
2. Otherwise: the Cortex Map's Collections table (Gnome Registry row). Then a page titled exactly "Cortex Gnome" in Notion, a folder named "Cortex Gnome" in Google Drive or connected folders, then a `cortex-gnome/` folder in a connected repo.
3. Not found: the Gnome isn't set up. Offer setup if someone is present; otherwise report it and stop.

Then find this gnome's Registry row by name. Two rows with the same name is an error: report it and stop.

## 2. Gnome Registry

One row per gnome. Fields:

| Field | Holds |
| --- | --- |
| Name | The gnome's name, unique ("Eric's Gnome", "Platform Gnome") |
| Owner | The person who set it up and receives its brief |
| Status | Active, Paused, Retired. Mirrors `status` in Settings; if the two disagree, the more restrictive one wins |
| Schedule | Plain words: "Daily 7pm America/Los_Angeles" |
| Lanes | Comma-separated areas it builds in by default (content, sales, platform repo, hiring). Empty means anything |
| Last Run | Date and link to its latest run |
| Summary | One line: what this gnome is for |

The body holds the Settings block, exactly this shape:

```text
gnome_version: 1
name: <gnome name>
owner: <first name>
owner_contact: <email or handle, for the brief>
time_zone: <IANA zone>
status: <active | paused | retired>
schedule: <cron in local time, for reference: 52 18 * * *>
scheduled_task: <id or name of the scheduled task>
home: <link to the Gnome home>
cortex_map: <link to the Cortex Map, or none>
manifesto: <link to the Manifesto page or file>
workspace: <link to where outputs are stored>

sources.cortex: <yes | no>
sources.tasks: <clickup | asana | linear | jira | monday | notion | todoist | github-issues | trello | none>
sources.tasks_scope: <workspaces, projects, or boards to read>
sources.ideas: <list: a Notion page, a Drive folder, an Apple Notes folder, a Slack channel, ... or none>
sources.meetings: <granola | fireflies | otter | fathom | notion-meetings | none>
sources.email: <gmail | outlook | none>
sources.calendar: <google-calendar | outlook | none>
sources.chat: <slack channels, or none>
sources.repos: <owner/repo list, or none>

queue.tag: gnome
queue.allowed_taggers: <team (members of the company's own workspace in each tool) | list of names>

targets.repos: <owner/repo list the gnome may branch and open pull requests in>
targets.docs: <where documents and decks go: native artifacts | notion | google-drive | repo>
targets.design: <native artifacts | canva | files>
targets.calendar: <owner's calendar id for holds, or none>
targets.email_drafts: <gmail | outlook | none>

brief.channels: <list: chat, email:<owner address>, slack:<#channel>>
brief.share_level: <owner | team>

trust.rung: <starter | trusted | proven>
budget.max_jobs: 3
budget.max_points: 5
infer.max_auto: 0
infer.max_size: S

spend.cap_usd: 0
cortex.inbox_writes: <yes | no>
harvest.max_window_hours: 72

coord.lease_minutes: 90
manifesto.consolidate_day: <monday ... sunday>
manifesto.max_chars: 8000
```

Defaults shown are the Starter rung (`setup.md`, Trust ladder); a Trusted gnome typically runs 5 jobs, 8 points, and `infer.max_auto: 2`.

Settings are owned by setup and status mode, and change only on the owner's yes. A run reads them and never edits them, except Last Run. When the Trust ladder calls for a demotion, the run applies it as a temporary override for that run only (`setup.md`, Trust ladder) and recommends the settings change in the brief.

## 3. Gnome Runs

One row per run. Fields:

| Field | Holds |
| --- | --- |
| Run | `<gnome name> <YYYY-MM-DD HH:MM>` |
| Gnome | Relation to the Registry row (Markdown: a wikilink) |
| Status | Running, Done, Failed, Abandoned, Skipped |
| Started, Heartbeat, Ended | Timestamps with time zone |
| Harvest Start, Harvest End | The window this run covered |
| Counts | `built 3, shipped 1, proposed 2, yielded 1, failed 0` |
| Keep Rate | Filled by review: kept jobs over reviewed jobs |
| Rung | The effective Trust ladder rung this run used, and any override (`starter (override: no reviews in 7 days)`) |
| Incident | Empty, or one line on a guardrail incident: a ship that shouldn't have happened, injected content acted on, private data in a shared place |

Body: the team-safe version of the brief (section 6, Share level: always redacted here, because every gnome and teammate can read the home), then a short Coordination note (other gnomes seen, claims yielded or released), then a **Grants** section listing any permissions or ship approvals the owner gave in a live review of this run, with who, when, and their words. Grants are only ever written by the gnome during a live review.

Statuses: Running while working. Done when the brief went out. Failed when it couldn't finish (say why in the body). Abandoned is set by another gnome when this run's heartbeat expired. Skipped when the gnome was paused or had nothing to harvest.

## 4. Gnome Jobs

One row per piece of work. This is the shared queue: people, other skills, and gnomes all add rows here.

| Field | Holds |
| --- | --- |
| Title | What gets made, as a verb phrase: "Draft Q4 board deck from the October metrics". For jobs from private sources (personal email, DMs, private calendar), keep it generic: "Draft a reply to an email thread" |
| Status | See below |
| Origin | Tagged (a person asked), Skill (another skill queued it), Inferred (the gnome spotted it), Revision (a Tweak), Ship (an approved ship step) |
| Requested By | The person or skill that queued it |
| Type | deck, document, landing page, research, code, task updates, email draft, scheduling, travel, content, analysis, other |
| Size | S (1 point), M (2), L (4) |
| Source | Links to what prompted it: the task, record, meeting, or thread. Links only, never copied content, so private sources stay readable only by their owner |
| Dedupe Key | Stable id of the source, used to stop two gnomes doing the same work (see coordination) |
| Claimed By, Claimed At | The gnome holding it, and when |
| For Gnome | Optional: the gnome this work is meant for |
| Run | Relation to the run that built it |
| Brief No | Its number in that run's brief (P1, P2 for proposals), so "keep 2" resolves |
| Output | Link to what was made: the doc, deck, pull request, draft, or hold |
| Ship | Draft, Approved to Ship, Shipped, Not Shippable |
| Approved By, Approved At | Who approved shipping, and when. Only honored when the approver is the owner of the gnome that built it (`guardrails.md`, Approvals) |
| Approved Amount | For spending: the most the owner approved, with currency |
| Verdict | Keep, Tweak, Kill, or empty |
| Answer | For proposals: Do Now, Do Next Run, Don't, or empty |
| Feedback | The reviewer's words, verbatim |
| Learned | Checked once the verdict, answer, or approval has been processed |
| Parent | For revisions, ship steps, and claims: the original job |
| Note | One line: what happened, what's left, or why it was skipped |

**Claim rows.** A claim is a separate row: Title "Claim: <title>", Status Claimed, Parent the job, the same Dedupe Key, Claimed By, Claimed At. Claim rows are only ever created, never edited by another gnome, so two gnomes can't overwrite each other (`coordination.md`).

**Statuses**

| Status | Means |
| --- | --- |
| Queued | Waiting to be built. Anyone can set this |
| Proposed | The gnome inferred it and didn't build it. Waiting for a yes |
| Claimed | A gnome has it for tonight |
| Building | Work in progress |
| Ready | Built, stored, waiting for review |
| Needs Decision | Blocked on a person: the Note says what's needed |
| Shipped | Delivered for real, with permission |
| Yielded | Another gnome had it |
| Skipped | Not built, with the reason in Note (out of budget, ruled out by the Manifesto, duplicate) |
| Failed | Tried and fell below the bar or broke |
| Closed | Reviewed and done (Keep with nothing to ship, or Kill) |

**Handing work to the gnome.** Any person or skill adds a row: Title, Status Queued, Origin, Requested By, Type if known, Source. That's the whole interface. A skill that wants overnight work done writes one row and moves on.

## 5. Gnome Manifesto

One page, shared by every gnome. Keep it under `manifesto.max_chars`. It has these sections, in this order:

```markdown
# Gnome Manifesto

What the gnomes work on, how well, and what they may ship. Built from the team's feedback. Newest rules win where two conflict. Read top to bottom before every run.

## Mission
<One paragraph: what the gnome is for in this company.>

## Valuable
- <rule> (since 2026-10-12, confirmed 3x, evidence: [[job]])

## Skip
- <rule>

## Inference
- <what the gnome may infer and build without being asked, and what it should only propose>

## Quality bars
### Decks
- <rule>
### Documents
### Landing pages
### Code
### Content
### Research
### Email
### All work
<add types as they come up>

## Voice
- <how outputs should sound>

## Permissions
Standing permissions to ship without a per-job approval. Each names exactly what, where, and who granted it. Anything not listed here stays a draft.
- <e.g. "Merge pull requests to acme/docs that pass CI and touch only /docs" (granted by Eric, 2026-10-14)>

## Provisional
Rules learned during unattended runs, waiting for confirmation in the next review.
- <rule> (learned 2026-10-13 from [[job]])

## Rule log
- 2026-10-12: Added "..." (from [[job]] Kill: "not our ICP")
```

Every rule is one line, in the reviewer's words where possible, with a date and the job it came from. A rule can be scoped: "(Eric's Gnome only)" or "(acme/web)". Unscoped rules in Valuable, Skip, Inference, Quality bars, and Voice apply to every gnome.

**Permissions are always scoped** to the gnome of the person who granted them, because each gnome runs on its own owner's credentials: "(Eric's Gnome, granted by Eric 2026-10-14, run <link>)". A permission line is honored only when the matching grant appears in that run's Grants section (section 3). Lines anyone adds by hand are flagged in the brief and ignored until the owner confirms them in a live review.

The Manifesto can narrow what the gnome does and grant ship permissions. It can never override `guardrails.md`.

**In a repo instead.** If the team keeps the Manifesto as a file (`GNOME.md` in a repo), same sections. Changes go through a pull request the owner merges; the gnome never pushes to the default branch, including for its own Manifesto.

## 6. Brief

Delivered at the end of every run. Under 400 words. No preamble.

```markdown
**Gnome brief, <Day Mon D>** · <gnome name> · <n> built, <n> need you

**Needs you**
1. <job>: <the decision or approval needed> · <link>

**Built**
| # | Job | Type | Origin | Output | Ship |
| --- | --- | --- | --- | --- | --- |
| 1 | <title> | deck | Tagged by Sam | <link> | Draft |

**Proposed, not built**
- P1. <what and why, size> 

**Context I picked up**
- <the 3 to 5 signals that drove tonight's work, each with its source>

**Skipped or yielded**
- <job>: <why, one line>

**Manifesto**
- <rules learned tonight, marked provisional>

Reply here: `1 keep` · `2 tweak: shorter, lead with the ask` · `3 kill: not our ICP` · `ship 1` · `P1 now` / `P1 later` / `P1 never`
```

Use the job numbers consistently: review mode resolves "keep 2" against this brief. Store each number in the job's Brief No field.

**Share level.** Two versions of the brief:

- **Owner version:** the full brief, sent only to owner-only channels (the run's chat, the owner's email).
- **Team-safe version:** the same brief with anything harvested from the owner's private sources (personal email, DMs, private calendar) reduced to generic job titles and links. Always used for the Run row body, and for every channel when `brief.share_level: team` or the channel is shared (a Slack channel).

Outputs built from private sources go in an owner-only part of the workspace (a private page or folder), not the shared workspace.

## 7. Operations by backend

| Operation | Notion | Markdown (Drive, Obsidian, local, repo) |
| --- | --- | --- |
| Read the Registry | Fetch the database | Read `Cortex Gnome/Registry/*.md` frontmatter |
| Read open jobs | Fetch the "Open jobs" view (Queued, Proposed, Claimed, Building, Needs Decision) | List `Cortex Gnome/Jobs/`, read frontmatter, filter by status |
| Read running runs | Fetch the "Running" view | List `Cortex Gnome/Runs/`, filter by status |
| Create a job or run | Create a page with all fields | Write `Jobs/<YYYY-MM-DD>-<slug>.md` or `Runs/<gnome>-<YYYY-MM-DD-HHMM>.md` |
| Update a job or run | Fetch fresh, change only the fields that changed | Read, change frontmatter, write back |
| Read or edit the Manifesto | Fetch the page; targeted edit of one section | Read the file; change one section; write back |

Setup creates the saved views in Notion: Open jobs, Ready for review (Status Ready or Needs Decision, Verdict empty), Unlearned verdicts (Verdict, Answer, or Ship Approved to Ship set, Learned unchecked), Running, Recent runs. On Markdown backends, each view is the same filter applied to the folder's frontmatter.

Markdown layout:

```
Cortex Gnome/
  Gnome Manifesto.md
  Registry/
    Eric's Gnome.md
  Runs/
    Eric's Gnome-2026-10-12-1852.md
  Jobs/
    2026-10-12-q4-board-deck.md
  Workspace/
```

On Google Drive, create files as plain Markdown, never Google Docs.
