# ToolBarContainerOptions

```TypeScript
export interface ToolBarContainerOptions
```

Defines options for configuring the layout, safe area avoidance, and handedness adaptation of the toolbar container.

**Since:** 26.1.0

<!--Device-unnamed-export interface ToolBarContainerOptions--><!--Device-unnamed-export interface ToolBarContainerOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { ToolBarState, DockArea, DockCornerMode, ToolBarSafeAreaMode, HandednessAdaptationMode, ToolBarFloatingOptions, ToolBarFloatingConfigs, ToolBarMinimizeOptions, ToolBarMinimizeConfigs, ToolBarController, ToolBarInitialParams, ToolBarParams, ToolBarConfigs, ToolBarCallbacks, ToolBarDockOffsetOptions, ToolBarSafeAreaOptions, ToolBarContainerOptions, ToolBarContainerConfigs, ToolBarContainer, ToolBarDragStateCallback, ToolBarDragOffsetCallback, ToolBarStateCallback, ToolBarDockCallback, } from '@kit.ArkUI';
```

## adaptToHandedness

```TypeScript
adaptToHandedness?: HandednessAdaptationMode
```

Handedness adaptation mode. Default value: HandednessAdaptationMode.NONE. This parameter takes effect only when there is a single toolbar.

**Type:** [HandednessAdaptationMode](arkts-arkui-arkui-advanced-toolbarcontainer-handednessadaptationmode-e.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarContainerOptions-adaptToHandedness?: HandednessAdaptationMode--><!--Device-ToolBarContainerOptions-adaptToHandedness?: HandednessAdaptationMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## dockOffset

```TypeScript
dockOffset?: ToolBarDockOffsetOptions
```

Docking offsets of the floating toolbar.

**Type:** [ToolBarDockOffsetOptions](arkts-arkui-arkui-advanced-toolbarcontainer-toolbardockoffsetoptions-i.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarContainerOptions-dockOffset?: ToolBarDockOffsetOptions--><!--Device-ToolBarContainerOptions-dockOffset?: ToolBarDockOffsetOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## gutter

```TypeScript
gutter?: LengthMetrics
```

Avoidance spacing used when the toolbar is too long and overflows.

**Type:** [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarContainerOptions-gutter?: LengthMetrics--><!--Device-ToolBarContainerOptions-gutter?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## safeArea

```TypeScript
safeArea?: ToolBarSafeAreaOptions
```

Safe area avoidance mode. Default value: [NONE](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarsafeareamode-e.md#none) for each edge.

**Type:** [ToolBarSafeAreaOptions](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarsafeareaoptions-i.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarContainerOptions-safeArea?: ToolBarSafeAreaOptions--><!--Device-ToolBarContainerOptions-safeArea?: ToolBarSafeAreaOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
