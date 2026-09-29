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
lang: zh
title: 社区公开入口与权限卡点处理
summary: 看板公开、主页上线、组织讨论复用 community，并同步双语文档与本地预览。
---

# 社区公开入口与权限卡点处理

对应 [C01 / Issue #3](https://github.com/OpenRDHub/community/issues/3)。本记录记述按用户指示实施的技术变更，不代表社区已通过全部治理提案或已确认接待分工。

## 已完成

- 权限核验：mattheliu 已是 OpenRDHub Owner，对 .github 和 community 均有管理权限。未修改其他成员权限。
- [Project #1](https://github.com/orgs/OpenRDHub/projects/1) 已公开，README 已移除私有说明；看板仍引用 community 原 Issue，公开阅读不等于开放编辑。
- [组织 Discussions](https://github.com/orgs/OpenRDHub/discussions) 已启用，源仓库为 community；现有讨论 #9 显示在组织入口，无需复制讨论。
- [组织主页 PR #1](https://github.com/OpenRDHub/.github/pull/1) 已合入，保留原介绍、数据、项目、合作内容，新增中英文指南及 Issues、PR、讨论、看板、资料、资源入口。
- 原来误指向 Khub-OpenRD 的组织主入口已修正为 OpenRDHub。既有需求池和 OpenRare 上游仍按实际归属标记。
- community 当前指南、任务链接、预览快照同步公开状态；历史检查记录注明后续结果，旧交接补丁标为已被合入版本替代。
- 原讨论 #9 已同步公开状态与已完成事项，删除过时的私有和权限不足说明，继续保留待确认的实际分工。

## 核验

设置页面显示 Project 为 Public、组织 Discussions 设置成功。正式主页可看到新增入口，主分支合并提交为 `c31fea7ea8cd35da5f6d3559931fad6df231fced`。10 个主要入口匿名访问均返回 HTTP 200；6 份主页快照与已发布源文件一致。双语预览构建通过，共生成 100 个页面、处理 78 份分语言 Markdown；现有回归测试、链接与资料收录校验通过。

## 剩余工作的接续入口

| 所需信息或行动 | 接续位置 |
|---|---|
| 另一位伙伴复核参与、需求、资源入口 | [Issue #3](https://github.com/OpenRDHub/community/issues/3) |
| 自愿承担接待、评审、需求分拣的范围与时间 | [讨论 #9](https://github.com/OpenRDHub/community/discussions/9) |
| 一份适合收录的真实会议或微信群整理稿 | [资料收录约定](../../../docs/knowledge/record-policy.md) |
| 提供方确认的支持内容、条件与有效期 | [资源协作说明](../../../docs/resources.md) |

未分配未经本人确认的职责，未导入微信或飞书原文，未把技术修订视作项目交付。网页继续本地预览；公开部署不是本次变更。当前可直接通过公开仓库、讨论区和看板开展协作。
