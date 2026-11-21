# ToolBarController

```TypeScript
export class ToolBarController
```

Defines a controller for imperatively managing toolbar docking, pinning, and minimization states.

**Since:** 26.1.0

<!--Device-unnamed-export class ToolBarController--><!--Device-unnamed-export class ToolBarController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { ToolBarState, DockArea, DockCornerMode, ToolBarSafeAreaMode, HandednessAdaptationMode, ToolBarFloatingOptions, ToolBarFloatingConfigs, ToolBarMinimizeOptions, ToolBarMinimizeConfigs, ToolBarController, ToolBarInitialParams, ToolBarParams, ToolBarConfigs, ToolBarCallbacks, ToolBarDockOffsetOptions, ToolBarSafeAreaOptions, ToolBarContainerOptions, ToolBarContainerConfigs, ToolBarContainer, ToolBarDragStateCallback, ToolBarDragOffsetCallback, ToolBarStateCallback, ToolBarDockCallback, } from '@kit.ArkUI';
```

## getDirection

```TypeScript
getDirection(): Axis
```

Obtains the docking direction of the floating toolbar.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarController-getDirection(): Axis--><!--Device-ToolBarController-getDirection(): Axis-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [Axis](arkts-arkui-axis-e.md) | Docking direction of the floating toolbar. |

## getDockArea

```TypeScript
getDockArea(): DockArea
```

Obtains the area where the floating toolbar is currently docked.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarController-getDockArea(): DockArea--><!--Device-ToolBarController-getDockArea(): DockArea-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [DockArea](arkts-arkui-arkui-advanced-toolbarcontainer-dockarea-e.md) | Area where the toolbar is currently docked. |

## getState

```TypeScript
getState(): ToolBarState
```

Obtains the current toolbar state.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarController-getState(): ToolBarState--><!--Device-ToolBarController-getState(): ToolBarState-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [ToolBarState](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarstate-e.md) | Current toolbar state. |

## minimize

```TypeScript
minimize(): void
```

Minimizes the floating toolbar to a floating ball, switching it from FLOATING to MINIMIZED.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarController-minimize(): void--><!--Device-ToolBarController-minimize(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## pin

```TypeScript
pin(): void
```

Pins the toolbar in the FIXED state.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarController-pin(): void--><!--Device-ToolBarController-pin(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## restore

```TypeScript
restore(): void
```

Restores the minimized floating ball to a floating toolbar, switching it from MINIMIZED to FLOATING.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarController-restore(): void--><!--Device-ToolBarController-restore(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## setDock

```TypeScript
setDock(area: DockArea, direction?: Axis): void
```

Docks the floating toolbar to the specified area, with an optional docking direction.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarController-setDock(area: DockArea, direction?: Axis): void--><!--Device-ToolBarController-setDock(area: DockArea, direction?: Axis): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| area | [DockArea](arkts-arkui-arkui-advanced-toolbarcontainer-dockarea-e.md) | Yes | Docking area to set. |
| direction | [Axis](arkts-arkui-axis-e.md) | No | Docking direction. By default, the docking direction is the arrangement direction of the current floating toolbar. |

## unpin

```TypeScript
unpin(): void
```

Unpins the toolbar, switching it from FIXED to FLOATING.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarController-unpin(): void--><!--Device-ToolBarController-unpin(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
