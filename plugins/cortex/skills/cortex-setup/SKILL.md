---
name: cortex-setup
description: Builds a Cortex, the context layer AI reads first, for one founder or a whole company, in Notion, Obsidian, or Google Drive. Fills it, writes the Map and custom instructions. Run once.
---

# Cortex Setup

Build the user's Cortex: a structured store of what stays true about their work, with a Map that every AI reads first. Then fill it with real context. Run once. If a Cortex already exists, build on it and never overwrite.

Read `references/cortex-spec.md` first. It defines the layers, the Map format, the record format, the backends, and the rules. On the company branch (Step 1b), also read `references/company-pack.md`.

Keep the user moving. Use AskUserQuestion for choices (up to 4 per call, recommended option first). Do discovery silently before asking.

## Step 1. Check for an existing Cortex

Look for a Cortex Map (spec section 4). If one exists and validates, say the Cortex is already set up, show where, and offer to: fill thin collections (Step 7), add a source, change a setting, schedule the nightly dream and weekly update if they aren't scheduled yet (Step 9), or repair the Map with cortex-map. Stop there unless they pick one.

If the Cortex exists, has no `pack.company` setting, and the user says it should now serve their company, offer the migration in company-pack section 12. Walk it step by step and never invite a second person before the private records have moved.

Also look for an older setup: a page named like "Brain", "Second Brain", or "My Brain" holding People, Initiatives, or Decisions databases, or a folder of notes organized the same way. If found, offer to adopt it: hand off to cortex-map in adopt mode, which registers what exists without moving or renaming anything.

## Step 1b. For you, or for your company?

Ask one question (AskUserQuestion): **"Is this Cortex for you, or for your company?"**

- **For me** (recommended for a founder working alone, or anyone in a bootcamp): a founder Cortex. Follow the steps below as written.
- **For my company:** a company Cortex that the exec team shares. Follow the steps below with the company additions marked **Company:** in each step. They come from `references/company-pack.md`.

**Company:** before going on, confirm who's setting it up (the CEO or the Chief of Staff; never an outside coach or consultant, who doesn't get a seat) and the company name. Explain in two lines that a company Cortex gives each person their own private space and that access is set by who joins which space.

## Step 2. Choose where it lives

Ask:

- **Notion** (recommended if they use Notion): databases with relations, easiest to browse and edit
- **Obsidian:** Markdown files in their vault, linked with wikilinks
- **Markdown in Google Drive:** plain files in a Drive folder, readable by any tool
- **Something else:** a local folder, or another app with a connector

Then confirm access:

- Check the matching connector or folder tool is available. If not, search the connector registry and suggest it. For Obsidian or a local folder, the Claude desktop app must connect the folder; explain how, and that scheduled runs need that computer on.
- Ask where to put it. Default: a page or folder named "Cortex".
- For Obsidian or a local folder, suggest Obsidian's Git plugin or a synced folder for version history (optional).
- Test write: create the parent. If it fails, report the error plainly and stop until access works.
- **Company:** recommend Notion, because teamspaces enforce who sees what. With Google Drive, folders are shared per space. With Obsidian or a local folder, say plainly that the folder can't restrict access, and recommend Notion or Drive instead. Then create the spaces (company-pack section 6): the Company teamspace or folder, the Exec teamspace or folder, and a Private space for the person setting it up. Ask them to make each teamspace closed or private.

## Step 3. Connect sources

Ask which tools they use, pre-selecting what's already connected:

- Meeting notes: Granola, Fireflies, Otter, Fathom, Notion meeting notes, a notes folder, or none
- Calendar: Google Calendar, Outlook, the device calendar, or none
- Email: Gmail, Outlook, or none
- Documents: Google Drive, Dropbox, OneDrive, Box, or none

Test each with one small read. Report each as connected or not. For failures, name the connector, suggest it from the registry, and continue. Missing sources limit what the Cortex learns; they don't block setup.

**Company:** these are the first member's sources. Each other member connects their own when they join (Step 8).

## Step 4. Build the structure

Under the parent, create (spec sections 2, 5, and 9):

