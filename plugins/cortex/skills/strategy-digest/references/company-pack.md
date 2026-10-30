# Cortex Company Pack

An optional pack that turns a founder's Cortex into a company's Cortex: a living model of the business that the whole exec team reads and writes. Read `cortex-spec.md` first. Everything there still holds; this pack only adds to it.

The master copy lives in `spec/company-pack.md` in the Cortex repository and is copied into each Cortex skill's `references/` folder by `python scripts/sync_spec.py`.

## 1. When to install it

Install the pack when more than one person will use the Cortex and the Cortex should hold the company, not one person's world: departments, the numbers, what each exec has promised, the org chart, the board, and the risks.

A founder using Cortex alone doesn't need it. A founder Cortex can take the pack later (section 11).

The pack is marked on the Map:

```text
pack.company: 1
company.name: <company name>
company.reviewer: <member name: the Chief of Staff, or the CEO if there is none>
```

Skills that see `pack.company` follow this file. Skills that don't see it behave exactly as `cortex-spec.md` says.

## 2. What the pack adds

| Adds | What it is |
| --- | --- |
| Six collections | Departments, Metrics, Company Commitments, Org, Board, Risks |
| One log | Metric Values: dated readings for each Metric |
| A Visibility field | On Company Commitments, Decisions, Initiatives, and Risks |
| A Members table on the Map | Who uses this Cortex, their role, their sources, their private space, their approval mode |
| Spaces | Company, Exec, and one Private space per member, which set who can open what |
| Rules | Who approves the dream's questions, how briefs are scoped to a member, and what never enters a shared space |

Company Commitments is named so it never collides with the Founder OS Commitments collection, which holds promises to self.

## 3. The collections

Every record carries Summary, Aliases, Status, Last Updated, and Source, and a body with Current and History (spec section 2). Relations follow the spec: Notion relations, or wikilink lists in Markdown frontmatter.

### 3.1 Departments

A function of the company and the person who leads it.

| Field | What it holds |
| --- | --- |
| Name (identity) | Engineering, Sales, Customer Success |
| Head | Relation to People |
| Mission | One line: what this team exists to do |
| Headcount | Number, as of Last Updated |
| Top Goals | Up to three, each one line |
| Metrics | Relation to Metrics |
| Dependencies | Relation to other Departments this one waits on |
| Health | Green, Yellow, Red. **Set only by the head or the CEO.** No skill sets or changes it |
| Health Note | One line from whoever set Health |
| Space | Company or Exec |

Statuses: Active, Archived.

Catalog line: `Engineering | Active | Head: Priya Shah | Yellow | 14 people; v2 migration behind; one senior role open`. Key columns: Head, Health.

### 3.2 Metrics

A number the company manages to.

| Field | What it holds |
| --- | --- |
| Name (identity) | ARR, Net revenue retention, Burn, Pipeline coverage |
| Owner | Relation to People |
| Department | Relation to Departments |
| Unit | $, %, count, months, days |
| Cadence | Weekly, Monthly, Quarterly |
| Direction | Up is good, Down is good, Hold steady |
| Target | Value and date, for example "$3.0M by 2027-06-30" |
| Latest | The most recent value and its date, copied from Metric Values |
| Prior | The value one cadence earlier, and its date |
| Source System | Where the number comes from: a spreadsheet, the finance tool, the CRM |
| Visibility | Company or Exec |

Statuses: Active, Retired.

Catalog line: `ARR | Active | Monthly | $2.31M (2026-10-31), +5.5% MoM | target $3.0M by Jun 2027`. Key columns: Owner, Cadence.

Every new reading is a Metric Values row first. Latest and Prior on the Metric record are then refreshed, and the catalog line with them. A Metric record's History holds target changes and owner changes, never every reading.

### 3.3 Metric Values (log)

One row per reading. A log: no catalog, no Summary, no Current or History (spec section 2, Logs).

| Field | What it holds |
| --- | --- |
| Reading (identity) | `<Metric> <date>`, for example "ARR 2026-10-31" |
| Metric | Relation to Metrics |
| Date | The date the value is true for, not the date it was entered |
| Value | The number |
| Source | Board pack, finance export, CRM report, interview |

