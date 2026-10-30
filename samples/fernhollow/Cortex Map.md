# Cortex Map

This is the map of Fernhollow's Cortex: what's in it, where each thing lives, and where new information goes.
**Reading:** resolve names through the Glossary, pick records from the Catalog, open only those records. Cite records and their dates. If something isn't here, say it's not in the Cortex; don't assume it doesn't exist.
**Writing:** route with the Routing rules, find the existing record by name or alias and update it in place, update its catalog line, then log it in the Ingest Log. If it fits nowhere or the match is unclear, put it in the Inbox. Never delete; close records with a status.

## Settings
```text
map_version: 2
owner: Maya
time_zone: America/Los_Angeles
backend: local-folder
root: samples/fernhollow
pack.company: 1
company.name: Fernhollow
company.reviewer: Theo Lindqvist
page.standing_context: Company/Standing Context.md
page.strategy: Exec/Strategy.md
page.schema: none
page.dream_journal: Company/Dream Journal.md
sources.meeting_notes: granola
sources.calendar: google-calendar
sources.calendar_id: primary
sources.email: gmail
sources.documents: google-drive
sources.strategy_folder: none
update.lookback_days: 7
update.approval: autonomous
health.stale_after_days: 60
health.stub_expire_days: 90
health.orphan_after_days: 90
dream.sources: meeting-notes
dream.max_records: 40
dream.started: 2026-10-28T02:00:00-07:00
dream.last_run: 2026-10-28T02:14:00-07:00
dream.cursor: Departments: Sales
```

## Members
| Member | Role | Sources | Private space | Approval | Briefs |
| --- | --- | --- | --- | --- | --- |
| Maya Okafor | CEO | calendar, email, granola | Private/Maya Okafor | autonomous | daily |
| Theo Lindqvist | Chief of Staff | calendar, email, granola | Private/Theo Lindqvist | autonomous | daily |
| Priya Raman | Exec: Engineering | calendar, granola | Private/Priya Raman | required | weekly |
| Jordan Ellis | Exec: Product | calendar, granola | Private/Jordan Ellis | required | weekly |
| Marcus Bell | Exec: Sales | calendar, granola | Private/Marcus Bell | required | weekly |
| Hana Sato | Exec: Customer Success | calendar, granola | Private/Hana Sato | required | weekly |
| Daniel Reyes | Exec: Finance and Ops | calendar, email | Private/Daniel Reyes | required | weekly |

## Synthesis
Fernhollow is at $7.75M ARR (Sept 30) against $10M by June 2027, with a Series C planned to close by April 2027. Retention is the story: NRR fell from 112% to 106% in two months and logo churn rose to 1.9%. Sales is Red with no VP Sales since July and coverage at 2.2x. The board's August asks (churn cohorts, VP Sales finalists) are both still open for the Nov 18 meeting. Pricing v2 keeps slipping on a sales decision. Runway is 17 months.

