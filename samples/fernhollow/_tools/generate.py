"""Generate the Fernhollow sample company Cortex (Markdown backend).

Fernhollow is fictional. Any resemblance to a real company or person is accidental.
Usage: python gen_fernhollow.py <output_dir>
"""
import sys
from pathlib import Path

OUT = Path(sys.argv[1])
TODAY = "2026-10-28"


def yaml_val(v):
    if isinstance(v, list):
        return "[" + ", ".join(f'"{x}"' if "[[" in str(x) or "," in str(x) or ":" in str(x) else str(x) for x in v) + "]"
    if isinstance(v, (int, float)):
        return str(v)
    s = str(v)
    if any(c in s for c in ":#[]{}\"'") or s.startswith(("$", "-", "*")):
        return '"' + s.replace('"', '\\"') + '"'
    return s


def wl(name):
    return f"[[{name}]]"


def record(folder, identity, fields, current, history):
    fm = ["---"]
    for k, v in fields.items():
        fm.append(f"{k}: {yaml_val(v)}")
    fm.append("---")
    body = "\n".join(fm) + "\n\n## Current\n" + current.strip() + "\n\n## History\n" + "\n".join(f"- {h}" for h in history) + "\n"
    path = OUT / folder / (identity.replace("/", "-").replace(":", "-") + ".md")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body, encoding="utf-8")


def write(rel, text):
    path = OUT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


def catalog(folder, title, header, rows, note=""):
    lines = [f"# {title}", f"{note}{len(rows)} rows. Rebuilt {TODAY}.", "", "| " + " | ".join(header) + " |", "| " + " | ".join("---" for _ in header) + " |"]
    for r in rows:
        lines.append("| " + " | ".join(r) + " |")
    write(f"{folder}/_catalog.md", "\n".join(lines))