Two readings for the same Metric and date from different sources: keep both, and the dream asks the reviewer which is right. Never average them.

### 3.4 Company Commitments

A promise someone in the company made to someone else, with an owner and a date.

| Field | What it holds |
| --- | --- |
| Title (identity) | Verb first: "Ship the pricing page", "Send the board the churn analysis" |
| Owner | Relation to People: the person who promised |
| Made To | Relation to People, or "Board", "Customers", "Exec team" |
| Department | Relation to Departments |
| Made On | Date |
| Due | Date |
| Made In | Where it was promised: a meeting, a decision, a board meeting (text, or relation to Board or Decisions) |
| Times Slipped | Count of times Due moved later |
| Visibility | Company, Exec, or Private |

Statuses: Open, Kept, Slipped, Dropped.

- **Kept:** done, on or before Due.
- **Slipped:** Due passed and the owner or the reviewer confirmed it moved. Set the new Due, add one to Times Slipped, add a History line with the old date, and set the status back to Open.
- **Dropped:** the owner or the reviewer confirmed it won't happen.

Only a person sets Kept, Slipped, or Dropped. A skill that sees a Due date pass flags it; it never changes the status on inference.

Catalog line: `Ship the pricing page | Open | Owner: Sam Ortiz | Due 2026-11-15 | slipped once; blocks the Q4 launch`. Key columns: Owner, Due.

### 3.5 Org

A seat in the org chart, filled or open.

| Field | What it holds |
| --- | --- |
| Role (identity) | VP Sales, Head of Engineering, Account Executive (East) |
| Holder | Relation to People, or empty when open |
| Reports To | Relation to another Org record |
| Department | Relation to Departments |
| Open Since | Date, for an open seat |
| Scorecard | Link or relation to the A-Team Roles record, when A-Team is installed |

Statuses: Filled, Open, Closed (the seat no longer exists).

Catalog line: `VP Sales | Open | Reports to: CEO | open since 2026-09-01 | scorecard drafted; two finalists`. Key columns: Holder, Reports To.

Org holds senior seats and open roles, not every employee. Headcount lives on Departments.

### 3.6 Board

One record per board meeting.

| Field | What it holds |
| --- | --- |
| Meeting (identity) | "Board 2026-11-18" |
| Date | Date |
| Members | Relation to People (directors and observers) |
| Asks of the Company | What the board asked for, one per line |
| Asks of the Board | What the company asked the board for, one per line |
| Follow-ups | Relation to Company Commitments made at or for this meeting |
| Pack | Link to the board pack |
| Prep Status | Not started, Drafting, Ready, Sent |
| Visibility | Exec |

Statuses: Upcoming, Held, Cancelled.

Catalog line: `Board 2026-11-18 | Upcoming | Prep: Drafting | 3 open asks of the company; pack due 2026-11-11`. Key columns: Date, Prep Status.

