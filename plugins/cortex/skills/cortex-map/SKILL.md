---
name: cortex-map
description: Builds or repairs the Cortex Map and catalogs from what's in the store, imports CRM or LinkedIn exports, and regenerates custom instructions. Use to adopt, upgrade, or fix.
---

# Cortex Map

Generate the Map and catalogs from the user's real store, so retrieval never depends on guessing. The Map is built by reading what exists, not written from memory.

Read `references/cortex-spec.md` first, especially sections 4, 5, and 10.

## Modes

Pick from the request:

| Mode | When | What it does |
| --- | --- | --- |
| **Rebuild** (default) | "Rebuild my Cortex map", or the Map is out of date | Re-reads the store, rewrites the Map's structure and every catalog |
| **Adopt** | An existing setup that was never a Cortex (an older "Brain", a Notion workspace, a notes folder) | Registers what exists without moving or renaming anything, adds the missing pieces |
| **Catalogs** | "Fix my catalogs", or called by the health check | Rebuilds catalogs only |
| **Repair** | The Map points somewhere that no longer exists | Finds where things went, fixes pointers, asks when unsure |
| **Import** | "Import my CRM contacts", "seed from my LinkedIn export", a CSV or JSON file attached | Turns exported records into People, Companies, or another collection (spec section 11) |
| **Upgrade** | The Map says `map_version: 1` | Adds Companies, Depth, and Mentions, and rebuilds (spec section 12) |

## Step 1. Find the root

- If a Cortex Map exists, use its `backend` and `root`.
- Otherwise, ask which tool and which page or folder holds the setup. Confirm access with one read.

## Step 2. Inventory the store

List everything under the root: every database or collection folder, and every page. For each collection, record:

- Its location
- Its identity (title) field and every field, with types and status values
- Row counts by status
- Relations to other collections

Read schemas and counts only. Don't open every record.

## Step 3. Classify each collection

- **Core:** People, Companies, Initiatives, Decisions, Inbox, Ingest Log, or a clear equivalent under another name ("Contacts" for People, "Accounts" or "Organizations" for Companies, "Projects" for Initiatives). Record the real names in the Field map.
- **Extension:** something that belongs (Founder OS collections, Customers, Pipeline, Coaching Sessions). Write a one-line "Holds" and routing rules for it.
- **Unclear:** in an interactive run, ask the user what it holds and whether it belongs in the Cortex. In a scheduled run, list it under "Needs a decision" in the report and leave it out of the Map.

Never register something that is clearly not context (a scratch page, a template gallery).

## Step 4. Add what's missing (adopt and rebuild)

Ask once before changing any schema, listing exactly what you'll add:

- Missing **Summary**, **Aliases**, **Status**, **Last Updated**, or **Source** fields on registered collections, and **Depth** and **Mentions** on People and Companies (existing records start as Full)
- A missing **Companies** collection, with an offer to create Company records from the companies named in People roles
- A missing **Inbox** or **Ingest Log** collection
- Missing **Standing Context** or **Strategy** pages

Never rename, move, or delete the user's existing fields, pages, or records.

**Backfill Summaries.** For records without one, write a Summary from the record's fields and body. Over 100 records to backfill: say how many, and do Active records first. Leave closed records until a later run if it's large.

## Step 5. Build the catalogs

For each registered collection, write its catalog and archive catalog (spec section 5): one row per record with identity, aliases, status, depth (People and Companies), summary, updated, and link, ordered most-linked first (spec section 2, Link weight). Shard any collection over 300 active rows by a field that divides it well, and list the shards in the Map.

## Step 6. Build the glossary

Collect candidate terms:

- Names of Active, Full people, companies, and initiatives the user refers to by name, most-linked first. Never Stubs
- Every Alias on Active records
- Acronyms and nicknames that recur across records

Keep the 50 most useful: things a user would type in a question. In an interactive run, show the list and ask for nicknames you missed. Each term points to exactly one record. If a term points to two records, it's a likely duplicate: list it in the report instead of choosing.

## Step 7. Write the Map

Write the Map in the exact format in spec section 4:

- Keep existing Settings values. Fill gaps by asking (interactive) or leave `none` (scheduled).
- Collections table: every registered collection with its catalog and location links, including extensions.
- Routing: the core rules plus one find and one file rule per extension.
- Glossary from Step 6. Freshness from the Ingest Log's latest date per source type, plus record counts.
- Keep the existing Synthesis if there is one.
- Check the size. Over 10,000 characters: trim the glossary to the most-referenced terms and tighten Synthesis.

## Import mode

1. **Read the file.** CSV, JSON, or a spreadsheet the user attached or named. Show the columns and the first three rows.
2. **Map the fields.** Propose which columns become which fields (Name, Company, Role, Email, Relationship, and so on). Confirm with the user before writing. Ignore columns with no home; never import sensitive fields like personal phone numbers or home addresses unless the user asks.
3. **Choose what to import.** For LinkedIn connections or any list over 200 rows, ask which ones to bring in (by company, title, or tag). Importing a whole network fills the Cortex with noise.
4. **Resolve identity.** Match each row against the People and Companies catalogs by name, email, and aliases. Matches update the existing record and add a Mention; unclear matches go to the Inbox.
5. **Write.** New records start as Stubs, unless the export marks an active relationship (a customer account, a current investor), which makes them Full. Link each person to their company, creating the company as a Stub if needed. Source is the file name.
6. **Finish.** Rebuild the affected catalogs, add one Ingest Log row (Source = file name, Type Document, What Changed = counts), and report: created, updated, sent to the Inbox, skipped.

## Step 8. Log and report

One Ingest Log row: Source "Cortex map [mode], [date]", Type Health Check, What Changed = collections registered, catalogs rebuilt, fields added, summaries backfilled.

Report:

- Collections registered (core and extensions), with row counts
- Fields and pages added
- Catalogs built, and any shards
- Likely duplicates and unclear collections that need a decision
- On adopt or first build, or whenever the user asks for their custom instructions: the filled-in text from spec section 14 (Map link and Snapshot included, no brackets), ready to paste, and where to paste it