# ---------------------------------------------------------------- People
people = [
    ("Maya Okafor", dict(role="CEO and co-founder", company=wl("Fernhollow"), depth="Full", mentions=14, context="Decides fast once she has the numbers; wants one page, not ten", cadence="Daily", open_thread="Needs VP Sales finalists before the Nov 18 board", initiatives=[wl("Series C Readiness"), wl("Pricing and Packaging v2")]),
     "Co-founder and CEO since 2019. Owns the Series C raise, targeted to close by April 2027. Set Sales Health to Red on 2026-10-14. Running the VP Sales search herself.",
     ["2026-10-14: Set Sales department Health to Red (exec meeting, Granola)", "2026-10-06: First added (Intake interview, CEO)"], "Exec"),
    ("Theo Lindqvist", dict(role="Chief of Staff", company=wl("Fernhollow"), depth="Full", mentions=11, context="Runs the operating rhythm; reviewer for the dream's questions", cadence="Daily", open_thread="Owns the Q1 hiring plan, due Nov 20", initiatives=[wl("Series C Readiness")]),
     "Chief of Staff since March 2026. Runs the Monday exec meeting and the board prep calendar. Reviewer for this Cortex.",
     ["2026-10-07: First added (Intake interview, Chief of Staff)"], "Exec"),
    ("Priya Raman", dict(role="CTO", company=wl("Fernhollow"), depth="Full", mentions=9, context="Protects the v2 migration timeline; pushes back on scope added late", cadence="Weekly", open_thread="SOC 2 Type I audit kickoff by Nov 30", initiatives=[wl("Platform v2 Migration")]),
     "CTO and co-founder. Leads Engineering (16 people). The v2 migration is three weeks behind its Dec 15 target.",
     ["2026-10-20: v2 migration target at risk; three weeks behind (exec meeting, Granola)", "2026-10-08: First added (Intake interview, Exec)"], "Exec"),
    ("Jordan Ellis", dict(role="VP Product", company=wl("Fernhollow"), depth="Full", mentions=8, context="Owns pricing v2; blocked on sales input with no VP Sales", cadence="Weekly", open_thread="Pricing page now due Nov 22 after two slips", initiatives=[wl("Pricing and Packaging v2")]),
     "VP Product since 2025. Owns Pricing and Packaging v2. The pricing page has slipped twice, both times waiting on sales input on the enterprise tier.",
     ["2026-10-21: Pricing page due moved to Nov 22, second slip (exec meeting, Granola)", "2026-10-08: First added (Intake interview, Exec)"], "Exec"),
    ("Marcus Bell", dict(role="Head of Sales (interim)", company=wl("Fernhollow"), depth="Full", mentions=7, context="Strong closer; covering the VP Sales seat since July while carrying a quota", cadence="Weekly", open_thread="Next-quarter pipeline coverage at 2.2x against a 3.0x target", initiatives=[wl("Pricing and Packaging v2")]),
     "Senior AE stepped up to interim Head of Sales in July 2026 when the VP Sales left. Still carries a personal quota.",
     ["2026-10-09: First added (Intake interview, Exec)"], "Exec"),
    ("Hana Sato", dict(role="VP Customer Success", company=wl("Fernhollow"), depth="Full", mentions=8, context="Close to every top-20 account; first to see churn coming", cadence="Weekly", open_thread="Churn cohort analysis owed to the board by Nov 18", initiatives=[wl("Series C Readiness")]),
     "VP Customer Success. NRR fell from 112% in July to 106% in September. Owns the board's churn cohort ask and the Brightside renewal plan.",
     ["2026-10-09: First added (Intake interview, Exec)"], "Exec"),
    ("Daniel Reyes", dict(role="VP Finance", company=wl("Fernhollow"), depth="Full", mentions=7, context="Conservative on runway math; wants the raise started in January", cadence="Weekly", open_thread="Data room checklist for the Series C", initiatives=[wl("Series C Readiness")]),
     "VP Finance. Owns the metrics sheet, the board pack numbers, and the runway model. Runway is 17 months at September burn.",
     ["2026-10-10: First added (Intake interview, Exec)"], "Exec"),
    ("Rachel Stein", dict(role="Board director, Northgate Ventures", company=wl("Northgate Ventures"), depth="Full", mentions=4, context="Led the Series B; asks about retention before growth", cadence="Quarterly, plus monthly calls with Maya", open_thread="Asked for the churn cohort analysis at the Aug 19 board", initiatives=[wl("Series C Readiness")]),
     "Board director since the Series B (2025). Partner at Northgate Ventures.",
     ["2026-10-12: First added (Board pack, Aug 19)"], "Exec"),
]
people_rows = []
for name, f, cur, hist, _ in people:
    fields = dict(name=name, summary=f["context"][:90], aliases=[], **f, status="Active", last_updated=hist[0][:10], source="Intake, Oct 2026")
    fields["summary"] = {"Maya Okafor": "CEO; running the VP Sales search and the Series C",
                         "Theo Lindqvist": "Chief of Staff; reviewer; owns the Q1 hiring plan",
                         "Priya Raman": "CTO; v2 migration three weeks behind",
                         "Jordan Ellis": "VP Product; pricing page slipped twice",
                         "Marcus Bell": "Interim Head of Sales since July; still carrying quota",
                         "Hana Sato": "VP CS; owes the board the churn cohort analysis",
                         "Daniel Reyes": "VP Finance; runway 17 months; wants raise started in January",
                         "Rachel Stein": "Northgate director; asked for churn cohorts in August"}[name]
    record("Company/People", name, fields, cur, hist)
    people_rows.append([name, "", "Active", "Full", fields["summary"], fields["last_updated"], wl(name)])
catalog("Company/People", "People Catalog", ["Name", "Aliases", "Status", "Depth", "Summary", "Updated", "Link"], people_rows,
        "Active and Dormant records. Archived: `_catalog-archive.md`. ")

catalog("Company/People", "People Catalog", ["Name", "Aliases", "Status", "Depth", "Summary", "Updated", "Link"], people_rows,
        "Active and Dormant records. Archived: `_catalog-archive.md`. ")
for folder, title, header in [("Company/People", "People Catalog (Archive)", ["Name", "Aliases", "Status", "Depth", "Summary", "Updated", "Link"])]:
    write(f"{folder}/_catalog-archive.md", f"# {title}\nNo archived records yet.\n\n| " + " | ".join(header) + " |\n| " + " | ".join("---" for _ in header) + " |")

