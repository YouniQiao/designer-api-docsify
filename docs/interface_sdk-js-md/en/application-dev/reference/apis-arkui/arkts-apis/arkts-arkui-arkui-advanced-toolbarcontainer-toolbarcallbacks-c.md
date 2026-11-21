# ToolBarCallbacks

```TypeScript
export class ToolBarCallbacks
```

Defines a collection of callbacks for toolbar dragging, snapping, and state changes.

**Since:** 26.1.0

<!--Device-unnamed-export class ToolBarCallbacks--><!--Device-unnamed-export class ToolBarCallbacks-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { ToolBarState, DockArea, DockCornerMode, ToolBarSafeAreaMode, HandednessAdaptationMode, ToolBarFloatingOptions, ToolBarFloatingConfigs, ToolBarMinimizeOptions, ToolBarMinimizeConfigs, ToolBarController, ToolBarInitialParams, ToolBarParams, ToolBarConfigs, ToolBarCallbacks, ToolBarDockOffsetOptions, ToolBarSafeAreaOptions, ToolBarContainerOptions, ToolBarContainerConfigs, ToolBarContainer, ToolBarDragStateCallback, ToolBarDragOffsetCallback, ToolBarStateCallback, ToolBarDockCallback, } from '@kit.ArkUI';
```

## onDock

```TypeScript
onDock?: ToolBarDockCallback
```

Callback invoked when the toolbar docks to a new area.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarCallbacks-onDock?: ToolBarDockCallback--><!--Device-ToolBarCallbacks-onDock?: ToolBarDockCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDrag

```TypeScript
onDrag?: ToolBarDragOffsetCallback
```

Callback invoked during dragging, which returns the X-axis and Y-axis offsets in vp.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarCallbacks-onDrag?: ToolBarDragOffsetCallback--><!--Device-ToolBarCallbacks-onDrag?: ToolBarDragOffsetCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDragEnd

```TypeScript
onDragEnd?: ToolBarDragStateCallback
```

Callback invoked when the user finishes dragging the toolbar.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarCallbacks-onDragEnd?: ToolBarDragStateCallback--><!--Device-ToolBarCallbacks-onDragEnd?: ToolBarDragStateCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDragStart

```TypeScript
onDragStart?: ToolBarDragStateCallback
```

Callback invoked when the user starts dragging the toolbar.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarCallbacks-onDragStart?: ToolBarDragStateCallback--><!--Device-ToolBarCallbacks-onDragStart?: ToolBarDragStateCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onStateChange

```TypeScript
onStateChange?: ToolBarStateCallback
```

Callback invoked when the toolbar state changes.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarCallbacks-onStateChange?: ToolBarStateCallback--><!--Device-ToolBarCallbacks-onStateChange?: ToolBarStateCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
