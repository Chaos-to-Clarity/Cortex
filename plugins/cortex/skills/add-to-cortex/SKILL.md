---
name: add-to-cortex
description: Digests one document (pasted, attached, or a named file or link) into the user's Cortex, routing people, initiatives, decisions, and context to the right place without duplicates.
---

# Add to Cortex

Digest one document into the user's Cortex. For a folder of strategy documents, use strategy-digest. For a sweep of recent meetings and email, use cortex-update.

Read `references/cortex-spec.md` first. Every write follows the Writing protocol in section 7.

If the Map has `pack.company: 1`, also read `references/company-pack.md`. Act for one member (its section 5): route with the pack's rules, and write anything from a 1:1 or anything private to that member's Private space, never a shared collection.

## Step 1. Load the Map

Find and validate the Cortex Map (spec section 4). If there isn't one, offer cortex-setup and stop. The Map tells you what collections exist, where they live, how to route, and what names mean.

## Step 2. Get the document

| Source | Action |
| --- | --- |
| Pasted text | Use it directly |
| Attached file (PDF, DOCX, image, slides) | Read it with file tools |
| A file name or link in their document source | Find it; if several match, ask which |
| A page in their store or another app | Open it with that connector |

## Step 3. Check the Ingest Log

Already logged: say when it was ingested and stop, unless they say re-ingest.

## Step 4. Extract what's durable

Keep only what stays true for weeks or months. For each item, note which collection the Map's Routing rules send it to, including any extension collection the Map lists.

Write in the user's words. Condense.

## Step 5. Resolve and write

For each item, follow spec section 7, steps 5 to 8:

- Resolve the identity through the Glossary, then catalog Names and Aliases.
- One clear match: update it (fields, Summary, a dated History line, Last Updated, Source).
- No match: create it, with Summary and Aliases. A person or company seen only in this document starts as a Stub; one the document shows a real working relationship with starts as Full. Link each person to their company.
- Existing person or company: add a Mention, and promote a Stub to Full when it qualifies.
- Unclear match, or no clear home: put it in the Inbox with the candidates and the suggested collection. Don't guess.
- Changed or reversed: close the old state with a status; for Decisions, create the new record and set Supersedes.
- **Strategy:** add a dated section for this document; refresh the Strategy summary only if positioning, ICP, GTM, targets, or brand changed.
- **Standing Context:** surgical edits only.
- Update each catalog row in the same step as its record. Add Glossary rows for new key names if there's room.
- Link relations where the document makes them obvious.

A clearly new category (Pipeline, Portfolio, Hiring): put the items in the Inbox and propose the collection in one line. Create it only after a yes, then register it in the Map with cortex-map.

## Step 6. Log

One Ingest Log row: Source = document name, Type = Document, Meeting Notes, Email, or Strategy, Date Ingested today, What Changed = "X created, Y updated, Z superseded, N to Inbox", with names.

## Step 7. Report

One short paragraph or a small table:

- Added (what and where)
- Updated in place
- Superseded, and why
- Sent to the Inbox, and why
- Anything thin or ambiguous, with one question to sharpen it