# ---------------------------------------------------------------- Companies
companies = [
    ("Fernhollow", "Other", "Series B, about 60 people", "Scheduling and dispatch software for home-service businesses", "Series C targeted to close by April 2027", "Our company", "The company this Cortex describes. Founded 2019. $7.75M ARR at Sept 30, 2026."),
    ("Northgate Ventures", "Investor", "Venture fund", "Led the Series B", "Rachel Stein wants the churn cohorts before discussing the C", "Lead Series B investor; board seat", "Led the 2025 Series B. Rachel Stein holds the board seat."),
    ("Brightside Home Services", "Customer", "Largest customer, 9% of ARR", "Plumbing and HVAC operator, 40 locations", "Renewal due Jan 31, 2027; asked for a price cut", "Largest customer; renewal at risk", "Largest account, 9% of ARR. Renewal Jan 31, 2027. Asked for 15% off and a dedicated CSM. Hana Sato sent the renewal plan on Oct 16: a dedicated CSM, no price cut, a two-year term at the current rate. Tracked as a Watching risk (Risks: Brightside concentration)."),
]
comp_rows = []
for name, rel, size, what, thread, summ, cur in companies:
    fields = dict(name=name, summary=summ, aliases=["Brightside"] if name.startswith("Bright") else [], relationship=rel, stage_or_size=size, what_they_do=what, open_thread=thread, depth="Full", mentions=5 if rel != "Other" else 20, people=[wl("Rachel Stein")] if name == "Northgate Ventures" else ([wl("Hana Sato")] if name.startswith("Bright") else []), related=[wl("Send Brightside a renewal plan"), wl("Brightside concentration")] if name.startswith("Bright") else [], status="Active", last_updated="2026-10-20", source="Intake, Oct 2026")
    record("Company/Companies", name, fields, cur, ["2026-10-06: First added (Intake)"])
    comp_rows.append([name, ", ".join(fields["aliases"]), "Active", "Full", summ, "2026-10-20", wl(name)])
catalog("Company/Companies", "Companies Catalog", ["Name", "Aliases", "Status", "Depth", "Summary", "Updated", "Link"], comp_rows,
        "Active and Dormant records. Archived: `_catalog-archive.md`. ")
write("Company/Companies/_catalog-archive.md", "# Companies Catalog (Archive)\nNo archived records yet.\n\n| Name | Aliases | Status | Depth | Summary | Updated | Link |\n| --- | --- | --- | --- | --- | --- | --- |")

# ---------------------------------------------------------------- Departments
depts = [
    ("Engineering", "Priya Raman", "Ship a reliable platform customers trust with their day", 16, ["Finish the v2 migration", "SOC 2 Type I", "Cut P1 incidents in half"], ["Product"], "Yellow", "Migration three weeks behind; on-call load high", [], "Eng"),
    ("Product", "Jordan Ellis", "Decide what we build and how we charge for it", 6, ["Pricing and packaging v2", "Mobile scheduling GA", "Discovery with top-20 accounts"], ["Sales", "Engineering"], "Yellow", "Pricing blocked on sales input", [], "Product"),
    ("Sales", "Marcus Bell", "Win new home-service operators at 20+ techs", 12, ["Rebuild pipeline coverage to 3.0x", "Hire a VP Sales", "Close 6 enterprise logos in Q4"], ["Product"], "Red", "No VP Sales since July; coverage 2.2x", ["Pipeline coverage"], "Sales"),
    ("Customer Success", "Hana Sato", "Keep and grow every account we win", 9, ["Get NRR back above 110%", "Renew Brightside", "Onboard in under 30 days"], ["Product", "Engineering"], "Yellow", "NRR down six points in two months", ["Net revenue retention", "Gross logo churn"], "CS"),
    ("Finance and Ops", "Daniel Reyes", "Keep the numbers true and the company funded", 5, ["Series C data room", "Close the books in 5 days", "Q1 hiring plan budget"], [], "Green", "On track", ["ARR", "Runway"], "Finance"),
]
dept_rows = []
for name, head, mission, hc, goals, deps, health, note, metrics, alias in depts:
    fields = dict(name=name, summary=f"{hc} people; {note if note[:2].isupper() else note[0].lower() + note[1:]}", aliases=[alias] if alias != name else [], head=wl(head), mission=mission, headcount=hc, top_goals=goals, metrics=[wl(m) for m in metrics], dependencies=[wl(d) for d in deps], health=health, health_note=note, visibility="Company", space="Company", status="Active", last_updated="2026-10-21", source="Intake interview and exec meeting Oct 20")
    hist = ["2026-10-21: Health set to " + health + " by " + ("Maya Okafor" if name == "Sales" else head) + " (exec meeting)", "2026-10-08: First added (Intake interview)"]
    record("Company/Departments", name, fields, f"{mission}. {hc} people, led by {head}. Goals: {'; '.join(goals)}. Health {health}: {note}.", hist)
    dept_rows.append([name, ", ".join(fields["aliases"]), "Active", wl(head), health, fields["summary"], "2026-10-21", wl(name)])
catalog("Company/Departments", "Departments Catalog", ["Name", "Aliases", "Status", "Head", "Health", "Summary", "Updated", "Link"], dept_rows)

