# SegmentButtonV2Item

Defines segmented button item.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-unnamed-export declare class SegmentButtonV2Item--><!--Device-unnamed-export declare class SegmentButtonV2Item-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## constructor

```TypeScript
constructor(options: SegmentButtonV2ItemOptions)
```

构造函数。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SegmentButtonV2Item-constructor(options: SegmentButtonV2ItemOptions)--><!--Device-SegmentButtonV2Item-constructor(options: SegmentButtonV2ItemOptions)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SegmentButtonV2ItemOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkuiadvancedsegmentbuttonv2-segmentbuttonv2itemoptions-i.md) | 是 | 分段按钮选项配置参数。 |

## accessibilityDescription

```TypeScript
@Trace
  accessibilityDescription?: ResourceStr
```

分段按钮选项的无障碍说明 accessibilityDescription。 默认值："" 值为undefined时，按默认值处理。

**类型：** ResourceStr

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SegmentButtonV2Item-@Trace  accessibilityDescription?: ResourceStr--><!--Device-SegmentButtonV2Item-@Trace  accessibilityDescription?: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## accessibilityLevel

```TypeScript
@Trace
  accessibilityLevel?: string
```

分段按钮选项的无障碍重要性 accessibilityLevel。 默认值："auto" 值为undefined时，按默认值处理。

**类型：** string

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SegmentButtonV2Item-@Trace  accessibilityLevel?: string--><!--Device-SegmentButtonV2Item-@Trace  accessibilityLevel?: string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## accessibilityText

```TypeScript
@Trace
  accessibilityText?: ResourceStr
```

分段按钮选项的无障碍文本 accessibilityText。 默认值："" 值为undefined时，按默认值处理。

**类型：** ResourceStr

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SegmentButtonV2Item-@Trace  accessibilityText?: ResourceStr--><!--Device-SegmentButtonV2Item-@Trace  accessibilityText?: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## enabled

```TypeScript
@Trace
  enabled: boolean
```

分段按钮选项是否可用。

默认值：true

true：可用；false：不可用。

不支持设置undefined

装饰器类型：@Trace

**类型：** boolean

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SegmentButtonV2Item-@Trace  enabled: boolean--><!--Device-SegmentButtonV2Item-@Trace  enabled: boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## icon

```TypeScript
@Trace
  icon?: ResourceStr
```

分段按钮选项图片类型图标。 默认值：undefined 装饰器类型：@Trace 。

**类型：** ResourceStr

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SegmentButtonV2Item-@Trace  icon?: ResourceStr--><!--Device-SegmentButtonV2Item-@Trace  icon?: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## iconModifier

```TypeScript
@Trace
  iconModifier?: ImageModifier
```

分段按钮选项图片类型图标属性的样式修改器。 默认值：undefined 装饰器类型：@Trace 。

**类型：** [ImageModifier](../../apis-arkui/arkts-components/arkts-arkui-imagemodifier-t.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SegmentButtonV2Item-@Trace  iconModifier?: ImageModifier--><!--Device-SegmentButtonV2Item-@Trace  iconModifier?: ImageModifier-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## symbol

```TypeScript
@Trace
  symbol?: Resource
```

分段按钮选项的HM Symbol类型图标。 默认值：undefined 装饰器类型：@Trace 。

**类型：** Resource

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SegmentButtonV2Item-@Trace  symbol?: Resource--><!--Device-SegmentButtonV2Item-@Trace  symbol?: Resource-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## symbolModifier

```TypeScript
@Trace
  symbolModifier?: SymbolGlyphModifier
```

分段按钮选项HM Symbol类型图标属性样式修改器。 默认值：undefined 装饰器类型：@Trace 。

**类型：** SymbolGlyphModifier

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SegmentButtonV2Item-@Trace  symbolModifier?: SymbolGlyphModifier--><!--Device-SegmentButtonV2Item-@Trace  symbolModifier?: SymbolGlyphModifier-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## text

```TypeScript
@Trace
  text?: ResourceStr
```

分段按钮选项文本。 默认值：undefined 装饰器类型：@Trace 。

**类型：** ResourceStr

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SegmentButtonV2Item-@Trace  text?: ResourceStr--><!--Device-SegmentButtonV2Item-@Trace  text?: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## textModifier

```TypeScript
@Trace
  textModifier?: TextModifier
```

分段按钮选项文本属性样式修改器。 默认值：undefined 装饰器类型：@Trace 。

**类型：** [TextModifier](../../apis-arkui/arkts-apis/arkts-arkui-textmodifier-c.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SegmentButtonV2Item-@Trace  textModifier?: TextModifier--><!--Device-SegmentButtonV2Item-@Trace  textModifier?: TextModifier-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

