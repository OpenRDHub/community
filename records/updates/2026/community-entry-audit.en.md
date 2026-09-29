---
id: KH-ENTRY-20260928
lang: en
type: daily
title: Three-route audit and profile handoff
summary: Repair participation, needs and resource routes; clarify access and prepare a checked profile patch.
date: '2026-09-28'
updated: '2026-09-28'
status: pending-review
visibility: public
publication: pending
authority: github
example: false
editor: Codex
reviewer: unassigned
source: User-authorized community setup and live GitHub repository inspection
source_url: https://github.com/OpenRDHub/community/issues/3
source_revision: community-entry-audit-2026-09-28-v1
---

> Update (2026-09-29): access blockers are resolved, the profile is live, the board is public, and organization Discussions uses community. The historical findings below are not a current to-do list. See the [completion record](community-unblocked.en.md).

# Three-route audit and profile handoff

> Follow-up (2026-09-28): community has been changed to PUBLIC under explicit user instruction. The findings below describe the earlier private state. Repository access requests are no longer needed; intake and review roles remain open. The linked profile patch now reflects public visibility; the board remains private.

This is a deliverable for [C01 / Issue #3](https://github.com/OpenRDHub/community/issues/3). Codex performed the checks and edits under user authorization. Independent review and community intake roles remain unconfirmed.

| Route | Finding | Repair | Still open |
|---|---|---|---|
| Participation | Access requirements and next actions were unclear | Link original Issues, proposal templates and the trial discussion; distinguish repository access from organization membership | Public access request route and contacts |
| Needs | No direct submission route; internal and existing public intake were mixed | Link localized templates, duplicate checks and project ownership guidance | Future owner and triage of the existing public needs tracker |
| Resources | No direct submission route or confirmed contact | Link localized resources templates and explain offers, requests and conditions | Intake contact and real confirmed resources |
| Routing table | Linked to a public CONTRIBUTING file that is not yet online | Link existing organization and community guidance | An authorized maintainer to publish the public guide |
| Profile draft | Claimed community was unpublished and left some access labels unclear | Mark the existing private repository and pending profile update accurately | Write access to `.github` or maintainer assistance |

## Profile handoff

The existing organization narrative, statistics, project descriptions, contributors and collaboration content are preserved. The personal-account needs tracker and OpenRare upstream remain explicitly identified. Community Issues, PRs, Discussions and records stay in community.

The current public profile baseline is `b73f5a4387b390ccde3074b515add470a07a7b74`. Its README matches the saved baseline. The six-file patch contains Chinese and English profiles and public contribution guides, plus default task and PR templates.

[Download the profile patch](https://github.com/OpenRDHub/community/raw/refs/heads/main/handoff/organization-profile.patch)

An authorized maintainer can create a branch from the latest `.github` default branch and run:

```sh
git apply --check /path/to/organization-profile.patch
git apply /path/to/organization-profile.patch
git diff --check
git diff
```

Review preserved content, ownership, access labels and language routes before submitting a PR. Reconcile newer upstream changes if the check fails. The patch contains profile and contribution guidance, not private community records; repository and board visibility do not change.

## Human arrangements

Use the [trial discussion](https://github.com/OpenRDHub/community/discussions/9) to state scope, availability, support needs and desired credit. Keep C01 feedback on its original Issue. No one is assigned support duties or dates without their agreement.

The proposed public entry is participation guidance in the existing public `.github` repository, with community remaining private for now. A public contact still needs confirmation; no new public form or recipient has been created.

## Verification limits

- Read the live profile, permissions and all six localized Issue templates; submission links reference existing template files.
- The patch passed `git apply --check` against a clean copy of the current public README.
- No test needs, WeChat or Feishu imports, or assignments to other people were created.
- C01 has an audit deliverable but remains open for independent review and public-profile rollout. Technical repairs do not complete the real community intake trial.
