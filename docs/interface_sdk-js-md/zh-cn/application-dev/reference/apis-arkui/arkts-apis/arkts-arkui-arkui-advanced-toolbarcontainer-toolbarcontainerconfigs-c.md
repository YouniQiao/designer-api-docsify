# ToolBarContainerConfigs

```TypeScript
export class ToolBarContainerConfigs
```

工具栏容器的可观察配置存储，与[ToolBarContainerOptions](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarcontaineroptions-i.md)对应。

**起始版本：** 26.1.0

**装饰器类型：** @ObservedV2

<!--Device-unnamed-export class ToolBarContainerConfigs--><!--Device-unnamed-export class ToolBarContainerConfigs-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { ToolBarState, DockArea, DockCornerMode, ToolBarSafeAreaMode, HandednessAdaptationMode, ToolBarFloatingOptions, ToolBarFloatingConfigs, ToolBarMinimizeOptions, ToolBarMinimizeConfigs, ToolBarController, ToolBarInitialParams, ToolBarParams, ToolBarConfigs, ToolBarCallbacks, ToolBarDockOffsetOptions, ToolBarSafeAreaOptions, ToolBarContainerOptions, ToolBarContainerConfigs, ToolBarContainer, ToolBarDragStateCallback, ToolBarDragOffsetCallback, ToolBarStateCallback, ToolBarDockCallback, } from '@kit.ArkUI';
```

## constructor

```TypeScript
constructor(options?: ToolBarContainerOptions)
```

构造函数。当options省略时，所有字段使用各自的默认值。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarContainerConfigs-constructor(options?: ToolBarContainerOptions)--><!--Device-ToolBarContainerConfigs-constructor(options?: ToolBarContainerOptions)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ToolBarContainerOptions](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarcontaineroptions-i.md) | 否 | 容器选项。 |

## adaptToHandedness

```TypeScript
adaptToHandedness?: HandednessAdaptationMode
```

接入智感握姿模式。默认值：HandednessAdaptationMode.NONE。

**类型：** [HandednessAdaptationMode](arkts-arkui-arkui-advanced-toolbarcontainer-handednessadaptationmode-e.md)

**起始版本：** 26.1.0

**装饰器类型：** @Trace

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarContainerConfigs-adaptToHandedness?: HandednessAdaptationMode--><!--Device-ToolBarContainerConfigs-adaptToHandedness?: HandednessAdaptationMode-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## dockOffset

```TypeScript
dockOffset?: ToolBarDockOffsetOptions
```

停靠偏移量，单位为vp。默认值：各边为16vp。

**类型：** [ToolBarDockOffsetOptions](arkts-arkui-arkui-advanced-toolbarcontainer-toolbardockoffsetoptions-i.md)

**起始版本：** 26.1.0

**装饰器类型：** @Trace

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarContainerConfigs-dockOffset?: ToolBarDockOffsetOptions--><!--Device-ToolBarContainerConfigs-dockOffset?: ToolBarDockOffsetOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## gutter

```TypeScript
gutter?: LengthMetrics
```

工具栏之间的间隔。

**类型：** [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)

**起始版本：** 26.1.0

**装饰器类型：** @Trace

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarContainerConfigs-gutter?: LengthMetrics--><!--Device-ToolBarContainerConfigs-gutter?: LengthMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## safeArea

```TypeScript
safeArea?: ToolBarSafeAreaOptions
```

安全区模式。默认值：各边为ToolBarSafeAreaMode.NONE。

**类型：** [ToolBarSafeAreaOptions](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarsafeareaoptions-i.md)

**起始版本：** 26.1.0

**装饰器类型：** @Trace

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarContainerConfigs-safeArea?: ToolBarSafeAreaOptions--><!--Device-ToolBarContainerConfigs-safeArea?: ToolBarSafeAreaOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
