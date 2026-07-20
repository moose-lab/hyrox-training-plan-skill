# Uniform Output Card Format · 输出卡片统一规范

All rendered deliverables (weekly overviews, daily cards, universal templates) MUST follow this
format. The goal: **numbers over prose, visual encodings over paragraphs, one glance = one week.**

## Deliverable set

| 场景 | 交付物 | 画布 |
|---|---|---|
| 周概览 weekly overview | 1 张卡:`txt + html + png`;memo 便签仅在用户要求时追加 | 卡 1080 × auto ≤1700px @1x |
| 单日课 daily session | 卡 `txt + html + png`;memo 便签仅在用户要求时追加 | 卡固定 1080×1920 |
| 通用模板 universal | 同周概览 | 1080 × auto |
| memo 便签(应约) | `html + png`,走 `templates/memo-note.html` | 1080 × auto ≤2400px @1x |

命名:`exports/hyrox-card-YYYY-MM-DD-<slug>.{txt,html,png}`
周概览 slug:`build-wN-overview`(双人默认)/ `singles-build-wN-overview`。

## Design tokens(所有卡共用)

```css
--paper:#F1EFE9; --ink:#121212; --panel:#FFFFFF; --soft:#E7E4DA; --hyx:#FFD900;
font-family:-apple-system,"PingFang SC","Noto Sans SC","Microsoft YaHei",sans-serif;
面板:白底 + 3px 墨黑边框 + 16px 圆角;强调 = HYROX 黄底/黄色荧光笔下划。
```

## Word budgets(硬性,超了删内容、不缩字号)

- 日程行:课名 ≤10 字,副行 ≤14 字,数值放独立数值列(数字优先)
- 章节用 **caption 式小标题**(12px 字距拉宽灰字),不用大号 sec-head
- 教练提示:**单行 ≤40 字**,全卡禁止段落文字
- 进阶对比:只写 `旧值 → 新值`,理由进 txt,不上卡
- txt 文件是完整文字版,细节和 rationale 都写在 txt 里,卡片只承载结构和数字

## Visual encodings(用图形替代文字)

1. **阶段进度条**:BASE|BUILD|PEAK|TAPER 四段横条,当前阶段黄底 + 段内周刻度(■□),已过阶段墨黑
2. **强度点**:每天 5 格方点 ■■■■□,easy=2 quality=4 strength=3 recovery=1 rest=0(休息行整行反色,配月亮图标)
3. **分布条**:按课型数的比例条(有氧/质量/力量/休),旁挂 `80/20 极化` `有氧≥60% ✓` 徽章
4. **进阶 chips**:`90–120″ → 75–105″` 带 ↑↓ 方向,一格一个变量
5. 质量日 tag 黄底描边,其余 soft 灰底

## Weekly overview 结构(自上而下,7 个部件)

1. 页眉:division logo 块 + 大标题 + 日期范围块(沿用日卡页眉)
2. 阶段进度条 panel
3. 进阶 chips panel(≤4 格,单变量原则)
4. 7 天日程 panel:每天一行 `[周几+日期][icon][课名+副行][数值][强度点][tag]`,行高 ≤60px;底部嵌分布条 strip
5. 教练一行(虚线框)
6. NEXT 墨黑条:下周关键数字,单行
7. credit 行:`#tags` + skill 署名

模板:`templates/weekly-overview-card.html`(`{{TOKEN}}` 占位,日程行注释标记可重复)。
单日卡继续沿用既有 5 分区 1080×1920 版式(见 exports/ 里 zone2-run / threshold-run 范例)。

## Memo 便签格式(应约交付,模板 `templates/memo-note.html`,两档通用)

定位:**卡片承载结构和数字,便签只承载"为什么"**——两者不重复内容。
保留胶带 + 米色便签视觉身份,但排版结构化,禁止段落散文。共用骨架:

1. 标题 + 日期行
2. `LOGIC` 区:≤3 条,黑方点 + **粗体引子(≤8字)** + 尾句(≤18字)
3. `WHY` 区:恰好 N 行 `[chip][名称≤10字][why ≤20字]`,虚线分隔
4. 教练一行(黄底框,≤40字)
5. NEXT 一行 + tags + credit

两个档位(只有 WHY 行定义不同):

| 档位 | LOGIC | WHY 行 | chip | 黄 chip 行 | NEXT |
|---|---|---|---|---|---|
| **周档** weekly | 本周逻辑 | 每天 1 行 ×7 | 周几+日期 | 休息日 | 下周数字 |
| **日档** daily | 今日逻辑 | 每段 1 行 ×5(热身/主课/技巧/冷身/纪律) | ①–⑤+时长或RPE | 主课行 | 明日课 |

硬预算:任何一行 ≤26 字;总高 ≤2400px @1x(超了删字,不缩字号)。
范例:周档 `exports/hyrox-memo-2026-07-20-build-w2-overview.*`;日档 `exports/hyrox-memo-2026-07-21-station-compound.*`。

## Render & verify

```bash
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
# 变高卡:先取 data-h,再按高截图(模板 <script> 会把卡片高度写入 body data-h)
"$CHROME" --headless --disable-gpu --virtual-time-budget=2000 --dump-dom "file://…/card.html" | grep -o 'data-h="[0-9]*"'
"$CHROME" --headless --disable-gpu --hide-scrollbars --force-device-scale-factor=2 \
  --window-size=1080,<data-h> --screenshot="…/card.png" "file://…/card.html"
```

渲染后必须 Read PNG 核验:无裁切、行未换行溢出、周概览高度 ≤1700px @1x(超了 = 内容超预算,删字)。
