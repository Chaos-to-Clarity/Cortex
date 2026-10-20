# Cortex Spec

How every Cortex skill, and any agent that uses a Cortex, stores and finds context. Read this before any read or write.

The master copy lives in `spec/cortex-spec.md` in the Cortex repository and is copied into each skill's `references/` folder. Edit the master, then run `python scripts/sync_spec.py`.

## 1. The idea

A Cortex is a business's context layer: what stays true about the work, structured so any AI can find the right piece fast and file new information in the right place.

Writing to a store is easy. Finding the right context in a growing, unique, many-writer store is the hard part. Cortex solves it with three layers, always read top-down:

| Layer | What it is | Size | When it's read |
| --- | --- | --- | --- |
| **Map** | One page: settings, every collection and where it lives, routing rules, a glossary of key names, freshness | Under 10,000 characters (about 2,500 tokens) | First, on every use |
| **Catalogs** | One compact table per collection, one line per record | About 150 characters per row | To choose which records to open |
| **Records** | The full detail on one person, initiative, decision, or item | Any | Only the records chosen |

Two supporting pieces keep it clean:

- **Inbox:** where anything goes that doesn't clearly fit. Nothing is forced into the wrong place, and no one invents structure on the fly.
- **Ingest Log:** what's been processed, so nothing is ingested twice.

A typical question costs one Map read, one or two catalog reads, and two or three records. No listing, no searching, no sifting.

**What's universal vs. what's unique.** The rules and protocols in this spec are the same for every business and live in the skills. The Map, catalogs, and glossary are unique to each business, evolve with it, and live in the user's own store.

## 2. Collections and records

**Core collections**

