# ToolBarCallbacks

```TypeScript
export class ToolBarCallbacks
```

用于工具栏拖拽、吸附以及状态回调的合集。

**起始版本：** 26.1.0

<!--Device-unnamed-export class ToolBarCallbacks--><!--Device-unnamed-export class ToolBarCallbacks-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { ToolBarState, DockArea, DockCornerMode, ToolBarSafeAreaMode, HandednessAdaptationMode, ToolBarFloatingOptions, ToolBarFloatingConfigs, ToolBarMinimizeOptions, ToolBarMinimizeConfigs, ToolBarController, ToolBarInitialParams, ToolBarParams, ToolBarConfigs, ToolBarCallbacks, ToolBarDockOffsetOptions, ToolBarSafeAreaOptions, ToolBarContainerOptions, ToolBarContainerConfigs, ToolBarContainer, ToolBarDragStateCallback, ToolBarDragOffsetCallback, ToolBarStateCallback, ToolBarDockCallback, } from '@kit.ArkUI';
```

## onDock

```TypeScript
onDock?: ToolBarDockCallback
```

工具栏停靠到新区域时的回调。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarCallbacks-onDock?: ToolBarDockCallback--><!--Device-ToolBarCallbacks-onDock?: ToolBarDockCallback-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## onDrag

```TypeScript
onDrag?: ToolBarDragOffsetCallback
```

拖拽过程中的回调，返回X/Y轴偏移量，单位为vp。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarCallbacks-onDrag?: ToolBarDragOffsetCallback--><!--Device-ToolBarCallbacks-onDrag?: ToolBarDragOffsetCallback-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## onDragEnd

```TypeScript
onDragEnd?: ToolBarDragStateCallback
```

用户结束拖拽时的回调。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarCallbacks-onDragEnd?: ToolBarDragStateCallback--><!--Device-ToolBarCallbacks-onDragEnd?: ToolBarDragStateCallback-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## onDragStart

```TypeScript
onDragStart?: ToolBarDragStateCallback
```

用户开始拖拽工具栏时的回调。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarCallbacks-onDragStart?: ToolBarDragStateCallback--><!--Device-ToolBarCallbacks-onDragStart?: ToolBarDragStateCallback-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## onStateChange

```TypeScript
onStateChange?: ToolBarStateCallback
```

工具栏状态变化时的回调。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarCallbacks-onStateChange?: ToolBarStateCallback--><!--Device-ToolBarCallbacks-onStateChange?: ToolBarStateCallback-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
