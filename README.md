# Cortex

**The context layer your AI reads first.**

Every AI conversation starts from zero: who your people are, what you're driving, what you already decided. Cortex gives every assistant you use (Claude, ChatGPT, Gemini, Grok) one shared, always-current memory of your business. It lives in your own tools, and a Map tells any AI exactly where to look and where to file things.

Built by Eric Weiss at [Chaos to Clarity](https://chaostoclarity.io).

Want help putting this to work in your company? [Work with Eric.](#work-with-eric)

## Quick start: 3 steps, about 30 minutes

**1. Install Cortex in Claude** (paid plan)

In the Claude app, open **Customize**, then **Plugins**, then **Add**, **Add marketplace**, **Add from a repository**. Enter:

```
Chaos-to-Clarity/Cortex
```

Then add the **Cortex** plugin. On a free plan, or if you prefer single skills, see [Install one skill at a time](#install-one-skill-at-a-time).

**2. Build your Cortex**

Start a new chat and say:

> Set up my Cortex.

Claude asks where to keep it (Notion, Obsidian, or Google Drive), connects your calendar, meeting notes, and email, builds everything, and interviews you to fill it. Answer in your own words; it pushes for specifics. When it's done, it hands you your custom instructions, filled in.

**3. Paste your custom instructions everywhere you use AI**

This is what makes Cortex universal. See the next section. Paste once per assistant and you're done.

That's it. From then on, ask anything: "Prep me for my call with Sam," "What's at risk this week?", "Here's a doc, add it to my Cortex." Setup schedules **cortex-dream** nightly and **cortex-update** weekly, and the Cortex keeps itself current.

Already have a "second brain" in Notion or Obsidian? In step 2, say **"Adopt my existing setup as a Cortex"** instead. Nothing gets moved or renamed. Have a CRM or LinkedIn export? Say **"Import my contacts into my Cortex"** to start with real people and companies.

## Custom instructions: make every AI aware of your Cortex

**You don't write these yourself.** At the end of setup, Claude gives you your own version, filled in with your Map link and details, ready to copy and paste. Nothing in brackets.

If you lose it, say **"Give me my Cortex custom instructions"** and Claude regenerates it.

<details>
<summary>See what it looks like</summary>

```text
## My Cortex
My business context lives in my Cortex, a structured knowledge base in [Notion]. Map: [link to your Cortex Map]

About me: [Name], [role] at [company], which [what the business does, in a few words].

When to look: only when my request is about my business, people, clients, projects, decisions, or priorities AND the answer would be clearly better or safer with that context (I name someone or something, want advice on my situation, or ask you to draft, plan, or prep). Skip it for general questions, generic writing, or code, or when this chat already has what you need. If unsure, ask me in one line instead of looking.

How: read the Map once per chat and reuse it. Use its Glossary and Catalogs to open only the few records you need; never search my whole workspace. Cite what you used and its date. If it isn't there, say so. If you can't reach it, tell me once and carry on.
```

</details>

**Where to paste it**

| Assistant | Where |
| --- | --- |
| Claude | Settings, in "Instructions for Claude" |
| ChatGPT | Settings, then Personalization, in Custom instructions |
| Gemini, Grok, and others | The custom instructions or personalization setting |
| Any project or custom GPT | Its project instructions, if you want Cortex there too |

**Each assistant needs a connector** to wherever your Cortex lives, Notion or Google Drive for example, or it can't read the Map. Obsidian and local folders are only reachable from assistants that can see that computer.

**Why it stays lightweight**

Most chats don't need your business context, and none should pay for a lookup they don't need. The instructions are built for that:

- **One line about you** answers "who am I" with no lookup at all. Everything that changes, your priorities, clients, and people, stays in the Cortex.
- **The gate** means the AI looks only when your request is about your business and the answer would be clearly better with the context. If it's unsure, it asks you in one line instead of fetching.
- **Cheapest step first.** One Map read per chat, reused after that. Catalogs only for names that matched, and records only for the few that matter. No searching your workspace.
- **It fits.** Under 1,000 characters, so it fits every platform's limit with room for your other preferences.

You paste it once. Nothing in it goes stale, so there's nothing to update when your priorities shift.

## How it works

Writing context into a store is easy. Finding the right context in a store that keeps growing, that's shaped differently for every business, and that many agents write to is the hard part. Without structure, every conversation sifts everything, burns tokens, and still answers from the wrong or incomplete pieces.

Cortex reads in three layers, top-down:

| Layer | What it is | Read |
| --- | --- | --- |
| **Map** | One page: every collection and where it lives, routing rules for finding and filing, a glossary of your names and nicknames, and how fresh everything is | First, once per chat |
| **Catalogs** | One compact line per record: name, aliases, status, one-line summary | To pick records |
| **Records** | The full detail, current state on top, dated history below | Only the ones picked |

It stays lean as it grows. People and companies start as one-line stubs and earn a full record once they show up in three sources or become a real relationship. When a record's history outgrows its summary, the summary is rewritten. The most-connected records surface first. And when a name isn't in the Map or catalogs, one search inside the Cortex, never your whole workspace, catches anything an index missed.

Writes follow the same Map: route it, match it to the existing record by name or alias, update it in place, update its catalog line, log it. Anything unclear goes to an **Inbox** instead of being guessed.

### It dreams

Every write adds a little, and a store that only grows drifts: the same fact ends up in two places with two values, "waiting on the proposal next week" is still there a month later, and summaries fall behind the history under them. So every night, while you sleep, **cortex-dream** does what sleep does for memory:

- **Replays the day.** New meeting notes become updates to the right records.
- **Consolidates.** When two facts disagree, the newer one wins and the old one is closed with a date, never erased. Relative dates become real ones. Records whose history has outgrown their summary are rewritten, keeping every name, number, and commitment.
- **Notices time.** Deadlines that passed, threads waiting too long, initiatives past their target, decisions left open. It asks you instead of guessing.
- **Spots patterns.** What no single record shows, like a topic coming up across four meetings that nothing in the Cortex tracks. Labeled as inferred until you confirm it.
- **Downscales.** Expires one-off mentions, fixes catalogs, and keeps the Map small, so reads stay fast as the Cortex grows.

It works on what changed plus a rolling few records each night, never the whole store, so quiet nights cost little and every record still gets revisited every few weeks. Every change is stamped and reversible, and anything consequential, like merging two records or closing one, waits for your yes. Each morning you get a short note: what changed overnight, what needs you, and what it noticed. The full record lives in your **Dream Journal**.

A weekly **cortex-update** does the wide sweep the dream doesn't: email and calendar, a health check across every record, and the review list.

The rules are universal and live in the skills. Your Map, catalogs, and glossary are unique to your business and grow with it.

### What it stores

| Collection | Holds |
| --- | --- |
| People | Everyone you deal with regularly, the one thing worth remembering, and the open thread |
| Companies | Customers, investors, partners, and competitors: the relationship, the people, and the open thread |
| Initiatives | What you're driving: why it matters, blocker, next action |
| Decisions | Calls made and questions open, with the reasoning |
| Inbox | Anything that didn't clearly fit, waiting to be filed |
| Ingest Log | What's been processed, so nothing is ingested twice |

Plus **Strategy**, **Standing Context**, and **Dream Journal** pages, and any collections you add (Customers, Pipeline, Portfolio). Register them on the Map and every skill uses them.

### Where it lives

You choose during setup: **Notion**, **Obsidian**, **Markdown in Google Drive**, a local folder, or another tool Claude can connect to. Same structure and rules everywhere.

### The skills

| Skill | Use it | Download |
| --- | --- | --- |
| cortex-setup | Once, to build your Cortex and Map | [ZIP](https://github.com/Chaos-to-Clarity/Cortex/releases/latest/download/cortex-setup.zip) |
| cortex-map | To adopt an existing setup, import contacts, upgrade, or rebuild and repair the Map | [ZIP](https://github.com/Chaos-to-Clarity/Cortex/releases/latest/download/cortex-map.zip) |
| add-to-cortex | Any time you have a doc worth keeping | [ZIP](https://github.com/Chaos-to-Clarity/Cortex/releases/latest/download/add-to-cortex.zip) |
| strategy-digest | When a strategy doc changes | [ZIP](https://github.com/Chaos-to-Clarity/Cortex/releases/latest/download/strategy-digest.zip) |
| cortex-dream | Nightly, on a schedule. The core routine that keeps it current and lean | [ZIP](https://github.com/Chaos-to-Clarity/Cortex/releases/latest/download/cortex-dream.zip) |
| cortex-update | Weekly, on a schedule | [ZIP](https://github.com/Chaos-to-Clarity/Cortex/releases/latest/download/cortex-update.zip) |
| ask-cortex | Any question about your work | [ZIP](https://github.com/Chaos-to-Clarity/Cortex/releases/latest/download/ask-cortex.zip) |

### Cortex Gnome: the overnight worker

A separate plugin in this repo. Every night it reads what changed across your Cortex, task tool, idea inbox, meetings, and repos, builds the work worth doing (decks, docs, landing pages, research, code with pull requests, drafts), logs it in your Cortex, and sends you a brief. Your feedback becomes rules in its Manifesto, so it gets better every night. Teams can run several gnomes; they share one queue and claim work before building it. It also runs without a Cortex.

**Read this first:** it costs tokens every night whether or not it produces anything useful, and it's only as good as your feedback. Start it reined in and give it more room once it proves itself. Best on high-limit plans such as Claude Max. [Details](plugins/cortex-gnome/README.md).

| Skill | Use it | Download |
| --- | --- | --- |
| cortex-gnome | Once to set up, then nightly on a schedule; review its brief each morning | [ZIP](https://github.com/Chaos-to-Clarity/Cortex/releases/latest/download/cortex-gnome.zip) |

## Install one skill at a time

For free plans, or if you only want some skills:

1. Click a **ZIP** link in the table above. Don't unzip it.
2. In Claude, open **Customize**, then **Skills**, then **Create skill**, then **Upload a skill**, and choose the ZIP.
3. Repeat for each skill. Start with cortex-setup.

**Claude Code:** `/plugin install cortex --marketplace Chaos-to-Clarity/cortex`, and `/plugin install cortex-gnome --marketplace Chaos-to-Clarity/cortex` for the gnome.

## Built on Cortex: the Cortex Suite

Cortex is the foundation. The Cortex Suite holds the skills that run on it. Each one reads your Cortex, does the work, and writes back what it learned, so every skill gets sharper as the others run. The suite lives in a private repo, [cortex-skills](https://github.com/Chaos-to-Clarity/cortex-skills), for Eric's workshop attendees, Realm members, and coaching clients. Once you have access, add the marketplace (`Chaos-to-Clarity/cortex-skills`) and it installs Cortex along with the suite. [Join a workshop](https://chaostoclarity.io) or [book a call](https://calendly.com/emweiss/clarity) to get access.

| Plugin | What it does |
| --- | --- |
| [**Founder OS**](https://github.com/Chaos-to-Clarity/cortex-skills/tree/main/plugins/founder-os) | Your weekly operating cycle. Plan Monday, brief each morning, reflect Friday. |
| [**Investor Update**](https://github.com/Chaos-to-Clarity/cortex-skills/tree/main/plugins/investor-update) | Your monthly investor update, drafted from your Cortex. Metrics with deltas, required lowlights, what you promised last time, and specific asks. Always a draft. |
| [**Customer Signal**](https://github.com/Chaos-to-Clarity/cortex-skills/tree/main/plugins/customer-signal) | Every customer and prospect call becomes evidence. Pains, requests, objections, churn risks, and praise, counted across accounts, with a weekly brief. |
| [**One-on-Ones**](https://github.com/Chaos-to-Clarity/cortex-skills/tree/main/plugins/one-on-ones) | Prep and debrief every 1:1 with your direct reports. Commitments both ways, recurring themes, and a monthly team review. Private by design. |
| [**Recap**](https://github.com/Chaos-to-Clarity/cortex-skills/tree/main/plugins/recap) | Every meeting becomes done work: a recap email, your to-dos with time booked, follow-ups drafted, and context saved to your Cortex. |
| [**Content Engine**](https://github.com/Chaos-to-Clarity/cortex-skills/tree/main/plugins/content-engine) | Last week's meetings become this week's framework, newsletter issue, and LinkedIn post, in your voice and kept confidential. |
| [**Handwritten Notes**](https://github.com/Chaos-to-Clarity/cortex-skills/tree/main/plugins/handwritten-notes) | Photograph a page of notes. Checkbox items become tasks with time booked; everything else is filed as notes linked to the right people and projects. |

Each suite skill registers its own collection on your Map the first time it runs, so you never set up the structure by hand. Building your own skill on Cortex? Follow [the spec](#the-spec) and register your collection the same way.

## The spec

[`spec/cortex-spec.md`](spec/cortex-spec.md) is the full contract: the Map format, record and catalog formats, the reading and writing protocols, backends, and the health check. Any agent that follows it can use a Cortex. [`spec/company-pack.md`](spec/company-pack.md) adds what a company Cortex needs.

## Cortex for a company

A Cortex can serve one founder or a whole exec team. When you run setup, Claude asks, "Is this for you, or for your company?" Choose the company and it installs the [Company Pack](spec/company-pack.md): departments, the numbers you manage to, what each exec has promised and by when, the org chart and open roles, the board, and the risks. Each person gets their own private space, so 1:1 notes and personal reflections never land where the team can read them.

Already built your own Cortex? Ask Claude to "turn my Cortex into a company Cortex." It moves your private records first, then adds the pack.

## Work with Eric

Cortex is one of the systems teams build in the Full-Stack AI Operating System, alongside a working AI strategy for the whole company.

I'm Eric Weiss, founder of Chaos to Clarity. I've spent ten years coaching more than 70 technical founders and CTOs at venture-backed companies, and every skill here came out of that work. There are a few ways I can help you go further.

**Executive coaching.** I coach founders and CTOs whose companies are growing faster than their leadership. Together we find the real bottleneck, name what you're tolerating, and build the habits and systems that let the company scale without routing everything through you.

**AI strategy.** I help leadership teams decide where AI belongs in the business, set the guardrails, and get their people using it well. I was an engineering leader and CTO before I became a coach, and I helped OpenAI operationalize its GPT models.

**AI products with a human edge.** I work with product teams to build AI into what they ship while keeping judgment, taste, and relationships in human hands.

**The Full-Stack AI Operating System.** This 12-week bootcamp is for founders and their executive teams. You'll build an AI strategy, an AI-native product roadmap, working systems with human checkpoints, and adoption guidelines for your team, and you'll leave with a library of AI skills and a 90-day plan. The program runs as six live workshops and six office hours in small cohorts. [See the program.](https://chaostoclarity.io/ai-os/)

**Let's talk.** [Book a call](https://calendly.com/emweiss/clarity), or email me at [eric@chaostoclarity.io](mailto:eric@chaostoclarity.io). Tell me what you're building and where you're stuck, and I'll reply personally.

## License

Free to use and adapt inside your own business. Not for resale, redistribution, or sharing.

These skills are licensed under the [PolyForm Internal Use License 1.0.0](LICENSE.md). In plain terms:

- **You can** install them, run them for your own company's internal operations, and change them to fit how you work.
- **You can't** share or distribute them, sublicense them, sell them, or package them into a product or service for others.

For other uses, such as rolling them out to clients or teaching them, contact Eric at [chaostoclarity.io](https://chaostoclarity.io).

## For maintainers

- Skills live in `plugins/cortex/skills/<name>/SKILL.md`.
- The spec's master copy is `spec/cortex-spec.md`. Edit it, then run `python scripts/sync_spec.py` to copy it into every skill. The build fails if a copy is stale.
- Don't set `version` in `plugin.json`; installs track each commit.
- Push to `main` and the release workflow checks everything, builds the ZIPs, and publishes a release.

Test locally:

```
python scripts/sync_spec.py
python scripts/build_zips.py
claude plugin validate .
```
