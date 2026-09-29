---
id: KH-UNBLOCK-20260929
type: daily
date: '2026-09-29'
updated: '2026-09-29'
status: pending-review
visibility: public
publication: approved
authority: github
example: false
editor: Codex
reviewer: unassigned
source: User-authorized GitHub settings and profile publication
source_url: https://github.com/OpenRDHub/.github/pull/1
source_revision: c31fea7ea8cd35da5f6d3559931fad6df231fced
lang: en
title: Community access and entry points completed
summary: Publish the board and profile, connect organization Discussions to community,
  and synchronize bilingual documentation and local previews.
---

# Community access and entry points completed

Related to [C01 / Issue #3](https://github.com/OpenRDHub/community/issues/3). This record describes user-authorized technical changes. It does not imply community approval of governance proposals or confirmed staffing.

## Completed

- Verified mattheliu as an OpenRDHub Owner with admin access to .github and community. Other members' permissions were not changed.
- Made [Project #1](https://github.com/orgs/OpenRDHub/projects/1) public and corrected its README. It still references original community Issues; public reading does not grant editing.
- Enabled [organization Discussions](https://github.com/orgs/OpenRDHub/discussions) with community as its source. Existing discussion #9 appears at the organization entry without being copied.
- Merged [profile PR #1](https://github.com/OpenRDHub/.github/pull/1), preserving the original introduction, statistics, projects, and partnership content while adding bilingual guides and collaboration links.
- Corrected the organization home link from Khub-OpenRD to OpenRDHub. The existing personal-account needs tracker and OpenRare upstream remain explicitly identified.
- Synchronized current guides, task links, and preview snapshots. Added updates to historical records and marked the old handoff patch as superseded.
- Updated the original discussion #9 to reflect public access and completed changes, while keeping real staffing decisions open.

## Verification

The settings UI confirmed Public for the Project and successful organization Discussions setup. The live organization profile shows the new links; its merge commit is `c31fea7ea8cd35da5f6d3559931fad6df231fced`. All 10 principal entry points returned HTTP 200 anonymously, and all 6 profile snapshot files matched the published sources. The bilingual build passed, generating 100 pages from 78 localized Markdown documents. Existing regression tests, link checks, and record-ingestion checks passed.

## Real participant follow-up

| Input or action | Continue here |
|---|---|
| Independent review of participation, needs, and resource routes | [Issue #3](https://github.com/OpenRDHub/community/issues/3) |
| Voluntary support, review, and triage availability | [Discussion #9](https://github.com/OpenRDHub/community/discussions/9) |
| One real meeting note or edited WeChat topic for archiving | [Record policy](../../../docs/knowledge/record-policy.en.md) |
| Provider-confirmed support, conditions, and expiry | [Resource guide](../../../docs/resources.en.md) |

No unconfirmed responsibilities were assigned, no WeChat or Feishu source material was imported, and technical changes were not counted as project delivery. Website preview remains local; public website deployment is separate. The public repository, discussions, and board are available for collaboration now.
