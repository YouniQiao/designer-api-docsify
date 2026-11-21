# ToolBarController

```TypeScript
export class ToolBarController
```

用于命令式操作工具栏停靠、固定和最小化状态控制器。

**起始版本：** 26.1.0

<!--Device-unnamed-export class ToolBarController--><!--Device-unnamed-export class ToolBarController-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { ToolBarState, DockArea, DockCornerMode, ToolBarSafeAreaMode, HandednessAdaptationMode, ToolBarFloatingOptions, ToolBarFloatingConfigs, ToolBarMinimizeOptions, ToolBarMinimizeConfigs, ToolBarController, ToolBarInitialParams, ToolBarParams, ToolBarConfigs, ToolBarCallbacks, ToolBarDockOffsetOptions, ToolBarSafeAreaOptions, ToolBarContainerOptions, ToolBarContainerConfigs, ToolBarContainer, ToolBarDragStateCallback, ToolBarDragOffsetCallback, ToolBarStateCallback, ToolBarDockCallback, } from '@kit.ArkUI';
```

## getDirection

```TypeScript
getDirection(): Axis
```

获取浮动工具栏的停靠方向。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarController-getDirection(): Axis--><!--Device-ToolBarController-getDirection(): Axis-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Axis](arkts-arkui-axis-e.md) | 浮动工具栏的停靠方向。 |

## getDockArea

```TypeScript
getDockArea(): DockArea
```

获取浮动工具栏当前停靠的区域。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarController-getDockArea(): DockArea--><!--Device-ToolBarController-getDockArea(): DockArea-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DockArea](arkts-arkui-arkui-advanced-toolbarcontainer-dockarea-e.md) | 工具栏当前停靠的区域。 |

## getState

```TypeScript
getState(): ToolBarState
```

获取当前工具栏状态。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarController-getState(): ToolBarState--><!--Device-ToolBarController-getState(): ToolBarState-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ToolBarState](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarstate-e.md) | 当前工具栏状态。 |

## minimize

```TypeScript
minimize(): void
```

将浮动工具栏最小化为悬浮球，从FLOATING切换为MINIMIZED。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarController-minimize(): void--><!--Device-ToolBarController-minimize(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## pin

```TypeScript
pin(): void
```

将工具栏固定为FIXED状态。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarController-pin(): void--><!--Device-ToolBarController-pin(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## restore

```TypeScript
restore(): void
```

将最小化悬浮球恢复为浮动工具栏，从MINIMIZED切换为FLOATING。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarController-restore(): void--><!--Device-ToolBarController-restore(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## setDock

```TypeScript
setDock(area: DockArea, direction?: Axis): void
```

将浮动工具栏停靠到指定区域，可指定停靠方向。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarController-setDock(area: DockArea, direction?: Axis): void--><!--Device-ToolBarController-setDock(area: DockArea, direction?: Axis): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| area | [DockArea](arkts-arkui-arkui-advanced-toolbarcontainer-dockarea-e.md) | 是 | 要设置的停靠区域。 |
| direction | [Axis](arkts-arkui-axis-e.md) | 否 | 停靠方向。停靠方向默认为当前浮动工具栏的排列方向。 |

## unpin

```TypeScript
unpin(): void
```

取消固定工具栏，从FIXED状态切换为FLOATING状态。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarController-unpin(): void--><!--Device-ToolBarController-unpin(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
