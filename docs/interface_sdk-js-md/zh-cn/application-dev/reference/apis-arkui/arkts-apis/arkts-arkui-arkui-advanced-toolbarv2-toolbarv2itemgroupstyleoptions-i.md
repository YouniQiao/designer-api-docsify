# ToolBarV2ItemGroupStyleOptions

```TypeScript
export interface ToolBarV2ItemGroupStyleOptions
```

定义ToolBarV2ItemGroupStyle的构造函数选项。

**起始版本：** 26.1.0

<!--Device-unnamed-export interface ToolBarV2ItemGroupStyleOptions--><!--Device-unnamed-export interface ToolBarV2ItemGroupStyleOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { ToolBarV2ItemState, ToolBarV2SymbolGlyph, ToolBarV2SymbolGlyphOptions, ToolBarV2ItemText, ToolBarV2ItemTextOptions, ToolBarV2ItemIconType, ToolBarV2ItemImage, ToolBarV2ItemImageOptions, ToolBarV2, ToolBarV2Item, ToolBarV2ItemOptions, ToolBarV2Modifier, ToolBarV2ItemAction, AdvancedToolBarV2Item, AdvancedToolBarV2ItemOptions, AdvancedToolBarV2Modifier, BarBackgroundVisibility, ToolBarV2ItemGroupStyle, ToolBarV2ItemGroupStyleOptions, ToolBarV2ItemPlacement, ToolBarV2OverflowMenuStyle, ToolBarV2PaddingOptions, ToolBarV2StyleConfigs, ToolBarV2StyleOptions, ToolBarV2TitleConfigs, ToolBarV2TitleOptions, ToolBarV2TitleStyle, ToolBarV2TitleStyleOptions, ToolBarV2MaterialStyle } from '@kit.ArkUI';
```

## backgroundColor

```TypeScript
backgroundColor?: ColorMetrics
```

组容器的背景颜色。

**类型：** [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarV2ItemGroupStyleOptions-backgroundColor?: ColorMetrics--><!--Device-ToolBarV2ItemGroupStyleOptions-backgroundColor?: ColorMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## borderColor

```TypeScript
borderColor?: ColorMetrics
```

组容器的圆角颜色。

**类型：** [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarV2ItemGroupStyleOptions-borderColor?: ColorMetrics--><!--Device-ToolBarV2ItemGroupStyleOptions-borderColor?: ColorMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## borderRadius

```TypeScript
borderRadius?: LengthMetrics
```

组容器的边界边框圆角半径。

**类型：** [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarV2ItemGroupStyleOptions-borderRadius?: LengthMetrics--><!--Device-ToolBarV2ItemGroupStyleOptions-borderRadius?: LengthMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## borderWidth

```TypeScript
borderWidth?: LengthMetrics
```

组容器的边框宽度。

**类型：** [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarV2ItemGroupStyleOptions-borderWidth?: LengthMetrics--><!--Device-ToolBarV2ItemGroupStyleOptions-borderWidth?: LengthMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## padding

```TypeScript
padding?: ToolBarV2PaddingOptions
```

group容器的Padding。

**类型：** [ToolBarV2PaddingOptions](arkts-arkui-arkui-advanced-toolbarv2-toolbarv2paddingoptions-i.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarV2ItemGroupStyleOptions-padding?: ToolBarV2PaddingOptions--><!--Device-ToolBarV2ItemGroupStyleOptions-padding?: ToolBarV2PaddingOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## placement

```TypeScript
placement?: ToolBarV2ItemPlacement
```

组在工具栏中的放置位置。组放置优先于组中单个项目的放置。

**类型：** [ToolBarV2ItemPlacement](arkts-arkui-arkui-advanced-toolbarv2-toolbarv2itemplacement-e.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarV2ItemGroupStyleOptions-placement?: ToolBarV2ItemPlacement--><!--Device-ToolBarV2ItemGroupStyleOptions-placement?: ToolBarV2ItemPlacement-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## space

```TypeScript
space?: LengthMetrics
```

组内项目之间的间距。默认值：0vp。

**类型：** [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarV2ItemGroupStyleOptions-space?: LengthMetrics--><!--Device-ToolBarV2ItemGroupStyleOptions-space?: LengthMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## stateEffect

```TypeScript
stateEffect?: boolean
```

是否显示组内项目的按压状态效果。

**类型：** boolean

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarV2ItemGroupStyleOptions-stateEffect?: boolean--><!--Device-ToolBarV2ItemGroupStyleOptions-stateEffect?: boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
