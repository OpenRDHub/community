---
id: KH-PLAN-20260928
lang: en
type: proposal
title: Community records and operations proposal
summary: Responsibilities across WeChat groups, Feishu, GitHub, and the website, with a two-week trial.
date: '2026-09-28'
updated: '2026-09-28'
status: draft
visibility: public
publication: pending
authority: github
example: false
editor: unassigned
reviewer: unassigned
source: local-proposal
source_revision: local-draft-2026-09-28
---

[简体中文](plan.md) · **English**

# Community Records and Operations Proposal

**For discussion · 2026-09-28 · Not an adopted community decision**

Keep everyday discussion in WeChat groups and use Feishu for collaborative drafting. Preserve useful process records and agreed outcomes in GitHub, and generate one searchable documentation website. Establish the workflow before automating document imports.

## 1. Preserve the organization homepage

Use the original organization README as the base. Retain the story, images, project content and section order. This iteration corrects the organization badge, intake labels and Follow destination and explains handling ownership. Retain the existing brand, history, principles, projects, collaboration model, contributor roles, partnerships, and joining routes. Add a section linking community participation and the library. Our current focus on community infrastructure does not redefine the whole organization. Existing figures and project statuses require reporting dates and maintainer verification.

## 2. Responsibilities

| Place | Responsibility | Avoid duplicate work |
|---|---|---|
| WeChat groups | Everyday discussion, questions, differing views, and coordination | Curate useful topics rather than copying every message |
| Feishu documents | Collaborative drafts, meeting notes, review of discussion summaries, and working materials | Simple records can go directly into a GitHub PR without a separate Feishu document |
| GitHub community | Versioned records, curated discussions, decisions, PR review, and actionable issues | Keep each action in one issue and link to its status |
| Documentation website | Reading, categories, full-text search, recent updates, sources, and related work | Generate from repository Markdown rather than a second article database |

Static pages can display and link to work. Saving changes requires GitHub PRs or the Feishu drafting workflow. Do not put repository credentials in frontend code or describe a static site as a collaborative editing backend.

## 3. Records to preserve

| Material | Record | Completion check |
|---|---|---|
| Daily files and references | A dated intake list; separate documents for substantial material | Source, date, purpose, and access scope are clear; no empty daily reports |
| Meetings | Context, main points, agreement, disagreement, open questions, and actions | A participant checks accuracy; absence of a decision remains explicit |
| WeChat discussions | One record per topic, with follow-ups, a group alias, and the discussion date range | Separate quotations, the editor's interpretation, and confirmed agreement |
| Decisions | Rationale, effect, confirmation method, effective date, and replacement links | Readers can trace how and why a decision was made |
| Guides, SOPs, and FAQs | Maintained instructions linked to their discussion history | A newcomer can follow the current instructions without reading every historical message |
| Attachments | Small distributable files with the record; controlled links for restricted or large files | Linked images and files are accessible; an external link is not a complete backup |

Drafts are useful records too. Merging a PR accepts the record into the library; it does not automatically approve the proposal described inside it.

## 4. Daily workflow

1. Register an authorized source document, revision, or export, or a WeChat discussion topic, date range, and necessary excerpts. People without Git experience can hand materials to an intake contact.
2. Prepare a record with a stable ID, source revision, summary, disagreements, open questions, and next steps. Participants may draft a WeChat summary together in Feishu or submit Markdown directly; individual message links are not required.
3. Ask the source owner to check accuracy and a records maintainer to check links and access scope. Confirm that attributed comments may be shared with the intended audience.
4. Open a PR showing the changes. The same source revision should not generate duplicate PRs; update an existing record in place.
5. Merge and regenerate the website and search index. Show the actual document revision date, not the build time.
6. Create issues for agreed actions. Keep status in the issue and link it from the record. Add outcomes and contribution credit later. The editor posts the record link and open questions back to the original WeChat group, within the record’s access scope, so participants can check and continue the work.

Proposed trial cadence: one intake batch on staffed workdays, meeting notes within two working days, and a weekly review of pending records and broken links. Confirm people and availability before making any service commitment.

## 5. One authoritative version per document

WeChat is a discussion source. The edited document has an authoritative version. Add later discussion to the same topic record for review rather than silently replacing previous decisions.

