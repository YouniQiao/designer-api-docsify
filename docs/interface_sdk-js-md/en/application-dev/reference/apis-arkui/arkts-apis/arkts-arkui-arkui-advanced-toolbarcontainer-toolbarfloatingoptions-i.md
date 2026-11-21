# ToolBarFloatingOptions

```TypeScript
export interface ToolBarFloatingOptions
```

Defines options for configuring the floating behavior of the toolbar.

**Since:** 26.1.0

<!--Device-unnamed-export interface ToolBarFloatingOptions--><!--Device-unnamed-export interface ToolBarFloatingOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { ToolBarState, DockArea, DockCornerMode, ToolBarSafeAreaMode, HandednessAdaptationMode, ToolBarFloatingOptions, ToolBarFloatingConfigs, ToolBarMinimizeOptions, ToolBarMinimizeConfigs, ToolBarController, ToolBarInitialParams, ToolBarParams, ToolBarConfigs, ToolBarCallbacks, ToolBarDockOffsetOptions, ToolBarSafeAreaOptions, ToolBarContainerOptions, ToolBarContainerConfigs, ToolBarContainer, ToolBarDragStateCallback, ToolBarDragOffsetCallback, ToolBarStateCallback, ToolBarDockCallback, } from '@kit.ArkUI';
```

## cornerMode

```TypeScript
cornerMode?: DockCornerMode
```

Corner snapping mode. MINIMIZE (default) indicates that the toolbar snaps to a corner and follows the edge where it is located; EXPAND indicates that the drag direction is retained.

**Type:** [DockCornerMode](arkts-arkui-arkui-advanced-toolbarcontainer-dockcornermode-e.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarFloatingOptions-cornerMode?: DockCornerMode--><!--Device-ToolBarFloatingOptions-cornerMode?: DockCornerMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## dockAreas

```TypeScript
dockAreas?: DockArea[]
```

Areas where the floating toolbar is allowed to dock. Default value: all eight areas.

**Type:** [DockArea](arkts-arkui-arkui-advanced-toolbarcontainer-dockarea-e.md)[]

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarFloatingOptions-dockAreas?: DockArea[]--><!--Device-ToolBarFloatingOptions-dockAreas?: DockArea[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## draggable

```TypeScript
draggable?: boolean
```

Whether the floating toolbar can be dragged. Default value: true. The value true indicates that dragging is supported, and false indicates that dragging is prohibited.

**Type:** boolean

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarFloatingOptions-draggable?: boolean--><!--Device-ToolBarFloatingOptions-draggable?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## minimizeConfigs

```TypeScript
minimizeConfigs?: ToolBarMinimizeConfigs
```

Minimization configuration for the floating ball of the floating toolbar.

**Type:** [ToolBarMinimizeConfigs](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarminimizeconfigs-c.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarFloatingOptions-minimizeConfigs?: ToolBarMinimizeConfigs--><!--Device-ToolBarFloatingOptions-minimizeConfigs?: ToolBarMinimizeConfigs-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
