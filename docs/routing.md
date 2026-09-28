**简体中文** · [English](routing.en.md)

# 入口与处理归属

核验日期：2026-09-28。先按事项找处理位置。接待人没有明确答应前，不能把仓库维护者直接写成值班人。

| 事项 | 当前入口与归属 | PR 接收位置 | 可见范围与接待 |
|---|---|---|---|
| 了解组织、修改主页 | [OpenRDHub](https://github.com/OpenRDHub) / [.github](https://github.com/OpenRDHub/.github) | .github | 公开；当前执行账号没有写权限，修改包交有权限维护者处理 |
| 公共参与说明 | [组织贡献说明草案](https://github.com/OpenRDHub/.github/blob/main/CONTRIBUTING.md) | .github | 该文件尚待合入；目前从组织主页、现有群联络或项目 README 进入 |
| 社区指南、纪要、公共事务 | [community 内容](../README.md) | community | 已创建为 PRIVATE；获授权人员使用，外部访客先走公开接待入口；接待人待确认 |
| 尚未归属项目的真实需求 | [Khub-OpenRD/rare-disease-list Issues](https://github.com/Khub-OpenRD/rare-disease-list/issues) | 依分拣结果进入项目 | 个人账号下的既有公开入口；是否继续作为统一需求池及谁分拣待确认 |
| 明确属于项目的功能或问题 | [项目目录](projects.md)列出的对应入口 | 该项目仓库 | 以项目当前说明为准；不重复在 community 开同义任务 |
| OpenRare 上游贡献 | [上游 Issues](https://github.com/OpenRare2026/OpenRare/issues) / [PR](https://github.com/OpenRare2026/OpenRare/pulls) | OpenRare2026/OpenRare | 公开上游；组织 fork 未开启 Issues |
| 查看整个组织的工作 | [组织 Projects](https://github.com/orgs/OpenRDHub/projects) | 原 Issue/PR 仓库不变 | [私有社区看板](https://github.com/orgs/OpenRDHub/projects/1)已建；只管理 community 事项。本地组织视图仍为公开条目快照 |
| 开放讨论 | [社区讨论区](discussions.md) | 文档修改发目标仓库 PR | community 仓库 Discussions 已启用且私有；组织级入口仍待确认源仓库和受众 |

## Issue 与 PR 怎样对应

已有任务就链接原任务。大的修改说明来源、答疑人、产出和验收；独立文字修正可直接发 PR，不要求先建 Issue。

跨项目总事项保留子任务链接；实现 PR 只自动关闭已完成的子任务，总事项由验收人确认。默认分支不一定叫 main。跨仓关闭示例为 `Closes OWNER/REPO#123`，需符合默认分支与仓库自动关单设置。

文档编号用完整 Markdown 链接，不只写 `#123`。组织主页修改与 community 文档修改落在不同仓库，由文件归属决定；必要时互链。

## 负责人如何落实

正式开放任务前填写主要处理人、答疑／评审角色、下次检查日；没有本人确认时保留待确认，不把候选事项当已分配任务。

[协作试行](pilot.md) · [维护分工](../MAINTAINERS.md)