Board records are Exec by default. The CEO may set a single field or section to Private (for example, a director's personal remark) by moving it into their Private space and linking it.

### 3.7 Risks

Something that could hurt the company, with a trigger and a plan.

| Field | What it holds |
| --- | --- |
| Title (identity) | "Runway under 12 months if the raise slips" |
| Owner | Relation to People |
| Likelihood | Low, Medium, High |
| Impact | Low, Medium, High |
| Trigger | What would turn it from watching to active, as specific as possible |
| Mitigation | What's being done, one or two lines |
| Related | Relation to Initiatives, Metrics, or Departments |
| Visibility | Exec or Company |

Statuses: Watching, Active, Closed.

Catalog line: `Runway under 12 months | Watching | Owner: CEO | High impact | trigger: no term sheet by 2027-03-01`. Key columns: Owner, Impact.

## 4. Visibility

A Visibility field sits on Company Commitments, Decisions, Initiatives, and Risks. Metrics and Departments carry it too (as above). The three values:

| Value | Who can read it |
| --- | --- |
| Company | Every member |
| Exec | The CEO, the Chief of Staff, the execs, and the Advisor seat (section 5) |
| Private | Only the member whose Private space holds it |

**Defaults when a writer isn't told:** Company Commitments, Initiatives, Departments: Company. Decisions, Risks, Metrics, Board: Exec. Anything from a 1:1, a performance conversation, or a personal remark about someone: Private, in the speaker's Private space, never in a shared collection.

**Visibility follows the space.** A record's Visibility must match where it lives (section 6). A Private record never sits in a Company or Exec collection. A writer that would put a Private item in a shared collection writes it to the member's Private space instead.

**Moving up is a person's call.** A skill never raises a record's Visibility (Private to Exec, Exec to Company). It may suggest it in the Dream Journal.

## 5. Members

The Map gains a Members section after Settings:

````markdown
## Members
| Member | Role | Sources | Private space | Approval | Briefs |
| --- | --- | --- | --- | --- | --- |
| Dana Kim | CEO | calendar: google-calendar, email: gmail, meeting_notes: granola | <link> | autonomous | daily |
| Luis Moreno | Chief of Staff | calendar: google-calendar, meeting_notes: granola | <link> | autonomous | daily |
| Priya Shah | Exec: Engineering | calendar: google-calendar, meeting_notes: granola | <link> | required | weekly |
| Eric Weiss | Advisor | none | none | required | monthly |
````

| Column | Meaning |
| --- | --- |
| Member | The person's name, matching their People record |
| Role | CEO, Chief of Staff, Exec: <Department>, or Advisor |
| Sources | Their own calendar, email, and meeting-notes sources, in the spec's source names. Scheduled skills run per member with these |
| Private space | Link to their Private space, or none |
| Approval | autonomous or required, for writes made on their behalf |
| Briefs | daily, weekly, monthly, or off: how often the company brief runs for them |

**What each role can read and write**

| Role | Reads | Writes |
| --- | --- | --- |
| CEO | Company, Exec, their own Private | Anything in Company and Exec, their own Private |
| Chief of Staff | Company, Exec, their own Private | Company pack collections, Board, Company Commitments, their own Private |
| Exec | Company, Exec, their own Private (and their Team records, which live there) | Their Department, their Metrics, their own Company Commitments, their own Private |
| Advisor | Company and Exec, never any Private space | Standing Context, Strategy, the Dream Journal, the Ingest Log, and monthly refresh writes |

The Members table records intent. The spaces (section 6) are what enforce it.

**Acting for a member.** Every skill run on a company Cortex knows which member it is acting for: the member whose session or scheduled task is running. It reads only what that member can read and writes only what they can write. A run that can't tell whose it is asks once, then uses the answer for the rest of the run.

**One-on-Ones and Team records.** These belong to the manager who keeps them. They live in that manager's Private space, never in a Company or Exec collection, and never in anyone's brief but the manager's. The One-on-Ones privacy rules apply unchanged. Only a Company Commitment the manager chooses to create, with Visibility Exec or Company, leaves a 1:1.

**No verdicts on people.** No skill writes a performance judgment, rating, or ranking of a person into any space. Health on a Department is set by people. Health on a Team record is set by the manager. Skills prepare conversations; people make people decisions.

## 6. Spaces

### Notion

| Teamspace | Members | Holds |
| --- | --- | --- |
| `<Company> Cortex` | Everyone | The Map, Standing Context, Dream Journal, Ingest Log, Inbox, catalogs, People, Companies, Departments, Initiatives, Company Commitments, Org, and Visibility-Company records |
| `<Company> Exec` | CEO, Chief of Staff, execs, Advisor | Board, Risks, Metrics, Metric Values, Decisions, Strategy, and Visibility-Exec records |
| `<Member> Private` | That member only | Their Team records (One-on-Ones), Founder OS reflections and commitments, private notes, Private records |

Set each teamspace to closed or private so membership is the access list. The Map lives in the Company teamspace and links into the Exec teamspace; members without Exec access see a link they can't open, which is the intended behavior.

Collections that hold both Company and Exec records (Initiatives, Decisions, Company Commitments): keep one database in the Company teamspace for Company records and one in the Exec teamspace for Exec records, both listed on the Map under the same collection name with a Location for each. Catalogs follow the same split: the Exec catalog lives in the Exec teamspace.

### Markdown backends

Markdown folders can't enforce access by themselves. Use three top-level folders and share each one only with the people who should see it, using the storage tool's own sharing (Google Drive folder sharing, a synced folder per person):

```
<Company> Cortex/
  Cortex Map.md
  Company/        everything in the Company teamspace above
  Exec/           everything in the Exec teamspace above
  Private/
    <Member>/     that member's private space
```

If the storage can't restrict a folder, say so plainly at setup and recommend Notion or Google Drive for a company Cortex.

## 7. Map additions

**Collections table.** One row per pack collection, with its catalog and location links. Metric Values is marked `log` in the Catalog column. Split collections list both locations.

**Routing.** Add these lines.

Find it:

- How a team is doing, a department's goals or people → Departments, then its Head on People, its Metrics, and its open Company Commitments
- A number, a trend, a target → Metrics, then Metric Values for history
- What someone promised, what's overdue, what's due this week → Company Commitments
- Who reports to whom, open roles, hiring → Org, then A-Team Roles if installed
- Board prep, what the board asked for, board follow-ups → Board, then its Follow-ups
- What could go wrong, what's on watch → Risks

File it:

- A change to a team's goals, head, headcount, or dependencies → Departments
- A new reading of a number → Metric Values, then refresh the Metric's Latest and Prior
- A new or changed target, owner, or definition of a number → Metrics
- A promise with an owner and a date, made to someone else → Company Commitments
- A promise to self → Founder OS Commitments, in the member's Private space
- A new seat, an opening, a hire, a departure, a reporting change → Org
- A board meeting, its asks, its pack → Board
- A threat with a trigger → Risks
- Anything from a 1:1 → the manager's Team record, in their Private space

**Glossary.** Departments and their nicknames ("Eng", "CS"), Metrics people refer to by shorthand ("NRR", "the burn"), and board members by first name.

## 8. Skills on a company Cortex

| Skill | Reads | Writes | What changes with the pack |
| --- | --- | --- | --- |
| cortex-setup | | Everything at setup | Asks "Is this for you, or for your company?" and installs the pack on the company branch |
| cortex-map | The Map | Map structure | Registers pack collections and Members; repairs split collections |
| ask-cortex | Everything the member can read | Query Insights | Scopes every answer to the asking member's Visibility |
| add-to-cortex | The Map | Any collection the member can write | Routes with the pack's rules; Private items go to the member's Private space |
| cortex-dream | Every member's meeting notes, the Ingest Log | Records, the Dream Journal | Questions go to `company.reviewer`; flags passed Due dates and stale Metrics |
| cortex-update | Every member's email, calendar, notes | Records, health check | Runs the pack's health checks (section 9) |
| strategy-digest | Strategy documents | Strategy, Exec space | Strategy lives in the Exec space |
| Founder OS | The member's own records plus Company | The member's Private space | Runs per member; reads Company Commitments for the member's own promises |
| Recap | The member's meetings | Company Commitments, Departments, the member's own records | Promises with an owner and a date become Company Commitments |
| One-on-Ones | The manager's Team records | The manager's Private space | Team lives in the Private space; nothing else changes |
| Investor Update | Metrics, Metric Values, Board, Initiatives | A draft in the Exec space | Reads Metrics instead of a spreadsheet |
| Customer Signal | Customer calls | Companies, its own collection | Nothing changes |
| Company brief, prep the room, monthly brief | The pack collections | Their outputs | Built for the pack; see each skill |

## 9. Health checks the pack adds

Run with the spec's health check (section 10). Fix what's safe to fix; report the rest to `company.reviewer`.

| Check | Action |
| --- | --- |
| Company Commitments Open past Due | List by owner for the reviewer to mark Kept, Slipped, or Dropped. Never change the status |
| Company Commitments with Times Slipped of 2 or more | List them; a pattern worth a conversation, never a verdict |
| Metrics with no reading within one cadence of their last | List them with the owner |
| Metric Latest that doesn't match the newest Metric Values row | Fix Latest and Prior from the log |
| Departments with no Head, or Health not set in 60 days | Report to the reviewer |
| Org seats Open for more than 90 days | Report |
| Board meetings within 14 days with Prep Status Not started | Report to the CEO and the reviewer |
| Records whose Visibility doesn't match their space | Report; never move a record to a wider space on its own |
| Records with no Visibility | Set the default (section 4) and report |
| Any Private-space content found in a shared space | Report to the member who owns it, only to them |

## 10. The dream on a company Cortex

The dream runs once for the company, not once per member. Its working set adds:

- Meeting notes from every member in the Members table with a meeting-notes source, read with that member's access. A note from a 1:1 is processed only into that manager's Private space, under the One-on-Ones rules.
- Company Commitments whose Due date passed since the last dream: flagged, never closed.
- Metrics whose cadence came due with no new reading: flagged.

Questions for you route to `company.reviewer`. Questions about a Private record go only to the member who owns it, in their Private space, never in the shared Dream Journal. The shared Dream Journal lives in the Company teamspace and never names Private content.

## 11. Custom instructions for each member

Each member gets their own copy of the spec section 14 template, with "About me" written for the company:

```text
## Our Cortex
[Company]'s context lives in our Cortex in [Notion]. Map: [link to the Cortex Map]

About me in this company: [Name], [role] at [company], which [what the business does, in a few words].

When to look: only when my request is about the company, its people, teams, numbers, decisions, commitments, the board, or my own work AND the answer would be clearly better or safer with that context. Skip it for general questions, generic writing, or code, or when this chat already has what you need. If unsure, ask me in one line instead of looking.

How: read the Map once per chat and reuse it. Use its Glossary and Catalogs to open only the few records you need; never search the whole workspace. I can only see what my spaces allow, and that's fine. Cite what you used and its date. If it isn't there, say so. If you can't reach it, tell me once and carry on.
```

Under 1,000 characters. No priorities, no names of clients or colleagues.

## 12. Turning a founder Cortex into a company Cortex

When a founder who built their own Cortex (for example in the AI OS bootcamp) wants it for the whole company:

1. **Back up.** Duplicate the Cortex parent (Notion) or copy the folder (Markdown) and note where the copy is.
2. **Make the spaces.** Create the Company, Exec, and the founder's Private teamspace or folders (section 6).
3. **Move the private things first.** Founder OS Weekly Goals, Tasks, Reflections, and Commitments, One-on-Ones Team records, Life Coaching pages, and any personal notes move to the founder's Private space. Do this before anyone else is invited.
4. **Move the exec things.** Strategy, Decisions the founder marks Exec, and anything about the board or fundraising move to the Exec space.
5. **Check People for private remarks.** Read each Full People record's Context and Current. A remark about someone's performance, health, or personal life moves to the founder's Private space; the shared record keeps the working facts.
6. **Add the pack.** Create the six collections and the log, their catalogs, and the Visibility field on the four collections that take it. Set existing Initiatives to Company and existing Decisions to Exec unless the founder says otherwise.
7. **Update the Map.** Add `pack.company`, `company.name`, `company.reviewer`, the Members table (the founder first), the pack's Collections rows and Routing lines, and the split locations.
8. **Invite members one at a time.** Each new member gets their Private space, a Members row, their sources connected, and their custom instructions.
9. **Log it.** One Ingest Log row, Type Document, Source "Company pack migration", listing what moved where.

Never invite a second person before steps 3 through 5 are done.

## 13. Rules the pack adds

- **Act for one member.** Every run knows whose it is and reads and writes only within their access.
- **Private stays private.** Nothing from a Private space appears in a shared space, a shared brief, or a shared journal.
- **People decide about people.** No ratings, rankings, or verdicts on a person anywhere. Health is set by people.
- **Promises need an owner and a date.** A promise without both goes to the Inbox, not to Company Commitments.
- **Readings before records.** A new number is a Metric Values row first.
- **Flag, don't close.** Passed dates are flagged to the owner or reviewer. Only people close commitments.
