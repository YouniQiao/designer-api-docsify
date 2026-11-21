# ToolBarFloatingConfigs

```TypeScript
export class ToolBarFloatingConfigs
```

浮动工具栏行为的可观察配置存储，与[ToolBarFloatingOptions](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarfloatingoptions-i.md)对应。

**起始版本：** 26.1.0

**装饰器类型：** @ObservedV2

<!--Device-unnamed-export class ToolBarFloatingConfigs--><!--Device-unnamed-export class ToolBarFloatingConfigs-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { ToolBarState, DockArea, DockCornerMode, ToolBarSafeAreaMode, HandednessAdaptationMode, ToolBarFloatingOptions, ToolBarFloatingConfigs, ToolBarMinimizeOptions, ToolBarMinimizeConfigs, ToolBarController, ToolBarInitialParams, ToolBarParams, ToolBarConfigs, ToolBarCallbacks, ToolBarDockOffsetOptions, ToolBarSafeAreaOptions, ToolBarContainerOptions, ToolBarContainerConfigs, ToolBarContainer, ToolBarDragStateCallback, ToolBarDragOffsetCallback, ToolBarStateCallback, ToolBarDockCallback, } from '@kit.ArkUI';
```

## constructor

```TypeScript
constructor(options?: ToolBarFloatingOptions)
```

ToolBarFloatingConfigs的构造函数。当options省略时，所有字段使用各自的默认值。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarFloatingConfigs-constructor(options?: ToolBarFloatingOptions)--><!--Device-ToolBarFloatingConfigs-constructor(options?: ToolBarFloatingOptions)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ToolBarFloatingOptions](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarfloatingoptions-i.md) | 否 | 浮动行为选项。 |

## cornerMode

```TypeScript
cornerMode?: DockCornerMode
```

角落吸附模式。MINIMIZE（默认）表示吸附到角落并跟随所在边缘；EXPAND表示保持拖拽方向。

**类型：** [DockCornerMode](arkts-arkui-arkui-advanced-toolbarcontainer-dockcornermode-e.md)

**起始版本：** 26.1.0

**装饰器类型：** @Trace

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarFloatingConfigs-cornerMode?: DockCornerMode--><!--Device-ToolBarFloatingConfigs-cornerMode?: DockCornerMode-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## dockAreas

```TypeScript
dockAreas?: DockArea[]
```

浮动工具栏允许停靠的区域。默认支持所有可吸附位置。

**类型：** [DockArea](arkts-arkui-arkui-advanced-toolbarcontainer-dockarea-e.md)[]

**起始版本：** 26.1.0

**装饰器类型：** @Trace

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarFloatingConfigs-dockAreas?: DockArea[]--><!--Device-ToolBarFloatingConfigs-dockAreas?: DockArea[]-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## draggable

```TypeScript
draggable?: boolean
```

浮动工具栏是否可拖拽。默认值：true。true表示支持拖拽，false表示禁止拖拽。

**类型：** boolean

**起始版本：** 26.1.0

**装饰器类型：** @Trace

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarFloatingConfigs-draggable?: boolean--><!--Device-ToolBarFloatingConfigs-draggable?: boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## minimizeConfigs

```TypeScript
minimizeConfigs?: ToolBarMinimizeConfigs
```

最小化配置。

**类型：** [ToolBarMinimizeConfigs](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarminimizeconfigs-c.md)

**起始版本：** 26.1.0

**装饰器类型：** @Trace

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarFloatingConfigs-minimizeConfigs?: ToolBarMinimizeConfigs--><!--Device-ToolBarFloatingConfigs-minimizeConfigs?: ToolBarMinimizeConfigs-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
