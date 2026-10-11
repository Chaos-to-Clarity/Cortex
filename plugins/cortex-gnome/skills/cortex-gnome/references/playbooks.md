# Playbooks

How to build each kind of job. The Manifesto's Quality bars for a type add to these and win where they differ. Every playbook ends the same way: store the output, link it on the job, check it, and ship only with permission (`guardrails.md`).

## Before any job

1. Open the job's Source and only the context it needs. With a Cortex, resolve names through the Map and catalogs and open the few records involved.
2. Write down, for yourself, the job's reader, the decision or action the output should drive, and the deadline.
3. Use the best format the environment offers. If the host has native output types (a slide deck type, a document type, a design type), use them: they open in an editor the reviewer can change directly and they export to PowerPoint, Word, PDF, or images. Otherwise build files (`.pptx`, `.docx`, `.html`, `.md`) and store them in the Gnome workspace. If a skill exists for the format, follow it.
4. Use the company's brand if the Cortex, Manifesto, or workspace has one (a design system, brand page, or template).

## Deck

- One message per slide, written as a headline sentence. Speaker notes carry the detail.
- Open with the ask or the answer; end with the decision or next step.
- Every number has a source in the notes. No invented figures, no placeholder logos.
- Default 6 to 12 slides unless the job says otherwise.
- Ship: sharing with or sending to anyone beyond the owner is Tier 3.

## Document or memo

- The answer or recommendation in the first three lines. Then the reasoning, then the details.
- Name the reader and what they should do after reading.
- Cite sources inline; list links at the end.
- Ship: sharing it beyond the workspace, or posting it, is Tier 3.

## Landing page or web page

- Build a complete, self-contained page: real copy from the context, one clear call to action, mobile layout, no lorem ipsum.
- Store a preview in the workspace (a published private page if the host offers one, otherwise an `.html` file).
- If it's for an existing site in a repo, make it a code job instead: branch, change, pull request with a preview link if the repo has preview deploys.
- Ship: publishing to a live domain is Tier 3.

## Research

- Answer the question first, then the evidence. Separate what's verified from what's inferred.
- Use original sources over aggregators; date everything; list sources with links.
- Stop at enough to decide. Note what would change the answer.

## Code

- Follow `guardrails.md`, Code.
- Read the issue, task, or Cortex context; restate the change in the PR description in two lines.
- Make the smallest change that does the job. Add or update tests. Run what the repo has.
- PR description: why (with source links), what changed, how it was tested, risks, and what a reviewer should check first.
- Review comments on the gnome's own open PRs are Revision jobs: address each, reply on the thread, push to the same branch.
- Ship: merging or deploying is Tier 3.

## Task updates

- Close the loop on the task tool: add a comment with the output link to the task that prompted it, update its status only if the Manifesto allows it, and add subtasks for what's left.
- Clean up only what the gnome made or what the job asks for. Don't reorganize someone else's board.
- Tier 2 by default.

## Email or message draft

- Draft in the owner's voice (the Manifesto's Voice section, and a writing-style profile if one exists).
- Put the ask in the first two lines. Keep it short.
- Leave it as a draft in the owner's email or chat tool, threaded where it belongs, with the job linked in the brief.
- Ship: sending is Tier 3, and never to someone new (`guardrails.md`).

## Scheduling

- Find two or three times that fit the owner's calendar and working hours. Place tentative holds on the owner's own calendar, titled "HOLD (gnome): <purpose>".
- Draft the invite or the scheduling email.
- Ship: sending invites or the email is Tier 3.

## Travel

- Build an options sheet: two or three itineraries with times, prices, total cost, and booking links; the owner's known preferences first.
- Hold calendar time for travel days on the owner's calendar.
- Ship: booking is Tier 3 plus spending, needing a per-job approval with the amount.

## Content (posts, newsletter, articles)

- Use the owner's voice and any content rules in the Manifesto. One idea per piece, a strong first line, a real example from the context, a concrete takeaway.
- Never put a client's, colleague's, or company's private details in public content unless the source was already public or they approved it.
- Ship: posting or scheduling the post is Tier 3.

## Analysis

- Get the data into files and compute in code; never estimate figures in prose.
- Lead with the answer and the one chart or table that shows it. Make every number traceable to its source.
- Store the notebook or script alongside the output so the reviewer can rerun it.

## Other

Anything else: decide the output format a person in that role would hand over, write a three-line plan in the job's Note, and build to the closest playbook above. Note in the brief that it was a new type, so review can add a Quality bar for it.
