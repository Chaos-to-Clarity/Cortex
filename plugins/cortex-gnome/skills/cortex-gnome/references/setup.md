# Setup

Set up a gnome for one owner, then schedule it. About 20 minutes. Use the host's multiple-choice question tool for choices (up to 4 per call, recommended first). Do discovery silently before asking: what's connected, whether a Cortex exists, whether a Gnome home exists.

## Step 0. Set expectations

Before anything else, say this plainly, in your own words, and get a yes:

> The gnome runs on its own every night and uses tokens every time, whether or not it makes anything useful. Out of the box it doesn't know what's valuable to you, so early runs may produce work you don't want. It gets good only as fast as you teach it: read each brief, say keep, tweak, or kill, and say why. You also decide how much it may do on its own. Start it reined in, and give it more room only after it proves useful.

Then the plan fit: the gnome is best suited to plans with high usage limits, such as Claude Max. A nightly run can use a large share of a smaller plan's limit and leave less for their own work during the day. On other plans, recommend the Starter rung, weekdays only, and a lighter budget.

If they'd rather not commit to reviewing for the first two weeks, recommend waiting: an unreviewed gnome doesn't improve.

## Step 1. Find what exists

1. **Gnome home** (`gnome-spec.md`, Finding it).
   - Found: this is a team that already has gnomes. Read the Registry and the Manifesto. Say who already runs one and in which lanes. This setup adds a new gnome; it doesn't touch the home, the Manifesto, or other gnomes. Skip Step 4's creation and go to Step 2.
   - This owner already has an Active gnome: offer status mode instead (change settings, add a source) and stop unless they want a second gnome.
2. **Cortex Map** (Cortex spec section 4). Found: the gnome will read it and its home goes under the Cortex. Not found: that's fine. The gnome runs on whatever sources are connected. Mention once that a Cortex makes it sharper, and that cortex-setup can build one later.

## Step 2. Connect where the context lives

Ask which they use, pre-selecting what's already connected. Test each with one small read and report connected or not. For anything missing, search the connector registry and suggest it, then continue.

- **Task or project tool:** ClickUp, Asana, Linear, Jira, Monday, Notion, Todoist, Trello, GitHub Issues, or none. Then which workspaces, projects, or boards it should read.
- **Where ideas get captured:** a Notion page or database, a Drive folder, a notes app, a Slack channel, a voice-memo folder, or none. Ideas are the gnome's best source of proposals, so push for at least one.
- **Meetings, email, calendar, chat:** pre-select what's connected. Explain in one line that the gnome reads them for commitments and prep, and never sends anything without permission.
- **Code:** which repos it may read, and which it may branch and open pull requests in.

## Step 3. Choose where work lands

