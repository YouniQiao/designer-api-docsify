# @ohos.graphics.text

文本模块


**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

## 导入模块

```TypeScript
import { text } from 'kits/@kit.ArkGraphics2D';
```

## 汇总

### 函数

| 名称 |
| --- |
| [getFontCount](arkts-arkgraphics2d-text-getfontcount-f.md) |
| [getFontDescriptorByFullName](arkts-arkgraphics2d-text-getfontdescriptorbyfullname-f.md) |
| [getFontDescriptorsFromPath](arkts-arkgraphics2d-text-getfontdescriptorsfrompath-f.md) |
| [getFontPathsByType](arkts-arkgraphics2d-text-getfontpathsbytype-f.md) |
| [getFontUnicodeSet](arkts-arkgraphics2d-text-getfontunicodeset-f.md) |
| [getSystemFontFullNamesByType](arkts-arkgraphics2d-text-getsystemfontfullnamesbytype-f.md) |
| [isFontSupported](arkts-arkgraphics2d-text-isfontsupported-f.md) |
| [matchFontDescriptors](arkts-arkgraphics2d-text-matchfontdescriptors-f.md) |
| [setTextHighContrast](arkts-arkgraphics2d-text-settexthighcontrast-f.md) |
| [setTextUndefinedGlyphDisplay](arkts-arkgraphics2d-text-settextundefinedglyphdisplay-f.md) |

### 类

| 名称 |
| --- |
| [FontCollection](arkts-arkgraphics2d-text-fontcollection-c.md) |
| [LineTypeset](arkts-arkgraphics2d-text-linetypeset-c.md) |
| [Paragraph](arkts-arkgraphics2d-text-paragraph-c.md) |
| [ParagraphBuilder](arkts-arkgraphics2d-text-paragraphbuilder-c.md) |
| [Run](arkts-arkgraphics2d-text-run-c.md) |
| [TextLine](arkts-arkgraphics2d-text-textline-c.md) |

### 接口

| 名称 |
| --- |
| [Decoration](arkts-arkgraphics2d-text-decoration-i.md) |
| [FontDescriptor](arkts-arkgraphics2d-text-fontdescriptor-i.md) |
| [FontFeature](arkts-arkgraphics2d-text-fontfeature-i.md) |
| [FontVariation](arkts-arkgraphics2d-text-fontvariation-i.md) |
| [FontVariationAxis](arkts-arkgraphics2d-text-fontvariationaxis-i.md) |
| [FontVariationInstance](arkts-arkgraphics2d-text-fontvariationinstance-i.md) |
| [LineMetrics](arkts-arkgraphics2d-text-linemetrics-i.md) |
| [ParagraphStyle](arkts-arkgraphics2d-text-paragraphstyle-i.md) |
| [PlaceholderSpan](arkts-arkgraphics2d-text-placeholderspan-i.md) |
| [PositionWithAffinity](arkts-arkgraphics2d-text-positionwithaffinity-i.md) |
| [Range](arkts-arkgraphics2d-text-range-i.md) |
| [RectStyle](arkts-arkgraphics2d-text-rectstyle-i.md) |
| [RunMetrics](arkts-arkgraphics2d-text-runmetrics-i.md) |
| [StrutStyle](arkts-arkgraphics2d-text-strutstyle-i.md) |
| [TextBox](arkts-arkgraphics2d-text-textbox-i.md) |
| [TextLayoutResult](arkts-arkgraphics2d-text-textlayoutresult-i.md) |
| [TextRectSize](arkts-arkgraphics2d-text-textrectsize-i.md) |
| [TextShadow](arkts-arkgraphics2d-text-textshadow-i.md) |
| [TextStyle](arkts-arkgraphics2d-text-textstyle-i.md) |
| [TextTab](arkts-arkgraphics2d-text-texttab-i.md) |
| [TypographicBounds](arkts-arkgraphics2d-text-typographicbounds-i.md) |

### 枚举

| 名称 |
| --- |
| [Affinity](arkts-arkgraphics2d-text-affinity-e.md) |
| [BreakStrategy](arkts-arkgraphics2d-text-breakstrategy-e.md) |
| [EllipsisMode](arkts-arkgraphics2d-text-ellipsismode-e.md) |
| [FontStyle](arkts-arkgraphics2d-text-fontstyle-e.md) |
| [FontWeight](arkts-arkgraphics2d-text-fontweight-e.md) |
| [FontWidth](arkts-arkgraphics2d-text-fontwidth-e.md) |
| [LineHeightStyle](arkts-arkgraphics2d-text-lineheightstyle-e.md) |
| [PlaceholderAlignment](arkts-arkgraphics2d-text-placeholderalignment-e.md) |
| [RectHeightStyle](arkts-arkgraphics2d-text-rectheightstyle-e.md) |
| [RectWidthStyle](arkts-arkgraphics2d-text-rectwidthstyle-e.md) |
| [SystemFontType](arkts-arkgraphics2d-text-systemfonttype-e.md) |
| [TextAlign](arkts-arkgraphics2d-text-textalign-e.md) |
| [TextBadgeType](arkts-arkgraphics2d-text-textbadgetype-e.md) |
| [TextBaseline](arkts-arkgraphics2d-text-textbaseline-e.md) |
| [TextDecorationStyle](arkts-arkgraphics2d-text-textdecorationstyle-e.md) |
| [TextDecorationType](arkts-arkgraphics2d-text-textdecorationtype-e.md) |
| [TextDirection](arkts-arkgraphics2d-text-textdirection-e.md) |
| [TextDisplayState](arkts-arkgraphics2d-text-textdisplaystate-e.md) |
| [TextHeightBehavior](arkts-arkgraphics2d-text-textheightbehavior-e.md) |
| [TextHighContrast](arkts-arkgraphics2d-text-texthighcontrast-e.md) |
| [TextProcessState](arkts-arkgraphics2d-text-textprocessstate-e.md) |
| [TextUndefinedGlyphDisplay](arkts-arkgraphics2d-text-textundefinedglyphdisplay-e.md) |
| [TextVerticalAlign](arkts-arkgraphics2d-text-textverticalalign-e.md) |
| [WordBreak](arkts-arkgraphics2d-text-wordbreak-e.md) |

### 类型

| 名称 |
| --- |
| [CaretOffsetsCallback](arkts-arkgraphics2d-text-caretoffsetscallback-t.md) |
