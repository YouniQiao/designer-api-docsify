# ToolBarMinimizeConfigs

```TypeScript
export class ToolBarMinimizeConfigs
```

最小化悬浮球的可观察配置存储，与[ToolBarMinimizeOptions](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarminimizeoptions-i.md)对应。

**起始版本：** 26.1.0

**装饰器类型：** @ObservedV2

<!--Device-unnamed-export class ToolBarMinimizeConfigs--><!--Device-unnamed-export class ToolBarMinimizeConfigs-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { ToolBarState, DockArea, DockCornerMode, ToolBarSafeAreaMode, HandednessAdaptationMode, ToolBarFloatingOptions, ToolBarFloatingConfigs, ToolBarMinimizeOptions, ToolBarMinimizeConfigs, ToolBarController, ToolBarInitialParams, ToolBarParams, ToolBarConfigs, ToolBarCallbacks, ToolBarDockOffsetOptions, ToolBarSafeAreaOptions, ToolBarContainerOptions, ToolBarContainerConfigs, ToolBarContainer, ToolBarDragStateCallback, ToolBarDragOffsetCallback, ToolBarStateCallback, ToolBarDockCallback, } from '@kit.ArkUI';
```

## constructor

```TypeScript
constructor(options?: ToolBarMinimizeOptions)
```

ToolBarMinimizeConfigs的构造函数。当options省略时，所有字段使用各自的默认值。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarMinimizeConfigs-constructor(options?: ToolBarMinimizeOptions)--><!--Device-ToolBarMinimizeConfigs-constructor(options?: ToolBarMinimizeOptions)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ToolBarMinimizeOptions](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarminimizeoptions-i.md) | 否 | 最小化悬浮球选项。 |

## builder

```TypeScript
builder?: CustomBuilder
```

自定义构建器。默认值为undefined，无自定义内容。

**类型：** [CustomBuilder](../arkts-components/arkts-arkui-common-comp-custombuilder-t.md)

**起始版本：** 26.1.0

**装饰器类型：** @Trace

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarMinimizeConfigs-builder?: CustomBuilder--><!--Device-ToolBarMinimizeConfigs-builder?: CustomBuilder-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## buoySize

```TypeScript
buoySize?: LengthMetrics
```

最小化悬浮球的直径。

**类型：** [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)

**起始版本：** 26.1.0

**装饰器类型：** @Trace

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarMinimizeConfigs-buoySize?: LengthMetrics--><!--Device-ToolBarMinimizeConfigs-buoySize?: LengthMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## icon

```TypeScript
icon?: ResourceStr | SymbolGlyphModifier
```

图标。默认值为undefined，表示无图标内容。

**类型：** [ResourceStr](arkts-arkui-resourcestr-t.md) &#124; [SymbolGlyphModifier](../../apis-default/arkts-apis/arkts-default-arkui-modifier.md)

**起始版本：** 26.1.0

**装饰器类型：** @Trace

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarMinimizeConfigs-icon?: ResourceStr | SymbolGlyphModifier--><!--Device-ToolBarMinimizeConfigs-icon?: ResourceStr | SymbolGlyphModifier-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## iconColor

```TypeScript
iconColor?: ColorMetrics
```

图标颜色。默认值为$r('sys.color.icon_primary')。

**类型：** [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md)

**起始版本：** 26.1.0

**装饰器类型：** @Trace

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarMinimizeConfigs-iconColor?: ColorMetrics--><!--Device-ToolBarMinimizeConfigs-iconColor?: ColorMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## iconSize

```TypeScript
iconSize?: LengthMetrics
```

图标尺寸。

**类型：** [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)

**起始版本：** 26.1.0

**装饰器类型：** @Trace

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarMinimizeConfigs-iconSize?: LengthMetrics--><!--Device-ToolBarMinimizeConfigs-iconSize?: LengthMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## text

```TypeScript
text?: ResourceStr
```

文本标签。默认值为undefined，表示无文本内容。

**类型：** [ResourceStr](arkts-arkui-resourcestr-t.md)

**起始版本：** 26.1.0

**装饰器类型：** @Trace

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarMinimizeConfigs-text?: ResourceStr--><!--Device-ToolBarMinimizeConfigs-text?: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## textColor

```TypeScript
textColor?: ColorMetrics
```

文本颜色。默认值为$r('sys.color.font_primary')。

**类型：** [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md)

**起始版本：** 26.1.0

**装饰器类型：** @Trace

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarMinimizeConfigs-textColor?: ColorMetrics--><!--Device-ToolBarMinimizeConfigs-textColor?: ColorMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