- **Workspace:** where finished outputs are stored for review. Default: a "Gnome Workspace" page or folder in the Gnome home. With a Cortex in Notion, a page under Cortex Gnome.
- **Docs and decks:** native output types if the host has them (recommended; they're editable and export to Word, PowerPoint, and PDF), otherwise Notion, Google Drive, or files in a repo.
- **Design:** native types, Canva if connected, or files.
- **Email drafts and calendar holds:** the owner's own email and calendar, if connected.

## Step 4. Build the home (first gnome only)

Create the Gnome home and its pieces exactly as in `gnome-spec.md` sections 1 to 5:

1. The home page or folder, "Cortex Gnome". With a Cortex: under the Cortex parent.
2. **Gnome Registry**, **Gnome Runs**, and **Gnome Jobs** collections with their fields. In Notion: Gnome Runs and Gnome Jobs relate to the Registry; Gnome Jobs relates to Gnome Runs; Parent is a self-relation. Create the saved views listed in section 7.
3. **Gnome Manifesto** from `manifesto-template.md`. Ask whether they'd rather keep it as a file in a repo (`GNOME.md`); default is the home.
4. **Gnome Workspace**.
5. **Test write:** create and then close a test job. If it fails, report the error plainly and stop until access works. No log, no gnome.
6. **With a Cortex:** register the three collections on the Map (Collections table) and add the two Routing lines from `gnome-spec.md` section 1. This is a structure change, so say what you're adding and do it on a yes, following the Cortex spec's ownership rules.

## Step 5. Settings

Ask in one or two calls:

- **Name:** default "<Owner>'s Gnome". Must be unique in the Registry.
- **Lanes:** which areas this gnome owns. With other gnomes, show their lanes and avoid overlap. Solo: leave empty (anything).
- **Starting rung:** every new gnome starts on Starter (3 jobs, 5 points, inferred work proposed, per-job ship approvals only). The only choice here is going lighter: 1 or 2 jobs a night, or tagged work only with no proposals. Explain sizes in one line: small 1 point, medium 2, large 4. Say plainly that the budget counts jobs, not tokens: it limits how much the gnome builds, which is the main driver of cost, but it isn't a hard token cap.
- **Who can tag work:** anyone on the team (recommended) or named people.
- **Brief:** where it goes. The chat of each run always gets it, and review happens there. Add email to the owner, a Slack channel, or both. If the brief goes to a shared channel, set `brief.share_level: team`.
- **Cortex Inbox:** may the gnome drop durable context it finds into the Cortex Inbox? (Only with a Cortex.)
- **Spending cap:** default 0. Explain that bookings and purchases always need a per-job approval with the amount, whatever the cap.

Write the Registry row with the Settings block (`gnome-spec.md` section 2).

## Step 6. Preview and agree the rules

This is the step that makes night one useful.

1. **Dry harvest.** Run the harvest and triage for the last 3 days (`harvest-and-triage.md`) without claiming or building anything.
2. **Show the would-do list:** each job with its type, size, origin, and why, split into "would build", "would propose", and "would skip".
3. **Ask:** "Good to go? Anything you'd never want me to do, always want me to do, or do differently?" Turn each answer into Manifesto rules (`review-and-learning.md`, Distilling rules). Permissions they grant here are live grants: record who and when, scoped to this gnome, marked "(active from Trusted)", since a Starter gnome ships only with per-job approvals.
4. **Show the guardrails** in three lines: it builds anything, ships only what they approve or have standing permission for, and never spends, deletes, changes access, or messages someone new on its own.
5. **Optional first build.** Offer to build one item from the list now, with them watching, so they see the quality bar before the first night.

## Step 7. Schedule it

1. **Time:** default 7pm in the owner's time zone, daily. Offer weekdays only. Follow the scheduling tool's own guidance on the exact minute.
2. **Create the scheduled task** with the session's scheduling tools. Each run starts a fresh session with no memory of this chat, so the prompt must stand alone:

   ```text
   Run my cortex-gnome skill in run mode.
   Gnome: <name>. Home: <link>. Registry row: <link>.
   This is an unattended overnight run: don't ask questions. Follow the run steps end to end, log everything, and deliver the brief to this chat and the configured channels.
   ```

3. **Make it able to run alone.** Check and tell them, in plain steps:
   - **Automatic approval.** A run that stops for approval stalls all night. If the task asks before acting, tell them to turn on automatic approval in the task's settings. Be clear about what that means: the host will no longer ask before each action, so the gnome's guardrails are the only check left on the tools it can reach. On Starter, recommend giving its connectors the narrowest access that works (read access, drafts, branches) and widening it as the gnome moves up.
   - **Connectors** used by the gnome must be enabled for scheduled runs, not just this chat.
   - **Local folders** (Obsidian, a local Cortex, local repos) are only reachable while that computer is on with the desktop app open. Mark the task as needing that computer.
   - **Notifications:** offer push or email when a run finishes.
4. Record the scheduled task's id and schedule in the Registry row.

If no scheduling tool is available, say so plainly and give the prompt above so they can schedule it wherever they run Claude.

## Trust ladder

New gnomes start reined in. They earn room through review, never by default. Rung settings: Starter sets `trust.rung: starter`, `budget.max_jobs: 3`, `budget.max_points: 5`, `infer.max_auto: 0`; Trusted raises them to 5, 8, and 2. The weekly consolidation checks the ladder and offers the next rung in the brief; the owner decides in a live review.

| Rung | Budget | Inference | Ship | Move up when |
| --- | --- | --- | --- | --- |
| **1. Starter** (default) | 3 jobs, 5 points | Propose only; build tagged work | Nothing standing; per-job approvals only | 10 or more jobs reviewed and at least 70% kept, over at least 7 runs |
| **2. Trusted** | 5 jobs, 8 points | Build small one-shot work, propose the rest | Standing permissions the owner grants, one at a time | 25 or more reviewed, 80% or more kept, no guardrail incidents |
| **3. Proven** | Owner's choice | Owner's Inference rules | Standing permissions as granted | The owner says so |

- **Down a rung, automatically for the night.** At the start of every run (SKILL.md, Step 0), the gnome drops to Starter for that run if it has Ready jobs older than 7 days and nothing was reviewed in that time, the keep rate over the last 10 reviewed jobs is under 50%, or a run in the last 14 days recorded an Incident. It records the override on the run's Rung field and recommends the settings change in the brief. An ignored gnome stops spending on builds nobody reads.
- **Up a rung, only with a yes.** The weekly consolidation checks the "Move up when" column and offers the next rung in the brief. The owner says yes in a live review or status mode, which updates the settings.
- Record the current rung in the Registry row's Summary ("Starter since 2026-10-11").

## Step 8. Report

Short:

- The gnome's name, lanes, budget, and schedule
- Where the home, Manifesto, workspace, and Registry row live, with links
- Sources connected, and any that failed
- What happens tonight: it runs at <time>, the brief arrives in that run's chat, reply there to review
- That it starts on the Starter rung, and what earns it more room (Trust ladder)
- One more reminder: it uses tokens every night, and the reviews are what make it worth them
- How to hand it work: tag `gnome` in <task tool>, write `@gnome` in a Cortex record, or add a Queued row to Gnome Jobs
