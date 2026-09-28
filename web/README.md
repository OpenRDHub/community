# 本地预览与维护

文档主版本位于仓库根目录的 docs/、records/、templates/ 等目录；web/ 直接读取它们，不维护第二份 community 正文。organization-profile/ 是另一个仓库 .github 的待应用修改副本，需通过单独补丁提交。

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
