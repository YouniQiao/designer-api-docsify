# ToolBarV2TitleStyle

```TypeScript
export declare class ToolBarV2TitleStyle
```

标题文本样式配置。

**起始版本：** 26.1.0

**装饰器类型：** @ObservedV2

<!--Device-unnamed-export declare class ToolBarV2TitleStyle--><!--Device-unnamed-export declare class ToolBarV2TitleStyle-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { ToolBarV2ItemState, ToolBarV2SymbolGlyph, ToolBarV2SymbolGlyphOptions, ToolBarV2ItemText, ToolBarV2ItemTextOptions, ToolBarV2ItemIconType, ToolBarV2ItemImage, ToolBarV2ItemImageOptions, ToolBarV2, ToolBarV2Item, ToolBarV2ItemOptions, ToolBarV2Modifier, ToolBarV2ItemAction, AdvancedToolBarV2Item, AdvancedToolBarV2ItemOptions, AdvancedToolBarV2Modifier, BarBackgroundVisibility, ToolBarV2ItemGroupStyle, ToolBarV2ItemGroupStyleOptions, ToolBarV2ItemPlacement, ToolBarV2OverflowMenuStyle, ToolBarV2PaddingOptions, ToolBarV2StyleConfigs, ToolBarV2StyleOptions, ToolBarV2TitleConfigs, ToolBarV2TitleOptions, ToolBarV2TitleStyle, ToolBarV2TitleStyleOptions, ToolBarV2MaterialStyle } from '@kit.ArkUI';
```

## constructor

```TypeScript
constructor(options?: ToolBarV2TitleStyleOptions)
```

构造ToolBarV2TitleStyle实例。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarV2TitleStyle-constructor(options?: ToolBarV2TitleStyleOptions)--><!--Device-ToolBarV2TitleStyle-constructor(options?: ToolBarV2TitleStyleOptions)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ToolBarV2TitleStyleOptions](arkts-arkui-arkui-advanced-toolbarv2-toolbarv2titlestyleoptions-i.md) | 否 | 构造函数选项。 |

## fontColor

```TypeScript
fontColor?: ColorMetrics
```

标题文本颜色。默认值：undefined。值为undefined或不设置时，标题文本的默认颜色为$r('sys.color.font_primary')，副标题文本的默认颜色为$r('sys.color.font_secondary')。

**类型：** [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md)

**起始版本：** 26.1.0

**装饰器类型：** @Trace

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarV2TitleStyle-fontColor?: ColorMetrics--><!--Device-ToolBarV2TitleStyle-fontColor?: ColorMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## fontSize

```TypeScript
fontSize?: LengthMetrics
```

标题文本的字体大小。默认值为：undefined。值为undefined或不设置时，标题文本的默认颜色字体大小为20fp，副标题文本的默认颜色字体大小为14fp。

**类型：** [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)

**起始版本：** 26.1.0

**装饰器类型：** @Trace

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarV2TitleStyle-fontSize?: LengthMetrics--><!--Device-ToolBarV2TitleStyle-fontSize?: LengthMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## fontWeight

```TypeScript
fontWeight?: FontWeight
```

标题文本字重。默认值：undefined。值为undefined或不设置时，标题文本的默认颜色字重为FontWeight.Bold，副标题文本的默认颜色字重为FontWeight.Regular。

**类型：** [FontWeight](arkts-arkui-fontweight-e.md)

**起始版本：** 26.1.0

**装饰器类型：** @Trace

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarV2TitleStyle-fontWeight?: FontWeight--><!--Device-ToolBarV2TitleStyle-fontWeight?: FontWeight-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## minLength

```TypeScript
minLength?: LengthMetrics
```

标题最小长度。默认值：undefined。值为undefined或不设置时默认为48vp。

**类型：** [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)

**起始版本：** 26.1.0

**装饰器类型：** @Trace

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarV2TitleStyle-minLength?: LengthMetrics--><!--Device-ToolBarV2TitleStyle-minLength?: LengthMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
