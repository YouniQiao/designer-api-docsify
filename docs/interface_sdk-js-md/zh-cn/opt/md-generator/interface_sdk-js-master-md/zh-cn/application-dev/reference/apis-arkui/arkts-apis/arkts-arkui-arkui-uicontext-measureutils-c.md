# MeasureUtils

MeasureUtils提供文本宽度、高度等相关计算能力，适用于文本自适应布局、多行文本截断、动态UI适配等场景。通过该类可精确计算文本尺寸，帮助开发者在布局前预判文本显示效果，避免文本溢出或布局错乱等问题。 > **说明：**> > - 以下API需先使用UIContext中的[getMeasureUtils()](arkts-arkui-arkui-uicontext-uicontext-c.md#getmeasureutils)方法获取MeasureUtils实例，再通过此实例调用对应方法。 > > - 如需更多测算文本参数，建议使用图形对应测算接口[Paragraph](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-text-paragraph-c.md#paragraph)接口。 > > - 调用文本计算接口时，应避免同时用[ApplicationContext.setFontSizeScale](../../apis-ability-kit/arkts-apis/arkts-ability-applicationcontext-c.md#setfontsizescale)设置应用字体大小缩放比例。为了确保时序正确性，建议开发者自行监听字体缩放变化，以保证测算结果的准确性。 > > - 在测算裁剪后的文本时，由于某些Unicode字符（如emoji）的码位长度大于1，直接按字符串长度裁剪会导致不准确的结果。建议基于Unicode码点进行迭代处理，避免错误截断字符，确保测算结果准确，请参考[measureTextSize](#measuretextsize)的示例2。

**起始版本：** 12

<!--Device-unnamed-export class MeasureUtils--><!--Device-unnamed-export class MeasureUtils-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## getParagraphs

```TypeScript
getParagraphs(styledString: StyledString, options?: TextLayoutOptions): Array<Paragraph>
```

将属性字符串根据文本布局选项转换成对应的[Paragraph](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-text-paragraph-c.md#paragraph)数组。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MeasureUtils-getParagraphs(styledString: StyledString, options?: TextLayoutOptions): Array<Paragraph>--><!--Device-MeasureUtils-getParagraphs(styledString: StyledString, options?: TextLayoutOptions): Array<Paragraph>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| styledString | [StyledString](arkts-arkui-styledstring-c.md) | 是 |
| options | [TextLayoutOptions](arkts-arkui-textlayoutoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Array & lt;Paragraph & gt; |

## measureText

```TypeScript
measureText(options: MeasureOptions): number
```

计算指定文本作为单行文本显示时的宽度，如果文本包含多行（由换行符`\n`分隔），则返回其中最长的行的宽度。 > **说明：**> > - 调用此接口时，应避免同时使用[ApplicationContext.setFontSizeScale](../../apis-ability-kit/arkts-apis/arkts-ability-applicationcontext-c.md#setfontsizescale)设置应用字体大小缩放比例。为了确保时序正确性，建议开发者自行监听字体缩放变化，以保证测算结果的准确性。 > > - measureText接口的计算结果始终是单行文本的宽度，入参options中配置的布局约束（如constraintWidth、maxLines）对measureText的结果没有影响。如果需要计算布局约束下的宽度，请使用[measureTextSize](#measuretextsize)方法。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MeasureUtils-measureText(options: MeasureOptions): number--><!--Device-MeasureUtils-measureText(options: MeasureOptions): number-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [MeasureOptions](arkts-arkui-measure-measureoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## measureTextSize

```TypeScript
measureTextSize(options: MeasureOptions): SizeOptions
```

计算指定文本的宽度和高度。 > **说明：**> > 调用此接口时，应避免同时使用[ApplicationContext.setFontSizeScale](../../apis-ability-kit/arkts-apis/arkts-ability-applicationcontext-c.md#setfontsizescale)设置应用字体大小缩放比例。为了确保时序正确性，建议开发者自行监听字体缩放变化，以保证测算结果的准确性。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MeasureUtils-measureTextSize(options: MeasureOptions): SizeOptions--><!--Device-MeasureUtils-measureTextSize(options: MeasureOptions): SizeOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [MeasureOptions](arkts-arkui-measure-measureoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [SizeOptions](arkts-arkui-sizeoptions-i.md) |
