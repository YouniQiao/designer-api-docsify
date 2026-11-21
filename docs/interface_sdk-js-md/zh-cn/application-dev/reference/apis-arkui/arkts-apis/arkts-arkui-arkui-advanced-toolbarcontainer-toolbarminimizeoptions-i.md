# ToolBarMinimizeOptions

```TypeScript
export interface ToolBarMinimizeOptions
```

配置工具栏最小化悬浮球的选项。

**起始版本：** 26.1.0

<!--Device-unnamed-export interface ToolBarMinimizeOptions--><!--Device-unnamed-export interface ToolBarMinimizeOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { ToolBarState, DockArea, DockCornerMode, ToolBarSafeAreaMode, HandednessAdaptationMode, ToolBarFloatingOptions, ToolBarFloatingConfigs, ToolBarMinimizeOptions, ToolBarMinimizeConfigs, ToolBarController, ToolBarInitialParams, ToolBarParams, ToolBarConfigs, ToolBarCallbacks, ToolBarDockOffsetOptions, ToolBarSafeAreaOptions, ToolBarContainerOptions, ToolBarContainerConfigs, ToolBarContainer, ToolBarDragStateCallback, ToolBarDragOffsetCallback, ToolBarStateCallback, ToolBarDockCallback, } from '@kit.ArkUI';
```

## builder

```TypeScript
builder?: CustomBuilder
```

自定义构建器。默认值为undefined，表示无自定义内容。

**类型：** [CustomBuilder](../arkts-components/arkts-arkui-common-comp-custombuilder-t.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarMinimizeOptions-builder?: CustomBuilder--><!--Device-ToolBarMinimizeOptions-builder?: CustomBuilder-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## buoySize

```TypeScript
buoySize?: LengthMetrics
```

最小化悬浮球的直径。

**类型：** [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarMinimizeOptions-buoySize?: LengthMetrics--><!--Device-ToolBarMinimizeOptions-buoySize?: LengthMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## icon

```TypeScript
icon?: ResourceStr | SymbolGlyphModifier
```

图标。默认值为undefined，表示无图标内容。

**类型：** [ResourceStr](arkts-arkui-resourcestr-t.md) &#124; [SymbolGlyphModifier](../../apis-default/arkts-apis/arkts-default-arkui-modifier.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarMinimizeOptions-icon?: ResourceStr | SymbolGlyphModifier--><!--Device-ToolBarMinimizeOptions-icon?: ResourceStr | SymbolGlyphModifier-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## iconColor

```TypeScript
iconColor?: ColorMetrics
```

图标颜色。默认值为$r('sys.color.icon_primary')。

**类型：** [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarMinimizeOptions-iconColor?: ColorMetrics--><!--Device-ToolBarMinimizeOptions-iconColor?: ColorMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## iconSize

```TypeScript
iconSize?: LengthMetrics
```

图标尺寸。

**类型：** [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarMinimizeOptions-iconSize?: LengthMetrics--><!--Device-ToolBarMinimizeOptions-iconSize?: LengthMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## text

```TypeScript
text?: ResourceStr
```

文本标签。默认值为undefined，表示无文本内容。

**类型：** [ResourceStr](arkts-arkui-resourcestr-t.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarMinimizeOptions-text?: ResourceStr--><!--Device-ToolBarMinimizeOptions-text?: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## textColor

```TypeScript
textColor?: ColorMetrics
```

文本颜色。默认值为$r('sys.color.font_primary')。

**类型：** [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarMinimizeOptions-textColor?: ColorMetrics--><!--Device-ToolBarMinimizeOptions-textColor?: ColorMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
