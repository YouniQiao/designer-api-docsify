# ToolBarFloatingConfigs

```TypeScript
export class ToolBarFloatingConfigs
```

Observable configuration store for floating toolbar behavior, corresponding to [ToolBarFloatingOptions](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarfloatingoptions-i.md).

**Since:** 26.1.0

**Decorator:** @ObservedV2

<!--Device-unnamed-export class ToolBarFloatingConfigs--><!--Device-unnamed-export class ToolBarFloatingConfigs-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { ToolBarState, DockArea, DockCornerMode, ToolBarSafeAreaMode, HandednessAdaptationMode, ToolBarFloatingOptions, ToolBarFloatingConfigs, ToolBarMinimizeOptions, ToolBarMinimizeConfigs, ToolBarController, ToolBarInitialParams, ToolBarParams, ToolBarConfigs, ToolBarCallbacks, ToolBarDockOffsetOptions, ToolBarSafeAreaOptions, ToolBarContainerOptions, ToolBarContainerConfigs, ToolBarContainer, ToolBarDragStateCallback, ToolBarDragOffsetCallback, ToolBarStateCallback, ToolBarDockCallback, } from '@kit.ArkUI';
```

## constructor

```TypeScript
constructor(options?: ToolBarFloatingOptions)
```

Constructor of ToolBarFloatingConfigs. When options is omitted, all fields use their respective default values.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarFloatingConfigs-constructor(options?: ToolBarFloatingOptions)--><!--Device-ToolBarFloatingConfigs-constructor(options?: ToolBarFloatingOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ToolBarFloatingOptions](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarfloatingoptions-i.md) | No | Floating behavior options. |

## cornerMode

```TypeScript
cornerMode?: DockCornerMode
```

Corner snapping mode. MINIMIZE (default) indicates that the toolbar snaps to a corner and follows the edge where it is located; EXPAND indicates that the drag direction is retained.

**Type:** [DockCornerMode](arkts-arkui-arkui-advanced-toolbarcontainer-dockcornermode-e.md)

**Since:** 26.1.0

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarFloatingConfigs-cornerMode?: DockCornerMode--><!--Device-ToolBarFloatingConfigs-cornerMode?: DockCornerMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## dockAreas

```TypeScript
dockAreas?: DockArea[]
```

Areas where the floating toolbar is allowed to dock. All snapping positions are supported by default.

**Type:** [DockArea](arkts-arkui-arkui-advanced-toolbarcontainer-dockarea-e.md)[]

**Since:** 26.1.0

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarFloatingConfigs-dockAreas?: DockArea[]--><!--Device-ToolBarFloatingConfigs-dockAreas?: DockArea[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## draggable

```TypeScript
draggable?: boolean
```

Whether the floating toolbar can be dragged. Default value: true. The value true indicates that dragging is supported, and false indicates that dragging is prohibited.

**Type:** boolean

**Since:** 26.1.0

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarFloatingConfigs-draggable?: boolean--><!--Device-ToolBarFloatingConfigs-draggable?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## minimizeConfigs

```TypeScript
minimizeConfigs?: ToolBarMinimizeConfigs
```

Minimization configuration.

**Type:** [ToolBarMinimizeConfigs](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarminimizeconfigs-c.md)

**Since:** 26.1.0

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarFloatingConfigs-minimizeConfigs?: ToolBarMinimizeConfigs--><!--Device-ToolBarFloatingConfigs-minimizeConfigs?: ToolBarMinimizeConfigs-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