# ---------------------------------------------------------------- Metrics + Values
metrics = [
    ("ARR", "Daniel Reyes", "Finance and Ops", "$", "Monthly", "Up is good", "$10.0M by 2027-06-30", [("2026-07-31", "7.40M"), ("2026-08-31", "7.60M"), ("2026-09-30", "7.75M")], "Exec", "arr"),
    ("Net revenue retention", "Hana Sato", "Customer Success", "%", "Monthly", "Up is good", "110% by 2026-12-31", [("2026-07-31", "112"), ("2026-08-31", "109"), ("2026-09-30", "106")], "Exec", "NRR"),
    ("Gross logo churn", "Hana Sato", "Customer Success", "% monthly", "Monthly", "Down is good", "Under 1.0% monthly", [("2026-07-31", "1.1"), ("2026-08-31", "1.4"), ("2026-09-30", "1.9")], "Exec", "logo churn"),
    ("Pipeline coverage", "Marcus Bell", "Sales", "x next-quarter target", "Monthly", "Up is good", "3.0x every month", [("2026-07-31", "3.1"), ("2026-08-31", "2.6"), ("2026-09-30", "2.2")], "Exec", "coverage"),
    ("Runway", "Daniel Reyes", "Finance and Ops", "months", "Monthly", "Up is good", "18 months or more until the Series C closes", [("2026-07-31", "19"), ("2026-08-31", "18"), ("2026-09-30", "17")], "Exec", "runway"),
]
met_rows = []
value_rows = []
for name, owner, dept, unit, cad, direction, target, vals, vis, alias in metrics:
    latest = f"{vals[-1][1]} ({vals[-1][0]})"
    prior = f"{vals[-2][1]} ({vals[-2][0]})"
    fields = dict(name=name, summary=f"{vals[-1][1]} {unit} at {vals[-1][0]}; target {target}", aliases=[alias] if alias.lower() != name.lower() else [], owner=wl(owner), department=wl(dept), unit=unit, cadence=cad, direction=direction, target=target, latest=latest, prior=prior, source_system="Finance metrics sheet" if dept == "Finance and Ops" else ("CRM report" if dept == "Sales" else "CS health dashboard"), visibility=vis, status="Active", last_updated="2026-10-10", source="Metrics sheet, Sept close")
    record("Exec/Metrics", name, fields, f"Owned by {owner}. Latest {latest}, prior {prior}. Target {target}.", ["2026-10-10: First added with July to September values (Metrics sheet)"])
    met_rows.append([name, ", ".join(fields["aliases"]), "Active", wl(owner), cad, fields["summary"], "2026-10-10", wl(name)])
    for d, v in vals:
        value_rows.append(f"| {name} {d} | {wl(name)} | {d} | {v} | {'Board pack, Aug 19' if d == '2026-07-31' else 'Metrics sheet, ' + ('Aug' if d.startswith('2026-08') else 'Sept') + ' close'} |")
catalog("Exec/Metrics", "Metrics Catalog", ["Name", "Aliases", "Status", "Owner", "Cadence", "Summary", "Updated", "Link"], met_rows)
write("Exec/Metric Values.md", "# Metric Values\nLog. One row per reading, newest at the bottom. No catalog.\n\n| Reading | Metric | Date | Value | Source |\n| --- | --- | --- | --- | --- |\n" + "\n".join(value_rows))