1. **People**, **Companies**, **Initiatives**, **Decisions**, and **Inbox** collections, each with its fields plus Summary, Aliases, Status, Last Updated, and Source. People and Companies also get Depth (Stub, Full) and Mentions.
2. **Ingest Log** collection.
3. **Standing Context**, **Strategy**, and **Dream Journal** pages. Strategy starts empty with a note that strategy-digest fills it. Dream Journal starts with empty Questions for you and Patterns sections (spec section 15).
4. **One catalog per collection** (People, Companies, Initiatives, Decisions, Inbox), each with just its header and an Archive catalog.

**Company:** also create the pack (company-pack section 3): Departments, Metrics, Metric Values (a log), Company Commitments, Org, Board, and Risks, each with its fields, statuses, catalog, and Archive catalog. Add a Visibility field (Company, Exec, Private) to Initiatives and Decisions. Put each collection in the space section 6 names; Initiatives, Decisions, and Company Commitments get one database in Company and one in Exec. The Dream Journal, Inbox, and Ingest Log go in the Company space.

Relations:

- Notion: People gets "Company" (two-way with Companies, shown there as "People"). Companies gets "Owner" (relation to People). Initiatives gets "Owner / Involved" (two-way with People, shown there as "Initiatives") and "Companies" (two-way with Companies, shown there as "Initiatives"). Decisions gets "Affects" (two-way with Initiatives, shown there as "Decisions").
- Markdown: wikilink lists in frontmatter.
- **Company:** Departments get Head (People), Metrics (two-way with Metrics), and Dependencies (Departments). Metrics get Owner (People) and Department. Metric Values get Metric. Company Commitments get Owner and Made To (People) and Department. Org gets Holder (People), Reports To (Org), and Department. Board gets Members (People) and Follow-ups (Company Commitments). Risks get Owner (People) and Related (Initiatives, Metrics, Departments).

## Step 5. Ask two settings

In one AskUserQuestion call:

- **Updates:** apply and report (recommended, needed for scheduled runs), or show edits first. This sets `update.approval`.
- **Time zone:** confirm the one detected from their calendar.
- **Company:** the reviewer, who answers the dream's questions: the Chief of Staff (recommended), or the CEO if there is none.

## Step 6. Write the Map

Create the Cortex Map page or file at the top of the parent (**Company:** in the Company space), in the exact format in spec section 4: the self-describing header, Settings (with `page.dream_journal` linked, `dream.sources` set to `meeting-notes` if a meeting-notes source is connected, and `dream.started`, `dream.last_run` at `never`), an empty Synthesis, Collections (with catalog and location links for every collection), the default Routing rules, an empty Glossary, Freshness, and Field map: none.

**Company:** add `pack.company: 1`, `company.name`, and `company.reviewer` to Settings; add the Members section with the first member's row (company-pack section 5); add the pack's Collections rows, with both locations for split collections and `log` for Metric Values; and add the pack's Routing lines (company-pack section 7).

## Step 7. Fill it with real context

1. **Seed from what they have.** Offer to import a CRM export or a LinkedIn connections CSV (spec section 11) through cortex-map; it's the fastest way to start with real People and Companies. Skip if they have none.
2. **Draft from sources.** If meeting notes or calendar are connected, scan the last 30 days. Draft People and Companies from recurring names and Initiatives from recurring themes. Show both lists before writing.
3. **Interview, one collection at a time:** People, Companies, Initiatives, Decisions, Standing Context. Three to seven records each to start. Push for specifics:
   - Every person needs the one thing worth remembering, and their company.
   - Every company needs its relationship to the owner (customer, investor, partner) and the open thread.
   - Every initiative needs a Next Action.
   - Every decision needs its reasoning.
   - Ask for nicknames and abbreviations they use ("we call it Realm"). Those become Aliases.
   - If an answer is vague, say so and ask them to sharpen it.
4. **Write** each record per spec section 7: Summary, Aliases, Status Active, Last Updated today, Source "Setup interview" or the meeting it came from, a body with Current and History. Interviewed people and companies start as Full; ones only found in sources start as Stubs. Update the catalog row with each write. Link relations where obvious.
5. **Glossary.** Add each Active person and initiative a user would refer to by name or nickname, up to 50.
6. **Synthesis and Freshness.** Write a one-paragraph Synthesis and fill Freshness.
7. **Log** one Ingest Log row: Source "Cortex setup", Type Document, What Changed = counts per collection. Add one row per meeting used in step 2 (Type Meeting Notes), so neither the dream nor cortex-update ingests it again.

