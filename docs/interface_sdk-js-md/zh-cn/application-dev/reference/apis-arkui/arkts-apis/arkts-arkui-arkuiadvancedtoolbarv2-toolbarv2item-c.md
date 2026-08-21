# ToolBarV2Item

Declare type ToolBarV2Item

**起始版本：** 18

<!--Device-unnamed-export declare class ToolBarV2Item--><!--Device-unnamed-export declare class ToolBarV2Item-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { ToolBarV2ItemState, ToolBarV2SymbolGlyph, ToolBarV2SymbolGlyphOptions, ToolBarV2ItemText, ToolBarV2ItemTextOptions, ToolBarV2ItemIconType, ToolBarV2ItemImage, ToolBarV2ItemImageOptions, ToolBarV2, ToolBarV2Item, ToolBarV2ItemOptions, ToolBarV2Modifier, ToolBarV2ItemAction } from '@kit.ArkUI';
```

## constructor

```TypeScript
constructor(options: ToolBarV2ItemOptions)
```

ToolBarV2Item的构造函数。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-ToolBarV2Item-constructor(options: ToolBarV2ItemOptions)--><!--Device-ToolBarV2Item-constructor(options: ToolBarV2ItemOptions)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ToolBarV2ItemOptions](arkts-arkui-arkuiadvancedtoolbarv2-toolbarv2itemoptions-i.md) | 是 | 子项信息。 |

## accessibilityDescription

```TypeScript
@Trace
  accessibilityDescription?: ResourceStr
```

The accessibilityDescription of item.

**类型：** [ResourceStr](../../apis-default/arkts-apis/arkts-resourcestr-t.md)

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-ToolBarV2Item-@Trace  accessibilityDescription?: ResourceStr--><!--Device-ToolBarV2Item-@Trace  accessibilityDescription?: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## accessibilityLevel

```TypeScript
@Trace
  accessibilityLevel?: string
```

The accessibilityLevel of item.

**类型：** string

**默认值：** "auto"

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-ToolBarV2Item-@Trace  accessibilityLevel?: string--><!--Device-ToolBarV2Item-@Trace  accessibilityLevel?: string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## accessibilityText

```TypeScript
@Trace
  accessibilityText?: ResourceStr
```

The accessibilityText of item.

**类型：** [ResourceStr](../../apis-default/arkts-apis/arkts-resourcestr-t.md)

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-ToolBarV2Item-@Trace  accessibilityText?: ResourceStr--><!--Device-ToolBarV2Item-@Trace  accessibilityText?: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## action

```TypeScript
@Trace
  action?: ToolBarV2ItemAction
```

Define the action event.

**类型：** [ToolBarV2ItemAction](arkts-arkui-toolbarv2itemaction-t.md)

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-ToolBarV2Item-@Trace  action?: ToolBarV2ItemAction--><!--Device-ToolBarV2Item-@Trace  action?: ToolBarV2ItemAction-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## content

```TypeScript
@Trace
  content: ToolBarV2ItemText
```

Define text content.

**类型：** [ToolBarV2ItemText](arkts-arkui-arkuiadvancedtoolbarv2-toolbarv2itemtext-c.md)

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-ToolBarV2Item-@Trace  content: ToolBarV2ItemText--><!--Device-ToolBarV2Item-@Trace  content: ToolBarV2ItemText-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## icon

```TypeScript
@Trace
  icon?: ToolBarV2ItemIconType
```

Define icon resource.

**类型：** [ToolBarV2ItemIconType](arkts-arkui-toolbarv2itemicontype-t.md)

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-ToolBarV2Item-@Trace  icon?: ToolBarV2ItemIconType--><!--Device-ToolBarV2Item-@Trace  icon?: ToolBarV2ItemIconType-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## state

```TypeScript
@Trace
  state?: ToolBarV2ItemState
```

Define item type.

**类型：** [ToolBarV2ItemState](arkts-arkui-arkuiadvancedtoolbarv2-toolbarv2itemstate-e.md)

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-ToolBarV2Item-@Trace  state?: ToolBarV2ItemState--><!--Device-ToolBarV2Item-@Trace  state?: ToolBarV2ItemState-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