# ---------------------------------------------------------------- Company Commitments
commits = [
    ("Ship the pricing page", "Jordan Ellis", "Exec team", "Product", "2026-09-08", "2026-11-22", "Exec meeting 2026-09-08", 2, "Open", "Company", "Owner: Jordan Ellis | Due 2026-11-22 | slipped twice; waiting on enterprise tier input from Sales",
     "Public pricing page for the v2 packaging. Due moved twice because the enterprise tier needs a sales owner to sign off.",
     ["2026-10-21: Slipped. Due moved from 2026-10-31 to 2026-11-22; Times Slipped 2 (exec meeting, Granola)", "2026-10-06: Slipped. Due moved from 2026-10-03 to 2026-10-31 (exec meeting, Granola)", "2026-09-08: Made in the exec meeting, due 2026-10-03"]),
    ("Send the board the churn cohort analysis", "Hana Sato", "Board", "Customer Success", "2026-08-19", "2026-11-11", "Board 2026-08-19", 0, "Open", "Exec", "Owner: Hana Sato | Due 2026-11-11 | the board's open ask; in the Nov 18 pack",
     "Rachel Stein asked for logo and revenue churn by signup cohort at the August board. Due in the pack on Nov 11. Daniel is pulling the revenue side.",
     ["2026-10-15: Drafting; Daniel Reyes pulling revenue cohorts (CS weekly, Granola)", "2026-08-19: Made at the board meeting"]),
    ("Name two VP Sales finalists", "Maya Okafor", "Board", "Sales", "2026-08-19", "2026-11-15", "Board 2026-08-19", 1, "Open", "Exec", "Owner: Maya Okafor | Due 2026-11-15 | slipped once; search with the recruiter",
     "Board asked for finalists before the November meeting. Two candidates in late rounds.",
     ["2026-10-01: Slipped. Due moved from 2026-09-30 to 2026-11-15 (Maya, CEO intake)", "2026-08-19: Made at the board meeting"]),
    ("Deliver the Q1 hiring plan", "Theo Lindqvist", "Exec team", "Finance and Ops", "2026-10-13", "2026-11-20", "Exec meeting 2026-10-13", 0, "Open", "Company", "Owner: Theo Lindqvist | Due 2026-11-20 | needs each exec's headcount ask by Nov 6",
     "Headcount and budget by department for Q1, tied to the Series C plan.", ["2026-10-13: Made in the exec meeting"]),
    ("Kick off the SOC 2 Type I audit", "Priya Raman", "Customers", "Engineering", "2026-09-22", "2026-11-30", "Exec meeting 2026-09-22", 0, "Open", "Company", "Owner: Priya Raman | Due 2026-11-30 | auditor shortlist done",
     "Three enterprise prospects asked for SOC 2. Auditor shortlist done; kickoff by Nov 30.", ["2026-10-20: Auditor shortlist done (exec meeting, Granola)", "2026-09-22: Made in the exec meeting"]),
    ("Send Brightside a renewal plan", "Hana Sato", "Brightside Home Services", "Customer Success", "2026-09-29", "2026-10-17", "Brightside QBR 2026-09-29", 0, "Kept", "Company", "Owner: Hana Sato | Kept 2026-10-16 | renewal Jan 31",
     "Renewal plan sent Oct 16: dedicated CSM, no price cut, a two-year term at the current rate.", ["2026-10-16: Kept. Plan sent a day early (CS weekly, Granola)", "2026-09-29: Made at the Brightside QBR"]),
]
cc_company, cc_exec = [], []
for title, owner, to, dept, made, due, made_in, slipped, status, vis, line, cur, hist in commits:
    made_to = wl(to) if to in [p[0] for p in people] or to == "Brightside Home Services" else to
    fields = dict(title=title, summary=line.split("| ", 2)[-1], aliases=[], owner=wl(owner), made_to=made_to, department=wl(dept), made_on=made, due=due, made_in=made_in, times_slipped=slipped, visibility=vis, status=status, last_updated=hist[0][:10], source=hist[0].split("(")[-1].rstrip(")"))
    space = "Company" if vis == "Company" else "Exec"
    record(f"{space}/Company Commitments", title, fields, cur, hist)
    row = [title, "", status, wl(owner), due, fields["summary"], fields["last_updated"], wl(title)]
    (cc_company if space == "Company" else cc_exec).append(row)
hdr = ["Title", "Aliases", "Status", "Owner", "Due", "Summary", "Updated", "Link"]
catalog("Company/Company Commitments", "Company Commitments Catalog (Company)", hdr, [r for r in cc_company if r[2] != "Kept"], "Open records with Visibility Company. Kept and Dropped: `_catalog-archive.md`. ")
catalog("Exec/Company Commitments", "Company Commitments Catalog (Exec)", hdr, cc_exec, "Open records with Visibility Exec. ")
write("Company/Company Commitments/_catalog-archive.md", "# Company Commitments Catalog (Archive)\nKept and Dropped. Read only for history.\n\n| " + " | ".join(hdr) + " |\n| " + " | ".join("---" for _ in hdr) + " |\n" + "\n".join("| " + " | ".join(r) + " |" for r in cc_company if r[2] == "Kept"))

# ---------------------------------------------------------------- Org
org = [
    ("VP Sales", "", "CEO", "Sales", "2026-07-15", "Open", "Open since 2026-07-15; two finalists in late rounds", "Seat opened when the previous VP Sales left on 2026-07-15. Marcus Bell covers it as interim Head of Sales."),
    ("CEO", "Maya Okafor", "Board", "Finance and Ops", "", "Filled", "Maya Okafor; reports to the board", "Co-founder."),
    ("CTO", "Priya Raman", "CEO", "Engineering", "", "Filled", "Priya Raman; leads Engineering", "Co-founder."),
    ("Head of Sales (interim)", "Marcus Bell", "CEO", "Sales", "", "Filled", "Marcus Bell, interim since July; carries quota", "Interim seat until the VP Sales starts."),
]
org_rows = []
for role, holder, rt, dept, since, status, summ, cur in org:
    fields = dict(role=role, summary=summ, aliases=[], holder=wl(holder) if holder else "", reports_to=wl(rt) if rt != "Board" else "Board", department=wl(dept), open_since=since, scorecard="", status=status, last_updated="2026-10-09", source="Org chart, Oct 2026")
    record("Company/Org", role, fields, cur, ["2026-10-09: First added (Org chart)"])
    org_rows.append([role, "", status, wl(holder) if holder else "open", rt, summ, "2026-10-09", wl(role)])
