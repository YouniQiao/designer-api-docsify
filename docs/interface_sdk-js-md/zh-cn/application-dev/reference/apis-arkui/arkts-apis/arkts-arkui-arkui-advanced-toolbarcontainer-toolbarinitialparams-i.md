# ToolBarInitialParams

```TypeScript
export interface ToolBarInitialParams
```

工具栏初始位置参数，指定创建时的停靠区域、方向和状态。

**起始版本：** 26.1.0

<!--Device-unnamed-export interface ToolBarInitialParams--><!--Device-unnamed-export interface ToolBarInitialParams-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { ToolBarState, DockArea, DockCornerMode, ToolBarSafeAreaMode, HandednessAdaptationMode, ToolBarFloatingOptions, ToolBarFloatingConfigs, ToolBarMinimizeOptions, ToolBarMinimizeConfigs, ToolBarController, ToolBarInitialParams, ToolBarParams, ToolBarConfigs, ToolBarCallbacks, ToolBarDockOffsetOptions, ToolBarSafeAreaOptions, ToolBarContainerOptions, ToolBarContainerConfigs, ToolBarContainer, ToolBarDragStateCallback, ToolBarDragOffsetCallback, ToolBarStateCallback, ToolBarDockCallback, } from '@kit.ArkUI';
```

## direction

```TypeScript
direction?: Axis
```

工具栏初始停靠方向。默认与吸附的边保持方向一致。

**类型：** [Axis](arkts-arkui-axis-e.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarInitialParams-direction?: Axis--><!--Device-ToolBarInitialParams-direction?: Axis-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## dockArea

```TypeScript
dockArea: DockArea
```

工具栏初始停靠的区域。

**类型：** [DockArea](arkts-arkui-arkui-advanced-toolbarcontainer-dockarea-e.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarInitialParams-dockArea: DockArea--><!--Device-ToolBarInitialParams-dockArea: DockArea-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## state

```TypeScript
state?: ToolBarState
```

工具栏初始状态。默认值：[FLOATING](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarstate-e.md#floating)。

**类型：** [ToolBarState](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarstate-e.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarInitialParams-state?: ToolBarState--><!--Device-ToolBarInitialParams-state?: ToolBarState-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
