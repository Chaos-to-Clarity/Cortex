# Cortex

**The context layer your AI reads first.**

Every AI conversation starts from zero: who your people are, what you're driving, what you already decided. Cortex gives every assistant you use (Claude, ChatGPT, Gemini, Grok) one shared, always-current memory of your business. It lives in your own tools, and a Map tells any AI exactly where to look and where to file things.

Built by Eric Weiss at [Chaos to Clarity](https://chaostoclarity.io).

Want help putting this to work in your company? [Work with Eric.](#work-with-eric)

## Quick start: 3 steps, about 30 minutes

**1. Install Cortex in Claude** (paid plan)

In the Claude app, open **Customize**, then **Plugins**, then **Add**, **Add marketplace**, **Add from a repository**. Enter:

```
chaostoclarity/Cortex
```

Then add the **Cortex** plugin. On a free plan, or if you prefer single skills, see [Install one skill at a time](#install-one-skill-at-a-time).

**2. Build your Cortex**

Start a new chat and say:

> Set up my Cortex.

Claude asks where to keep it (Notion, Obsidian, or Google Drive), connects your calendar, meeting notes, and email, builds everything, and interviews you to fill it. Answer in your own words; it pushes for specifics. When it's done, it hands you your custom instructions, filled in.

**3. Paste your custom instructions everywhere you use AI**

This is what makes Cortex universal. See the next section. Paste once per assistant and you're done.

That's it. From then on, ask anything: "Prep me for my call with Sam," "What's at risk this week?", "Here's a doc, add it to my Cortex." Schedule **cortex-update** weekly when setup offers, and the Cortex keeps itself current.

Already have a "second brain" in Notion or Obsidian? In step 2, say **"Adopt my existing setup as a Cortex"** instead. Nothing gets moved or renamed.

## Custom instructions: make every AI aware of your Cortex

**You don't write these yourself.** At the end of setup, Claude gives you your own version, filled in with your Map link and details, ready to copy and paste. Nothing in brackets.

If you lose it, say **"Give me my Cortex custom instructions"** and Claude regenerates it.

<details>
<summary>See what it looks like</summary>

```text
## My Cortex
My business context lives in my Cortex, a structured knowledge base in [Notion]. Map: [link to your Cortex Map]

Snapshot (no lookup needed): [Name], [role] at [company]. Focus now: [top 2-3 priorities]. Key people: [3-5 names].

When to look: only when my request is about my business, people, clients, projects, decisions, or priorities AND the answer would be clearly better or safer with that context (I name someone or something, want advice on my situation, or ask you to draft, plan, or prep). Skip it for general questions, generic writing, or code, or when this chat already has what you need. If unsure, ask me in one line instead of looking.

How: read the Map once per chat and reuse it. Use its Glossary and Catalogs to open only the few records you need; never search my whole workspace. Cite what you used and its date. If it isn't there, say so. If you can't reach it, tell me once and carry on.
```

</details>

**Where to paste it**

| Assistant | Where |
| --- | --- |
| Claude | Settings, then Profile, in the preferences field |
| ChatGPT | Settings, then Personalization, in Custom instructions |
| Gemini, Grok, and others | The custom instructions or personalization setting |
| Any project or custom GPT | Its project instructions, if you want Cortex there too |

**Each assistant needs a connector** to wherever your Cortex lives, Notion or Google Drive for example, or it can't read the Map. Obsidian and local folders are only reachable from assistants that can see that computer.

**Why it stays lightweight**

Most chats don't need your business context, and none should pay for a lookup they don't need. The instructions are built for that:

- **The Snapshot** answers basic "who am I, what's my focus" context with no lookup at all.
- **The gate** means the AI looks only when your request is about your business and the answer would be clearly better with the context. If it's unsure, it asks you in one line instead of fetching.
- **Cheapest step first.** One Map read per chat, reused after that. Catalogs only for names that matched, and records only for the few that matter. No searching your workspace.
- **It fits.** Under 1,000 characters, so it fits every platform's limit with room for your other preferences.

When your priorities shift, the weekly update gives you a refreshed Snapshot line to paste.

## How it works

Writing context into a store is easy. Finding the right context in a store that keeps growing, that's shaped differently for every business, and that many agents write to is the hard part. Without structure, every conversation sifts everything, burns tokens, and still answers from the wrong or incomplete pieces.

Cortex reads in three layers, top-down:

| Layer | What it is | Read |
| --- | --- | --- |
| **Map** | One page: every collection and where it lives, routing rules for finding and filing, a glossary of your names and nicknames, and how fresh everything is | First, once per chat |
| **Catalogs** | One compact line per record: name, aliases, status, one-line summary | To pick records |
| **Records** | The full detail, current state on top, dated history below | Only the ones picked |

Writes follow the same Map: route it, match it to the existing record by name or alias, update it in place, update its catalog line, log it. Anything unclear goes to an **Inbox** instead of being guessed. A weekly health check keeps catalogs accurate, flags stale records and likely duplicates, and keeps the Map small.

The rules are universal and live in the skills. Your Map, catalogs, and glossary are unique to your business and grow with it.

### What it stores

| Collection | Holds |
| --- | --- |
| People | Everyone you deal with regularly, the one thing worth remembering, and the open thread |
| Initiatives | What you're driving: why it matters, blocker, next action |
| Decisions | Calls made and questions open, with the reasoning |
| Inbox | Anything that didn't clearly fit, waiting to be filed |
| Ingest Log | What's been processed, so nothing is ingested twice |

Plus **Strategy** and **Standing Context** pages, and any collections you add (Customers, Pipeline, Portfolio). Register them on the Map and every skill uses them.

### Where it lives

You choose during setup: **Notion**, **Obsidian**, **Markdown in Google Drive**, a local folder, or another tool Claude can connect to. Same structure and rules everywhere.

### The skills

| Skill | Use it | Download |
| --- | --- | --- |
| cortex-setup | Once, to build your Cortex and Map | [ZIP](https://github.com/chaostoclarity/Cortex/releases/latest/download/cortex-setup.zip) |
| cortex-map | To adopt an existing setup, or rebuild and repair the Map | [ZIP](https://github.com/chaostoclarity/Cortex/releases/latest/download/cortex-map.zip) |
| add-to-cortex | Any time you have a doc worth keeping | [ZIP](https://github.com/chaostoclarity/Cortex/releases/latest/download/add-to-cortex.zip) |
| strategy-digest | When a strategy doc changes | [ZIP](https://github.com/chaostoclarity/Cortex/releases/latest/download/strategy-digest.zip) |
| cortex-update | Weekly, on a schedule | [ZIP](https://github.com/chaostoclarity/Cortex/releases/latest/download/cortex-update.zip) |
| ask-cortex | Any question about your work | [ZIP](https://github.com/chaostoclarity/Cortex/releases/latest/download/ask-cortex.zip) |

## Install one skill at a time

For free plans, or if you only want some skills:

1. Click a **ZIP** link in the table above. Don't unzip it.
2. In Claude, open **Customize**, then **Skills**, then **Create skill**, then **Upload a skill**, and choose the ZIP.
3. Repeat for each skill. Start with cortex-setup.

**Claude Code:** `/plugin install cortex --marketplace chaostoclarity/cortex`

Cortex is also in the [Chaos to Clarity skills marketplace](https://github.com/chaostoclarity/Claude-skills), next to **Founder OS**, the weekly operating system that runs on it.

## The spec

[`spec/cortex-spec.md`](spec/cortex-spec.md) is the full contract: the Map format, record and catalog formats, the reading and writing protocols, backends, and the health check. Any agent that follows it can use a Cortex.

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