catalog("Company/Org", "Org Catalog", ["Role", "Aliases", "Status", "Holder", "Reports To", "Summary", "Updated", "Link"], org_rows)

# ---------------------------------------------------------------- Board
board = [
    ("Board 2026-08-19", "2026-08-19", "Held", "Sent", "Asked: churn cohort analysis; VP Sales finalists by Sept 30", "None open", [wl("Send the board the churn cohort analysis"), wl("Name two VP Sales finalists")],
     "Q2 review. Board pushed on retention before growth and on the VP Sales gap.", "Held; two asks still open; see Follow-ups"),
    ("Board 2026-11-18", "2026-11-18", "Upcoming", "Drafting", "Open from August: churn cohorts; VP Sales finalists", "Intros to two Series C leads", [wl("Send the board the churn cohort analysis"), wl("Name two VP Sales finalists")],
     "Q3 review and Series C timing. Pack due Nov 11. Theo owns the prep calendar.", "Prep Drafting; pack due 2026-11-11; two open asks"),
]
b_rows = []
for meet, date, status, prep, ask_co, ask_bd, fu, cur, summ in board:
    fields = dict(meeting=meet, summary=summ, aliases=[], date=date, members=[wl("Maya Okafor"), wl("Rachel Stein")], asks_of_the_company=ask_co, asks_of_the_board=ask_bd, follow_ups=fu, pack="Board pack (data room)" if status == "Held" else "Due 2026-11-11", prep_status=prep, visibility="Exec", status=status, last_updated="2026-10-20", source="Board pack Aug 19; CoS intake")
    record("Exec/Board", meet, fields, cur, ["2026-10-20: Prep status Drafting (CoS)", "2026-10-07: First added (Intake interview, Chief of Staff)"] if status == "Upcoming" else ["2026-10-12: First added (Board pack)"])
    b_rows.append([meet, "", status, date, prep, summ, "2026-10-20", wl(meet)])
catalog("Exec/Board", "Board Catalog", ["Meeting", "Aliases", "Status", "Date", "Prep Status", "Summary", "Updated", "Link"], b_rows)

# ---------------------------------------------------------------- Risks
risks = [
    ("Runway under 12 months if the Series C slips", "Daniel Reyes", "Medium", "High", "No term sheet by 2027-03-01", "Start the raise in January; cut planned Q1 hires by half if February is slow", ["Series C Readiness", "Runway"], "Watching"),
    ("Sales leadership gap", "Maya Okafor", "High", "High", "No VP Sales signed by 2026-12-15", "Two finalists; interim Head of Sales; Maya joining enterprise deals", ["Sales", "Pipeline coverage"], "Active"),
    ("Brightside concentration", "Hana Sato", "Medium", "Medium", "Brightside signals non-renewal before 2026-12-31", "Renewal plan sent Oct 16; exec sponsor call booked", ["Brightside Home Services", "Net revenue retention"], "Watching"),
]
r_rows = []
for t, owner, lik, imp, trig, mit, rel, status in risks:
    fields = dict(title=t, summary=f"{status}; trigger: {trig}", aliases=[], owner=wl(owner), likelihood=lik, impact=imp, trigger=trig, mitigation=mit, related=[wl(x) for x in rel], visibility="Exec", status=status, last_updated="2026-10-21", source="CEO and VP Finance intake")
    record("Exec/Risks", t, fields, f"{mit}. Trigger: {trig}.", ["2026-10-21: First added (Intake)"])
    r_rows.append([t, "", status, wl(owner), imp, fields["summary"], "2026-10-21", wl(t)])
catalog("Exec/Risks", "Risks Catalog", ["Title", "Aliases", "Status", "Owner", "Impact", "Summary", "Updated", "Link"], r_rows)

