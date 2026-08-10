# ParagraphStyle

段落样式，用于控制段落的整体布局行为，包括对齐方式、断行策略和最大行数等属性。ParagraphStyle作为[ParagraphBuilder](arkts-arkgraphics2d-text-paragraphbuilder-c.md)构造函数的必要参数，与  
[TextStyle](arkts-arkgraphics2d-text-textstyle-i.md)（控制文本级别样式）分工协作，共同决定段落的最终排版效果。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-text-interface ParagraphStyle--><!--Device-text-interface ParagraphStyle-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { text } from 'kits/@kit.ArkGraphics2D';
```

## align

```TypeScript
align?: TextAlign
```

文本对齐方式，默认为START。若同时配置tab属性，制表符对齐方式将失效。

**Type:** [TextAlign](arkts-arkgraphics2d-text-textalign-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-ParagraphStyle-align?: TextAlign--><!--Device-ParagraphStyle-align?: TextAlign-End-->

**System capability:** SystemCapability.Graphics.Drawing

## autoSpace

```TypeScript
autoSpace?: boolean
```

设置文本排版时是否使能自动间距。true表示使能自动间距，则会在文本排版时自动调整CJK（中文字符、日文字符、韩文字符）与西文（拉丁字母、西里尔字母、希腊字母）、CJK与数字、CJK与版权符号、版权符号与数字、版权符号与西文之间的间距。false表示不使能自动间距，默认值为false。

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-ParagraphStyle-autoSpace?: boolean--><!--Device-ParagraphStyle-autoSpace?: boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

## breakStrategy

```TypeScript
breakStrategy?: BreakStrategy
```

断行策略，默认为GREEDY。

**Type:** [BreakStrategy](arkts-arkgraphics2d-text-breakstrategy-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-ParagraphStyle-breakStrategy?: BreakStrategy--><!--Device-ParagraphStyle-breakStrategy?: BreakStrategy-End-->

**System capability:** SystemCapability.Graphics.Drawing

## compressHeadPunctuation

```TypeScript
compressHeadPunctuation?: boolean
```

设置文本排版时是否使能行首标点压缩。true表示使能行首标点压缩，false表示不使能行首标点压缩，默认值为false。

**说明：**

1. 需要字体文件支持[FontFeature](arkts-arkgraphics2d-text-fontfeature-i.md)中的"ss08"特性，否则无法压缩。2. 在行首标点压缩范围内的标点才在本特性作用范围内。行首压缩的标点范围:  
| 标点 | Unicode码位 | Unicode名称 |  
|---------|---------|-------------|  
| 「 | U+300C | LEFT CORNER BRACKET |  
| 『 | U+300E | LEFT WHITE CORNER BRACKET |  
| " | U+201C | LEFT DOUBLE QUOTATION MARK |  
| ' | U+2018 | LEFT SINGLE QUOTATION MARK |  
| （ | U+FF08 | FULLWIDTH LEFT PARENTHESIS |  
| 《 | U+300A | LEFT DOUBLE ANGLE BRACKET |  
| 〈 | U+3008 | LEFT ANGLE BRACKET |  
| 【 | U+3010 | LEFT BLACK LENTICULAR BRACKET |  
| 〖 | U+3016 | LEFT WHITE LENTICULAR BRACKET |  
| 〔 | U+3014 | LEFT TORTOISE SHELL BRACKET |  
| ［ | U+FF3B | FULLWIDTH LEFT SQUARE BRACKET |  
| ｛ | U+FF5B | FULLWIDTH LEFT CURLY BRACKET |

**Type:** boolean

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ParagraphStyle-compressHeadPunctuation?: boolean--><!--Device-ParagraphStyle-compressHeadPunctuation?: boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

## fallbackLineSpacing

```TypeScript
fallbackLineSpacing?: boolean
```

设置文本排版时是否使能行高回退，当设置的行高小于实际行高时，将行高回退为实际行高。true表示使能行高回退，false表示不使能行高回退，默认值为false。

**Type:** boolean

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ParagraphStyle-fallbackLineSpacing?: boolean--><!--Device-ParagraphStyle-fallbackLineSpacing?: boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

## firstLineHeadIndent

```TypeScript
firstLineHeadIndent?: double
```

设置段落首行缩进，缩进值需大于等于0，单位为物理像素px，默认值为0。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ParagraphStyle-firstLineHeadIndent?: double--><!--Device-ParagraphStyle-firstLineHeadIndent?: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

## headIndents

```TypeScript
headIndents?: Array<double>
```

设置行首缩进数组，数组中每个元素代表一行缩进值，当实际文本行数超过缩进数组个数时，超过行的缩进为数组最后一个值，缩进值需全大于等于0，单位为物理像素px，默认为空数组。

**Type:** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;double&gt;

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ParagraphStyle-headIndents?: Array<double>--><!--Device-ParagraphStyle-headIndents?: Array<double>-End-->

**System capability:** SystemCapability.Graphics.Drawing

## includeFontPadding

```TypeScript
includeFontPadding?: boolean
```

设置文本排版时是否使能首尾行padding。true表示使能首尾行padding，false表示不使能首尾行padding，默认值为false。

**Type:** boolean

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ParagraphStyle-includeFontPadding?: boolean--><!--Device-ParagraphStyle-includeFontPadding?: boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

## lineSpacing

```TypeScript
lineSpacing?: double
```

行间距，单位为物理像素px，默认值为0。lineSpacing不受[TextStyle](arkts-arkgraphics2d-text-textstyle-i.md)中lineHeightMaximum和lineHeightMinimum限制。尾行默认保留行间距，可通过设置[ParagraphStyle](arkts-arkgraphics2d-text-paragraphstyle-i.md)的textHeightBehavior为DISABLE_ALL或DISABLE_LAST_ASCENT禁用尾行行间距。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-ParagraphStyle-lineSpacing?: double--><!--Device-ParagraphStyle-lineSpacing?: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

## maxLines

```TypeScript
maxLines?: int
```

最大行数限制，整数，默认为1e9。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-ParagraphStyle-maxLines?: int--><!--Device-ParagraphStyle-maxLines?: int-End-->

**System capability:** SystemCapability.Graphics.Drawing

## orphanCharOptimization

```TypeScript
orphanCharOptimization?: boolean
```

设置文本排版时是否使能孤字优化。孤字优化通过更高效地处理孤立字符（段落尾行首字符）来改善文本布局。使能后，它会调整换行点以尽可能避免孤立字符。孤字优化特性需在[wordBreak](arkts-arkgraphics2d-text-wordbreak-e.md)为非BREAK_ALL并且待排版文本首个[TextStyle](arkts-arkgraphics2d-text-textstyle-i.md)的locale为“zh-Hans”或“zh-Hant”时生效。true表示使能孤字优化，false表示不使能孤字优化，默认值为false。

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ParagraphStyle-orphanCharOptimization?: boolean--><!--Device-ParagraphStyle-orphanCharOptimization?: boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

## punctuationOverflow

```TypeScript
punctuationOverflow?: boolean
```

设置文本排版时是否使能行尾标点悬挂。true表示使能行尾标点悬挂，允许行尾单个标点超出排版宽度而不换行，false表示不使能行尾标点悬挂，默认值为false。

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ParagraphStyle-punctuationOverflow?: boolean--><!--Device-ParagraphStyle-punctuationOverflow?: boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

## strutStyle

```TypeScript
strutStyle?: StrutStyle
```

支柱样式，默认为初始的StrutStyle。

**Type:** [StrutStyle](arkts-arkgraphics2d-text-strutstyle-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-ParagraphStyle-strutStyle?: StrutStyle--><!--Device-ParagraphStyle-strutStyle?: StrutStyle-End-->

**System capability:** SystemCapability.Graphics.Drawing

## tab

```TypeScript
tab?: TextTab
```

表示段落中文本制表符后的文本对齐方式及位置，默认将制表符替换为一个空格。此参数与文本对齐方式（align属性）或省略号样式（[TextStyle](arkts-arkgraphics2d-text-textstyle-i.md)中的ellipsis属性）共同配置时无效。

**Type:** [TextTab](arkts-arkgraphics2d-text-texttab-i.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-ParagraphStyle-tab?: TextTab--><!--Device-ParagraphStyle-tab?: TextTab-End-->

**System capability:** SystemCapability.Graphics.Drawing

## tailIndents

```TypeScript
tailIndents?: Array<double>
```

设置行尾缩进数组，数组中每个元素代表一行缩进值，当实际文本行数超过缩进数组个数时，超过行的缩进为数组最后一个值，缩进值需全大于等于0，单位为物理像素px，默认为空数组。

**Type:** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;double&gt;

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ParagraphStyle-tailIndents?: Array<double>--><!--Device-ParagraphStyle-tailIndents?: Array<double>-End-->

**System capability:** SystemCapability.Graphics.Drawing

## textDirection

```TypeScript
textDirection?: TextDirection
```

文本方向，默认为LTR。

**Type:** [TextDirection](arkts-arkgraphics2d-text-textdirection-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-ParagraphStyle-textDirection?: TextDirection--><!--Device-ParagraphStyle-textDirection?: TextDirection-End-->

**System capability:** SystemCapability.Graphics.Drawing

## textHeightBehavior

```TypeScript
textHeightBehavior?: TextHeightBehavior
```

文本高度修饰符模式，默认为ALL。

**Type:** [TextHeightBehavior](arkts-arkgraphics2d-text-textheightbehavior-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-ParagraphStyle-textHeightBehavior?: TextHeightBehavior--><!--Device-ParagraphStyle-textHeightBehavior?: TextHeightBehavior-End-->

**System capability:** SystemCapability.Graphics.Drawing

## textStyle

```TypeScript
textStyle?: TextStyle
```

作用于整个段落的文本样式，默认为初始的文本样式。

**Type:** [TextStyle](../../apis-arkui/arkts-apis/arkts-arkui-styledstring-textstyle-c.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-ParagraphStyle-textStyle?: TextStyle--><!--Device-ParagraphStyle-textStyle?: TextStyle-End-->

**System capability:** SystemCapability.Graphics.Drawing

## trailingSpaceOptimized

```TypeScript
trailingSpaceOptimized?: boolean
```

表示文本排版时是否考虑行尾空格的对齐影响。true表示忽略行尾空格的对齐影响，false表示考虑行尾空格的对齐影响，默认值为false。

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-ParagraphStyle-trailingSpaceOptimized?: boolean--><!--Device-ParagraphStyle-trailingSpaceOptimized?: boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

## verticalAlign

```TypeScript
verticalAlign?: TextVerticalAlign
```

文本垂直对齐方式，默认为BASELINE，即文本基线对齐。开启行高缩放（即设置[TextStyle](arkts-arkgraphics2d-text-textstyle-i.md)的heightScale）或行内不同字号（即设置  
[TextStyle](arkts-arkgraphics2d-text-textstyle-i.md)的fontSize）文本混排时生效。若行内有上下标文本（即设置[TextStyle](arkts-arkgraphics2d-text-textstyle-i.md)的badgeType属性文本），上下标文本将与普通文本一样参与垂直对齐。

**Type:** [TextVerticalAlign](../../apis-arkui/arkts-apis/arkts-arkui-textverticalalign-e.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-ParagraphStyle-verticalAlign?: TextVerticalAlign--><!--Device-ParagraphStyle-verticalAlign?: TextVerticalAlign-End-->

**System capability:** SystemCapability.Graphics.Drawing

## wordBreak

```TypeScript
wordBreak?: WordBreak
```

断词类型，默认为BREAK_WORD。

**Type:** [WordBreak](../../apis-arkui/arkts-apis/arkts-arkui-enums-wordbreak-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-ParagraphStyle-wordBreak?: WordBreak--><!--Device-ParagraphStyle-wordBreak?: WordBreak-End-->

**System capability:** SystemCapability.Graphics.Drawing

