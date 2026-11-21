# ToolBarInitialParams

```TypeScript
export interface ToolBarInitialParams
```

Initial position parameters of the toolbar, specifying the docking area, direction, and state at creation.

**Since:** 26.1.0

<!--Device-unnamed-export interface ToolBarInitialParams--><!--Device-unnamed-export interface ToolBarInitialParams-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { ToolBarState, DockArea, DockCornerMode, ToolBarSafeAreaMode, HandednessAdaptationMode, ToolBarFloatingOptions, ToolBarFloatingConfigs, ToolBarMinimizeOptions, ToolBarMinimizeConfigs, ToolBarController, ToolBarInitialParams, ToolBarParams, ToolBarConfigs, ToolBarCallbacks, ToolBarDockOffsetOptions, ToolBarSafeAreaOptions, ToolBarContainerOptions, ToolBarContainerConfigs, ToolBarContainer, ToolBarDragStateCallback, ToolBarDragOffsetCallback, ToolBarStateCallback, ToolBarDockCallback, } from '@kit.ArkUI';
```

## direction

```TypeScript
direction?: Axis
```

Initial docking direction of the toolbar. By default, the direction is aligned with the edge to which the toolbar is snapped.

**Type:** [Axis](arkts-arkui-axis-e.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarInitialParams-direction?: Axis--><!--Device-ToolBarInitialParams-direction?: Axis-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## dockArea

```TypeScript
dockArea: DockArea
```

Initial area where the toolbar is docked.

**Type:** [DockArea](arkts-arkui-arkui-advanced-toolbarcontainer-dockarea-e.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarInitialParams-dockArea: DockArea--><!--Device-ToolBarInitialParams-dockArea: DockArea-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## state

```TypeScript
state?: ToolBarState
```

Initial state of the toolbar. Default value: [FLOATING](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarstate-e.md#floating).

**Type:** [ToolBarState](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarstate-e.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarInitialParams-state?: ToolBarState--><!--Device-ToolBarInitialParams-state?: ToolBarState-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