# ---------------------------------------------------------------- Initiatives
inits = [
    ("Series C Readiness", "Exec", "Raise $25M to $30M by April 2027 to reach $15M ARR", "NRR trend and the VP Sales gap", "Daniel: data room checklist by Nov 14", "2026-09-01", "2027-04-30", ["Maya Okafor", "Daniel Reyes", "Theo Lindqvist"], "Raise prep; blocked by NRR trend and no VP Sales", ["Series C", "the C"]),
    ("Pricing and Packaging v2", "Company", "Annual contracts and an enterprise tier lift ACV", "Enterprise tier needs sales sign-off", "Jordan and Marcus: agree enterprise tier limits by Nov 7", "2026-08-15", "2026-11-30", ["Jordan Ellis", "Marcus Bell"], "Pricing page slipped twice; enterprise tier undecided", ["pricing v2"]),
    ("Platform v2 Migration", "Company", "Moves every customer off the legacy scheduler; required for SOC 2 and mobile", "On-call load; two engineers pulled to incidents", "Priya: revised cutover plan at the Nov 3 exec meeting", "2026-05-01", "2026-12-15", ["Priya Raman"], "Three weeks behind the Dec 15 target", ["v2", "migration"]),
]
i_company, i_exec = [], []
for name, vis, why, blk, nxt, start, target, owners, summ, aliases in inits:
    fields = dict(name=name, summary=summ, aliases=aliases, why_it_matters=why, blocker=blk, next_action=nxt, start=start, target=target, owner_involved=[wl(o) for o in owners], companies=[wl("Northgate Ventures")] if name.startswith("Series") else [], decisions=[], visibility=vis, status="Active", last_updated="2026-10-21", source="Exec meeting Oct 20, Granola")
    record(f"{vis}/Initiatives", name, fields, f"{why}. Blocker: {blk}. Next: {nxt}.", ["2026-10-21: Updated after the exec meeting (Granola)", "2026-10-08: First added (Intake)"])
    row = [name, ", ".join(aliases), "Active", summ, "2026-10-21", wl(name)]
    (i_company if vis == "Company" else i_exec).append(row)
ih = ["Name", "Aliases", "Status", "Summary", "Updated", "Link"]
catalog("Company/Initiatives", "Initiatives Catalog (Company)", ih, i_company)
catalog("Exec/Initiatives", "Initiatives Catalog (Exec)", ih, i_exec)

# ---------------------------------------------------------------- Decisions
decs = [
    ("Delay EU expansion to 2027 H2", "Protect runway into the Series C; localization not ready", "2026-09-15", ["Series C Readiness"], "Decided", "Exec"),
    ("Annual contracts become the default", "Lifts ACV and cuts churn risk; part of pricing v2", "2026-08-15", ["Pricing and Packaging v2"], "Decided", "Exec"),
]
d_rows = []
for t, reason, date, aff, status, vis in decs:
    fields = dict(title=t, summary=reason[:80], aliases=[], reasoning=reason, date=date, supersedes="", affects=[wl(a) for a in aff], visibility=vis, status=status, last_updated=date, source="Exec meeting, Granola")
    record("Exec/Decisions", t, fields, reason + ".", [f"{date}: Decided in the exec meeting"])
    d_rows.append([t, "", status, fields["summary"], date, wl(t)])
catalog("Exec/Decisions", "Decisions Catalog", ih, d_rows)

# ---------------------------------------------------------------- Inbox
record("Company/Inbox", "Possible duplicate - Marcus and Marc B", dict(title="Possible duplicate - Marcus and Marc B", summary="A Sales standup note names 'Marc B.'; likely Marcus Bell", aliases=[], content="Sales standup Oct 22 notes say 'Marc B. owns the enterprise tier call'.", suggested_collection="People", candidates=[wl("Marcus Bell")], date="2026-10-22", status="New", last_updated="2026-10-22", source="Dream, 2026-10-27"),
       "Waiting for the reviewer to confirm.", ["2026-10-27: Added by the dream"])
catalog("Company/Inbox", "Inbox Catalog", ih, [["Possible duplicate - Marcus and Marc B", "", "New", "Likely Marcus Bell; confirm", "2026-10-22", wl("Possible duplicate - Marcus and Marc B")]])

