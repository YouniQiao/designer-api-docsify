# RichEditorParagraphStyle

段落样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## leadingMargin

```TypeScript
leadingMargin?: Dimension | LeadingMarginPlaceholder
```

设置文本段落缩进，当段落仅存在ImageSpan或BuilderSpan时，此属性值不生效。参数为Dimension类型时，不支持以Percentage形式设置， 默认单位为vp。默认值：{"size":["0.00px","0.00px"]}

**类型：** [Dimension](arkts-arkui-dimension-t.md) \| [LeadingMarginPlaceholder](arkts-arkui-richeditor-leadingmarginplaceholder-i.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## lineBreakStrategy

```TypeScript
lineBreakStrategy?: LineBreakStrategy
```

设置折行规则。默认值：LineBreakStrategy.GREEDY在wordBreak不等于breakAll的时候生效，不支持连字符。

**类型：** [LineBreakStrategy](arkts-arkui-linebreakstrategy-e.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## paragraphSpacing

```TypeScript
paragraphSpacing?: double
```

设置段落间距大小。单位：fp取值范围：[0, +∞)。传入负值时，按默认值处理。段落间距默认大小为0。

**类型：** double

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## shaderStyle

```TypeScript
shaderStyle?: ShaderStyle
```

设置文本着色器效果。默认值：undefined，不设置着色器效果。该接口与[RichEditorTextStyle](arkts-arkui-richeditor-richeditortextstyle-i.md)中的strokeWidth同时设置时，该接口不生效，shaderStyle的优先级高于 [RichEditorTextStyle](arkts-arkui-richeditor-richeditortextstyle-i.md)的fontColor。  
**模型约束：** 此接口仅可在Stage模型下使用。

**类型：** [ShaderStyle](arkts-arkui-textcommon-shaderstyle-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## textAlign

```TypeScript
textAlign?: TextAlign
```

设置文本段落在水平方向的对齐方式。默认值：TextAlign.START

**类型：** [TextAlign](arkts-arkui-textalign-e.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## textDirection

```TypeScript
textDirection?: TextDirection
```

设置文本方向。默认值：TextDirection.DEFAULT

**类型：** [TextDirection](arkts-arkui-textcommon-textdirection-e.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## textVerticalAlign

```TypeScript
textVerticalAlign?: TextVerticalAlign
```

设置文本段落在垂直方向的对齐方式。默认值：TextVerticalAlign.BASELINE  
**模型约束：** 此接口仅可在Stage模型下使用。

**类型：** [TextVerticalAlign](arkts-arkui-textcommon-textverticalalign-e.md)

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## wordBreak

```TypeScript
wordBreak?: WordBreak
```

设置断行规则。默认值：WordBreak.BREAK_WORD。

**类型：** [WordBreak](arkts-arkui-wordbreak-e.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