- During Feishu drafting, Feishu is authoritative and GitHub stores labeled snapshots. Feed suggested edits back to the source before importing the next revision.
- For maintained guides and decisions, GitHub becomes authoritative. Add a pointer in the Feishu original and make further changes through PRs.
- Record any handover with its date and reciprocal links. If both sides changed, stop automatic overwrite and resolve the differences in a PR.

Keep metadata and text together in Markdown. Generate indexes instead of maintaining parallel tables. Daily records can start in Chinese; translate stable entry points, rules, and important decisions first. Label missing or outdated translations rather than blocking routine intake.

## 6. Repository and website

```text
OpenRDHub/.github
  profile/README.md
  profile/README.en.md

OpenRDHub/community        # Changed to PUBLIC on 2026-09-28 under user instruction
  README.md
  docs/knowledge/
  records/meetings/2026/
  records/discussions/2026/
  records/decisions/
  records/updates/2026/
  templates/
  docs/
  site/                    # Reads the same Markdown sources
```

Community-wide material belongs here; implementation material stays in the project repository and is linked from the library. Do not duplicate all text in another website repository or expand the collaboration platform for this first iteration.

Metadata should include a stable ID, title, type, event date, revision date, record status, visibility, publication eligibility, source and revision, authority, editor/reviewer roles, and related records.

The first website offers category and full-text search, recent updates, status labels, sources, source downloads, related records, and templates. Real editing links lead to GitHub or Feishu; the local prototype demonstrates the intended reading and intake routes.

## 7. Archiving and publication are separate

GitHub storage does not mean public distribution. WeChat originals stay within the original conversation audience. Store necessary excerpts or attachments in restricted documents when agreed. Patient or identity information remains in access-controlled locations. If internal Git backups are needed, use a separately restricted repository; an `internal/` directory in a public repository is not an access boundary.

community is now PUBLIC under explicit user instruction; its files and history are publicly readable. Keep non-public source material in a separate access-controlled location. Website publication metadata does not restrict GitHub access. A public build must filter pages, search indexes, source downloads, attachments, and ZIP files to reviewed, explicitly publishable content.

GitHub Pages serves static websites. A private repository does not itself make the website private; private Pages access control has GitHub Enterprise Cloud requirements. The repository is now publicly readable, while the website remains a local preview. Choose hosting for approved website content according to the actual plan. [GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages) · [Pages access control](https://docs.github.com/en/enterprise-cloud@latest/pages/getting-started-with-github-pages/changing-the-visibility-of-your-github-pages-site)

## 8. Two-week trial

| Stage | Action | Observe |
|---|---|---|
| Week 1 | Confirm an intake contact and reviewer; process 5–10 authorized historical documents manually | Sources are traceable, drafts are not mistaken for decisions, and people without Git can contribute |
| Week 2 | Process one real meeting and one WeChat discussion; update an existing record; ask a newcomer to find information | Prior conclusions and open questions are findable, no duplicate records appear, and actions have a destination |
| After the trial | Consider one-way imports and draft PRs for an explicitly authorized Feishu folder | Repeated runs are idempotent; failures are recorded; conflicting edits stop overwrites; revisions remain traceable |

Feishu supports Markdown exports, but comments are not exported with the body. Move important review conclusions into the text and check image and attachment links. [Markdown export](https://www.feishu.cn/content/article/7644456827538820052)

Participants curate WeChat discussions by topic, recording a group alias, date range, key views, disagreements, and open questions. Retain necessary excerpts or screenshots in a restricted location when needed for review, and ask the relevant participants to check the summary. If no shareable original link is available, use a source description and contact role. Do not invent message links or describe a summary as a complete chat backup. This proposal does not depend on automatically reading WeChat messages; any later automation starts with curated Feishu documents or Markdown.

Credit editing, review, translation, intake, and maintenance as contributions. Offer attribution, reusable portfolio work, feedback, and progressively larger responsibilities. Funding or employment opportunities require actual resources and separate agreements.

## 9. Questions for community discussion

1. Does the WeChat discussion–Feishu drafting–GitHub records–website reading workflow fit how people work?
2. Who can help with intake and review, and with what availability?
3. Which initial documents may be used, and which must remain internal?
4. Does preserving the current homepage while adding community and library routes make sense?

This delivery is a local proposal and clickable preview. It has not connected to WeChat or Feishu, created repositories, published a website, or changed any existing access settings.
