---
title: 竞品路线调研 — 消费级AR/BirdBath/光波导眼镜作为低视力助视平台的可行性
date: 2026-09-18
type: 竞品调研
project: 面向白化病患者的分体式 AR+AI 助视眼镜
target_user: 白化病 / 眼球震颤 / 畏光 / 视力 0.1~0.3 / 场景：课堂看黑板 + 出行
business_model: 公益 + 残联采购（价格敏感）
scope: 2025-2026 在售或即将发售的消费级 AR/光波导/AI 眼镜
---

# 竞品路线：消费级 AR 眼镜作为低视力助视平台的可行性

## 0. 阅读须知：研究方法与数据可信度分级

**方法**：以厂商官网 / 京东天猫商品页 / 第三方参数库（AR Compare、vrarwiki、SensorSpecs、SmartGlassesGeek）为主，科技媒体实测（Tom's Guide、TechRadar、Digital Trends、NotebookCheck、Gizmodo、Tom's Hardware、IT之家、央广网）为交叉验证。

**数据分级**（本文所有数字均标注来源 URL）：
- **【官方】**：厂商官网 / 官方旗舰店商品页标注
- **【实测】**：第三方媒体或实验室仪器实测（如 X3 Pro 的暗室亮度实测）
- **【第三方】**：参数库收录，无厂商原文确认
- **【折算】**：本文根据官方等效屏幕口径反算，非官方数值
- **未公开**：检索不到可信来源，**不做猜测**

> ⚠️ 重点提醒：消费级 AR 眼镜的「亮度」有两个完全不同的口径，混用会得出错误结论。
> - **面板峰值亮度 / 光源峰值**（nits）：XREAL One 标 5000 nits、Rokid Max 标 5000 nits、X3 Pro 标 6000 nits —— 这是光机出光，**不是入眼值**。
> - **入眼亮度 / 感知亮度**（perceived nits）：XREAL One 600 nits、One Pro 700 nits、Rokid Max 600 nits、雷鸟 Air 3 650 nits —— **只有这个值决定户外能不能看清**。
> - 更极端的是 X3 Pro：官方标称平均 3500 / 峰值 6000 nits，第三方暗室实测眼盒内最大仅 **513 nits**、视场中心 **291 nits**。两者差一个数量级，说明"标称亮度"不能直接用于户外可用性判断。

---

## 1. XREAL

### 1.1 XREAL One Pro（2025-04 上市，当前主力旗舰）

| 项目 | 参数 |
|---|---|
| 显示技术 | 自研 **X Prism** 光学引擎（平板棱镜波导，"混合波导"折叠光路，官方称光学模组厚度较前代降低 41%）；索尼 0.55″ Micro-OLED（2025 年 4 月 CES 首发口径） |
| 分辨率 / 刷新率 | 1920×1080 / 眼，120 Hz，3 ms M2P 延迟 |
| FOV | **57°**（XREAL 称行业最大）✅【官方】 |
| 入眼亮度 | **700 nits**（比 XREAL One 的 600 nits 更高）✅【官方】 |
| 虚像尺寸 | 34″~556″ 可调，等效距离 1~10 m（营销口径，**不等于** FOV 换算） |
| 屈光调节 | **无内置屈光调节**（官方未提供调焦）；方案为**近视镜框 + 处方镜片插入** |
| 瞳距(IPD) | M 号 57–66 mm / L 号 66–75 mm，两个硬件版本，官方称适配 95% 用户 |
| 重量 | **87 g** |
| 续航 | **无内置电池**，由 USB-C 宿主供电（线缆供电，无续航指标） |
| 空间定位 | 自研 X1 芯片，原生 **3DoF**；6DoF 需选配 XREAL Eye 摄像头模块 |
| 摄像头 | 本体无；可选插拔模块 XREAL Eye（官方称未来固件升级支持物体识别/实时翻译） |
| 遮光 | **电致变色镜片，3 档透光率** |
| 音频 | Sound by Bose |
| 可装 APP | ❌ 本体无 OS、无存储、无内存。只能作 USB-C DP1.4 显示器，镜像宿主画面 |
| 价格 | ¥4299 首发预售；京东近期 ¥3869–4299（历史最低 ¥3739）；海外 $599–$649 |
| 状态 | 在售 |

