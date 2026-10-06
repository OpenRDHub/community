# 材料提取手册（Source Extraction）

从 Khub 项目文件夹提取材料并转化为需求内容的方法。

---

## 一、目录盘点

项目文件夹通常有 1–3 层，且材料形式混杂：

```bash
# 递归盘点（脚本化，不要手工逐层看）
lark-cli drive files list --params '{"folder_token":"<tok>","page_size":200}' --format json
# 对 type=folder 的子项继续递归
```

**盘点产出**：一份完整的 path → type → name → token 清单。先看清全貌再决定读什么。

---

## 二、材料分流

Khub 项目的材料形式与提取方法：

| 形式 | 提取方法 | 注意 |
|------|---------|------|
| **docx**（飞书文档） | `lark-cli docs +fetch --doc <token> --doc-format markdown` | token 可用文件 token 或 URL |
| **md 文件**（Drive 上传） | `lark-cli drive +download --file-token <tok> --output x.md` | 多为调研笔记 |
| **PDF** | `lark-cli drive +download` → `read_file` 或 `pdftotext` | 扫描版需 OCR |
| **HTML** | 正则剥标签（见下方） | 常为方案/报告 |
| **PPTX** | 提取 slide XML **和 notesSlide XML** | 备注页信息量大 |
| **RAR** | `bsdtar -xf`（系统通常无 unrar/7z） | 情报/资料包 |
| **slides**（飞书幻灯片） | `lark-cli drive +export --url <url> --file-extension pptx` | 导出后按 PPTX 处理 |
| **外链**（GitHub/公众号） | `curl` 或 raw.githubusercontent | 见第四章 |

### HTML 提取

```bash
python3 -c "import re,html; c=open('x.html',encoding='utf-8',errors='ignore').read();\
t=re.sub(r'<(script|style).*?</\1>','',c,flags=re.S); t=re.sub(r'<[^>]+>','\n',t);\
print(re.sub(r'\n\s*\n+','\n',html.unescape(t)).strip())"
```

### PPTX 提取（含备注页）

```bash
python3 -c "import zipfile,re,html; z=zipfile.ZipFile('x.pptx');\
notes=sorted([n for n in z.namelist() if 'notesSlide' in n and n.endswith('.xml')],\
key=lambda x:int(re.search(r'notesSlide(\d+)',x).group(1)));\
[print('==',n,'==\n', '\n'.join(html.unescape(t) for t in re.findall(r'<a:t>(.*?)</a:t>', z.read(n).decode('utf-8','ignore'), re.S) if t.strip())) for n in notes]"
```

**备注页往往比正文更有信息量** —— 正文是标题，备注是数据、边界声明、技术细节、资料路径。

---

## 三、识别核心需求文档

项目文件夹里文件很多，但不是每个都是需求来源。优先级：

| 优先级 | 文档类型 | 判断标志 |
|--------|---------|---------|
| **P0** | 需求书/需求说明 | 文件名含「需求」「需求说明」；内容含「患者痛点 / 需要的设计」结构 |
| **P0** | 需求问答实录 | 文件名含「问答」「访谈」「实录」；含需求提出人原话 |
| **P1** | 产品机会分析 | 文件名含「机会分析」「真实需求」；含痛点与设计映射 |
| **P1** | 背景知识文档 | 文件名含「赛题背景」「知识文档」；含疾病介绍与使用场景 |
| **P2** | 技术文档/SOP | 用于写「技术路线」与「验收指标」 |
| **P2** | 竞品调研 | 用于写「竞品格局」章节 |
| **P3** | 文献/论文 | 用于支撑数据与机制说明 |
| **P3** | 项目进度/Readme | 用于写「当前技术基础」 |

**P0 文档必读全文**；P1 读关键章节；P2/P3 按需检索。

---

## 四、外链材料

Khub 项目里常见两类外链：

### GitHub 仓库

```bash
# 仓库元信息
curl -s https://api.github.com/repos/<owner>/<repo>
# 文件树
curl -s "https://api.github.com/repos/<owner>/<repo>/git/trees/main?recursive=1"
# 读文件（raw，最稳）
curl -s https://raw.githubusercontent.com/<owner>/<repo>/main/README.md
```

**注意**：`web_extract` 对 github.com 可能返回「Blocked: private or internal network address」，直接用 `curl` 或 `urllib` 取 raw 内容。

### 微信公众号文章

```python
# 用移动端 UA + 正则提取 js_content
req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0 (iPhone; ...)'})
# 正文在 <div id="js_content"> 里
```

**注意**：`web_extract` 对 mp.weixin.qq.com 也会被 Blocked，需用 urllib 直取。

---

## 五、从材料到需求的转化

### 5.1 三层信息分离

材料里混着三类信息，必须分开处理：

| 类型 | 例 | 处理方式 |
|------|-----|---------|
| **需求方原话** | 「一节课举几十次望远镜，肩颈酸痛」 | **直接引用**，是最强证据 |
| **二手转述/解读** | 「这说明用户需要解放双手的方案」 | 可用作分析，但标注为解读 |
| **背景数据** | 发病率 1/18000、患者约 10 万 | 用于背景章节，标注来源 |

### 5.2 定性 → 量化的转化

需求书的核心价值在于把定性诉求转为可验收指标：

| 定性诉求（原话） | 量化指标（需求书） |
|----------------|------------------|
| 「要把睡着的人叫醒」 | 强震动 + 声音 + 闪光三通道；持续至实际取药才停止 |
| 「放大到能辨识」 | 等效阅读倍率 > 10×；AI 超分而非插值 |
| 「不要打扰家人」 | 夜间模式：贴身强震动弱声、夜光指示 |
| 「电池要够用一天」 | 续航 ≥ 8 小时 |

**转化原则**：保留原话作为引证，同时给出可测量指标。

### 5.3 冲突处理

材料之间可能矛盾，常见三类：

**类型一：版本演进**（后期材料覆盖前期）
> 处理：以最新为准，并在正文注明「旧文档仅保留其已验证的业务逻辑」

**类型二：认知修正**（后发现的机制推翻早期判断）
> 例：项目1 早期判断「用户最需要 OCR 朗读」，后被需求提出人的病理机制说明推翻（「不是模糊，是细节少」，核心诉求是放大）
> 处理：**按修正后的判断组织内容**，并在正文显式标注这次修正及依据来源

**类型三：范围冲突**（材料涉及需求书排除的阶段）
> 处理：在「实施范围边界」章节明确划出，范围外内容列为「后续路线」

### 5.4 缺口标注

材料不足时**不要编造**。在需求书中显式标注：

- 待确认项（列出需要向需求方确认的问题）
- 数据缺口（哪些指标暂无数据支撑）
- 需后续验证的假设

---

## 六、常见陷阱

- **只读「需求」文件** —— 背景知识文档、问答实录、项目 Readme 里往往藏着关键约束（如阶段范围、技术限制）
- **忽略 PPTX 备注页** —— 备注里有真机数据、边界声明、资料路径
- **把转述当原话** —— 项目方的总结 ≠ 患者原话，证据强度不同
- **忽略材料中的「不做」声明** —— 「本次不开发/不演示/不包含」是硬边界，必须保留
- **用 web_extract 取 GitHub/微信** —— 会被 Blocked，用 curl/urllib
- **RAR 用 unrar/7z** —— 系统通常没有，用 `bsdtar -xf`
