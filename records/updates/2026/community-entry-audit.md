---
id: KH-ENTRY-20260928
lang: zh
type: daily
title: 三条参与路径检查与主页交接
summary: 补齐参与、需求和资源入口，修正访问说明，提供已校验的组织主页修改包。
date: '2026-09-28'
updated: '2026-09-28'
status: pending-review
visibility: internal
publication: pending
authority: github
example: false
editor: Codex
reviewer: unassigned
source: User-authorized community setup and live GitHub repository inspection
source_url: https://github.com/OpenRDHub/community/issues/3
source_revision: community-entry-audit-2026-09-28-v1
---

# 三条参与路径检查与主页交接

对应 [C01 / Issue #3](https://github.com/OpenRDHub/community/issues/3)。本记录由 Codex 根据用户授权完成，记录实际检查和修订；独立评审尚待确认，不代表已落实社区接待人。

## 检查范围与结果

| 路径 | 查到的问题 | 本轮修订 | 还缺什么 |
|---|---|---|---|
| 参与社区 | 私有仓库指南未说明访问条件；只有描述，没有清楚的参与入口 | 补充已有 Issue、社区建议模板和试行讨论链接，区分仓库权限与组织成员身份 | 公开申请入口及接待人 |
| 提出需求 | 说明页没有提交按钮；内部登记与个人账号下的公开入口容易混淆 | 补充中英文需求模板入口、查重、项目归属和已有 Issue 的处理方式 | 是否继续使用既有公开需求池、由谁分拣 |
| 提供或申请资源 | 说明页没有提交入口，也没有已确认接待者 | 补充资源模板入口，要求区分提供与申请、说明条件和有效期 | 接待人和真实可用资源 |
| 入口归属表 | 链接到尚未上线的 `.github/CONTRIBUTING.md` | 改为现有公开组织主页和私有社区贡献说明 | 有权限者合入公开贡献指南 |
| 主页修改稿 | 仍写 community 尚未发布，部分私有入口缺少权限提示 | 说明私有仓库已建立、主页稿尚待合入，为成员入口补权限提示 | `.github` 写权限或维护者协助 |

## 保留原有主页与仓库归属

线上组织主页的介绍、数据、项目、共建者和合作内容保留。个人账号下的需求池和 OpenRare 上游仍按实际归属标明，不把它们伪装成 OpenRDHub 内部仓库。community 的 Issue、PR、Discussion 和资料继续留在 community。

当前公开主页基准提交：`b73f5a4387b390ccde3074b515add470a07a7b74`。线上 README 与本地修改包的基准文件一致。修改包包含中英文主页、公开贡献说明、默认任务与 PR 模板，共六个文件。

[下载组织主页修改包（需 community 权限）](https://github.com/OpenRDHub/community/raw/refs/heads/main/handoff/organization-profile.patch)

## 有写权限的维护者怎样应用

在 `.github` 仓库最新默认分支上创建工作分支，下载上面的修改包到本地，再执行：

```sh
git apply --check /path/to/organization-profile.patch
git apply /path/to/organization-profile.patch
git diff --check
git diff
```

检查原内容保留、组织内外归属、私有链接标记和中英文入口后，再提交 PR。若基准已经变化或检查不通过，先对照差异调整。此包只包含主页与贡献规则，不包含 community 内部记录；仓库与看板可见性不随它改变。

## 需要实际参与者补充

在[试行讨论](https://github.com/OpenRDHub/community/discussions/9)说明愿意接待或评审的范围、可用时间、所需支持和希望获得的成果认可；C01 的具体反馈留在原 Issue。没有本人回复时，不安排值班、检查日期或资源承诺。

对外入口建议先在现有公开 `.github` 提供参与说明；community 暂时保留私有协作资料。具体公开联络方式和接待者仍需确认，当前没有新增公开表单或收件人。

## 核验边界

- 已读取线上组织 README、仓库权限和六份中英文 Issue 模板，修订链接对应真实模板文件。
- 修改包在当前公开 README 的干净副本上通过 `git apply --check`。
- 未提交测试需求、未导入微信或飞书原文、未指定他人为接待者。
- C01 已有检查交付，仍待独立评审及公开主页落地；不提前关单，也不把技术修订视作完整的社区接待试行。
