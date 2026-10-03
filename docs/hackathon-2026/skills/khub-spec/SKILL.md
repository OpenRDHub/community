---
name: khub-spec
version: 1.0.0
author: Hermes Agent
license: MIT
description: "Turn project materials into a requirement doc."
metadata:
  hermes:
    tags: [requirements, documentation, khub, hackathon, feishu, pdf]
    related_skills: [chinese-markdown-to-pdf, lark-drive, lark-doc, khub-eval]
---

# Khub Spec（从项目材料生成需求书）

把 Khub 罕见病项目文件夹里的散乱材料（需求文档、问答实录、背景知识、调研笔记、论文、外链），整理成一份结构化的**产品需求书** PDF，并归档回项目文件夹。

## When to Use

- 「查看整理全部内容，写成一份需求书」
- 「把这个项目的材料整理成需求文档」
- 「给项目 N 写需求书」
- 需要从零散材料提炼需求并量化

**与 khub-eval 的关系**：本 skill 产出的需求书是 khub-eval 的评估基准。先有需求书，才能做符合度评估。

## 核心纪律

1. **材料是唯一来源**。不编造材料中没有的需求、数据、指标。材料不足时显式标注缺口。
2. **定性 → 量化**。需求书的核心价值是把「要响亮」转成「强震动+声音+闪光三通道，持续至取药」。
3. **原话优先**。需求提出人的原话是最强证据，直接引用；转述要标注为解读。
4. **边界必写**。材料中的「本次不做 X」是硬约束，必须单独立章。
5. **冲突以最新为准**。材料矛盾时用最新版本，并注明旧材料保留了什么。
6. **认知修正要显式标注**。若后期材料推翻了早期判断，按修正后的组织内容，并说明修正依据。

## 工作流

### Step 1 — 定位项目文件夹

```bash
lark-cli drive +search --query '项目N' --doc-types folder --format json
```

赛题对应（截至 2026-10）：

| 项目 | 赛题 |
|------|------|
| 1 | 白化病+弱视力+轻便眼镜 |
| 2 | 空鼻症+鼻腔气流模拟分析工具 |
| 3 | 发作性睡病+智能药盒 |
| 4 | 无障碍乐器改造 |
| 5 | Dravet 综合征夜间癫痫睡眠监测设备 |
| 6 | 遗传性视网膜色素变性+游戏辅助工具 |
| 7 | sJIA+合并MAS动态预警平台 |
| 8 | FSHD等手部肌肉萎缩+手部力量辅具 |

### Step 2 — 递归盘点目录

**脚本化，不要手工逐层看。** 对 `type=folder` 的子项继续递归，产出完整 path → type → name → token 清单。

详见 [`references/source-extraction.md`](references/source-extraction.md) 第一章。

### Step 3 — 分流提取材料

材料形式混杂，按类型分流：docx / md / PDF / HTML / PPTX / RAR / slides / 外链。

**关键**：
- PPTX **必须同时提取 notesSlide**（备注页信息量大于正文）
- RAR 用 `bsdtar -xf`（系统通常无 unrar/7z）
- GitHub/微信公众号外链用 `curl`/`urllib` 直取（`web_extract` 会被 Blocked）

完整提取命令见 [`references/source-extraction.md`](references/source-extraction.md) 第二、四章。

### Step 4 — 识别核心需求文档

按优先级筛选（P0 必读全文，P1 读关键章节，P2/P3 按需）：

| 优先级 | 文档类型 | 判断标志 |
|--------|---------|---------|
| **P0** | 需求书/需求说明 | 含「患者痛点 / 需要的设计」结构 |
| **P0** | 需求问答实录 | 含需求提出人原话 |
| **P1** | 产品机会分析 | 含痛点与设计映射 |
| **P1** | 背景知识文档 | 含疾病介绍与使用场景 |
| **P2** | 技术文档/SOP、竞品调研 | 用于技术路线与竞品章节 |
| **P3** | 文献/论文、项目进度 | 用于支撑数据与现状说明 |

### Step 5 — 三层信息分离

材料里混着三类信息，分开处理：

| 类型 | 处理方式 |
|------|---------|
| **需求方原话** | **直接引用**，最强证据 |
| **二手转述/解读** | 可用作分析，但标注为解读 |
| **背景数据** | 用于背景章节，标注来源 |

### Step 6 — 定性 → 量化转化

这是需求书的核心工作：

| 定性诉求（原话） | 量化指标（需求书） |
|----------------|------------------|
| 「要把睡着的人叫醒」 | 强震动+声音+闪光三通道；持续至实际取药才停止 |
| 「放大到能辨识」 | 等效阅读倍率 > 10×；AI 超分而非插值 |
| 「不要打扰家人」 | 夜间模式：贴身强震动弱声、夜光指示 |

