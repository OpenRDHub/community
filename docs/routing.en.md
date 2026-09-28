[简体中文](routing.md) · **English**

# Entry points and ownership

Verified on 2026-09-28. Choose the handling location by the work involved. A maintainer is not an on-call contact until they agree.

| Work | Entry / owner | PR destination | Access and handling |
|---|---|---|---|
| Organization profile | [OpenRDHub](https://github.com/OpenRDHub) / [.github](https://github.com/OpenRDHub/.github) | .github | Public; the current account has no write access. A patch is prepared for an authorized maintainer. |
| Public guidance | [Proposed guide](https://github.com/OpenRDHub/.github/blob/main/CONTRIBUTING.en.md) | .github | Not merged yet; use the existing profile, known group contact or project README for now. |
| Community guides, records, operations | [community content](../README.en.md) | community | Created PRIVATE; authorized readers only. External visitors need a public entry. Contacts remain unconfirmed. |
| Needs without a project | [Khub-OpenRD/rare-disease-list](https://github.com/Khub-OpenRD/rare-disease-list/issues) | The selected project | Existing personal-account intake; continued ownership and triage remain to be confirmed. |
| A known project's bug or feature | [Project directory](projects.en.md) | That project | Follow its guidance; do not duplicate tasks in community. |
| OpenRare upstream work | [Upstream Issues](https://github.com/OpenRare2026/OpenRare/issues) / [PRs](https://github.com/OpenRare2026/OpenRare/pulls) | OpenRare2026/OpenRare | Public upstream; Issues are disabled in the organization fork. |
| Organization-wide work | [Organization Projects](https://github.com/orgs/OpenRDHub/projects) | Original repositories | A [private community board](https://github.com/orgs/OpenRDHub/projects/1) now tracks community work. The local organization view remains a snapshot of public items. |
| Open-ended discussion | [Repository discussions](discussions.en.md) | The document's repository | Repository Discussions is enabled and private. Organization Discussions still needs an agreed source repository and audience. |

## Relating Issues and PRs

Link an existing task when available. Explain the source, output and acceptance for substantial changes. Small independent fixes may go directly to a PR.

A cross-project parent item links to project tasks. Implementation PRs close only completed child tasks; keep the parent open until overall acceptance. The default branch is not necessarily main. Cross-repository closing syntax is `Closes OWNER/REPO#123`; default-branch rules and the repository setting apply.

Use full Markdown links in documentation. Profile changes belong in .github; community documents belong in community. Link across them where needed.

Before opening tasks for participation, confirm the handler, review contact and next check-in. Keep unconfirmed roles unassigned.

[Working pilot](pilot.en.md) · [Maintainer roles](../MAINTAINERS.en.md)
