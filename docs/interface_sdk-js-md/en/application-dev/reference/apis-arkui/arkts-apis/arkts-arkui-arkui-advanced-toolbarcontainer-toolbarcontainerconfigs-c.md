# ToolBarContainerConfigs

```TypeScript
export class ToolBarContainerConfigs
```

Observable configuration store for the toolbar container, corresponding to [ToolBarContainerOptions](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarcontaineroptions-i.md).

**Since:** 26.1.0

**Decorator:** @ObservedV2

<!--Device-unnamed-export class ToolBarContainerConfigs--><!--Device-unnamed-export class ToolBarContainerConfigs-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { ToolBarState, DockArea, DockCornerMode, ToolBarSafeAreaMode, HandednessAdaptationMode, ToolBarFloatingOptions, ToolBarFloatingConfigs, ToolBarMinimizeOptions, ToolBarMinimizeConfigs, ToolBarController, ToolBarInitialParams, ToolBarParams, ToolBarConfigs, ToolBarCallbacks, ToolBarDockOffsetOptions, ToolBarSafeAreaOptions, ToolBarContainerOptions, ToolBarContainerConfigs, ToolBarContainer, ToolBarDragStateCallback, ToolBarDragOffsetCallback, ToolBarStateCallback, ToolBarDockCallback, } from '@kit.ArkUI';
```

## constructor

```TypeScript
constructor(options?: ToolBarContainerOptions)
```

Constructor. When options is omitted, all fields use their respective default values.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarContainerConfigs-constructor(options?: ToolBarContainerOptions)--><!--Device-ToolBarContainerConfigs-constructor(options?: ToolBarContainerOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ToolBarContainerOptions](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarcontaineroptions-i.md) | No | Container options. |

## adaptToHandedness

```TypeScript
adaptToHandedness?: HandednessAdaptationMode
```

Handedness adaptation mode. Default value: HandednessAdaptationMode.NONE.

**Type:** [HandednessAdaptationMode](arkts-arkui-arkui-advanced-toolbarcontainer-handednessadaptationmode-e.md)

**Since:** 26.1.0

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarContainerConfigs-adaptToHandedness?: HandednessAdaptationMode--><!--Device-ToolBarContainerConfigs-adaptToHandedness?: HandednessAdaptationMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## dockOffset

```TypeScript
dockOffset?: ToolBarDockOffsetOptions
```

Docking offsets, in vp. Default value: 16 vp for each edge.

**Type:** [ToolBarDockOffsetOptions](arkts-arkui-arkui-advanced-toolbarcontainer-toolbardockoffsetoptions-i.md)

**Since:** 26.1.0

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarContainerConfigs-dockOffset?: ToolBarDockOffsetOptions--><!--Device-ToolBarContainerConfigs-dockOffset?: ToolBarDockOffsetOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## gutter

```TypeScript
gutter?: LengthMetrics
```

Spacing between toolbars.

**Type:** [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)

**Since:** 26.1.0

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarContainerConfigs-gutter?: LengthMetrics--><!--Device-ToolBarContainerConfigs-gutter?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## safeArea

```TypeScript
safeArea?: ToolBarSafeAreaOptions
```

Safe area mode. Default value: ToolBarSafeAreaMode.NONE for each edge.

**Type:** [ToolBarSafeAreaOptions](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarsafeareaoptions-i.md)

**Since:** 26.1.0

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarContainerConfigs-safeArea?: ToolBarSafeAreaOptions--><!--Device-ToolBarContainerConfigs-safeArea?: ToolBarSafeAreaOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