| Collection | Identity | Fields |
| --- | --- | --- |
| People | Name | Role, Context (the one thing worth remembering), Cadence, Open Thread, Company (relation to Companies), Initiatives (relation), Depth, Mentions |
| Companies | Name | Relationship (Customer, Prospect, Investor, Partner, Vendor, Competitor, Portfolio, Other), Stage or Size, What They Do, Open Thread, Owner (relation to People, who on the owner's side holds the relationship), People (relation), Initiatives (relation), Depth, Mentions |
| Initiatives | Name | Why It Matters, Blocker, Next Action, Start, Target, Owner / Involved (relation to People), Companies (relation), Decisions (relation) |
| Decisions | Title | Reasoning, Date, Supersedes (title of the earlier decision), Affects (relation to Initiatives) |
| Inbox | Title | Content, Suggested Collection, Candidates (possible matching records), Date |
| Ingest Log | Source | Type (Meeting Notes, Email, Document, Strategy, Query Insight, Health Check, Dream), Date Ingested, What Changed |

**Core pages:** Map, Standing Context (durable facts about the business and the user's role), Strategy (a summary at the top, then one dated section per strategy document), Dream Journal (what each night's dream changed, noticed, and needs the owner to decide; section 15).

**Status values**

| Collection | Values |
| --- | --- |
| People | Active, Dormant, Archived |
| Companies | Active, Dormant, Archived |
| Initiatives | Active, Paused, Done, Dropped |
| Decisions | Decided, Open, Reversed, Superseded |
| Inbox | New, Filed, Discarded |

**Every record in every collection** (core or added, except the Ingest Log) also carries:

- **Summary:** one line, 15 words or fewer, stating the current state. This is what goes in the catalog.
- **Aliases:** other names it goes by (nicknames, abbreviations, old names), comma-separated.
- **Status**, **Last Updated** (date), **Source** (where the latest change came from).

**Record body.** Keep properties short. Long text goes in the body:

```markdown
## Current
What's true now, in a few lines.

## History
- 2026-10-10: Role changed from Head of Sales to CRO (Granola, Acme sync)
- 2026-08-02: First added (Setup interview)
```

When a fact changes, update the field and the Summary, and add a dated History line. Readers get the truth from the top without reading history. History is never deleted.

**Compaction.** History grows; Current must not fall behind it. When a record has five or more History lines dated after its Current section was last rewritten, rewrite Current from the full record, refresh the Summary, and add a History line "Current rewritten". Writers may compact when they notice it; the weekly health check guarantees it. Never shorten or delete History lines while compacting.

**Depth (People and Companies).** Not everyone mentioned once deserves a full record. Depth keeps the Cortex lean:

| Depth | When | What it holds |
| --- | --- | --- |
| **Stub** | First mention in a source, no working relationship yet | Name, Summary, Company (for people), Source, Mentions. No body beyond one History line. No glossary entry |
| **Full** | A third mention in separate sources, a working relationship (client, investor, teammate, active deal), or the user asks | Every field, a Current section, History, and a glossary entry if the user refers to them by name |

**Mentions** counts the separate sources (meetings, emails, documents) that referenced the record. Writers add one per new source and promote a Stub to Full when it qualifies. A Stub that never reaches a second mention in `health.stub_expire_days` is archived by the health check.

**Link weight.** A record's importance is how connected it is: the number of records it relates to plus the number that relate to it. Catalogs list their rows most-linked first, the glossary keeps the most-linked terms, and readers open the most-linked match first when two records fit. Nothing stores the count; it's computed from relations when a catalog is rebuilt.

**Added collections.** Businesses add their own (Customers, Pipeline, Portfolio, Coaching Sessions). Each one has a title identity plus Summary, Aliases, Status, Last Updated, and Source, gets a catalog, and is registered in the Map with routing rules. Plugins that build on Cortex (Founder OS, for example) register their collections the same way.

**Logs.** Some collections are logs rather than records: the Ingest Log, and plugin logs such as Cortex Gnome's Gnome Runs and Gnome Jobs. Logs skip the catalog, the Summary, and the Current and History body. They're registered on the Map like any collection, marked "log" in the Catalog column, and read through saved views or a folder listing, newest first.

**Cortex Gnome.** The overnight worker registers Gnome Registry, Gnome Runs, Gnome Jobs, and a Gnome Manifesto page under a "Cortex Gnome" page or folder. Any skill or person hands work to it by adding a Gnome Jobs row with Status Queued. Gnomes read the Cortex with the Reading protocol and write to core collections only through the Inbox.

## 3. Backends

| Backend | Where it lives | How the skill reaches it |
| --- | --- | --- |
| Notion | A parent page: the Map and other pages as pages, collections as databases, catalogs as pages | The Notion connector |
| Google Drive | A folder of Markdown files | The Google Drive connector |
| Obsidian | A folder inside the user's vault | A folder connected through the Claude desktop app, or an Obsidian connector |
| Local folder | Any Markdown folder on the user's computer, including Dropbox, iCloud, and OneDrive sync folders | A folder connected through the Claude desktop app |

For any other tool with a connector (Airtable, Coda, Confluence), map the same model as closely as it allows and record the mapping in the Map's field map.

Obsidian and local folders live on the user's computer. Scheduled runs reach them only while that computer is on with the Claude desktop app open. For version history on Markdown backends, suggest Obsidian's community Git plugin or a synced folder with file history; Cortex works the same either way.

## 4. The Map

### Finding it

1. If the user's instructions give a direct link to their Cortex Map, open it. No searching.
2. Otherwise: search Notion for a page titled exactly "Cortex Map", then Google Drive for "Cortex Map.md", then connected folders for "Cortex Map.md".
3. Not found: the Cortex isn't set up. Say so in one line and offer cortex-setup.

Then validate: open one collection the Map points to. If it fails, say which pointer broke and offer cortex-map to repair it. Never guess a replacement silently.

### Format

The Map is self-describing, so an agent that has never seen this spec can still use it correctly. Keep this structure and these headings:

````markdown
# Cortex Map

This is the map of [Owner]'s Cortex: what's in it, where each thing lives, and where new information goes.
**Reading:** resolve names through the Glossary, pick records from the Catalog, open only those records. Cite records and their dates. If something isn't here, say it's not in the Cortex; don't assume it doesn't exist.
**Writing:** route with the Routing rules, find the existing record by name or alias and update it in place, update its catalog line, then log it in the Ingest Log. If it fits nowhere or the match is unclear, put it in the Inbox. Never delete; close records with a status.

## Settings
```text
map_version: 2
owner: <first name>
time_zone: <IANA zone>
backend: <notion | google-drive | obsidian | local-folder | other: name>
root: <Notion page URL, or folder path / Drive folder ID>
page.standing_context: <link>
page.strategy: <link>
page.schema: <link, or none>
page.dream_journal: <link, or none>
sources.meeting_notes: <granola | fireflies | otter | fathom | notion-meetings | folder: path | none>
sources.calendar: <google-calendar | outlook | device | none>
sources.calendar_id: <primary or id>
sources.email: <gmail | outlook | none>
sources.documents: <google-drive | dropbox | onedrive | box | none>
sources.strategy_folder: <folder, or none>
update.lookback_days: 7
update.approval: <autonomous | required>
health.stale_after_days: 60
health.stub_expire_days: 90
health.orphan_after_days: 90
dream.sources: <meeting-notes | none>
dream.max_records: 40
dream.started: <ISO datetime, or never>
dream.last_run: <ISO datetime, or never>
dream.cursor: <Collection: Identity, or start>
```

## Synthesis
<One paragraph: where things stand right now.>

## Collections
| Collection | Holds | Identity | Key fields | Statuses | Catalog | Location |
| --- | --- | --- | --- | --- | --- | --- |
| People | Everyone the owner deals with regularly | Name | Role, Company, Context, Open Thread, Depth | Active, Dormant, Archived | <link> | <link> |
| Companies | Customers, investors, partners, vendors, competitors | Name | Relationship, What They Do, Open Thread, Depth | Active, Dormant, Archived | <link> | <link> |

## Routing
**Find it**
- Who someone is, a relationship, meeting prep → People, then their Company and linked Initiatives
- A customer, investor, partner, or competitor; "what's going on with [company]" → Companies, then its People and Initiatives
- What's being driven, status, blockers → Initiatives
- What was decided and why → Decisions
- Positioning, ICP, GTM, brand, targets → Strategy
- Durable facts about the business or role → Standing Context

**File it**
- A new person, or a change about a person → People (a Stub on first mention)
- A new company, or a change in a relationship with one → Companies (a Stub on first mention)
- Something the owner is driving, or a change to it → Initiatives
- A call made, a question opened or closed → Decisions
- A durable fact about the business → Standing Context
- Strategy content → Strategy (dated section)
- Unclear fit or unclear match → Inbox

## Glossary
| Term | Means | Points to |
| --- | --- | --- |
| <name, nickname, acronym> | <a few words> | <Collection: record> |

## Freshness
| Source | Last processed |
| --- | --- |
| Meeting notes | <date> |

Records: <People 42 active, 10 archived; Initiatives 9 active; ...>. Inbox: <n> waiting. Map rebuilt <date>.

## Field map
<none, or collection.field = actual name, one per line>
````

### Budget and ownership

- Keep the Map under 10,000 characters (about 2,500 tokens), counting any table markup the backend adds. The glossary holds the 50 terms that matter most; when it's full, the least-referenced Archived or Dormant terms drop first (their records keep their Aliases, so catalogs still find them).
- **Structure** (Settings, Collections, Routing, Field map) changes only through cortex-setup or cortex-map, or when a user approves a new collection.
- **Any writer** may add a Glossary row for a new key entity or nickname, while the glossary has room.
- **cortex-update** and **cortex-dream** maintain Synthesis and Freshness. cortex-dream also owns the `dream.*` settings and `page.dream_journal`, and may add them to a Map that lacks them.

## 5. Catalogs

One per collection. In Notion, a page titled "[Collection] Catalog" under the Cortex parent. In Markdown, `_catalog.md` inside the collection's folder.

```markdown
# People Catalog
Active and Dormant records. Archived: [People Catalog (Archive)]. 42 rows. Rebuilt 2026-10-10.

| Name | Aliases | Status | Depth | Summary | Updated | Link |
| --- | --- | --- | --- | --- | --- | --- |
| Jane Rivera | Jane R | Active | Full | Acme CRO; renewal decision owner; wants short written updates | 2026-10-10 | <link> |
```

Rows are ordered most-linked first (see Link weight), then by most recently updated.

- **Depth column.** People and Companies catalogs show Depth, so readers can tell a one-line stub from a full record.
- **Key columns.** A collection may add up to three columns it is commonly filtered by, between Status and Summary (Tasks: Due, Priority, Week). List them in the Map's Collections table under Key fields.
- **Every write updates the catalog row** in the same step as the record. A record missing from its catalog is invisible to readers.
- **Archive split.** Records with a closed status (Archived, Done, Dropped, Reversed, Superseded, Filed, Discarded) move to "[Collection] Catalog (Archive)". Default reads skip it. Read it only when the question is about history.
- **Sharding.** When a catalog passes 300 rows, split it by a field that divides it well (Type, Stage, Year) into "[Collection] Catalog: [value]" pages, and list the shards in the Map's Collections table.
- **Catalogs are an index, not the truth.** The record wins. If they disagree, fix the catalog and say so.

## 6. Reading (any agent, any question)

1. **Map first.** One read. If the question doesn't need business context, stop here.
2. **Resolve names.** Match every person, company, project, and term in the question against the Glossary, then catalog Names and Aliases. Use near-matches for typos. Two plausible matches: say which you picked, or ask.
3. **Route.** Use the Routing rules to choose collections. Read their catalogs, not the databases.
4. **Open only what's needed.** Open the chosen records. Follow relations one hop (a person's initiatives, an initiative's decisions), no further unless the question demands it. If the answer needs more than about 10 records, answer from catalog summaries and say so.
5. **Check freshness.** Compare record dates and the Map's Freshness to what the question needs. For time-sensitive questions, pull live sources too. When live data is newer and conflicts with a record, the live data wins for the answer, and the conflict is flagged.
6. **Answer with provenance.** Cite each record used and its Last Updated date.
7. **Scoped search, only on a miss.** If the Glossary and catalogs found nothing for a name or topic the question depends on, run one keyword search limited to the Cortex itself: the Cortex parent page in Notion, the Cortex folder in Drive or a local folder. Use the two or three most distinctive words. Open at most three hits. If something turns up that a catalog should have found, fix that record's Summary or Aliases so the next read finds it directly.
8. **Absence is not evidence.** If the scoped search also misses, say "not in the Cortex," never "doesn't exist" or "hasn't happened."

Never list whole databases, search the workspace outside the Cortex, or load every record "to be safe." That's what the Map and catalogs replace. If the Map is missing or broken, say so and offer cortex-map; don't fall back to sifting.

## 7. Writing (any agent, any source)

1. **Map first.** Read the Settings, Collections, Routing, and Field map.
2. **Check the Ingest Log** for this source. Already there: skip it, unless the user says re-ingest.
3. **Keep only what's durable**: true for weeks or months. Day-to-day task noise doesn't belong in the Cortex.
4. **Route** each item with the Routing rules.
5. **Resolve identity** through the Glossary and catalog Names and Aliases.
   - One clear match: update it.
   - No match: create a new record.
   - Two or more plausible matches, or you're unsure: don't guess. Put it in the Inbox with the candidates listed.
6. **Write the record.** If History now has five or more lines since Current was rewritten, compact it (section 2).
   - New: all fields, Summary, Aliases if known, Status Active (Open for an undecided question), Last Updated today, Source. People and Companies start as a Stub unless they already qualify as Full (section 2, Depth).
   - Existing People or Companies record from a new source: add one to Mentions, and promote a Stub to Full when it qualifies.
   - A person tied to a company: link them, creating the company as a Stub if it doesn't exist.
   - Change: re-read the record first, update the fields and Summary, add a dated History line, refresh Last Updated and Source.
   - Ended or reversed: set the closing status and add a History line. Decisions: create the new one and set Supersedes. Never delete; delete only a true accidental duplicate.
7. **Update the catalog row** in the same step. Moving to a closed status moves the row to the Archive catalog.
8. **Glossary.** If a new key entity or nickname appeared and the glossary has room, add a row. Stubs never get glossary rows.
9. **Log it:** one Ingest Log row per source with what changed.
10. **New category?** If content clearly needs a collection that doesn't exist, put it in the Inbox and propose the collection. Create it only after the user approves, even in autonomous runs.

Write in the user's words. Condense. Drop marketing language and filler.

## 8. Operations by backend

| Operation | Notion | Markdown (Drive, Obsidian, local) |
| --- | --- | --- |
| Read Map or page | Fetch the page | Read the `.md` file |
| Edit a page section | Targeted edit of that section only | Read, change that section, write the file back |
| Read a catalog | Fetch the catalog page | Read `_catalog.md` |
| Open a record | Fetch the page | Read `<Identity>.md` |
| Create a record | Create a page in the database with all fields, body as in section 2 | Write `<Identity>.md` with frontmatter and body |
| Update a record | Fetch fresh, update only changed fields, append to History | Read, change frontmatter and body, write back |
| Update a catalog row | Edit that row on the catalog page | Edit that row in `_catalog.md` |
| Log | Create an Ingest Log row | Append a row to `Ingest Log.md` |
| Rebuild a catalog | Query the database through a saved view (SQL queries count against usage limits on some Notion plans), write the catalog page | List the folder, read frontmatter, write `_catalog.md` |

**Notion catalogs.** Notion returns page mentions without their titles when a page is read back, so a catalog's Name column is always plain text and the link goes in its own Link cell. Never rely on a mention to carry a name.

**Concurrency.** Several agents may write the same Cortex. Re-read a record or catalog immediately before changing it, and change only your rows. The weekly health check repairs any drift.

## 9. Markdown layout

```
Cortex/
  Cortex Map.md
  Standing Context.md
  Strategy.md
  Dream Journal.md
  Cortex Schema.md        (optional; user's own extra rules)
  Ingest Log.md
  People/
    _catalog.md
    _catalog-archive.md
    Jane Rivera.md
  Companies/
  Initiatives/
  Decisions/
  Inbox/
```

Added collections get their own folder, for example `Founder OS/Tasks/`.

**Record file.** File name is the identity, with `/ \ : * ? " < > |` replaced by `-`. Fields go in YAML frontmatter, dates as `YYYY-MM-DD`, relations as wikilink lists so Obsidian renders them:

```markdown
---
name: Jane Rivera
summary: Acme CRO; renewal decision owner; wants short written updates
aliases: [Jane R]
role: CRO
company: "[[Acme]]"
depth: Full
mentions: 6
context: Decides on renewals; prefers short written updates
cadence: Biweekly
open_thread: Waiting on Q3 pricing proposal
status: Active
initiatives: ["[[Q3 Pricing Reset]]"]
last_updated: 2026-10-10
source: Granola, Acme sync Oct 10
---

## Current
...

## History
- 2026-10-10: ...
```

Catalog link cells use wikilinks: `[[Jane Rivera]]`. `Ingest Log.md` is one table, newest row at the bottom.

**Google Drive.** Create files as plain Markdown (`text/markdown`), never as Google Docs. Updates rewrite the whole file: read, change, write back in one step.

## 10. Health check

Run in full by cortex-update each week and by cortex-map on demand. cortex-dream runs the same checks nightly, but only on the records in its working set (section 15). Fix what's safe to fix; report the rest.

| Check | Action |
| --- | --- |
| Catalog drift: rows missing, extra, or out of date | Rebuild the catalog from the records |
| Records missing a Summary | Write one from the record |
| Records with five or more History lines since Current was rewritten | Compact them (section 2) |
| Stubs mentioned in three or more sources, or tied to an active relationship | Promote to Full |
| Stubs with one mention older than `health.stub_expire_days` | Archive them |
| Orphans: Active records with no relations, no glossary entry, and no update in `health.orphan_after_days` | List them as archive candidates; archive only with a yes |
| Catalog order | Re-sort by link weight |
| Active records not updated in `health.stale_after_days` | List them for the user to confirm, close, or refresh |
| Alias collisions (two records share a name or alias) | Report as likely duplicates; merge only with a yes |
| Inbox items waiting | Triage: file the clear ones, report the rest |
| Map over 10,000 characters | Trim the glossary and Synthesis |
| Collections in the store that the Map doesn't list | Report them; offer cortex-map to register them |
| Broken Map pointers | Report; offer cortex-map to repair |

Log one Ingest Log row, Type Health Check, with what was fixed and what needs the user.

## 11. Imports

To seed a Cortex from what the user already has, cortex-map imports exports:

| Export | Becomes |
| --- | --- |
| CRM contacts or accounts (CSV) | People and Companies, as Stubs unless marked as active relationships |
| LinkedIn connections (CSV) | People Stubs with Company links. Import only the ones the user selects, never the whole network |
| A notes vault (Obsidian, Notion, Logseq, Roam, plain Markdown) | Registered or mapped collections, through cortex-map adopt |
| JSON or spreadsheets of records | The matching collection, with fields mapped and confirmed first |

Every import resolves identity against existing records first, sets Source to the file name, logs one Ingest Log row, and rebuilds the affected catalogs.

## 12. Upgrading from map version 1

Maps with `map_version: 1` have no Companies collection and no Depth. cortex-map upgrades them on request: it adds Companies (and offers to create Company records from People roles), adds Depth and Mentions to People, marks existing People as Full, rebuilds catalogs, and sets `map_version: 2`. Skills keep working on version 1 Maps until then; they skip Depth rules where the fields are missing.

## 13. Rules

These apply to every read and write. If the user keeps a Cortex Schema page with extra rules, read it once and follow it too; theirs win where they differ.

- **Map first.** Every use starts at the Map. Never sift the store.
- **Identity first.** Find the existing record by name or alias before writing. Never create a second record for the same thing.
- **Unsure goes to the Inbox.** An unclear fit or an unclear match is never guessed.
- **Earn depth.** First mentions are Stubs. Records grow as relationships do.
- **Keep Current current.** Compact when History outruns it.
- **Supersede, don't delete.** Close with a status and keep history.
- **Catalog with every write.** The record and its catalog row change together.
- **Stamp every write.** Last Updated and Source, every time. The dream's maintenance edits stamp a History line instead (section 15).
- **Log every ingest.** Check the log before, add a row after.
- **Durable only.** Task noise belongs in Founder OS or a task tool, and overnight work in Gnome Jobs.
- **Cite and date.** Answers name the records they used and how fresh they are.
- **Inferred stays labeled.** Patterns an agent infers live in the Dream Journal with their evidence. They enter records only when the owner confirms them.

## 14. Global awareness: custom instructions

Any AI assistant that can reach the user's store can use a Cortex. Custom instructions give every conversation, on any platform, awareness that the Cortex exists, without making every chat pay for a lookup.

**Design rules**

- **Aware always, fetch rarely.** Most chats don't need business context. The instructions carry one line about who the user is, plus a gate for when a lookup is worth it.
- **The gate.** Look only when the request is about the user's business, people, clients, projects, decisions, or priorities, *and* the answer would be clearly better or safer with that context. If unsure, ask in one line instead of fetching.
- **Cheapest step first.** The Map, once per conversation, reused after that. Catalogs only for names or topics that matched. Records only for the few that matter.
- **Direct link.** The Map's URL is in the instructions, so finding it never takes a search.
- **Under 1,000 characters,** so it fits every platform's custom-instructions limit with room for the user's own preferences.
- **Fail quietly.** If the assistant can't reach the store, it says so once and carries on.
- **Set once.** Nothing in them changes week to week. Priorities, clients, and key people live in the Map and records, so the instructions never go stale and never expose names.

**Template.** cortex-setup fills in the brackets: the backend, the Map's direct link, and one durable line about the user. Never put priorities, client names, or anything else that changes into it.

```text
## My Cortex
My business context lives in my Cortex, a structured knowledge base in [Notion]. Map: [link to your Cortex Map]

About me: [Name], [role] at [company], which [what the business does, in a few words].

When to look: only when my request is about my business, people, clients, projects, decisions, or priorities AND the answer would be clearly better or safer with that context (I name someone or something, want advice on my situation, or ask you to draft, plan, or prep). Skip it for general questions, generic writing, or code, or when this chat already has what you need. If unsure, ask me in one line instead of looking.

How: read the Map once per chat and reuse it. Use its Glossary and Catalogs to open only the few records you need; never search my whole workspace. Cite what you used and its date. If it isn't there, say so. If you can't reach it, tell me once and carry on.
```

**Keeping it current.** There is nothing to keep current. Current priorities live in the Map's Synthesis, which cortex-update maintains. The text changes only if the Map moves or the user's role changes; cortex-map reports the new text when the Map moves.

## 15. Dreaming: nightly consolidation

Every write adds a little: a History line, a Stub, a catalog row, an Inbox item. Without a pass that steps back, the Cortex drifts. Current falls behind History, the same fact lives in two places with two values, "waiting on the proposal next week" is still on a record a month later, and catalogs and the glossary slowly stop matching what's in the records. cortex-dream is that pass. It runs nightly while no one is working, so daytime reads hit a store that is already clean.

It works like sleep: replay the day, fold it into what's already known, notice patterns, downscale what no longer matters, and leave a short note for the morning.

**Localized, not global.** A dream opens a bounded working set, never the whole Cortex. Rewriting everything every night costs the most and loses the most detail. In priority order, up to `dream.max_records` records:

1. Last night's carryover: what didn't fit, listed in the last journal entry
2. Meeting notes from the last `update.lookback_days` days not yet in the Ingest Log (when `dream.sources` includes them)
3. Records written since `dream.last_run`, named in the Ingest Log rows since then or found by the catalogs' Updated column
4. New Inbox items, and Ingest Log rows of Type Query Insight since the last dream
5. One-hop neighbors of the records in 3 (a changed person's company and initiatives)
6. A rolling slice: the next Active records after `dream.cursor`, walking the catalogs in Map order, so every record is revisited every few weeks even when nothing touches it

What doesn't fit carries to the next night. The cursor moves past what was reviewed. A dream reads the Map, the journal, and the Ingest Log first, and only the catalogs they point to.

**The phases**

| Phase | What it does |
| --- | --- |
| Orient | Read the Map, the Dream Journal, the Ingest Log since the last dream, and only the catalogs those point to; build the working set. No writes |
| Replay | Ingest the new meeting notes with the Writing protocol (section 7). Email and calendar stay with the weekly cortex-update |
| Consolidate | In the working set: resolve contradictions by superseding, turn relative dates into absolute ones, flag what time has made stale, compact, promote and expire Stubs, add relations the text makes obvious, triage clear Inbox items, apply alias fixes from Query Insights |
| Abstract | Look across the working set and recent journal entries for patterns no single record shows. Write them to the Dream Journal, labeled inferred, with evidence. Refresh Synthesis if the picture shifted |
| Downscale | Fix catalog rows for the working set, re-sort only changed catalogs, trim the glossary and Map to budget, update Freshness and the `dream.*` settings |
| Journal | Add the night's entry to the Dream Journal and one Ingest Log row, Type Dream |

**Contradictions.** Two claims about the same thing in the records: the newer dated source wins, and the older claim is closed, never erased. The field takes the new value and History gets "Was [old] until [date] ([source])", so the Cortex can still answer what was true then. If the dates tie, the sources are different in kind (a record says one thing, a strategy doc another), or the claim is about a person's private context, the dream doesn't choose. It asks the owner.

**Time.** Relative dates in Current and the short fields are rewritten as absolute ones, anchored to the History line that introduced them ("next Friday" added on 2026-10-10 becomes "Oct 16, 2026"). With no clear anchor, the dream asks. Then the dream flags what time has passed by: an Open Thread or Next Action that names a date already gone, a "waiting on" older than 14 days, an Active initiative past its Target, an Open decision older than 30 days. Flags go to the owner. The dream never closes a record because a date passed.

**What a dream may do on its own:** supersede a contradicted field with a dated History line, rewrite relative dates, compact Current and refresh Summaries, promote Stubs, archive Stubs past `health.stub_expire_days`, add obvious relations, file clear Inbox items, discard exact duplicate Inbox items, add aliases and glossary rows, fix catalogs, trim the Map, update Synthesis and Freshness. Every change gets a History line with Source "Dream, [date]", so each one is visible and reversible. Last Updated moves only when a change brings in a new fact (a replayed meeting, an owner's answer). Maintenance alone leaves it, so stale and orphan checks still measure real activity. This is the one exception to stamping every write.

**What needs the owner's yes:** merging records, archiving or closing anything that isn't an expired Stub, changing a status on inference, saving an inferred pattern to a record, Standing Context, Strategy, or Decisions, and any change to Map structure. These go to the journal's Questions for you.

**Compaction keeps specifics.** A rewritten Current keeps every name, number, date, amount, and commitment that is still true. It drops repetition, not detail. Abstracting "Jane wants the Q3 pricing proposal by Oct 30" into "Jane wants updates" is information loss, not consolidation.

**Approval.** With `update.approval: required`, a dream changes nothing except the Dream Journal, the Ingest Log, and its own `dream.*` settings. The journal lists the edits it would make.

**One at a time.** A dream sets `dream.started` before its first write and `dream.last_run` when it finishes. If `dream.started` is newer than `dream.last_run` and under two hours old, another dream is running: stop. If `dream.last_run` is under 12 hours old, the night's work is done: stop, unless the owner asks for another pass.

**Light nights.** If nothing new arrived and no records changed, a dream reviews only the rolling slice and writes a one-line entry. Most nights should cost little.

**Dream Journal.** One page (`Dream Journal.md` in Markdown), newest entry first:

```markdown
# Dream Journal

## Questions for you
- [ ] Acme renewal: Initiative target was Oct 15 and it's still Active. Done, or new date? (Initiatives: Acme Renewal)
- [ ] "Sam" and "Sam Ortiz" look like one person. Merge? (People: Sam, Sam Ortiz)

## Patterns
- Hiring came up in 4 meetings with 3 people this week, and no initiative holds it. Seen 3 nights. (Inferred. Evidence: ...)

## 2026-10-20
Replayed 3 meetings. Updated 7 records, superseded 2 facts, compacted 2, promoted 1 Stub, filed 2 Inbox items. Reviewed People A to D.
```

Questions stay until the owner answers them, then they are applied and removed. The same question is never listed twice. One unanswered for 14 nights is dropped and noted once, and returns only if its record changes. A pattern seen on three or more nights, or one the owner confirms, becomes a question proposing where to save it. Keep 14 nightly entries; roll older ones into one line per month under "Earlier". Keep the page under 6,000 characters.
