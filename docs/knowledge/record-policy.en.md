---
id: KH-GUIDE-20260928
lang: en
type: guide
title: Record policy
summary: How to maintain record status, source revisions, authority, and follow-up
  actions.
date: '2026-09-28'
updated: '2026-09-28'
status: draft
visibility: internal
publication: pending
authority: github
example: false
editor: unassigned
reviewer: unassigned
source: local-proposal
source_revision: local-draft-2026-09-28
---

[简体中文](record-policy.md) · **English**

# Record Policy

**Proposed working agreement, pending community discussion.**

## Preserve the process without inventing agreement

Meetings and WeChat discussions may be archived before they reach a conclusion. Separate what was discussed, what was confirmed, and what remains unresolved. Do not turn an editor's interpretation into another person's commitment.

Draft, awaiting review, reviewed, and superseded describe the record. Whether a proposal was adopted is a separate question. A decision needs confirmation evidence and a date; merging an archival PR does not adopt a proposal.

## Metadata

| Field | Convention |
|---|---|
| ID | Stable identifier for links and deduplication |
| Type | Meeting, discussion, decision, daily materials, proposal, or reference |
| Dates | Event date and actual last revision date |
| Source | Feishu document and revision, or WeChat group alias, discussion dates, and summary revision; use a source description and contact role when no shareable link exists; respect the intended audience |
| Authority | Feishu or GitHub; make changes in that authoritative source |
| Editor and reviewer | Actual contributors; leave unconfirmed roles unassigned |
| Record status | Draft / awaiting review / reviewed / superseded |
| Visibility | Internal / public-eligible; missing values default to internal |
| Publication | Explicit permission to include the record in public output |
| Related work | Discussions, decisions, documents, PRs, and actionable issues |

## Common cases

- A new Feishu revision updates the existing record, revision metadata, and change note.
- A discussion spanning several days stays in one topic record unless it introduces a separate issue.
- Three agreed actions become three issues. Link to them rather than maintaining another progress list in the minutes.
- A replacement decision gets a new record. Mark and link the older record as superseded while preserving the rationale.
- A source link alone means registered, not fully archived or synchronized.
- Restricted images and attachments keep an access note. Mark archival completion only after authorized copying and verification.
- Withdrawing public content requires addressing published pages, download copies, repository history, and caches; deleting the current file does not erase history.

- When a WeChat discussion has no shareable original link, record a group alias, date range, and contact role. Keep necessary excerpts or screenshots restricted for review; do not invent links.
- After review, post the summary link and open questions back to the original group. Add follow-ups to the same record.

## Contributions

People without Git can give an edited draft to an intake contact. People using Git can open a PR from a template. Credit remains with the actual contributors. A weekly digest can link newly added, updated, and pending records.

Templates and examples are stored in the private community repository; policies remain subject to community review. There is no live source-material import queue, scheduled synchronization, or assigned records contact.

## Template ingestion and validation

Copy a template into records/, complete YAML and replace REPLACE-ME, dates and source revision. Missing/invalid fields fail validation. Templates are not indexed. Single-language records show an original-language notice in the other interface.

`status`: draft / pending-review / reviewed / superseded; `authority`: github / feishu; `visibility`: internal / public / restricted; `publication`: pending / approved / published.

Optional source_url and authority_url must be audience-appropriate http(s) URLs. Publication metadata does not publish a site.
