# ToolBarFloatingOptions

```TypeScript
export interface ToolBarFloatingOptions
```

配置工具栏浮动行为的选项。

**起始版本：** 26.1.0

<!--Device-unnamed-export interface ToolBarFloatingOptions--><!--Device-unnamed-export interface ToolBarFloatingOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { ToolBarState, DockArea, DockCornerMode, ToolBarSafeAreaMode, HandednessAdaptationMode, ToolBarFloatingOptions, ToolBarFloatingConfigs, ToolBarMinimizeOptions, ToolBarMinimizeConfigs, ToolBarController, ToolBarInitialParams, ToolBarParams, ToolBarConfigs, ToolBarCallbacks, ToolBarDockOffsetOptions, ToolBarSafeAreaOptions, ToolBarContainerOptions, ToolBarContainerConfigs, ToolBarContainer, ToolBarDragStateCallback, ToolBarDragOffsetCallback, ToolBarStateCallback, ToolBarDockCallback, } from '@kit.ArkUI';
```

## cornerMode

```TypeScript
cornerMode?: DockCornerMode
```

角落吸附模式。MINIMIZE（默认）表示吸附到角落并跟随所在边缘；EXPAND表示保持拖拽方向。

**类型：** [DockCornerMode](arkts-arkui-arkui-advanced-toolbarcontainer-dockcornermode-e.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarFloatingOptions-cornerMode?: DockCornerMode--><!--Device-ToolBarFloatingOptions-cornerMode?: DockCornerMode-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## dockAreas

```TypeScript
dockAreas?: DockArea[]
```

浮动工具栏允许停靠的区域。默认值：全部8个区域。

**类型：** [DockArea](arkts-arkui-arkui-advanced-toolbarcontainer-dockarea-e.md)[]

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarFloatingOptions-dockAreas?: DockArea[]--><!--Device-ToolBarFloatingOptions-dockAreas?: DockArea[]-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## draggable

```TypeScript
draggable?: boolean
```

浮动工具栏是否可拖拽。默认值：true。true表示支持拖拽，false表示禁止拖拽。

**类型：** boolean

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarFloatingOptions-draggable?: boolean--><!--Device-ToolBarFloatingOptions-draggable?: boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## minimizeConfigs

```TypeScript
minimizeConfigs?: ToolBarMinimizeConfigs
```

浮动工具栏悬浮球的最小化配置。

**类型：** [ToolBarMinimizeConfigs](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarminimizeconfigs-c.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarFloatingOptions-minimizeConfigs?: ToolBarMinimizeConfigs--><!--Device-ToolBarFloatingOptions-minimizeConfigs?: ToolBarMinimizeConfigs-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
