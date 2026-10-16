# Cortex plugin

The skills for [Cortex](../../README.md), the context layer your AI reads first.

```
/plugin install cortex --marketplace Chaos-to-Clarity/cortex
```

| Skill | Run it | What it does |
| --- | --- | --- |
| `cortex-setup` | Once | Asks where to store it, connects sources, builds the collections, catalogs, and Map, interviews you to fill it, and gives you custom instructions |
| `cortex-map` | When needed | Adopts an existing setup, imports CRM or LinkedIn exports, upgrades older Maps, rebuilds catalogs, or repairs the Map |
| `add-to-cortex` | Any time | Digests one document into the right records, without duplicates |
| `strategy-digest` | When a strategy doc changes | Condenses plans, decks, personas, and brand docs into Strategy |
| `cortex-update` | Weekly, scheduled | Updates records from recent meetings, email, and calendar, triages the Inbox, and runs the health check |
| `ask-cortex` | Any time | Answers from the Map, catalogs, and records, plus your live calendar, meetings, and email |

For overnight work on top of your Cortex, see [Cortex Gnome](../cortex-gnome/README.md).

Every skill follows [`spec/cortex-spec.md`](../../spec/cortex-spec.md). Each carries a copy in its `references/` folder.

Built by Eric Weiss at [Chaos to Clarity](https://chaostoclarity.io). For executive coaching, AI strategy, or the Full-Stack AI Operating System bootcamp, [book a call](https://calendly.com/emweiss/clarity) or email [eric@chaostoclarity.io](mailto:eric@chaostoclarity.io).