来源：[京东 XREAL One Pro](https://union-click.jd.com/jdc?e=&p=JF8BAaoJK1olWAcAVVxfD0kXBV8IGloWWQEKXFhbD0InRzBQRQQlBENHFRxWFlVWQDEXR0ROCBlQCgJDVBtKXnFYSR5NGlIcUVoabhJnX2dda1lNVQF3Cj4PfSxNBylaRDxwDxhaCwsJQVRORjNVFRlPGQpkBDs4eDFrSzNpGCYTAU9xKFpbfTYRVypsXRBMDWNsFhgJfCAWUGtOGghvJXF9CFsHHw9IWzFXRgtKCGNKFQpRCFxLUzdXeQFRUQYDVV1ZD0MfBWkPEmsUNFlSFgkiYykJfSZofhtXNX59ARw9BEcnB2kLHV8UXAcBZF5cCUoWCmcBE1klWQBsVTBdAU55UGcNGw4dCgMDB1pbC08fV18IGmtFMw4KXF5bDE0SA2YIK1olXQALXFhcCUsXB2YBGmsVVQIyg_fz3sex19aizOmXbTYyV25tOEgRM2w4RTUUWgNWVgteWiVLR2hdEgRCVWgFVl5VAEoSCl8KGloXXzYyZDgNbS5neRNARzoWIABeHS0hDE1ifmlcXj9TFl9SMTAfTh9jaG5bHx0UDnx6IyEBDREnA18PH1glXDY) · [gfan 上市报道](https://gfan.com/info/592164.html) · [SensorSpecs](https://sensorspecs.fyi/device/xreal-one-pro) · [vrarwiki](https://vrarwiki.com/index.php?direction=next&oldid=37075&title=Xreal_One_Pro)

### 1.2 XREAL One

| 项目 | 参数 |
|---|---|
| 显示技术 | **BirdBath**；索尼 0.6″/0.68″ Micro-OLED（来源口径不一，官方商品页写 0.68″） |
| 分辨率 / 刷新率 | 1920×1080 / 眼，120 Hz |
| FOV | **50°** ✅【官方】 |
| 入眼亮度 | **600 nits** 入眼（面板峰值 5000 nits）✅【官方】 |
| 屈光调节 | ❌ **无近视调焦**（Digital Trends 实测结论："No diopter adjustment for myopia"）；靠处方镜片插入 |
| 瞳距 | 眼镜内软件 IPD 调节（官方描述） |
| 重量 | 82 g（官方 shop）/ 84 g（TechRadar 实测） |
| 续航 | 无内置电池，USB-C 供电 |
| 空间定位 | X1 芯片原生 3DoF（Anchor / Follow 模式切换） |
| 摄像头 | ❌ 无 |
| 遮光 | 电致变色 3 档（前代 Air 2 Pro 才有的 Pro 功能下放到标准版） |
| 可装 APP | ❌ 无 OS，只作显示器；配套 **XREAL Beam Pro**（$199，安卓设备）可跑 APP |
| 价格 | 首发 $499 / £449；当前官网 $399（有降价）|
| 状态 | 在售 |

来源：[Digital Trends 评测](https://www.digitaltrends.com/computing/xreal-one-review) · [TechRadar 评测](https://www.techradar.com/computing/virtual-reality-augmented-reality/xreal-one-review-top-notch-ar-smart-glasses-that-come-at-a-price) · [Front Desk Review 参数摘录](https://frontdeskreview.com/product/smart-glasses/xreal-one)

### 1.3 XREAL Air 2 Ultra（开发者向，已被 One Pro 取代）

| 项目 | 参数 |
|---|---|
| 显示技术 | **BirdBath**；索尼 0.55″ Micro-OLED |
| 分辨率 / 刷新率 | 1920×1080 / 眼，120 Hz，42 PPD |
| FOV | **52°** ✅【官方】 |
| 入眼亮度 | **500 nits**（第三方明确点评"500-nit brightness limits outdoor visibility"）|
| 屈光调节 | ❌ 无内置；官方提供**处方镜片插入（prescription lens inserts）** |
| 重量 | **80 g**，钛合金镜架 |
| 续航 | 无内置电池，USB-C 供电 |
| 空间定位 | **6DoF**（双 3D 环境摄像头）+ 手势/手部跟踪 + 空间锚定（NRSDK 2.2，Unity） |
| 摄像头 | ✅ 2× |
| 遮光 | 电致变色 3 档 |
| 可装 APP | ❌ 无片上算力，依赖 Samsung 安卓机 / Beam Pro / PC 作宿主；SDK 为 NRSDK |
| 价格 | $699 |
| 状态 | **AR Compare 标记为 Discontinued**，官方后继机型为 XREAL One Pro |

来源：[AR Compare 规格页](https://www.arcompare.com/ar-glasses/xreal-air-2-ultra) · [vrarwiki](https://vrarwiki.com/index.php?curid=10129&diff=37034&title=Xreal_Air_2_Ultra)

### 1.4 【延伸】XREAL AURA（前 Project Aura）— 2026 秋季，最值得盯的一条线

| 项目 | 参数 |
|---|---|
| 平台 | **Android XR**（Google）+ Gemini 深度集成，Google Play 全量 APP 可用 |
| 芯片 | 高通 **Snapdragon Reality Elite** 计算吊舱（分体式）+ 眼镜端 XREAL X1S 协处理芯片（双芯片分离计算） |
| 显示 | 索尼 Micro-OLED，1920×1200 / 眼，120 Hz |
| FOV | **70°** ✅【官方】，XREAL 迄今最大 |
| 重量 | **< 95 g** |
| 屈光调节 | **未公开**（官方未披露处方镜片方案） |
| 续航 | 计算吊舱 34.84 Wh（约为眼镜本体外置）；眼镜本体续航未公开 |
| 跟踪 | 手部跟踪 + 6DoF + 世界朝向传感器阵列 |
| 遮光 | 电致变色 |
| 可装 APP | ✅ **Android XR，Google Play 数百万 APP 首发当日可用** |
| 价格 | 官方承诺基础版**零售价不超过 US$1,500**；预订 $99 / $199 / $299 三档 |
| 状态 | 2026 秋季上市（美/英/日/韩/加，欧洲随后）；2026-09 威尼斯电影节已公开实机演示；预订量 >10,000 |

来源：[XREAL 官网 AURA](https://www.xreal.com/ca/aura) · [Ubergizmo](https://www.ubergizmo.com/2026/06/xreal-aura) · [GCN 报道](https://gcn.com/xreal-aura-android-xr-glasses-venice/21630) · [央广网/搜狐](https://m.sohu.com/a/1037947210_362042)

---

## 2. Rokid

### 2.1 Rokid Glasses（乐奇 AI 眼镜，2024-11 发布 / 2025 上市）

| 项目 | 参数 |
|---|---|
| 显示技术 | **衍射光波导** + 双目单绿 Micro-LED（JBD Hummingbird Mini II，一拖二光学设计降本） |
| 分辨率 | 480×398 ~ 480×400 / 眼（第三方口径） |
| FOV | **30°**【官方/第三方标称】；Tom's Guide、Forbes 实测口径为 **23°** —— 两个口径并存，按 23–30° 区间理解 |
| 亮度 | **1500 nits** |
| 屈光调节 | ❌ 无内置；官方"支持近视/散光人群镜片定制，卡扣安装"（磁吸夹片） |
| 重量 | **49 g** |
| 续航 | 210 mAh，官方"满工作续航 4 小时"，充电盒可充 10 次；AR Compare 记录**常显状态仅 2 小时**，AI 功能走付费额度 |
| 芯片 / OS | 高通 **Snapdragon AR1 Gen 1** + NXP RT600 协处理器；2 GB RAM / 32 GB ROM；**YodaOS-Master（基于 Android）** |
| 摄像头 | ✅ 12 MP（索尼 IMX681，f/2.25） |
| 音频 | 双定向扬声器 + 4 麦克风阵列（AI 降噪），支持头动接听/拒接 |
| 可装 APP | ⚠️ **有 Android 底层 + SoC**，官方生态为 Rokid 自有应用商店；第三方 APK 侧载能力**未公开** |
| 价格 | 国内发布价 **¥2499**（2024-11 与暴龙联名发布，2025 Q2 上市）；当前京东/天猫 **¥3299**、充电仓套装 **¥3558**（国补型号在列）。海外 $599 MSRP（Kickstarter 早鸟 $499），AR Compare 记录 $699 |
| 状态 | 在售（Kickstarter 交付期曾有延迟、配件缺失的公开投诉记录） |

来源：[Rokid 官网产品页](https://glasses.rokid.com/) · [AR Compare](https://www.arcompare.com/ar-glasses/rokid-glasses) · [SmartGlassesGeek](https://smartglassesgeek.com/glasses/rokid-glasses) · [Tom's Guide 实机体验](https://www.tomsguide.com/computing/smart-glasses/i-just-tested-the-futuristic-rokid-glasses-bringing-ar-and-ai-together-to-make-meta-nervous) · [VR陀螺 发布会](https://www.vrtuoluo.cn/541407.html)

### 2.2 Rokid Max（分体式显示眼镜）与 Max 2 / AR Spatial

| 项目 | Rokid Max | Rokid Max 2 / AR Spatial |
|---|---|---|
| 显示技术 | **BirdBath**；索尼 Micro-OLED | 同（YodaOS-Master 空间浏览器） |
| 分辨率 | 1920×1080 / 眼 | 1080P / 1200P |
| FOV | **约 50°** | 约 50° |
| 入眼亮度 | **峰值 600 nits / 默认 400 nits**（面板峰值 5000 nits）✅【官方】 | 600 nits，6 档可调 |
| 刷新率 | 120 Hz | 90 Hz |
| **屈光调节** | ✅ **0.00D ~ -6.00D 双眼独立实时调节，内置旋钮，无需另购镜片**；❌ **不支持散光** | 同：0.00D~-6.00D"全球首个近视+瞳距调节" |
| 瞳距 | 瞳孔智能适配 | 同 |
| Eyebox | 7×11 mm | 未公开 |
| 重量 | **75 g** | 75 g |
| 续航 | 无内置电池（宿主供电）；配 Rokid Station 约 5 h | 无内置电池；Station 2 5000 mAh / 18W |
| 摄像头 | ❌ 无 | ❌ 无 |
| 遮光 | 偏振膜技术（正面漏光削减 90%），**无电致变色** | 未公开 |
| 3DoF | ✅ | ✅（DRM 内容自动切 0-DoF） |
| 可装 APP | ❌ 本体无 OS。宿主方案：**Rokid Station / Station 2（Android TV + Google Play，可装 APP）** | 同左（Google Play 可用，需开 GMS） |
| 价格 | 京东 ¥2499；海外 $439，AR Compare 记录清仓价 **$159** | AR Spatial $698 |
| 状态 | 在售（价格已大幅下探） | 在售 |

来源：[Rokid Max 官网](https://max.rokid.com) · [Rokid Global AR Spatial 规格](https://global.rokid.com/products/rokid-ar-spatial) · [vrarwiki Rokid Max](https://vrarwiki.com/index.php?title=Rokid_Max&diff=prev&oldid=37300) · [AR Compare 对比页](https://www.arcompare.com/compare/rokid-max-vs-viture-pro-xr)

> **Rokid 对本项目最关键的一条**：Rokid Max 是本次调研中**唯一内置 0~-600 度近视调节**的消费级 AR 眼镜（双眼独立、旋钮实时）。但**明确不支持散光**，上限 -6.00D —— 对白化病常见的高度近视 + 中高散光仍不够用。

---

## 3. 雷鸟创新（TCL RayNeo）

### 3.1 雷鸟 Air 3 / Air 3s（¥1299 档，最便宜的可验证平台）

| 项目 | 雷鸟 Air 3 | 雷鸟 Air 3s（四周年纪念版） |
|---|---|---|
| 发布时间 | 2024-10-28 | 2025-10 |
| 显示技术 | 孔雀光学引擎 + 第五代 Micro-OLED（0.6″，双层发光）+ **BirdBath** 光路 | 同系列 |
| 分辨率 | 1920×1080（2D）/ 3840×1080（3D），**135″/100″ 口径** | 1920×1080 |
| FOV | 官方未直接公布；按"3 米等效 100 英寸"【折算】约 **46°（对角）** | 未公开 |
| 入眼亮度 | **650 nits**，200000:1 对比度 ✅【官方】 | **1200 nits** ✅【官方】 |
| 刷新率 | 120 Hz | 120 Hz |
| 屈光调节 | ❌ 无内置；**全球镜片合作方支持 1–600 度近视镜片搭配** | 未公开（同渠道配镜） |
| 瞳距 | **Eyebox 14×7 mm，适配 93% 瞳距人群**（三档镜腿 + 可调鼻托） | 未公开 |
| 重量 | **76 g** | 未公开（同量级） |
| 续航 | 无内置电池；配套设备 4000 mAh，6–8 h | 同左（宿主供电，实测"耗手机电"明显） |
| 护眼 | 3840 Hz 高频 PWM，TÜV 南德防蓝光 + 抗疲劳双认证，ΔE<2 | 未公开 |
| 摄像头 | ❌ 无 | ❌ 无 |
| 可装 APP | ❌ 无 OS，USB-C DP 镜像（1000+ 设备适配） | ❌ 同左 |
| 价格 | **¥1699**（发布价） | **¥1299** 到手（京东 ¥1470，国补 ¥1113.93） |
| 状态 | 在售 | 在售 |

来源：[IT之家 Air 4 发布会（含 Air 3s 信息）](https://www.ithome.com/0/891/877.htm) · [太平洋电脑网](https://www.pconline.com.cn/zhizao/1832/18329870.html) · [MicroLED 网](https://microled.cn/news/3860.html) · [百度百科 Air 3](https://baike.baidu.com/item/%E9%9B%B7%E9%B8%9FAir%203/65042219) · [京东 Air 3S](https://union-click.jd.com/jdc?e=&p=JF8BARQJK1olXDYCVV9fCEMVBGcBGlolGVlaCgFtUQ5SQi0DBUVNGFJeSwUIFxlJX3EIGloXXQ4AU1ZUCUoIWipURmtXAAZDPQAJey5jAA98ZVl1X0RKMlYbBEcnB2kLHV8UXAcBZF5cCUoWCmcBE1klWQBsVTBdAU55C20LGgtCCFILUgtZCkIfC18IGmteMwcyVW5dDkIfBW4JG1kRVAcAZF5VDHvAqsHel_3B5KzV5txtOHsUM184G2sWbVhsVVlYXBsUCm5mRx8SCA4BFh4zD0kUAmkAG1glXwcDVlxtOHtMCmt-YwZ9I1kKPAM0CTsfYjxobFhMCmd-IxxdDSUVZRtOUh8QIHZVETcGaS1SUGY4G2slXDY)

### 3.2 雷鸟 Air 4 / Air 4 Pro（2025-10-23 发布，HDR 观影向）

| 项目 | 参数 |
|---|---|
| 显示技术 | 孔雀光引擎 2.0 + 第 5.5 代 Micro-OLED + 自研 **Vision 4000** 画质芯片（与 Pixelworks 联合），**BirdBath** |
| 亮点 | 全球首款 HDR10 显示眼镜，10 bit 色彩，AI 实时 SDR→HDR、AI 2D→3D |
| 分辨率 | 未公开（前代 1080P/眼 口径） |
| FOV | **未公开**（官方仅给"135 英寸巨幕"） |
| 入眼亮度 | **1200 nits** ✅【官方】 |
| 屈光调节 | ❌ 无内置；官方"**一站式近视配镜**" |
| 重量 | **76 g**，亲肤软质镜腿 |
| 音频 | 4 扬声器 + 独立 DAC，**B&O 联调**（雷鸟首款 B&O 合作机型） |
| 可装 APP | ❌ 无 OS，Type-C 直连 iPhone / 安卓 / Steam Deck / 笔记本 / 平板 |
| 价格 | 标准版 **¥1599**（国补 ¥1519.34）/ Pro 版 **¥1699**（国补 ¥1614.24） |
| 状态 | 在售 |

来源：[IT之家](https://www.ithome.com/0/891/877.htm) · [央广网/腾讯新闻](https://news.qq.com/rain/a/20251024A03OEB00) · [新华网](https://www.news.cn/tech/20251024/8390fb0b04584412be742f11fd92070f/c.html)

### 3.3 雷鸟 X3 Pro（双目光波导旗舰，2025-05 发布 / 2025-12 上市）

| 项目 | 参数 |
|---|---|
| 显示技术 | **0.36 cc 全彩 Micro-LED + 衍射光波导（刻蚀工艺/表面浮雕）**，双目，雷鸟称"全球最小可量产全彩 Micro-LED 光引擎"，材料方案来自 Applied Materials |
| 分辨率 | **640×480**，60 Hz |
| FOV | **30°**（官方；第三方实测水平左右各 24.1–24.3°、垂直 18.4°、对角 30.04°）|
| 亮度 | 官方标称：**平均 3500 nits / 峰值 6000 nits** ⚠️ 第三方暗室 LMD 实测：**眼盒内最大 513 nits、视场中心 291 nits**（左右眼近似）。两个口径差异极大 |
| 眼盒 | 实测 **17×13 mm**（以 50% 中心亮度为阈值）|
| 环境光透过率 | 实测 A 光源 74.22% / D65 74.34% |
| 屈光调节 | ❌ 无内置；方案为**磁吸处方夹片**（官方不建议叠戴日常眼镜）；2025-11 起开放**全贴合镜片定制**（重量 <4 g，官方称解决鬼影与色散），全贴合版 ¥10999 |
| 重量 | **76 g**（镜框） |
| 电池 / 续航 | 245 mAh；**官方"综合续航 24 小时"**；⚠️ 评测普遍打脸：Tom's Hardware "alarming battery life"（最长约 1 h），Android Central 一个月测试**从未超过 30 分钟** |
| 芯片 / OS | 高通 **Snapdragon AR1 Gen 1** + Hexagon NPU；4 GB RAM / 32 GB ROM；**RayNeo AIOS（基于 Android）**，Gemini 2.5 / GPT 双通道 |
| 摄像头 | ✅ 索尼 IMX681 12 MP + OV 空间摄像头（1080p30、6DoF 辅助定位），支持 3K 视频录制 |
| 交互 | 镜腿五维触控、语音、手机空鼠、Apple Watch 手势 |
| 可装 APP | ⚠️ 有 Android 虚拟环境，官方演示可开 TikTok/Instagram/WhatsApp；但 Gizmodo 称**侧载体验"major headache"**，生态薄 |
| 价格 | 京东自营 **¥8499**（常卖价；全贴合定制版 ¥10999）；海外 $1299（早鸟 $1099） |
| 状态 | 在售 |

来源：[TCL CES 官方页](https://www.tcl.com/ces) · [AR Compare 评测汇总](https://www.arcompare.com/ar-glasses/rayneo-x3-pro/) · [WearableXP 评测](https://wearablexp.com/smart-glasses/rayneo-x3-pro-review/) · [京东 X3 Pro](https://union-click.jd.com/jdc?e=&p=JF8BATIJK1olWAcEVF1ZCUkRC18IGloWXg8FU15YCkInRzBQRQQlBENHFRxWFlVPRjtUBABAQlRcCEBdCUoUAGYPHFsQXw8dDRsBVXsWeR1DUFxPVGZgEDwtcCBCVAtcaShDUQoyUFheDk8WAm4LK1sUXAcDXVZUAEknB2lmGjUVVANsVFkODUMfA2ddGAkQWFIFXG5dCXtVbbeinYOc89Gq34ndvpyomruAlWsUbQYEXVZbCUoXA28NElMlXQ4GZIn0pp2bpbuxsYyn3zYyZF1tOHsXM2w4RTUUWgNWVgteWCVLR2hdEgEVVGgFVl5VC04UAl8KGloXXzYyZAUbaE5SQxRyQydeNEZfDB49fxJVai9hYC9cB2BfNDNDBffChnfThJWA1oBUYFNgVbTDInA18PH1glXDY) · [雷鸟官方 2026 选购指南](https://www.rayneo.com/blogs/news/best-smart-glasses-2026-guide)

### 3.4 雷鸟 V3 / V3 系列（AI 拍摄眼镜，无显示）

| 项目 | 参数 |
|---|---|
| 显示 | ❌ **无光机、无显示**（另有"AI 智能影像眼镜，无 AR 光机版本"） |
| 重量 | **39 g**（不含镜片） |
| 摄像头 | ✅ 索尼 IMX681 12 MP，F2.2 16 mm 广角，4032×3024 / 1080p30 / 竖屏 1440p30 |
| 音频 | 9×20 mm 单元，3 麦克风阵列（降噪 + 抗风噪 + 空间收音） |
| 芯片 | 高通骁龙 AR1（台积电 4 nm），AI 由阿里通义系列大模型定制 |
| 续航 | 159 mAh，官方 7 h，40 分钟充满 |
| 价格 | **¥1799 起**（首发）；2025 秋季版京东 **¥1960**（含充电盒）；迷你充电仓 ¥149 起 |
| 渠道 | 与博士眼镜合作，全国 100+ 门店提供验光/配镜 |
| 状态 | 在售 |

来源：[长城证券 CES 2025 跟踪报告（新浪/ima 存档）](https://ima.qq.com/wiki/?shareId=1ad13190d4f7ee3f55dd1d907b377344ac1f66c5c8570af323d2e86764b138aa) · [京东 雷鸟V3](https://union-click.jd.com/jdc?e=&p=JF8BARQJK1olXDYCVV9fCEMSBG4IH1wlGVlaCgFtUQ5SQi0DBUVNGFJeSwUIFxlJX3EIGloXXQ4HU19dDEwIWipURmtiFHgAFAVfTSt-fS9ccwIXXFlaKVctBEcnB2kLHV8UXAcBZF5cCUoWCmcBE1klWQBsVTBdAU55BW5bGA4WDVFVUFcNDx4UCl8IGmteMwcyVW5dDkIfBW4JG10VVQQLZF5VDHvAqsHel_3B5KzV5txtOHsUM184G2sWbVhsVVlYCUISUT1mRx8SCA5GCggzD0kUAGcJHVwlXwcDVlxtOHtpdDV-HTsQXGF0UlsLVAxQfjFPEjAUG3x8AzotDSUVBW1jEyYWWlNEKwggDjIVVAw4G2slXDY)

---

## 4. 其他简项

### 4.1 Even Realities G1（2025，$599）

| 项目 | 参数 |
|---|---|
| 显示技术 | **衍射光波导** + 双 Micro-LED 投影（自研 HAOS™ 全息自适应光学系统），镜片保持透明 |
| 分辨率 / 刷新率 | **640×200 / 眼，单色绿，20 Hz** |
| FOV | **25°**（Tom's Guide）/ 20°（第三方口径） |
| 亮度 | **1000 nits**（自动亮度调节） |
| 屈光调节 | ❌ 无内置；**处方镜片 +$150**（德国 +€129–150）；渐进片可做（需到合作验光店） |
| 重量 | **43–44 g**（镁合金 + 砂岩涂层 + 钛合金镜腿） |
| 续航 | **约 1.5 天**（160 mAh + 2000 mAh 充电盒） |
| 摄像头 / 扬声器 | ❌ 无 / ❌ 无 |
| 可装 APP | ❌ 不能装第三方 APP；仅 Even 官方 App（Android/iOS）推送通知、13 语翻译、ChatGPT/Perplexity 集成、提词器 |
| 遮光 | ❌ 无电致变色；**官方太阳镜夹片 $100**（PCMag：户外日光下"borderline necessary"，因为投影压不过阳光） |
| 价格 | **$599 / £594 / €699**；配齐处方 + 夹片约 $850+ |
| 状态 | 在售（2025 年固件更新加入 ChatGPT / Perplexity） |

**对本项目的关键意义**：G1 是"最像普通眼镜 + 最轻 + 最长续航"的形态标杆，但单色 640×200 / 20 Hz / 25° 的分辨率完全无法承载放大阅读；PCMag 明确写过"1,000 nits 在户外会被环境光压掉"。可作为**机壳/人机工学参考**，不能作为助视平台。

来源：[PCMag 评测](https://au.pcmag.com/wearables/110274/even-realities-g1) · [Tom's Guide 评测](https://www-tomsguide-com.translate.goog/computing/smart-glasses/even-realities-g1-smart-glasses-review) · [Xpert.digital 规格](https://xpert.digital/en/even-realities-g1/)

### 4.2 小米 AI 眼镜（2025-06-26 发布，仅中国）

| 项目 | 参数 |
|---|---|
| 显示 | ❌ **无内置光学显示模块**（官方答网友问明确："专注于拍摄与 AI 语音交互，并未配备屏幕显示功能，所有信息反馈均通过开放式扬声器以音频形式呈现"） |
| 重量 | 裸框 **40 g**（含默认镜片实测 44.8 g） |
| 摄像头 | ✅ 12 MP 索尼 IMX681，1G+4P，105° 超广角，4:3 无裁切，2304×1728 录像 / 2K30fps，EIS 防抖，0.8 s 抓拍 |
| 音频 | 5 麦克风阵列（含骨传导）+ 双开放式扬声器 |
| 芯片 / OS | 高通骁龙 AR1 + 恒玄 BES2700H 低功耗双芯；**Vela OS** |
| 续航 | 263 mAh 金沙江电池，典型 **8.6 h**；USB-C 可边充边用 |
| 遮光 | ✅ **电致变色镜片，0.2 s 变色，4 档**（国内眼镜首次落地电致变色） |
| 配镜 | 线下 400 家门店验光 + 线上定制处方镜片 |
| 可装 APP | ❌ Vela OS 封闭，不能装第三方 APP；小米生态联动（微信/QQ 视频通话、B站/抖音直播推流） |
| 价格 | 标准版 **¥1999** / 单色电致变色版 **¥2699** / 彩色电致变色版 **¥2999** |
| 状态 | 在售（限中国） |

**对本项目的关键意义**：小米 AI 眼镜是**"无显示 + 摄像头 + 音频 + 电致变色遮光"**的极简形态。对白化病用户，它恰好同时满足"遮光"和"OCR 朗读"两个需求，缺的只有"放大"。可作为**低成本音频助视形态的对照实验组**（¥1999 已接近残联采购可接受区间）。

来源：[小米商城](https://www.mi.com/shop/buy/detail?product_id=21399) · [PChome 官方答网友问](https://article.pchome.net/info/4339.html) · [Guru3D](https://www.guru3d.com/story/xiaomi-launches-smart-glasses-with-voice-assistant-and-ai-translation/) · [长城证券/国泰海通研报](https://ima.qq.com/wiki/?shareId=df0c9577d6377f32145e18671de1da856a35adc9a0b3f0c9199932d9ee36fd20)

### 4.3 Meta Ray-Ban Display（2025-09-30 美国首发，$799）

| 项目 | 参数 |
|---|---|
| 显示技术 | **未公开**（官方仅称"镜片内嵌显示/in-lens display"；媒体普遍描述为单目、非波导方案，未获官方技术确认） |
| 分辨率 / 刷新率 | **600×600，单目（仅右镜片）**，90 Hz |
| FOV | **20°** |
| 亮度 | **最高 5000 nits**（口径未细分感知/面板，第三方直接引用"up to 5,000 nits"） |
| 屈光调节 | ❌ 无内置；处方镜片 **-4.00 ~ +4.00 SPH，散光 CYL ≤ 4.00**，**加 $200** |
| 重量 | **69 g**（大号 70 g） |
| 续航 | **6 h 混合使用** + 折叠充电盒 4 次（共 24 h）；神经腕带 18 h |
| 摄像头 | ✅ 12 MP，3× 数码变焦，最高 3K30 录制 |
| 音频 | 2 开放式扬声器 + 6 麦克风（含唇边接触麦） |
| 交互 | **Meta Neural Band（sEMG 肌电腕带）**，捏/滑/点手势，IPX7 |
| 可装 APP | ❌ Meta 自有平台，不可装第三方 APK。✅ **平台内置原生屏幕阅读器（盲文级无障碍读屏，初始设置阶段即可开启）** |
| 价格 | **$799**（含 Neural Band）；国内京东国际 **¥9889** |
| 状态 | 美国在售（需到店演示后购买）；2026 年初扩展加/法/意/英 |

**无障碍侧的关键参考**：AppleVis 上一位先天失明用户的实测长文（[原文](https://www.applevis.com/comment/205397)）指出：**这类产品不是为视障设计的助视器**，但因为是大规模消费电子，价格只有专业助视器的零头、外观正常、且能吃到 Meta 在 AI 上的巨额投入。他认为把主流消费级硬件当助视平台是正确方向，但对"它是否够用"要逐功能验证。

来源：[MalaysianWireless 发布报道](https://www.malaysianwireless.com/2025/09/meta-ray-ban-display-gen-2-smart-glasses/) · [AR Compare 规格](https://www.arcompare.com/reviews/ray-ban-meta-display/) · [Front Desk Review](https://frontdeskreview.com/product/smart-glasses/ray-ban-meta-display) · [AppleVis 视障用户实测](https://www.applevis.com/comment/205397)

### 4.4 Dream Glass 4K（旧方案，Android 眼镜）

| 项目 | 参数 |
|---|---|
| 厂商 / 发布 | DreamWorld（美国），2019 Indiegogo 众筹，**2020 上市** |
| 形态 | **眼镜 + 控制盒**分体（控制盒内放电 8000 mAh 与处理器，10 个界面按键），可有线连接 |
| 显示 | 双 1920×1080（合并"4K"口径），60 Hz，18:9，2D/3D |
| FOV | **90° 超宽**（水平约 90°/垂直约 50°），200 英寸等效 @3 m |
| 亮度 | **未公开**（vrarwiki 明确"Peak Brightness: Not specified"） |
| 屈光调节 | ❌ 无；但**可直接戴近视眼镜使用**（"不用额外配镜片"，搜狐实测口径） |
| 重量 | **185 g（仅眼镜）** + 控制盒 |
| 续航 | 8000 mAh，**约 5 h** |
| 摄像头 | ❌ 无 |
| OS | ❌ 无独立 OS；HDMI / USB-C 输入（不支持 iPhone） |
| 价格 | 原价 **$599 / 4K Plus $799**；当前渠道报价极度混乱：淘宝有 **¥298** 清仓价，也有 **¥5292** 的标价 |
| **当前状态** | ⚠️ **判定为上一代清库存产品**：官方站点 `dreamworldvision.com` 本次抓取失败（无法访问）；参数库无 2025–2026 任何新品迭代记录；无厂商在售信息。**不建议作为平台方案** |

> 结论性提醒：旧资料里把 Dream Glass 4K 当"Android 眼镜"是一个常见误传 —— 它**没有 Android 系统、没有片上算力、没有摄像头**，本质是一块 HDMI/USB-C 显示器，且 185 g 重量对日常佩戴不可接受。如果项目历史文档引用过它，建议在文档中标注"已停产/清库存，参数不可作为设计基线"。

来源：[vrarwiki Dream Glass 4K](https://vrarwiki.com/index.php?oldid=37231&title=Dream_Glass_4K) · [vrarwiki 修订历史](https://vrarwiki.com/index.php?diff=prev&oldid=37389&title=Dream_Glass_4K) · [搜狐 4 款设备横评](https://www.sohu.com/a/1067442741_122645258) · [TechBloat 评测](https://www.techbloat.com/review-dreamglass-4k-straps-a-big-screen-tv-to-your-noggin.html)

---

## 5. 横向对比总表

> 亮度列统一口径：**粗体为"入眼/感知亮度"**（决定户外可用性）；括号内为面板/光源峰值（营销口径）。标 ⚠️ 者为官方与第三方差值巨大。

| 产品 | 显示技术 | FOV | 亮度（入眼 / 峰值口径） | 屈光调节 | 重量 | 续航 | 可装 APP / OS | 价格（参考） |
|---|---|---|---|---|---|---|---|---|
| **XREAL One Pro** | X Prism 平板棱镜波导（BirdBath 演进） | 57° | **700 nits** | ❌ 无内置，靠处方镜片插入；IPD M/L 两版 | 87 g | 无电池，USB-C 宿主供电 | ❌ 无 OS 无芯片，仅镜像宿主；需 Beam Pro 才能跑 APP | ¥3869–4299 / $599–649 |
| **XREAL One** | BirdBath | 50° | **600 nits**（峰值 5000） | ❌ 无近视调焦，靠处方镜片 | 82–84 g | 无电池 | ❌ 同上 | ~$399–499 |
| **XREAL Air 2 Ultra** | BirdBath | 52° | **500 nits** | ❌ 无内置，处方镜片插入 | 80 g（钛） | 无电池 | ❌ 需宿主（NRSDK / Beam Pro / PC） | $699（已停产） |
| **XREAL AURA**（2026秋） | OST 光波导（X Prism） | **70°** | 未公开 | 未公开 | <95 g | 计算吊舱 34.84 Wh | ✅ **Android XR + Google Play** | ≤$1500 |
| **Rokid Glasses** | 衍射光波导 + 单绿 Micro-LED（双目） | 30°（评测 23°） | **1500 nits** | ❌ 无内置，磁吸定制夹片（可配散光） | **49 g** | 210 mAh，官方 4 h，常显约 2 h | ⚠️ 有 Android 底座 + AR1，侧载能力未公开 | ¥3299 / ¥3558 套装；$599 |
| **Rokid Max** | BirdBath | 50° | **600 nits 峰值 / 400 nits 默认** | ✅ **0 ~ -6.00D 双眼独立旋钮**（❌ 不支持散光） | 75 g | 无电池；配 Station 约 5 h | ❌ 本体无 OS；Station 2 可跑 Google Play | ¥2499 / 海外清仓 $159 |
| **雷鸟 Air 3** | BirdBath（孔雀光引擎） | ~46°【折算】 | **650 nits** | ❌ 无内置，**支持 1–600 度镜片定制** | 76 g | 无电池（宿主供电） | ❌ 无 OS | ¥1699 |
| **雷鸟 Air 3s** | BirdBath | 未公开 | **1200 nits** | ❌ 同上 | 未公开 | 无电池 | ❌ 无 OS | **¥1299**（国补 ¥1113） |
| **雷鸟 Air 4 / Pro** | BirdBath + Vision 4000 芯片（HDR10） | 未公开 | **1200 nits** | ❌ 无内置，一站式近视配镜 | 76 g | 无电池 | ❌ 无 OS | ¥1599 / ¥1699 |
| **雷鸟 X3 Pro** | 全彩 Micro-LED + 衍射光波导（双目） | 30° | 官方 3500/6000 nits；⚠️ **实测眼盒最大 513 nits、中心 291 nits** | ❌ 无内置；磁吸夹片 / 全贴合定制（<4 g） | 76 g | 245 mAh；官方 24 h；⚠️ 评测实测 **0.5–1 h** | ⚠️ RayNeo AIOS（Android 底座），侧载体验差 | ¥8499（全贴合 ¥10999）；$1299 |
| **Even Realities G1** | 衍射光波导 + 双 Micro-LED（HAOS） | 25° | **1000 nits**（单色绿） | ❌ 无内置，处方镜片 +$150 | **43 g** | **约 1.5 天** | ❌ 封闭，仅官方 App | $599 / €699（+夹片 $100） |
| **小米 AI 眼镜** | ❌ **无显示模块** | — | — | ❌；线下 400 店验光定制 | **40 g** | 263 mAh，**8.6 h** | ❌ Vela OS 封闭 | ¥1999 / ¥2699 / ¥2999 |
| **Meta Ray-Ban Display** | 未公开（单目镜片内嵌） | 20° | 最高 **5000 nits**（口径未细分） | ❌ 无内置；处方 -4.00~+4.00 SPH、CYL≤4.00，+$200 | 69 g | 6 h + 盒 24 h | ❌ 不可装 APK；✅ 平台内置读屏器 | $799（国内 ¥9889） |
| **Dream Glass 4K** | 双 1080p 透视光学（非波导） | 90° | **未公开** | ❌ 无内置，可直接戴近视眼镜 | **185 g** + 控制盒 | 8000 mAh，约 5 h | ❌ 无 OS，HDMI/USB-C 显示器 | 原 $599；现 ¥298 清仓 ~ ¥5292 混乱报价 |
| **雷鸟 V3** | ❌ 无显示 | — | — | ❌；与博士眼镜合作配镜 | 39 g | 159 mAh，7 h | ❌ | ¥1799 起 |
| **【国内对标】瞳行「瞳者」AI 助盲眼镜** | 未公开（音频 + 手机协同为主） | — | — | 未公开 | 未公开 | 未公开 | ✅ **眼镜主体 + 手机 + 遥控指环 + 盲杖**四件套，Qwen-VL + OCR | 未公开 |

### 5.1 【重要参照】专业助视器价格锚点

| 产品 | 类型 | 价格 |
|---|---|---|
| OrCam MyEye 2 Pro | 专业助视（骨传导朗读、可穿戴） | **$4250**（2024-07 口径） |
| Envision Glasses Home Edition | 专业助视（Google Glass 底座 + 云端 OCR/AI） | **$2499**（2024-07 口径） |
| Seeing AI / Google Lookout | 手机 APP | **免费** |
| 瞳行「瞳者」 | 国产 AI 助盲眼镜（四件套） | 未公开 |

来源：[TVST 2025 年低视力 AI 助视对比研究](https://tvst.arvojournals.org/article.aspx?articleid=2802438) · [Seeing AI 官网](https://www.seeingai.com/) · [瞳者（百度百科）](https://baike.baidu.com/item/AI%E5%8A%A9%E7%9B%B2%E7%9C%BC%E9%95%9C/67050788) · [潮新闻/今日头条 发布报道](https://www.toutiao.com/article/7579472082422039046)

---

## 6. 作为白化病助视平台的可行性评估

### 6.0 用户临床基线（决定所有技术取舍的起点）

白化病的低视力特征与标准干预路径（来源：[大连盲聋学校《低视力的屈光矫正、选配助视器》](http://www.dltjxx.com/index.php?a=article&id=250)、[《康复辅助器具临床应用指南》](https://mingyi.sogou.com/h5/pages/book-detail?id=1953101312425984001_c8)、[AAO Low-Vision Aids](https://www.aao.org/eye-health/diseases/low-vision-aids)）：

- **屈光**：常伴**高度近视 + 中高度散光**，需矫正；部分可达 -10.00D 以上。
- **远用助视**：在矫正眼镜基础上加 **2.5× 双筒望远镜**；**出行时加用眩光眼镜/变色镜/太阳帽/大沿帽**。
- **近用助视**：眼镜式助视器 **+8.00D ~ +12.00D**（放大 2–3×，阅读距离 12.5–30 cm）；必要时 CCTV 电子助视器。
- **照明环境**：白化病推荐 **50 lx ~ 100 lx** —— 注意这个数字**远低于**常规阅读照明的 300–500 lx，说明临床目标是"**降低环境光 + 保对比度**"，而不是"把环境照亮"。
- **眼球震颤**：常合并，需先找**零点位/中间带**进行检影取功能性屈光度；眼位不稳定导致视细胞无法接受固定影像。
- **放大倍率需求（本项目 0.1~0.3 视力）**：按 Kestenbaum 法则 `放大率 = 1/视力（D）÷ 4`：
  - 视力 0.1（≈20/200）→ **2.5×**
  - 视力 0.2（≈20/100）→ **1.25×**
  - 视力 0.3（≈20/66）→ **约 0.8×，但考虑对比敏感度与眼震，实际仍需 1.5–2×**
  - → **项目应按 2–3× 的设计目标放大倍率做光学预算，而不是按 1× 假设。**

### 6.1 光学放大实现路径：摄像头+屏幕放大 vs 光学放大

这是整个项目**最根本的一条技术分叉**，必须先讲清楚一个事实：

> **消费级 AR 眼镜（BirdBath 与光波导两类都是）不放大真实世界。**
> BirdBath 的分光面是**平面**，透射光路没有角放大；衍射波导同理，只把光机图像"导"到眼前。
> 所以戴上任何一款 XREAL / 雷鸟 Air / Rokid Max，用户看黑板的清晰度**仍然是 0.1**。

因此只有两条路：

#### 路径 A：真·光学放大（望远镜式）

- 做法：在眼外光路加伽利略/开普勒望远系统，或做"AR 眼镜 = 望远镜的目镜"。
- 优点：**放大不消耗角分辨率**。望远镜是光子级的角放大，放大 2.5× 后像素/细节不损失，这是它至今仍是白化病标准远用方案的原因。
- 致命缺点：**视野随放大倍率成反比收缩**。低视力文献明确指出"戴着望远镜助视器上街行走是比较危险，因为此时视野较小"，且"放大倍率越高，视野越小，移动镜筒时物像向相反方向移动的速率也越快，需要经过训练才能交付使用"。2.5× 下可见真实视野只有几度到十几度。
- 与消费级 AR 的兼容性：**极差**。AR 眼镜的 Eyebox 通常只有 7×11 mm（Rokid Max）到 17×13 mm（X3 Pro 实测），FOV 20–57°。要在入射光路上叠一个 2.5× 望远系统并把出瞳对准 8–17 mm 的眼盒，工程上等价于"把一台双筒望远镜塞进眼镜框"，重量与体积不可接受。
- **结论**：路径 A 在产品形态上等同于现有**双筒望远镜助视器（头戴式/眼镜夹持式）**，属于"必须自研、也无法用消费级 AR 改造获得"的能力。但它是唯一不受分辨率限制的远用方案。

#### 路径 B：摄像头 → 电子放大 → 屏幕显示（消费级 AR 唯一可走的路径）

- 本质是**头戴式 CCTV 电子助视器**（低视力领域已有的成熟品类）。
- 优点：放大倍率可软件任意调、可叠加 OCR/增强对比度/边缘增强/滤色（黄底黑字等低视力常用模式）、可与朗读共存、可录制回看。
- **物理上限：由相机的角分辨率决定，而不是显示器。** 下面用公开参数算一笔账（**本文自算，非厂商数据，假设已注明**）：

  **假设**：12 MP 索尼 IMX681（本项目多数竞品采用），4000×3000 像素，水平 FOV ≈ 80°（超广角口径；Rokid Glasses 标注 109° 对角、小米 105°，取 80° 水平）。

  - 相机角分辨率 ≈ 4000 px ÷ 80° ≈ **50 px/° ≈ 0.83 px/arcmin**
  - 用户视力 0.1 ≈ 分辨极限 **10 arcmin**；舒适阅读需放大到极限的 3 倍 ≈ **30 arcmin**

  **近用场景（距离 40 cm，书本/试卷）**：
  1 cm 高汉字在 40 cm 处张角 ≈ 86 arcmin → 相机采样 ≈ **71 px 字高 / 约 10–12 px 笔画**。
  → **够清晰。近用放大路线成立。**

  **远用场景（课堂黑板，距离 6 m）**：
  粉笔字笔画宽约 1.5 cm，在 6 m 处张角 ≈ **8.6 arcmin**（实际粉笔字更细，取 5 arcmin 更保守）→ 相机采样仅 **约 4–7 px**。
  要放大到 30 arcmin，需要 **3.5×–6×** 放大倍率；放大后这 4–7 个源像素要铺满约 17 个显示像素（按 XREAL One Pro 1920 px / 57° ≈ 34 PPD 计）。
  → **结果是 4–7 px 的插值色块，不是字。** 放大倍率越高，越糊。

  **结论（三条工程约束）**：
  1. **近用（阅读、看试卷、看药品说明）**：摄像头+屏幕放大路线**可行**，消费级 AR 即可验证。
  2. **远用（黑板）**：摄像头+屏幕放大路线**受相机角分辨率硬限制，无法靠"调大倍率"解决**。唯一出路是把相机端采样率提上去——即**长焦/双摄融合（牺牲视野）或 1–2 亿像素级传感器**。这正是自研必须做的事。
  3. **黑板场景的正确产品形态可能不是"放大"，而是"OCR + 语义朗读"**：不传递像素，传递语义，彻底绕开分辨率瓶颈。这与 Seeing AI、Envision、瞳行「瞳者」都主推 OCR/语音而非画面放大，是同一个原因（参见 [TVST 2025 研究](https://tvst.arvojournals.org/article.aspx?articleid=2802438)：Text 任务完成率在 AI 助视下显著提升）。

#### 路径 A + B 的组合才是完整答案

| 场景 | 推荐路径 | 理由 |
|---|---|---|
| 课堂看黑板（6–10 m） | **B 的语义分支**：长焦/高像素相机 → OCR → 语音朗读 + 关键行放大 | 放大受分辨率限制；朗读不受限 |
| 课堂跟着看板书细节、图表 | A（2.5× 光学望远镜）或 B 的"注视点局部高清放大"（需长焦） | 图形/公式无法朗读 |
| 近用阅读、写作业、看屏幕 | B（摄像头+屏幕放大 2–3×） | 近距采样充足，可叠加对比度增强 |
| 出行（避障、看路牌、看公交） | B 的语义分支（OCR 播报 + 障碍提示） | 视野需大，放大反而有害 |

### 6.2 眼震下的防抖需求

这是本项目**最容易被低估、也最没有现成方案**的一条。

**核心事实**：眼球震颤是**眼球自身**的运动（常见波形为冲击型、钟摆型、混合型，主频大致在 1–10 Hz 量级），不是头部运动。当头戴显示随头一起运动时：

- 显示相对头是固定的 → 但眼在动 → **字仍然在视网膜上滑动**。因此：
  - ❌ **XREAL X1 芯片的 3DoF"空间锚定/悬停"不解决眼震**。它稳定的是"屏幕相对外部空间"，与眼球运动无关。这是一个极容易被误读为"AR 眼镜能治眼震"的技术陷阱，必须在项目文档中明确否定。
  - ❌ 头显的"防抖算法"（XREAL 宣传的"No Shaking & No Flicker"）针对的是**头动导致的画面迟滞/抖动**（M2P 延迟），不是眼震。
- **唯一真正有效的电子方案**：眼动跟踪 + 反向图像位移补偿（需要 ≥ 数百 Hz 眼动采样 + 亚帧级渲染延迟）。
  - **本次调研的全部 8 款消费级 AR 眼镜，均未公开具备眼动追踪能力**（XREAL One/One Pro/Air 2 Ultra、Rokid Glasses/Max、雷鸟 Air 3/3s/4/X3 Pro、Even G1、小米、Meta Display、Dream Glass 4K）。
  - → **眼震补偿是当前消费级 AR 生态里完全空白的能力，不存在"买现成方案"的选项。** 这既是风险，也是本项目最核心的差异化技术门槛（见 §7 路线 C）。
- **可用的间接缓解手段**（第一代产品可以考虑）：
  1. **让信息不依赖凝视**：主推 OCR + 语音朗读，从根本上绕开视网膜滑动。这是投入产出比最高的手段。
  2. **降低必需分辨力**：把字号放大到远超用户极限（≥5× 分辨极限），让一定量的视网膜滑动仍落在可辨识范围内；代价是信息密度下降（一屏字更少）。
  3. **大 Eyebox 支撑偏心注视 / 零点位代偿**：眼震患者习惯把视线偏到"中间带"以抑制震颤，需要眼盒足够大。本次调研中的实测/标称眼盒：**雷鸟 Air 3 为 14×7 mm**、**X3 Pro 实测 17×13 mm**、**Rokid Max 为 7×11 mm**。→ Eyebox 应作为选型/自研的关键指标之一，并要求"在 Eyebox 边缘仍能清晰成像"。
  4. **⚠️ 一个头戴形态的固有劣势必须提前想清楚**：眼震患者常用**头位代偿（转颈找到零点位）**来提升视力。但头戴显示器随头一起转，**头位代偿的收益被抵消了**；而手持/立式放大镜、桌面 CCTV 则保留代偿收益。这一点在做 1:1 原型时必须做对照测试（同一批被试：头戴 vs 手持 vs 桌面，测阅读速度与正确率），否则可能做出"技术上更先进但实际更难看"的产品。

### 6.3 畏光与亮度的矛盾

**矛盾陈述**：显示器要"压过"环境光（需要更亮），但白化病用户要"环境更暗"（临床推荐 50–100 lx，且处方里明确要求眩光眼镜/变色镜/太阳帽）。两者若都靠提高绝对亮度解决，会直接造成用户不适。

**正确的解法：把矛盾转移到"对比度"而不是"绝对亮度"**，并让"遮光"与"显示"解耦。

1. **BirdBath 结构天然占优（这是本次调研最重要的正面发现）**：
   XREAL One / One Pro / Air 2 Ultra、雷鸟 Air 3/3s/4、Rokid Max 都带**电致变色（EC）镜片**（XREAL 三档、Rokid Max 用偏振膜削减 90% 正面漏光）。其光路特征是：**外界透射光要穿过外侧镜片才到眼，而虚拟像由内部分光面反射入眼**（本项目对光学结构的判断，非厂商原文）。因此调暗 EC 相当于**压低背景、几乎不衰减虚拟像** → 得到"暗背景 + 亮字"的高对比画面。这**同时满足了畏光和对比度两个需求，是白化病用户最匹配的物理特性**。
   → **判断：BirdBath + 电致变色是本项目显示形态的首选，优先级高于光波导。**
2. **光波导（Rokid Glasses / X3 Pro / Meta Display / Even G1）在本项上天然劣势**：镜片近乎透明（X3 Pro 实测环境光透过率 74%），无法遮光。只能靠：
   - 加挂太阳镜夹片（Even G1 官方夹片 $100，PCMag 评价"户外日光下几乎是必需品"）；
   - 或靠高亮度硬顶。但 X3 Pro 的**实测值**（眼盒最大 513 nits、视场中心 291 nits）说明标称的 6000 nits 在真实使用条件下根本拿不到，户外可用性存疑。
   - 更关键的是：**在畏光用户的眼睛正前方放一个 1500–6000 nits 的小面积高亮光源，本身就是刺激源**。这是波导形态对白化病用户的根本不适配点。
3. **必须量化的验收指标（建议写入产品需求）**：
   - 在室外约 10⁴ lx 环境下，用户**不需要眯眼/不需要手遮挡**，可辨读 HUD 文字；
   - 提供**连续可调**的减光能力（不是三档，最好是无级），覆盖室内 ~300 lx 到正午室外 ~10⁵ lx；
   - 显示内容支持**低亮度 + 高对比**模式（低视力常用黄底黑字/黑底黄字的反向对比方案）；
   - 侧向挡光（侧挡/包覆式镜框）应作为标配，因为眩光来源不只是正前方。
4. **产品机会点**：畏光用户的"可调光太阳镜"与"信息呈现"其实是同一个产品需求。消费级 AR 眼镜要额外买夹片或另配墨镜，而**本项目可以把"医用级遮光 + HUD + 助视"做成一体**，这是相对消费级 AR 的明确差异化优势，也更容易获得临床与残联渠道的认可。

### 6.4 屈光适配

**难点**：白化病常见高度近视（可达 -10D 以上）+ 中高度散光 + 眼球震颤（需按零点位取功能性屈光度）。而消费级 AR 眼镜在屈光上普遍很弱：

| 屈光方案 | 产品 | 评价（针对白化病） |
|---|---|---|
| **内置旋钮调焦 0 ~ -6.00D** | 仅 **Rokid Max（及 Max 2/AR Spatial）** | 优点：唯一"不戴眼镜也能用"的方案，双眼独立、实时可调。<br>❌ 致命限制：**不支持散光**；上限 -6.00D，覆盖不了白化病常见的高度近视。仍要另配镜片。 |
| **处方镜片插入 / 磁吸夹片** | XREAL One / One Pro / Air 2 Ultra、Rokid Glasses、雷鸟 X3 Pro、雷鸟 V3 | ✅ 度数不受 -6D 限制，可做高近视 + 散光；✅ 成本相对可控（Rokid Glasses 官方支持近视/散光定制卡扣安装）。<br>❌ 磁吸夹片在 X3 Pro 上被官方提示有鬼影/色散问题（全贴合方案才解决，但 ¥10999）。 |
| **全贴合 / 一站式配镜** | 雷鸟 Air 3（1–600 度）、Air 4（一站式配镜）、X3 Pro 全贴合（<4 g，¥10999 版本） | ✅ 光学质量最好（X3 Pro 官方称解决鬼影与色散）。❌ 成本高、交付链路长（需验光 + 定制 + 装片）。 |
| **无内置、无处方方案** | Even G1（+$150）、Meta Ray-Ban Display（-4.00~+4.00 SPH、CYL≤4.00，+$200） | 度数范围对白化病不够（Evens 未公开范围；Meta 明确 ±4.00D 上限）。 |
| **可直接戴在日常眼镜外** | Dream Glass 4K | 仅此一款明确支持；但该产品已属上一代且 185 g。**"叠戴"路线值得保留为设计选项**，但需解决配重、杂光、双镜间距引起的视野缩减问题。 |

**本项目必须做对的三件事**：
1. **不采用内置旋钮调焦作为主方案**，因为散光不可调，而白化病散光率高。应以**全贴合定制处方镜片**为设计基线（这是雷鸟 X3 Pro 已经趟过的路），并把"镜片度数覆盖 -20D 以上 + 高散光 + 棱镜（如需）"写进供应商规格。
2. **必须解决"不戴 AR 时看不清"的依从性风险**。低视力用户若不戴这副眼镜就完全无法行动，会导致：① 用户不敢取下来；② 设备没电/维修期间用户失能；③ 电池与重量压力翻倍。→ 建议**产品在关机/无电状态下仍可作为普通矫正眼镜使用**（即"眼镜优先，AR 是附加层"），这也是 Even G1 的核心设计哲学。
3. **远用/近用是两套处方**（远用望远镜 vs 近用 +10D）。AR 眼镜只能提供一套物理屈光。→ 近用放大应通过**电子放大 + 屏幕虚像距离**实现，而不是靠换镜片；这一点需要与验配流程配合（验光时同时测远/近、零点位、对比敏感度）。

### 6.5 APP 生态

**能不能跑 Seeing AI / OCR，取决于三类架构**：

| 架构 | 代表产品 | 能否跑第三方 APP | 对低视力用户的可用性 |
|---|---|---|---|
| **① 纯显示眼镜**（无 OS、无芯片、无摄像头） | XREAL One / One Pro / Air 2 Ultra、雷鸟 Air 3 / 3s / 4、Rokid Max | ❌ 本体不能；只能镜像宿主手机画面 | ❌ **最差**。眼镜上没有任何触摸/按键输入，操作必须回到手机。低视力用户"在手机上找按钮、对着目标取景"本身就是最大的失败点。且这些眼镜**大多没有摄像头**（Air 3/4、Rokid Max、XREAL One 均无），无法自主取景。 |
| **② 分体式宿主**（眼镜 + 安卓计算设备） | XREAL + **Beam Pro**（$199 安卓设备）、Rokid Max + **Station / Station 2**（Android TV + Google Play）、**瞳行「瞳者」（眼镜 + 手机 + 遥控指环）** | ✅ **可以**（宿主设备跑 APP） | ✅ **最现实**。指环/遥控器给了低视力用户不需要精细触摸的输入通道；手机承担算力与联网，天然解决重量、发热、续航。这是国内助盲产品与 XREAL AURA 共同选择的架构。 |
| **③ 一体化 AI 眼镜**（有 SoC + OS + 摄像头） | 雷鸟 X3 Pro（RayNeo AIOS）、Rokid Glasses（YodaOS-Master）、Meta Ray-Ban Display（Meta 平台）、小米 AI 眼镜（Vela OS） | ⚠️ 理论可以，实际受限：Meta/小米封闭不可装 APK；X3 Pro 侧载被评价为"major headache"；Rokid Glasses 侧载能力未公开 | ⚠️ 交互（语音 + 镜腿触控）是为"轻量通知"设计的，不是为"长时间阅读/逐行校读"设计的。**Meta Ray-Ban Display 是唯一内置原生屏幕阅读器的产品**（AppleVis 视障用户实测确认），但它 600×600 单目、20° FOV，且处方上限 ±4.00D。 |

**最关键的一条判断**：

> **"能装 APP" ≠ "能用"。**
> Seeing AI / Envision / Google Lookout 的交互模型是为**"手持手机 + 触摸屏 + 把相机对准目标"**设计的。搬到眼镜上后，"取景"这一步消失，必须重建一整套"**看哪里 → 触发 → 捕获 → 朗读 → 逐行跟读**"的交互（包含眼动触发、指环触发、语音确认、朗读节奏控制、断行续读）。现成 APP 直接镜像到 AR 眼镜上，用户大概率会卡在"对准"和"翻页"两步。
> → **项目必须自研眼镜端 APP（至少自研交互层）**，而不是指望复用现成 APP；OCR/大模型能力可以复用（国内可用通义 Qwen-VL、豆包、混元等，如瞳行「瞳者」就是"基模复用 + 微调优化"的路径）。

**国内可参考的对标**：杭州瞳行的「瞳者」（2025-12-03 发布，国内首款 AI 助盲眼镜）——**分体式四件套（眼镜主体 + 手机 + 遥控指环 + 盲杖）**，121° 超广角双摄，通义千问 Qwen-VL + OCR，出行避障 300 ms 延迟，核心功能为"找、读、看、聊"，2026-01 入选行业榜单、2026-02 登上央视新闻。这条路线（**眼镜轻量化 + 手机算力 + 指环交互 + 保留盲杖/拐杖类传统辅具**）在架构上是本项目最应该深入研究的国产样本。

来源：[瞳者（百度百科）](https://baike.baidu.com/item/AI%E5%8A%A9%E7%9B%B2%E7%9C%BC%E9%95%9C/67050788) · [潮新闻](https://www.toutiao.com/article/7579472082422039046) · [太平洋电脑网](https://ai.pconline.com.cn/2030/20303613.html) · [AR Compare X3 Pro 生态评价](https://www.arcompare.com/ar-glasses/rayneo-x3-pro/) · [AppleVis 无障碍实测](https://www.applevis.com/comment/205397)

### 6.6 续航与佩戴：消费级 AI 眼镜的真实底线

这一项必须单独拉出来，因为它是本次调研中**最一致的负面结论**：

| 产品 | 官方续航 | 真实反馈 |
|---|---|---|
| 雷鸟 X3 Pro | "综合续航 24 h" | Tom's Hardware 最长约 **1 h**；Android Central 一个月测试**从未超过 30 分钟**；结论"poor battery makes them effectively unusable" |
| Rokid Glasses | "满工作续航 4 h" | AR Compare 记录**常显状态 2 h**；AI 功能走付费额度 |
| Meta Ray-Ban Display | 6 h | 5 款同类中最短（Front Desk Review 口径） |
| 小米 AI 眼镜 | 8.6 h | 但**无显示**，功耗结构完全不同 |
| Even G1 | 约 1.5 天 | 唯一达成全天候；代价是 640×200 / 20 Hz / 无摄像头 / 无扬声器 |
| 雷鸟 Air 3/3s/4、XREAL One/One Pro、Rokid Max | 无内置电池 | 续航转移到宿主；但 Air 系列实测**吃手机 20–30% 电量/2 h 电影** |

→ **结论**：**"带显示 + 带算力 + 带摄像头 + 全天候续航 + 轻量"这五件事在 2026 年没有一款消费级产品能同时做到。** 这正是"分体式"唯一合理的原因：把算力与电池从脸上拿下去，才能同时保住重量、续航和发热。任何"一体化眼镜形态"的本项目方案，都会正面撞上 X3 Pro 那 30 分钟的现实。

---

## 7. 结论：消费级 AR 改造 vs 自研分体式 AR

### 7.1 消费级 AR 能直接拿来用的部分（建议买现货）

| 能力 | 可直接采购 | 省下什么 |
|---|---|---|
| BirdBath Micro-OLED 光学模组 + 高入眼亮度 | 雷鸟 Air 3s（**¥1299**，1200 nits）、Air 4（¥1599）、XREAL One（$399） | 光学设计与量产工艺（2–3 年） |
| **电致变色遮光** | XREAL One/One Pro/Air 2 Ultra、雷鸟 Air 3/3s/4、小米 AI 眼镜（4 档 0.2 s）、Rokid Max（偏振减光） | 白化病最核心的"畏光"需求，直接命中 |
| 定制处方镜片供应链 | 雷鸟（1–600 度配镜、一站式配镜、全贴合 <4g）、Rokid（磁吸定制，支持散光）、博士眼镜 100+ 门店 | 验配渠道与服务链路 |
| 结构件与佩戴人机工学 | Even G1（43 g）、小米 AI 眼镜（40 g）、雷鸟 V3（39 g）的镜架方案 | 佩戴舒适度的行业答案 |
| 相机 + 云端大模型 + 语音 | 12 MP IMX681 是行业标准件；OCR/VLM 可用通义 Qwen-VL、豆包等（参考瞳行"基模复用 + 微调"） | AI 能力自建 |
| 安卓侧宿主 | XREAL Beam Pro（$199）、Rokid Station 2、以及"手机"这条最便宜的路径 | 应用生态从零起步 |

### 7.2 消费级 AR 改造"一定不够用"的部分（必须自研）

按严重程度排序：

1. **无眼震补偿能力**（全部 8 款均无眼动追踪）→ 这是低视力助视与消费级 AR 之间最大的能力鸿沟。
2. **相机角分辨率不足以支撑"黑板级"放大**（12 MP + 80° 广角 ≈ 0.83 px/arcmin，粉笔笔画仅 4–7 px）→ 需要长焦/双摄融合或超大像素传感器。
3. **屈光适配不足**：唯一带内置调焦的 Rokid Max 不支持散光且上限 -600 度；其余全靠定制镜片（成本/交期/复杂度）。
4. **交互模型不适配低视力**：无触摸、无取景框、无逐行跟读；语音触发在课堂场景（需要安静、不能频繁说话）尤其不适用。
5. **APP 生态"能装不能用"**：X3 Pro 侧载困难、Meta/小米封闭、显示眼镜无输入通道。
6. **续航**：带显示的 AI 眼镜实测 0.5–1 h；即使分体式，眼镜端显示功耗仍是真实约束。
7. **价格与残联采购量级错配**：¥8499（X3 Pro）/ ¥9889（Meta Display）/ ≤$1500（AURA）都远离"公益 + 残联采购"的预算带；本项目的价格锚点应该是 **雷鸟 Air 3s 的 ¥1299**、**Rokid Max 的清仓 $159**、**小米 AI 眼镜的 ¥1999**。

### 7.3 建议的路线（三档，逐级验证、逐级加码）

#### A 档｜近期（0–6 个月）：用现货做"可行性硬数据"，不出货

- **设备**：雷鸟 Air 3s（¥1299）或 XREAL One（$399）作显示端 + 手机/Beam Pro 跑 OCR；再配一台 **小米 AI 眼镜（¥1999，无显示、纯音频 + 遮光）** 作为对照。
- **要回答的四个问题**（每个都要量，不能靠主观）：
  1. 近用（看书/试卷）在 2–3× 电子放大下，阅读速度、正确率、可持续时长是多少？
  2. 黑板场景下，"放大画面"和"OCR 朗读"两种方式的完成率差多少？（预期：朗读显著占优，需数据确认）
  3. 头戴 vs 手持放大镜 vs 桌面 CCTV，三种形态下眼震被试的表现差多少？（检验 §6.2 中"头位代偿被抵消"的假设）
  4. 户外正午，用户是否需要眯眼？电致变色开到最大后能否舒适辨读？
- **样本量**：8–12 名白化病被试，覆盖视力 0.1 / 0.2 / 0.3 三档，招募可通过残联或白化病互助组织。
- **预算量级**：设备 + 测试 < ¥5 万。
- **交付物**：一份《消费级 AR 助视可行性实测报告》，直接决定 B 档的光学与相机规格。

#### B 档｜中期（6–18 个月）：自研分体式样机

**架构建议**（目标价 ¥1500–2500，与残联采购量级匹配）：

| 部件 | 放在哪 | 为什么 |
|---|---|---|
| BirdBath Micro-OLED 显示 + **电致变色（无级或 4 档以上）** | 眼镜端 | §6.3：唯一同时解决畏光与对比度的方案 |
| **全贴合定制处方镜片**（覆盖高近视 + 高散光） | 眼镜端 | §6.4：散光不可用旋钮解决 |
| **双摄：广角（避障/出行）+ 长焦（黑板/远距）** | 眼镜端 | §6.1：这是解决"黑板放大"的**唯一**硬件出路 |
| IMU + 大 Eyebox 光学设计（≥14×7 mm，目标 17×13 mm） | 眼镜端 | §6.2：支撑偏心注视/零点位与眼震下的容错 |
| 侧挡遮光 + 包覆式镜框 | 眼镜端 | §6.3：眩光不只在正前方 |
| **算力、电池、发热源** | **颈挂/口袋盒（分体）** | §6.6：X3 Pro 30 分钟续航的反面教材；同时保重量与续航 |
| **遥控指环 / 单键控制器 + 触觉反馈** | 手持 | §6.5：不需要精细触摸的输入通道（参考瞳行「瞳者」） |
| 眼镜端 APP（自研交互层） | 分体盒 / 手机 | §6.5："能装 APP ≠ 能用"，必须自研取景-朗读交互 |
| OCR / VLM 能力 | 复用云端（通义 Qwen-VL 等） | 不自建模型，学瞳行"基模复用 + 微调优化" |

**必须写入产品需求的验收线**（建议）：
- 远用：6 m 处粉笔字可被正确 OCR 并朗读，端到端延迟 ≤ 1 s（参考瞳行出行避障 300 ms 的口径）
- 近用：2–3× 电子放大下，阅读速度不低于用户的日常助视器表现
- 户外：10⁴ lx 环境下无需眯眼可辨读
- 续航：显示 + 持续 OCR 场景 ≥ 4 h（含分体盒换电）
- 重量：眼镜端 ≤ 80 g；整机（含分体盒 + 指环）不影响日常出行

#### C 档｜长期：眼动跟踪 + 反向补偿（技术分水岭）

- 这是**唯一能真正服务眼震用户**的技术路径（§6.2）。建议把它作为**第二代产品的立项门槛**，而不是第一代的门槛——成本、成熟度、供应链都不支持现在做。
- 第一代产品对眼震的策略应是**"绕开"而不是"解决"**：以 OCR + 朗读为主通道，以"大字 + 大 Eyebox"为视觉容错，并诚实告知用户"本产品不抑制眼球震颤"。**不要宣传任何形式的"防抖/稳定眼球震颤"能力**——现有消费级 AR 的所有"防抖"都是头动补偿，与眼震无关，宣传上混淆会带来严重的临床与合规风险。

### 7.4 一句话结论

> **消费级 AR 眼镜可以直接作为"近用 OCR 朗读 + 遮光 + 高对比显示"的验证平台和低配产品形态（¥1299–¥2499 区间已有可用现货），但不能直接当"课堂看黑板"的成品——黑板场景的放大受相机角分辨率硬限制，必须走"长焦双摄 + OCR 语义输出 + 遮光解耦"的自研分体式路线。**
>
> **消费级 AR 改造的价值在于：省下光学模组、电致变色遮光、处方镜片供应链和佩戴人机工学这四块 2–3 年的工程积累；自研的价值在于：长焦采样、屈光全贴合、无触摸交互、眼震绕开策略，以及把价格压到残联采购可承受的量级。**

---

## 附：全部来源 URL 清单

**XREAL**
- https://union-click.jd.com/jdc?e=&p=JF8BAaoJK1olWAcAVVxfD0kXBV8IGloWWQEKXFhbD0InRzBQRQQlBENHFRxWFlVWQDEXR0ROCBlQCgJDVBtKXnFYSR5NGlIcUVoabhJnX2dda1lNVQF3Cj4PfSxNBylaRDxwDxhaCwsJQVRORjNVFRlPGQpkBDs4eDFrSzNpGCYTAU9xKFpbfTYRVypsXRBMDWNsFhgJfCAWUGtOGghvJXF9CFsHHw9IWzFXRgtKCGNKFQpRCFxLUzdXeQFRUQYDVV1ZD0MfBWkPEmsUNFlSFgkiYykJfSZofhtXNX59ARw9BEcnB2kLHV8UXAcBZF5cCUoWCmcBE1klWQBsVTBdAU55UGcNGw4dCgMDB1pbC08fV18IGmtFMw4KXF5bDE0SA2YIK1olXQALXFhcCUsXB2YBGmsVVQIyg_fz3sex19aizOmXbTYyV25tOEgRM2w4RTUUWgNWVgteWiVLR2hdEgRCVWgFVl5VAEoSCl8KGloXXzYyZDgNbS5neRNARzoWIABeHS0hDE1ifmlcXj9TFl9SMTAfTh9jaG5bHx0UDnx6IyEBDREnA18PH1glXDY （京东 One Pro）
- https://gfan.com/info/592164.html
- https://sensorspecs.fyi/device/xreal-one-pro
- https://vrarwiki.com/index.php?direction=next&oldid=37075&title=Xreal_One_Pro
- https://www.digitaltrends.com/computing/xreal-one-review
- https://www.techradar.com/computing/virtual-reality-augmented-reality/xreal-one-review-top-notch-ar-smart-glasses-that-come-at-a-price
- https://frontdeskreview.com/product/smart-glasses/xreal-one
- https://www.arcompare.com/ar-glasses/xreal-air-2-ultra
- https://www.arcompare.com/compare/asus-airvision-m1-vs-xreal-air-2-ultra
- https://vrarwiki.com/index.php?curid=10129&diff=37034&title=Xreal_Air_2_Ultra
- https://www.xreal.com/ca/aura
- https://www.xreal.com/cz-en/aura
- https://m.sohu.com/a/1037947210_362042
- https://www.ubergizmo.com/2026/06/xreal-aura
- https://gcn.com/xreal-aura-android-xr-glasses-venice/21630

**Rokid**
- https://glasses.rokid.com/
- https://max.rokid.com
- https://global.rokid.com/products/rokid-ar-spatial
- https://www.arcompare.com/ar-glasses/rokid-glasses
- https://www.arcompare.com/compare/rokid-max-vs-viture-pro-xr
- https://smartglassesgeek.com/glasses/rokid-glasses
- https://www.tomsguide.com/computing/smart-glasses/i-just-tested-the-futuristic-rokid-glasses-bringing-ar-and-ai-together-to-make-meta-nervous
- https://www.vrtuoluo.cn/541407.html
- https://vrarwiki.com/index.php?title=Rokid_Max&diff=prev&oldid=37300
- https://forbespanama.com/rokid-glasses-carry-on-a-regular-basis-ar-to-ifa-2025

**雷鸟创新**
- https://www.tcl.com/ces
- https://rayneo.cn/
- https://www.rayneo.com/blogs/news/best-smart-glasses-2026-guide
- https://www.arcompare.com/ar-glasses/rayneo-x3-pro/
- https://wearablexp.com/smart-glasses/rayneo-x3-pro-review/
- https://www.ithome.com/0/891/877.htm
- https://news.qq.com/rain/a/20251024A03OEB00
- https://www.news.cn/tech/20251024/8390fb0b04584412be742f11fd92070f/c.html
- https://www.pconline.com.cn/zhizao/1832/18329870.html
- https://microled.cn/news/3860.html
- https://baike.baidu.com/item/%E9%9B%B7%E9%B8%9FAir%203/65042219
- https://digitalproducer.com/rayneo-showcases-new-ar-lineup-at-ces-2025/amp
- https://www.etcentric.org/ces-tcl-introduces-three-models-of-rayneo-smart-glasses/
- https://union-click.jd.com/jdc?e=&p=JF8BATIJK1olWAcEVF1ZCUkRC18IGloWXg8FU15YCkInRzBQRQQlBENHFRxWFlVPRjtUBABAQlRcCEBdCUoUAGYPHFsQXw8dDRsBVXsWeR1DUFxPVGZgEDwtcCBCVAtcaShDUQoyUFheDk8WAm4LK1sUXAcDXVZUAEknB2lmGjUVVANsVFkODUMfA2ddGAkQWFIFXG5dCXtVbbeinYOc89Gq34ndvpyomruAlWsUbQYEXVZbCUoXA28NElMlXQ4GZIn0pp2bpbuxsYyn3zYyZF1tOHsXM2w4RTUUWgNWVgteWCVLR2hdEgEVVGgFVl5VC04UAl8KGloXXzYyZAUbaE5SQxRyQydeNEZfDB49fxJVai9hYC9cB2BfNDBffChnfThJWA1oBUYFNgVbTDInA18PH1glXDY （京东 X3 Pro）
- https://union-click.jd.com/jdc?e=&p=JF8BARQJK1olXDYCVV9fCEMVBGcBGlolGVlaCgFtUQ5SQi0DBUVNGFJeSwUIFxlJX3EIGloXXQ4AU1ZUCUoIWipURmtXAAZDPQAJey5jAA98ZVl1X0RKMlYbBEcnB2kLHV8UXAcBZF5cCUoWCmcBE1klWQBsVTBdAU55C20LGgtCCFILUgtZCkIfC18IGmteMwcyVW5dDkIfBW4JG1kRVAcAZF5VDHvAqsHel_3B5KzV5txtOHsUM184G2sWbVhsVVlYXBsUCm5mRx8SCA4BFh4zD0kUAmkAG1glXwcDVlxtOHtMCmt-YwZ9I1kKPAM0CTsfYjxobFhMCmd-IxxdDSUVZRtOUh8QIHZVETcGaS1SUGY4G2slXDY （京东 Air 3S）
- https://union-click.jd.com/jdc?e=&p=JF8BARQJK1olXDYCVV9fCEMSBG4IH1wlGVlaCgFtUQ5SQi0DBUVNGFJeSwUIFxlJX3EIGloXXQ4HU19dDEwIWipURmtiFHgAFAVfTSt-fS9ccwIXXFlaKVctBEcnB2kLHV8UXAcBZF5cCUoWCmcBE1klWQBsVTBdAU55BW5bGA4WDVFVUFcNDx4UCl8IGmteMwcyVW5dDkIfBW4JG10VVQQLZF5VDHvAqsHel_3B5KzV5txtOHsUM184G2sWbVhsVVlYCUISUT1mRx8SCA5GCggzD0kUAGcJHVwlXwcDVlxtOHtpdDV-HTsQXGF0UlsLVAxQfjFPEjAUG3x8AzotDSUVBW1jEyYWWlNEKwggDjIVVAw4G2slXDY （京东 V3）
- https://ima.qq.com/wiki/?shareId=1ad13190d4f7ee3f55dd1d907b377344ac1f66c5c8570af323d2e86764b138aa （长城证券 CES 2025 / 小米研报存档）

**其他产品**
- https://au.pcmag.com/wearables/110274/even-realities-g1
- https://www-tomsguide-com.translate.goog/computing/smart-glasses/even-realities-g1-smart-glasses-review
- https://xpert.digital/en/even-realities-g1/
- https://nexttechbuy.com/?p=9723/
- https://www.mi.com/shop/buy/detail?product_id=21399
- https://article.pchome.net/info/4339.html
- https://www.guru3d.com/story/xiaomi-launches-smart-glasses-with-voice-assistant-and-ai-translation/
- https://en.tempo.co/read/2022856/xiaomi-gearing-up-for-ai-glasses-debut-to-rival-ray-ban-meta
- https://ima.qq.com/wiki/?shareId=df0c9577d6377f32145e18671de1da856a35adc9a0b3f0c9199932d9ee36fd20 （国泰海通研报存档）
- https://www.malaysianwireless.com/2025/09/meta-ray-ban-display-gen-2-smart-glasses/
- https://www.arcompare.com/reviews/ray-ban-meta-display/
- https://frontdeskreview.com/product/smart-glasses/ray-ban-meta-display
- https://www.applevis.com/comment/205397
- https://vrarwiki.com/index.php?oldid=37231&title=Dream_Glass_4K
- https://vrarwiki.com/index.php?diff=prev&oldid=37389&title=Dream_Glass_4K
- https://www.techbloat.com/review-dreamglass-4k-straps-a-big-screen-tv-to-your-noggin.html
- https://www.sohu.com/a/1067442741_122645258
- https://shuma.taobao.com/topic/zhinengyanjing_1140/99f45cc424ef1eff5e2d4f17f08c77d3.html
- https://setupai.cc/update/viture-launches-323b2207 （VITURE Beast 对比数据）

**临床与低视力助视依据**
- http://www.dltjxx.com/index.php?a=article&id=250 （低视力屈光矫正与助视器选配，白化病/眼球震颤专节）
- https://mingyi.sogou.com/h5/pages/book-detail?id=1953101312425984001_c8 （《康复辅助器具临床应用指南》低视力适配）
- https://mingyi.sogou.com/h5/pages/book-detail?id=2031281293060210690_c4 （眼镜式助视器：×1 = +4.00D 换算）
- https://www.aao.org/eye-health/diseases/low-vision-aids （AAO Low-Vision Aids / Kestenbaum 法则）
- https://www.familydoctor.com.cn/oculus/info/201004/592716421585.html （放大原理与远用助视器处方原则）
- https://tvst.arvojournals.org/article.aspx?articleid=2802438 （TVST 2025：OrCam / Envision / Seeing AI / Lookout 对照研究）
- https://www.seeingai.com/
- https://visionscienceacademy.org/augmented-reality-the-modern-elpis-among-the-eye-care-practitioners/amp
- https://www.visiononline.org/blog-article.cfm/Augmented-Reality-Glasses-Aid-Patients-with-Low-Vision/232
- https://healthtechdigital.com/how-are-people-with-vision-loss-actually-using-smart-glasses

**国内助视对标**
- https://baike.baidu.com/item/AI%E5%8A%A9%E7%9B%B2%E7%9C%BC%E9%95%9C/67050788 （瞳行「瞳者」）
- https://www.toutiao.com/article/7579472082422039046
- https://ai.pconline.com.cn/2030/20303613.html
- https://www.c114pro.com/ainews/130274.html

---

## 附录 2：本文的"未公开"清单（禁止在后续文档中填空猜测）

| 项目 | 缺失参数 |
|---|---|
| XREAL AURA | 入眼亮度、屈光调节范围、眼镜本体续航、重量精确值（仅"<95 g"） |
| 雷鸟 Air 4 / Air 4 Pro | FOV、分辨率（官方仅给"135 英寸巨幕"） |
| 雷鸟 Air 3s | FOV、重量、Eyebox |
| 雷鸟 X3 Pro | 真实使用条件下的续航（官方 24 h 与实测 0.5–1 h 冲突，需以实测为准） |
| Rokid Glasses | 第三方 APK 侧载是否可行（YodaOS-Master 开放度未公开） |
| Even Realities G1 | 处方镜片可支持的度数上限；FOV 亦有两套口径（20° / 25°） |
| 小米 AI 眼镜 | 处方镜片可支持的度数上限 |
| Meta Ray-Ban Display | 显示技术路线（波导 / LCoS / 全息反射均无官方确认） |
| Dream Glass 4K | 亮度（vrarwiki 明确"Not specified"）；当前官方在售状态（官网本次无法访问） |
| 瞳行「瞳者」 | 重量、续航、FOV、价格、光学方案 |
