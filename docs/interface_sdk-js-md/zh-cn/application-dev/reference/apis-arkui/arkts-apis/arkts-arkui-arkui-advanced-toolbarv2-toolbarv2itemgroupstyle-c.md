# ToolBarV2ItemGroupStyle

```TypeScript
export declare class ToolBarV2ItemGroupStyle
```

定义工具栏项组的样式配置。

**起始版本：** 26.1.0

**装饰器类型：** @ObservedV2

<!--Device-unnamed-export declare class ToolBarV2ItemGroupStyle--><!--Device-unnamed-export declare class ToolBarV2ItemGroupStyle-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { ToolBarV2ItemState, ToolBarV2SymbolGlyph, ToolBarV2SymbolGlyphOptions, ToolBarV2ItemText, ToolBarV2ItemTextOptions, ToolBarV2ItemIconType, ToolBarV2ItemImage, ToolBarV2ItemImageOptions, ToolBarV2, ToolBarV2Item, ToolBarV2ItemOptions, ToolBarV2Modifier, ToolBarV2ItemAction, AdvancedToolBarV2Item, AdvancedToolBarV2ItemOptions, AdvancedToolBarV2Modifier, BarBackgroundVisibility, ToolBarV2ItemGroupStyle, ToolBarV2ItemGroupStyleOptions, ToolBarV2ItemPlacement, ToolBarV2OverflowMenuStyle, ToolBarV2PaddingOptions, ToolBarV2StyleConfigs, ToolBarV2StyleOptions, ToolBarV2TitleConfigs, ToolBarV2TitleOptions, ToolBarV2TitleStyle, ToolBarV2TitleStyleOptions, ToolBarV2MaterialStyle } from '@kit.ArkUI';
```

## constructor

```TypeScript
constructor(options?: ToolBarV2ItemGroupStyleOptions)
```

构造ToolBarV2ItemGroupStyle实例。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarV2ItemGroupStyle-constructor(options?: ToolBarV2ItemGroupStyleOptions)--><!--Device-ToolBarV2ItemGroupStyle-constructor(options?: ToolBarV2ItemGroupStyleOptions)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ToolBarV2ItemGroupStyleOptions](arkts-arkui-arkui-advanced-toolbarv2-toolbarv2itemgroupstyleoptions-i.md) | 否 | 构造函数选项。 |

## backgroundColor

```TypeScript
backgroundColor?: ColorMetrics
```

组容器的背景颜色。默认值：undefined。值为undefined或不设置时，值为$r('sys.color.comp_background_primary').

**类型：** [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md)

**起始版本：** 26.1.0

**装饰器类型：** @Trace

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarV2ItemGroupStyle-backgroundColor?: ColorMetrics--><!--Device-ToolBarV2ItemGroupStyle-backgroundColor?: ColorMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## borderColor

```TypeScript
borderColor?: ColorMetrics
```

组容器的圆角颜色。默认值：undefined。值为undefined或不设置时，默认无颜色。

**类型：** [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md)

**起始版本：** 26.1.0

**装饰器类型：** @Trace

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarV2ItemGroupStyle-borderColor?: ColorMetrics--><!--Device-ToolBarV2ItemGroupStyle-borderColor?: ColorMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## borderRadius

```TypeScript
borderRadius?: LengthMetrics
```

组容器的边界边框圆角半径。默认值：undefined。值为undefined或不设置时，默认值为工具栏交叉轴长度的一半。

**类型：** [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)

**起始版本：** 26.1.0

**装饰器类型：** @Trace

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarV2ItemGroupStyle-borderRadius?: LengthMetrics--><!--Device-ToolBarV2ItemGroupStyle-borderRadius?: LengthMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## borderWidth

```TypeScript
borderWidth?: LengthMetrics
```

组容器的边框宽度。默认值：undefined。值为undefined或不设置时，默认无宽度。

**类型：** [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)

**起始版本：** 26.1.0

**装饰器类型：** @Trace

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarV2ItemGroupStyle-borderWidth?: LengthMetrics--><!--Device-ToolBarV2ItemGroupStyle-borderWidth?: LengthMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## padding

```TypeScript
padding?: ToolBarV2PaddingOptions
```

group容器的Padding。默认值：undefined。值为undefined或不设置时，默认值为12vp。

**类型：** [ToolBarV2PaddingOptions](arkts-arkui-arkui-advanced-toolbarv2-toolbarv2paddingoptions-i.md)

**起始版本：** 26.1.0

**装饰器类型：** @Trace

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarV2ItemGroupStyle-padding?: ToolBarV2PaddingOptions--><!--Device-ToolBarV2ItemGroupStyle-padding?: ToolBarV2PaddingOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## placement

```TypeScript
placement?: ToolBarV2ItemPlacement
```

组在工具栏中的放置位置。组放置优先于组中单个项目的放置。默认值：ToolBarV2ItemPlacement.MAIN。

**类型：** [ToolBarV2ItemPlacement](arkts-arkui-arkui-advanced-toolbarv2-toolbarv2itemplacement-e.md)

**起始版本：** 26.1.0

**装饰器类型：** @Trace

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarV2ItemGroupStyle-placement?: ToolBarV2ItemPlacement--><!--Device-ToolBarV2ItemGroupStyle-placement?: ToolBarV2ItemPlacement-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## space

```TypeScript
space?: LengthMetrics
```

组内项目之间的间距。默认值：0vp。

**类型：** [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)

**起始版本：** 26.1.0

**装饰器类型：** @Trace

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarV2ItemGroupStyle-space?: LengthMetrics--><!--Device-ToolBarV2ItemGroupStyle-space?: LengthMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## stateEffect

```TypeScript
stateEffect?: boolean
```

是否显示组内项目的按压状态效果。默认值：true。

**类型：** boolean

**起始版本：** 26.1.0

**装饰器类型：** @Trace

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarV2ItemGroupStyle-stateEffect?: boolean--><!--Device-ToolBarV2ItemGroupStyle-stateEffect?: boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