**Company:** if the cortex-intake skill is installed, offer it instead of the interview in item 3: it runs a structured interview with each exec and a batch intake of the company's documents, and drafts every pack record into the Inbox for review. Without it, interview the person setting up for Departments (head, goals, health only if they set it), the five to ten Metrics they manage to with the latest values, open Company Commitments with owners and dates, senior Org seats and open roles, the next Board meeting, and the top three Risks. Departments' Health is theirs to set; never infer it.

## Step 8. Custom instructions

This step gives every AI conversation, on any platform, awareness of the Cortex without a lookup in every chat.

1. Fill in the template from spec section 14: the backend, the Map's direct link, and one durable line about the user (name, role, company, what it does). No priorities or names of clients or people: those change and belong in the Cortex. Keep the whole text under 1,000 characters.
2. Show it in a code block, ready to copy.
3. Tell them where it goes, in one short list:
   - **Claude:** Settings, in "Instructions for Claude"
   - **ChatGPT, Gemini, Grok, or any other assistant:** its custom instructions or personalization setting
   - Each assistant also needs a connector to wherever the Cortex lives (Notion or Google Drive, for example), or it can't read the Map. Obsidian and local folders are reachable only from assistants with access to that computer.
4. Ask them to paste it now, before moving on. It's the step that makes the Cortex work everywhere.
5. **Company:** use the company template (company-pack section 11) for each member. For every other member, write an invite checklist: join the Company teamspace (and Exec, if their role has it), get a Private space, connect their own calendar, email, and meeting notes, add their Members row, and paste their own custom instructions. Offer to add each member now or later; never add one to a space their role doesn't allow.

## Step 9. Schedule the routines

A Cortex stays useful only if it's maintained. Two scheduled tasks do that, and the dream is the core one:

| Routine | When | What it does |
| --- | --- | --- |
| **cortex-dream** | Nightly, about 2am their time | Replays the day's meetings, resolves contradictions, flags what time has made stale, compacts records, spots patterns, keeps catalogs and the Map lean, and leaves a morning note |
| **cortex-update** | Weekly, Sunday about 5pm | Email and calendar, the full health check across every record, and the review list |

1. **Say the cost in one line.** The dream runs every night and uses tokens each time. Quiet nights are cheap because it only touches what changed. On plans with lower usage limits, offer weeknights only.
2. **Check the computer.** With Obsidian or a local folder, scheduled runs reach the Cortex only while that computer is on with the Claude desktop app open. Pick a dream time when it will be, or say plainly that nights it's off are skipped.
3. **Ask once** (AskUserQuestion): both (recommended), the dream only, the update only, or neither for now. Confirm the dream time.
4. **Create the scheduled tasks** with the session's scheduling tools, following the tool's own guidance on the exact minute. Each run starts a fresh session with no memory of this chat, so each prompt stands alone:

   ```text
   Run my cortex-dream skill. Cortex Map: <link>. Time zone: <IANA zone>.
   ```

   ```text
   Run my cortex-update skill. Cortex Map: <link>. Time zone: <IANA zone>.
   ```

   If no scheduling tools are available, give the two prompts and the times, and tell them to set them up as scheduled tasks.
5. **Run the first dream now** if they're willing, so they see the morning note and the Dream Journal before the first night. It creates the Dream Journal and adds its settings to the Map.

**Company:** the dream and the update run once for the company, scheduled by the reviewer (company-pack section 10). Each member schedules their own per-member routines (Founder OS, Recap) from their own account.

Scheduled runs need `update.approval: autonomous`. With `required`, the dream still runs but only proposes; its edits wait in the Dream Journal for approval.

## Step 10. Report

Short:

- Where the Cortex and its Map live, with links
- Records created per collection
- Sources connected, and any that failed
- What's thin and worth filling next
- Which routines are scheduled, and when the first dream runs
- Next steps: strategy-digest to fill Strategy, add-to-cortex for any document, ask-cortex to query it, Founder OS for the weekly operating cycle, and Cortex Gnome for overnight work once the Cortex has a few weeks of context