## Collections
| Collection | Holds | Identity | Key fields | Statuses | Catalog | Location |
| --- | --- | --- | --- | --- | --- | --- |
| People | Team, board, key contacts | Name | Role, Company, Context, Open Thread, Depth | Active, Dormant, Archived | Company/People/_catalog.md | Company/People |
| Companies | Customers, investors, competitors | Name | Relationship, What They Do, Open Thread, Depth | Active, Dormant, Archived | Company/Companies/_catalog.md | Company/Companies |
| Departments | Each function and its head | Name | Head, Health | Active, Archived | Company/Departments/_catalog.md | Company/Departments |
| Initiatives | What the company is driving | Name | Next Action, Blocker, Target, Visibility | Active, Paused, Done, Dropped | Company/Initiatives/_catalog.md; Exec/Initiatives/_catalog.md | Company/Initiatives; Exec/Initiatives |
| Company Commitments | Promises with an owner and a date | Title | Owner, Due, Visibility | Open, Kept, Slipped, Dropped | Company/Company Commitments/_catalog.md; Exec/Company Commitments/_catalog.md | Company/Company Commitments; Exec/Company Commitments |
| Org | Senior seats and open roles | Role | Holder, Reports To | Filled, Open, Closed | Company/Org/_catalog.md | Company/Org |
| Decisions | Calls made, questions open | Title | Date, Reasoning, Visibility | Decided, Open, Reversed, Superseded | Exec/Decisions/_catalog.md | Exec/Decisions |
| Metrics | The numbers the company manages to | Name | Owner, Cadence, Latest, Target | Active, Retired | Exec/Metrics/_catalog.md | Exec/Metrics |
| Metric Values | Dated readings | Reading | Metric, Date, Value | none | log | Exec/Metric Values.md |
| Board | Board meetings, asks, follow-ups | Meeting | Date, Prep Status | Upcoming, Held, Cancelled | Exec/Board/_catalog.md | Exec/Board |
| Risks | Threats with a trigger | Title | Owner, Impact, Trigger | Watching, Active, Closed | Exec/Risks/_catalog.md | Exec/Risks |
| Inbox | Unclear fit or match | Title | Suggested Collection, Candidates | New, Filed, Discarded | Company/Inbox/_catalog.md | Company/Inbox |
| Ingest Log | Sources processed | Source | Type, Date Ingested | none | log | Company/Ingest Log.md |

## Routing
**Find it**
- Who someone is, meeting prep → People, then their Department, Company Commitments, and Initiatives
- How a team is doing → Departments, then its Head, Metrics, and open Company Commitments
- A number, a trend, a target → Metrics, then Metric Values
- What someone promised, what's overdue → Company Commitments
- Reporting lines, open roles → Org
- Board prep, board asks → Board, then its Follow-ups
- What could go wrong → Risks
- What's being driven → Initiatives; what was decided → Decisions
- Positioning, targets, the plan → Strategy; durable facts → Standing Context

**File it**
- A person → People (a Stub on first mention); a company → Companies
- A team's goals, head, headcount → Departments
- A new reading → Metric Values, then the Metric's Latest and Prior
- A promise with an owner and a date → Company Commitments; without both → Inbox
- A promise to self → Founder OS Commitments in the member's Private space
- A seat, hire, departure, reporting change → Org
- A board meeting or its asks → Board; a threat → Risks
- Something being driven → Initiatives; a call made → Decisions
- Anything from a 1:1 → the manager's Team record in their Private space
- Unclear fit or match → Inbox

## Glossary
| Term | Means | Points to |
| --- | --- | --- |
| Maya | CEO | People: Maya Okafor |
| Theo | Chief of Staff, reviewer | People: Theo Lindqvist |
| Priya | CTO | People: Priya Raman |
| Jordan | VP Product | People: Jordan Ellis |
| Marcus, Marc | Interim Head of Sales | People: Marcus Bell |
| Hana | VP CS | People: Hana Sato |
| Daniel | VP Finance | People: Daniel Reyes |
| Rachel | Northgate board director | People: Rachel Stein |
| Brightside | Largest customer | Companies: Brightside Home Services |
| Northgate | Series B lead | Companies: Northgate Ventures |
| Eng | Engineering | Departments: Engineering |
| CS | Customer Success | Departments: Customer Success |
| NRR | Net revenue retention | Metrics: Net revenue retention |
| the C, Series C | The raise | Initiatives: Series C Readiness |
| pricing v2 | Pricing and Packaging v2 | Initiatives: Pricing and Packaging v2 |
| v2, the migration | Platform v2 Migration | Initiatives: Platform v2 Migration |

## Freshness
| Source | Last processed |
| --- | --- |
| Meeting notes | 2026-10-28 |
| Documents | 2026-10-12 |
| Metrics | 2026-10-10 (Sept close) |

Records: People 9, Companies 3, Departments 5, Initiatives 3, Company Commitments 6 (5 open), Org 4, Decisions 2, Metrics 5, Board 2, Risks 3. Metric Values 15 rows. Inbox: 1 waiting. Map rebuilt 2026-10-28.

## Field map
none