# ---------------------------------------------------------------- Pages
write("Company/Standing Context.md", """
# Standing Context

- Fernhollow sells scheduling and dispatch software to home-service businesses (plumbing, HVAC, electrical) with 20 to 200 technicians.
- Founded 2019 by Maya Okafor (CEO) and Priya Raman (CTO). About 60 people as of October 2026.
- Series B in 2025, led by Northgate Ventures. Series C targeted to close by April 2027.
- Customers buy on technician count. Annual contracts are the default from 2026-08-15.
- The exec team meets Mondays at 9am PT. Board meets quarterly.
- This Cortex is a fictional sample for testing Cortex skills. It describes no real company.
""")
write("Exec/Strategy.md", """
# Strategy

## Summary
Grow from $7.75M to $10M ARR by June 2027 with NRR back above 110%, then raise a Series C of $25M to $30M by April 2027 to reach $15M ARR. Win operators with 20+ technicians; stay in the US until 2027 H2.

## 2026-09-15: FY27 plan (board-approved Aug 19)
- Targets: $10M ARR by 2027-06-30, NRR 110% by year end, logo churn under 1% monthly.
- Bets: pricing and packaging v2, the v2 platform (SOC 2, mobile), and an enterprise motion led by a new VP Sales.
- Not doing: EU expansion before 2027 H2; self-serve under 10 technicians.
""")
write("Company/Dream Journal.md", """
# Dream Journal

## Questions for you
- [ ] Ship the pricing page: Due 2026-11-22 after two slips, both waiting on Sales. Worth naming one sales owner for the enterprise tier? (Company Commitments: Ship the pricing page). Reviewer: Theo Lindqvist
- [ ] "Marc B." in the Oct 22 Sales standup looks like Marcus Bell. Merge? (Inbox: Possible duplicate). Reviewer: Theo Lindqvist
- [ ] Gross logo churn has no October reading yet; the cadence comes due Oct 31. Who sends it? (Metrics: Gross logo churn). Reviewer: Theo Lindqvist

## Patterns
- Both commitments that slipped since September (the pricing page, twice; the VP Sales finalists, once) wait on a sales decision, and the Sales seat has been open since July. Seen 2 nights. (Inferred. Evidence: Ship the pricing page, Name two VP Sales finalists, exec meeting Oct 20.)

## 2026-10-28
Replayed 2 meetings (CS weekly, Sales standup). Updated 3 records, flagged 1 passed due date, added 1 Inbox item. Reviewed Departments A to S.

## 2026-10-27
Replayed the Oct 20 exec meeting. Superseded the pricing page Due date, added a History line to Platform v2 Migration, flagged the logo churn cadence. Reviewed People A to M.
""")
ingest = [
    ("Intake interview: Maya Okafor (CEO)", "Document", "2026-10-06", "People 3, Initiatives 2, Risks 2, Company Commitments 1"),
    ("Intake interview: Theo Lindqvist (Chief of Staff)", "Document", "2026-10-07", "Board 1, Company Commitments 1, Standing Context"),
    ("Intake interviews: Priya Raman, Jordan Ellis (Exec)", "Document", "2026-10-08", "Departments 2, Initiatives 2, Company Commitments 2"),
    ("Intake interviews: Marcus Bell, Hana Sato, Daniel Reyes (Exec)", "Document", "2026-10-10", "Departments 3, Metrics 5, Risks 1"),
    ("Board pack 2026-08-19", "Document", "2026-10-12", "Board 1, People 1, Metric Values 5"),
    ("Metrics sheet, Sept close", "Document", "2026-10-10", "Metric Values 10, Metrics 5"),
    ("Granola: Exec meeting 2026-10-20", "Meeting Notes", "2026-10-21", "Company Commitments 2, Departments 5, Initiatives 3"),
    ("Dream 2026-10-27", "Dream", "2026-10-27", "1 superseded, 1 flagged, 1 Inbox"),
    ("Dream 2026-10-28", "Dream", "2026-10-28", "3 updated, 1 flagged"),
]
write("Company/Ingest Log.md", "# Ingest Log\n\n| Source | Type | Date Ingested | What Changed |\n| --- | --- | --- | --- |\n" + "\n".join(f"| {a} | {b} | {c} | {d} |" for a, b, c, d in ingest))

for member in ["Maya Okafor", "Theo Lindqvist", "Priya Raman", "Jordan Ellis", "Marcus Bell", "Hana Sato", "Daniel Reyes"]:
    write(f"Private/{member}/README.md", f"# {member}: private space\n\nOnly {member} can open this folder. It holds their One-on-Ones Team records, Founder OS reflections and commitments, and private notes. The sample leaves it empty on purpose: nothing private belongs in a sample, and no skill should ever read it for anyone else.")

# ---------------------------------------------------------------- Map
write("Cortex Map.md", f"""
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

Records: People 9, Companies 3, Departments 5, Initiatives 3, Company Commitments 6 (5 open), Org 4, Decisions 2, Metrics 5, Board 2, Risks 3. Metric Values 15 rows. Inbox: 1 waiting. Map rebuilt {TODAY}.

## Field map
none
""")
print("done")
