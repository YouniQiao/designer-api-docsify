# ToolBarMinimizeConfigs

```TypeScript
export class ToolBarMinimizeConfigs
```

Observable configuration store for the minimized floating ball, corresponding to [ToolBarMinimizeOptions](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarminimizeoptions-i.md).

**Since:** 26.1.0

**Decorator:** @ObservedV2

<!--Device-unnamed-export class ToolBarMinimizeConfigs--><!--Device-unnamed-export class ToolBarMinimizeConfigs-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { ToolBarState, DockArea, DockCornerMode, ToolBarSafeAreaMode, HandednessAdaptationMode, ToolBarFloatingOptions, ToolBarFloatingConfigs, ToolBarMinimizeOptions, ToolBarMinimizeConfigs, ToolBarController, ToolBarInitialParams, ToolBarParams, ToolBarConfigs, ToolBarCallbacks, ToolBarDockOffsetOptions, ToolBarSafeAreaOptions, ToolBarContainerOptions, ToolBarContainerConfigs, ToolBarContainer, ToolBarDragStateCallback, ToolBarDragOffsetCallback, ToolBarStateCallback, ToolBarDockCallback, } from '@kit.ArkUI';
```

## constructor

```TypeScript
constructor(options?: ToolBarMinimizeOptions)
```

Constructor of ToolBarMinimizeConfigs. When options is omitted, all fields use their respective default values.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarMinimizeConfigs-constructor(options?: ToolBarMinimizeOptions)--><!--Device-ToolBarMinimizeConfigs-constructor(options?: ToolBarMinimizeOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ToolBarMinimizeOptions](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarminimizeoptions-i.md) | No | Options for the minimized floating ball. |

## builder

```TypeScript
builder?: CustomBuilder
```

Custom builder. Default value: undefined, indicating that there is no custom content.

**Type:** [CustomBuilder](../arkts-components/arkts-arkui-common-comp-custombuilder-t.md)

**Since:** 26.1.0

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarMinimizeConfigs-builder?: CustomBuilder--><!--Device-ToolBarMinimizeConfigs-builder?: CustomBuilder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## buoySize

```TypeScript
buoySize?: LengthMetrics
```

Diameter of the minimized floating ball.

**Type:** [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)

**Since:** 26.1.0

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarMinimizeConfigs-buoySize?: LengthMetrics--><!--Device-ToolBarMinimizeConfigs-buoySize?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## icon

```TypeScript
icon?: ResourceStr | SymbolGlyphModifier
```

Icon. Default value: undefined, indicating that there is no icon content.

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md) &#124; [SymbolGlyphModifier](../../apis-default/arkts-apis/arkts-default-arkui-modifier.md)

**Since:** 26.1.0

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarMinimizeConfigs-icon?: ResourceStr | SymbolGlyphModifier--><!--Device-ToolBarMinimizeConfigs-icon?: ResourceStr | SymbolGlyphModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## iconColor

```TypeScript
iconColor?: ColorMetrics
```

Icon color. Default value: $r('sys.color.icon_primary').

**Type:** [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md)

**Since:** 26.1.0

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarMinimizeConfigs-iconColor?: ColorMetrics--><!--Device-ToolBarMinimizeConfigs-iconColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## iconSize

```TypeScript
iconSize?: LengthMetrics
```

Icon size.

**Type:** [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)

**Since:** 26.1.0

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarMinimizeConfigs-iconSize?: LengthMetrics--><!--Device-ToolBarMinimizeConfigs-iconSize?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## text

```TypeScript
text?: ResourceStr
```

Text label. Default value: undefined, indicating that there is no text content.

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 26.1.0

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarMinimizeConfigs-text?: ResourceStr--><!--Device-ToolBarMinimizeConfigs-text?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textColor

```TypeScript
textColor?: ColorMetrics
```

Text color. Default value: $r('sys.color.font_primary').

**Type:** [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md)

**Since:** 26.1.0

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarMinimizeConfigs-textColor?: ColorMetrics--><!--Device-ToolBarMinimizeConfigs-textColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
