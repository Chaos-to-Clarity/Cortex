---
name: cortex-setup
description: Builds the user's Cortex, the context layer their AI reads first, in Notion, Obsidian, or Google Drive, then fills it and generates their Map and custom instructions. Run once.
---

# Cortex Setup

Build the user's Cortex: a structured store of what stays true about their work, with a Map that every AI reads first. Then fill it with real context. Run once. If a Cortex already exists, build on it and never overwrite.

Read `references/cortex-spec.md` first. It defines the layers, the Map format, the record format, the backends, and the rules.

Keep the user moving. Use AskUserQuestion for choices (up to 4 per call, recommended option first). Do discovery silently before asking.

## Step 1. Check for an existing Cortex

Look for a Cortex Map (spec section 4). If one exists and validates, say the Cortex is already set up, show where, and offer to: fill thin collections (Step 7), add a source, change a setting, or repair the Map with cortex-map. Stop there unless they pick one.

Also look for an older setup: a page named like "Brain", "Second Brain", or "My Brain" holding People, Initiatives, or Decisions databases, or a folder of notes organized the same way. If found, offer to adopt it: hand off to cortex-map in adopt mode, which registers what exists without moving or renaming anything.

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

## Step 3. Connect sources

Ask which tools they use, pre-selecting what's already connected:

- Meeting notes: Granola, Fireflies, Otter, Fathom, Notion meeting notes, a notes folder, or none
- Calendar: Google Calendar, Outlook, the device calendar, or none
- Email: Gmail, Outlook, or none
- Documents: Google Drive, Dropbox, OneDrive, Box, or none

Test each with one small read. Report each as connected or not. For failures, name the connector, suggest it from the registry, and continue. Missing sources limit what the Cortex learns; they don't block setup.

## Step 4. Build the structure

Under the parent, create (spec sections 2, 5, and 9):

1. **People**, **Companies**, **Initiatives**, **Decisions**, and **Inbox** collections, each with its fields plus Summary, Aliases, Status, Last Updated, and Source. People and Companies also get Depth (Stub, Full) and Mentions.
2. **Ingest Log** collection.
3. **Standing Context** and **Strategy** pages. Strategy starts empty with a note that strategy-digest fills it.
4. **One catalog per collection** (People, Companies, Initiatives, Decisions, Inbox), each with just its header and an Archive catalog.

Relations:

- Notion: People gets "Company" (two-way with Companies, shown there as "People"). Companies gets "Owner" (relation to People). Initiatives gets "Owner / Involved" (two-way with People, shown there as "Initiatives") and "Companies" (two-way with Companies, shown there as "Initiatives"). Decisions gets "Affects" (two-way with Initiatives, shown there as "Decisions").
- Markdown: wikilink lists in frontmatter.

## Step 5. Ask two settings

In one AskUserQuestion call:

- **Updates:** apply and report (recommended, needed for scheduled runs), or show edits first. This sets `update.approval`.
- **Time zone:** confirm the one detected from their calendar.

## Step 6. Write the Map

Create the Cortex Map page or file at the top of the parent, in the exact format in spec section 4: the self-describing header, Settings, an empty Synthesis, Collections (with catalog and location links for every collection), the default Routing rules, an empty Glossary, Freshness, and Field map: none.

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
7. **Log** one Ingest Log row: Source "Cortex setup", Type Document, What Changed = counts per collection.

## Step 8. Custom instructions

This step gives every AI conversation, on any platform, awareness of the Cortex without a lookup in every chat.

1. Fill in the template from spec section 14: the backend, the Map's direct link, and one durable line about the user (name, role, company, what it does). No priorities or names of clients or people: those change and belong in the Cortex. Keep the whole text under 1,000 characters.
2. Show it in a code block, ready to copy.
3. Tell them where it goes, in one short list:
   - **Claude:** Settings, then Profile, in the preferences field
   - **ChatGPT, Gemini, Grok, or any other assistant:** its custom instructions or personalization setting
   - Each assistant also needs a connector to wherever the Cortex lives (Notion or Google Drive, for example), or it can't read the Map. Obsidian and local folders are reachable only from assistants with access to that computer.
4. Ask them to paste it now, before moving on. It's the step that makes the Cortex work everywhere.

## Step 9. Offer the weekly routine

Offer to schedule **cortex-update** weekly (suggest Sunday at 5pm their time). It keeps the Cortex current and runs the health check. If scheduling tools are available, create a scheduled task with the prompt "Run my cortex-update skill." Otherwise give the steps. Scheduled runs need `update.approval: autonomous`.

## Step 10. Report

Short:

- Where the Cortex and its Map live, with links
- Records created per collection
- Sources connected, and any that failed
- What's thin and worth filling next
- Next steps: strategy-digest to fill Strategy, add-to-cortex for any document, ask-cortex to query it, and Founder OS for the weekly operating cycle