**保留原话作为引证 + 给出可测量指标**，两者都要。

### Step 7 — 冲突处理

材料矛盾时按三类处理：

| 类型 | 处理 |
|------|------|
| **版本演进**（后期覆盖前期） | 以最新为准，注明旧文档保留了什么 |
| **认知修正**（新机制推翻旧判断） | 按修正后组织，**显式标注修正及依据来源** |
| **范围冲突**（涉及排除阶段） | 在范围边界章划出，范围外列为后续路线 |

### Step 8 — 按骨架撰写

骨架见 [`references/requirement-doc-template.md`](references/requirement-doc-template.md)。章节按项目实际材料取舍（该文件有章节选择矩阵）。

**必写章节**：项目背景 / 产品定位 / 核心功能需求 / 非功能需求 / 安全伦理边界 / 附录

**有阶段划分时必写**：实施范围边界（用表格明确 in-scope / out-of-scope）

### Step 9 — 转 PDF 并归档

```bash
# 中文 PDF：用 chinese-markdown-to-pdf skill 的模板
# 模板路径：~/.hermes/skills/productivity/chinese-markdown-to-pdf/templates/ctex.tex
TPL=~/.hermes/skills/productivity/chinese-markdown-to-pdf/templates/ctex.tex
pandoc 项目N_需求书.md --pdf-engine=xelatex --template="$TPL" -o 项目N_需求书.pdf
pdfinfo 项目N_需求书.pdf | grep -i pages

# 上传回项目文件夹
lark-cli drive +upload --file 项目N_需求书.pdf --folder-token <项目文件夹token> \
  --name "<项目名>_产品需求书_V1.0.pdf"
```

**命名约定**：`<项目名>_产品需求书_V1.0.pdf`

**归档位置**：项目文件夹根目录（用户可能要求放到子目录，按需）

**上传后必须验证**：`lark-cli drive files list --params '{"folder_token":"<tok>","page_size":200}' --format json`

## References

| 文件 | 内容 |
|------|------|
| [`references/requirement-doc-template.md`](references/requirement-doc-template.md) | 章节选择矩阵、通用骨架、写作要点、篇幅参考 |
| [`references/source-extraction.md`](references/source-extraction.md) | 目录盘点、材料分流、文档优先级、外链提取、三层信息分离、冲突处理、常见陷阱 |

**跨 skill 依赖**：PDF 转换用 `chinese-markdown-to-pdf`（模板在其 `templates/ctex.tex`）。该模板已修复 pandoc 3.10 的四个失败点（`\newcounter{none}` / `\tightlist` / `Shaded` 环境 / `$highlighting-macros$` 位置）+ unicode 符号映射，不要另外维护一份。

## Pitfalls

- **只读「需求」文件** —— 背景知识文档、问答实录、Readme 里往往藏着关键约束（阶段范围、技术限制）
- **忽略 PPTX 备注页** —— 备注里有真机数据、边界声明、资料路径
- **把转述当原话** —— 证据强度不同，需区分
- **忽略材料中的「不做」声明** —— 「本次不开发/不演示/不包含」是硬边界
- **`web_extract` 取 GitHub/微信会被 Blocked** —— 用 `curl`/`urllib` 直取 raw
- **RAR 用 unrar/7z** —— 系统通常没有，用 `bsdtar -xf`
- **不要为凑篇幅注水** —— 材料不足时短一点更好，但要标注缺口
- **材料不足时不要编造** —— 标注待确认项与数据缺口

## 已验证的项目类型

截至 2026-10 完成的八份需求书，材料规模与产出：

| 项目 | 材料规模 | 页数 | 特点 |
|------|---------|------|------|
| 1 白化病 | 13 份 md + 5 篇论文 + 94 篇公众号 | 15 | 含认知修正（OCR 朗读 → 放大） |
| 2 鼻腔气流 | 5 份文档（含 SOP） | 14 | 含严格阶段边界 |
| 3 智能药盒 | 1 份 PDF（含竞品对比） | 11 | 竞品格局详实 |
| 4 乐器改造 | 1 份 docx | 6 | 材料少，短而精 |
| 5 Dravet | 7 项（含问卷文件夹） | 7 | 含分级预警 |
| 6 RP 游戏辅助 | 2 份（文档 + PDF） | 13 | 含七条设计铁律 |
| 7 sJIA/MAS | 2 份文档 | 8 | 含三套诊断标准 |
| 8 FSHD 手部辅具 | 仅 3 个外链 | 13 | **外链材料为主**（GitHub + 公众号） |

**项目 8 是最极端的情况**：飞书目录里只有 3 个外链，全部内容靠 GitHub 仓库 + 两篇公众号文章抓取。说明外链提取能力是必需的。
