# Cortex

**The context layer your AI reads first.**

Every AI conversation starts from zero: who your people are, what you're driving, what you already decided. Cortex gives your AI a structured, always-current memory of your business that lives in your own tools, and a Map that tells any assistant exactly where to look and where to file things.

Built by Eric Weiss at [Chaos to Clarity](https://chaostoclarity.io).

## Why a Map

Writing context into a store is easy. Finding the right context in a store that keeps growing, that's shaped differently for every business, and that many agents write to is the hard part. Without structure, every conversation sifts the whole thing, burns tokens, and still answers from the wrong or incomplete pieces.

Cortex reads in three layers, top-down:

| Layer | What it is | Read |
| --- | --- | --- |
| **Map** | One page: every collection and where it lives, routing rules for finding and filing, a glossary of your names and nicknames, and how fresh everything is | First, every time |
| **Catalogs** | One compact line per record: name, aliases, status, one-line summary | To pick records |
| **Records** | The full detail, current state on top, dated history below | Only the ones picked |

A typical question costs one Map read, a catalog or two, and two or three records. No searching.

Writes follow the same Map: route it, match it to the existing record by name or alias, update it in place, update its catalog line, log it. Anything unclear goes to an **Inbox** instead of being guessed. A weekly health check keeps catalogs accurate, flags stale records and likely duplicates, and keeps the Map small.

The rules are universal and live in the skills. Your Map, catalogs, and glossary are unique to your business and grow with it.

## What it stores

| Collection | Holds |
| --- | --- |
| People | Everyone you deal with regularly, the one thing worth remembering, and the open thread |
| Initiatives | What you're driving: why it matters, blocker, next action |
| Decisions | Calls made and questions open, with the reasoning |
| Inbox | Anything that didn't clearly fit, waiting to be filed |
| Ingest Log | What's been processed, so nothing is ingested twice |

Plus **Strategy** and **Standing Context** pages, and any collections you add (Customers, Pipeline, Portfolio). Register them on the Map and every skill uses them.

## Where it lives

You choose during setup: **Notion**, **Obsidian**, **Markdown in Google Drive**, a local folder, or another tool Claude can connect to. Same structure and rules everywhere.

## Install

**Claude app** (paid plans): open **Customize**, then **Plugins**, then **Add**, **Add marketplace**, **Add from a repository**, and enter `chaostoclarity/Cortex`. Then add the Cortex plugin.

**Claude Code**

```
/plugin install cortex --marketplace chaostoclarity/cortex
```

Cortex is also listed in the [Chaos to Clarity skills marketplace](https://github.com/chaostoclarity/Claude-skills), alongside Founder OS, which runs on it.

**One skill at a time:** download a ZIP below, then in Claude open **Customize**, **Skills**, **Create skill**, **Upload a skill**.

| Skill | Use it | Download |
| --- | --- | --- |
| cortex-setup | Once, to build your Cortex and Map | [ZIP](https://github.com/chaostoclarity/Cortex/releases/latest/download/cortex-setup.zip) |
| cortex-map | To adopt an existing setup, or rebuild and repair the Map | [ZIP](https://github.com/chaostoclarity/Cortex/releases/latest/download/cortex-map.zip) |
| add-to-cortex | Any time you have a doc worth keeping | [ZIP](https://github.com/chaostoclarity/Cortex/releases/latest/download/add-to-cortex.zip) |
| strategy-digest | When a strategy doc changes | [ZIP](https://github.com/chaostoclarity/Cortex/releases/latest/download/strategy-digest.zip) |
| cortex-update | Weekly, on a schedule | [ZIP](https://github.com/chaostoclarity/Cortex/releases/latest/download/cortex-update.zip) |
| ask-cortex | Any question about your work | [ZIP](https://github.com/chaostoclarity/Cortex/releases/latest/download/ask-cortex.zip) |

## Get started

1. Say **"Set up my Cortex."** It asks where to store it, connects your sources, builds everything, and interviews you to fill it.
2. Paste the custom instructions it gives you into Claude (Settings, then Profile) and ChatGPT (Custom instructions). Every conversation then starts from your Map, with a direct link, so nothing searches.
3. Say **"Digest my strategy docs"**, then ask anything: **"Prep me for my call with Sam."**
4. Let **cortex-update** run weekly. It keeps everything current and clean.

Already have a "second brain" in Notion or Obsidian? Say **"Adopt my existing setup as a Cortex."** cortex-map registers what's there without moving anything.

## The spec

[`spec/cortex-spec.md`](spec/cortex-spec.md) is the full contract: the Map format, record and catalog formats, the reading and writing protocols, backends, and the health check. Any agent that follows it can use a Cortex.

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
