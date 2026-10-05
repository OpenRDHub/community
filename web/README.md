# 本地预览与维护

文档主版本位于仓库根目录的 docs/、records/、templates/ 等目录；web/ 直接读取它们，不维护第二份 community 正文。organization-profile/ 是 .github 已上线文件的预览快照（2026-09-29，PR #1）；主页主版本在 .github，修改合入后再同步此目录。handoff/ 中的旧补丁仅供历史追溯，不应重复应用。

需要 Node.js 20+、Python 3.10+。在仓库根目录：

```sh
python3 -m venv .venv
.venv/bin/pip install -r web/requirements.txt
cd web
npm ci
PYTHON=../.venv/bin/python npm test
PYTHON=../.venv/bin/python npm run build
npm start
```

只监听 127.0.0.1:5274。打开 http://127.0.0.1:5274/index.html 。可用 SITE_OUTPUT 指定输出目录；构建先写临时目录，成功才替换旧站点。不要直接把包含内部记录、原始下载和文档 ZIP 的 site/ 发布为公开网站。

activity.json 是带日期的远端条目快照；改网页不改变 GitHub Issue、PR 或 Projects。deployment.json 记录本轮真实仓库和任务链接。

模板复制到 records/ 后要替换 REPLACE-ME 并填写 YAML。支持中文或英文单独收录；翻译共用同一个 ID。构建会检查必填字段、枚举值、ID 冲突与日期。测试在临时目录复现收录、单语回退、元信息渲染、链接和失败不覆盖原站点。

## 自动检查

`.github/workflows/ci.yml` 在提交到 main 的 PR、main 更新及合并队列中运行，也可从 Actions 手动运行。所有文件改动都会触发，避免资料或图片变动绕过合并检查。固定检查名称为 `Community checks`。

检查内容：JavaScript/JSON 语法、改动中的空白错误、记录必填字段与重复 ID、真实记录的公开标记、双语回退、网页内部链接和实际仓库构建。真实记录须标为 `visibility: public`；内部和受限原件留在受限来源。`examples/records/` 下标明 `example: true` 的演示记录可保留内部标记。`publication: pending` 可用于待复核的公开草稿，CI 通过不代表来源授权、健康信息脱敏或内容结论已经得到人工确认。

本地复现：

```sh
.venv/bin/python web/check-public-records.py
PYTHON=../.venv/bin/python npm --prefix web test
PYTHON=../.venv/bin/python npm --prefix web run build
```

检查使用只读 GitHub 权限和临时构建目录；不上传网页、文档 ZIP 或记录正文，不配置飞书 Token，也不自动部署网站。新增资料仍需在 PR 中说明来源与公开范围，由资料负责人复核。需登录的飞书链接不做外链存活检查。

main 合并规则使用 `Community checks` 作为必需检查，要求分支与 main 同步并解决评审对话。维护者可在仓库 Settings → Branches 查看规则；首次贡献者的 fork 工作流仍遵循 GitHub 的运行审批设置。
