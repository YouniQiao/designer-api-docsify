# ToolBarContainerOptions

```TypeScript
export interface ToolBarContainerOptions
```

配置工具栏容器的布局、安全区避让和握姿适配的选项。

**起始版本：** 26.1.0

<!--Device-unnamed-export interface ToolBarContainerOptions--><!--Device-unnamed-export interface ToolBarContainerOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { ToolBarState, DockArea, DockCornerMode, ToolBarSafeAreaMode, HandednessAdaptationMode, ToolBarFloatingOptions, ToolBarFloatingConfigs, ToolBarMinimizeOptions, ToolBarMinimizeConfigs, ToolBarController, ToolBarInitialParams, ToolBarParams, ToolBarConfigs, ToolBarCallbacks, ToolBarDockOffsetOptions, ToolBarSafeAreaOptions, ToolBarContainerOptions, ToolBarContainerConfigs, ToolBarContainer, ToolBarDragStateCallback, ToolBarDragOffsetCallback, ToolBarStateCallback, ToolBarDockCallback, } from '@kit.ArkUI';
```

## adaptToHandedness

```TypeScript
adaptToHandedness?: HandednessAdaptationMode
```

接入智感握姿模式。默认值：HandednessAdaptationMode.NONE。仅在单工具栏时生效。

**类型：** [HandednessAdaptationMode](arkts-arkui-arkui-advanced-toolbarcontainer-handednessadaptationmode-e.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarContainerOptions-adaptToHandedness?: HandednessAdaptationMode--><!--Device-ToolBarContainerOptions-adaptToHandedness?: HandednessAdaptationMode-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## dockOffset

```TypeScript
dockOffset?: ToolBarDockOffsetOptions
```

浮动工具栏的停靠偏移量。

**类型：** [ToolBarDockOffsetOptions](arkts-arkui-arkui-advanced-toolbarcontainer-toolbardockoffsetoptions-i.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarContainerOptions-dockOffset?: ToolBarDockOffsetOptions--><!--Device-ToolBarContainerOptions-dockOffset?: ToolBarDockOffsetOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## gutter

```TypeScript
gutter?: LengthMetrics
```

工具栏超长溢出时的避让间隔。

**类型：** [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarContainerOptions-gutter?: LengthMetrics--><!--Device-ToolBarContainerOptions-gutter?: LengthMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## safeArea

```TypeScript
safeArea?: ToolBarSafeAreaOptions
```

安全区避让模式。默认值：各边为[NONE](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarsafeareamode-e.md#none)。

**类型：** [ToolBarSafeAreaOptions](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarsafeareaoptions-i.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarContainerOptions-safeArea?: ToolBarSafeAreaOptions--><!--Device-ToolBarContainerOptions-safeArea?: ToolBarSafeAreaOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
