# ToolBarMinimizeOptions

```TypeScript
export interface ToolBarMinimizeOptions
```

Defines options for configuring the minimized floating ball of the toolbar.

**Since:** 26.1.0

<!--Device-unnamed-export interface ToolBarMinimizeOptions--><!--Device-unnamed-export interface ToolBarMinimizeOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { ToolBarState, DockArea, DockCornerMode, ToolBarSafeAreaMode, HandednessAdaptationMode, ToolBarFloatingOptions, ToolBarFloatingConfigs, ToolBarMinimizeOptions, ToolBarMinimizeConfigs, ToolBarController, ToolBarInitialParams, ToolBarParams, ToolBarConfigs, ToolBarCallbacks, ToolBarDockOffsetOptions, ToolBarSafeAreaOptions, ToolBarContainerOptions, ToolBarContainerConfigs, ToolBarContainer, ToolBarDragStateCallback, ToolBarDragOffsetCallback, ToolBarStateCallback, ToolBarDockCallback, } from '@kit.ArkUI';
```

## builder

```TypeScript
builder?: CustomBuilder
```

Custom builder. Default value: undefined, indicating that there is no custom content.

**Type:** [CustomBuilder](../arkts-components/arkts-arkui-common-comp-custombuilder-t.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarMinimizeOptions-builder?: CustomBuilder--><!--Device-ToolBarMinimizeOptions-builder?: CustomBuilder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## buoySize

```TypeScript
buoySize?: LengthMetrics
```

Diameter of the minimized floating ball.

**Type:** [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarMinimizeOptions-buoySize?: LengthMetrics--><!--Device-ToolBarMinimizeOptions-buoySize?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## icon

```TypeScript
icon?: ResourceStr | SymbolGlyphModifier
```

Icon. Default value: undefined, indicating that there is no icon content.

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md) &#124; [SymbolGlyphModifier](../../apis-default/arkts-apis/arkts-default-arkui-modifier.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarMinimizeOptions-icon?: ResourceStr | SymbolGlyphModifier--><!--Device-ToolBarMinimizeOptions-icon?: ResourceStr | SymbolGlyphModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## iconColor

```TypeScript
iconColor?: ColorMetrics
```

Icon color. Default value: $r('sys.color.icon_primary').

**Type:** [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarMinimizeOptions-iconColor?: ColorMetrics--><!--Device-ToolBarMinimizeOptions-iconColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## iconSize

```TypeScript
iconSize?: LengthMetrics
```

Icon size.

**Type:** [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarMinimizeOptions-iconSize?: LengthMetrics--><!--Device-ToolBarMinimizeOptions-iconSize?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## text

```TypeScript
text?: ResourceStr
```

Text label. Default value: undefined, indicating that there is no text content.

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarMinimizeOptions-text?: ResourceStr--><!--Device-ToolBarMinimizeOptions-text?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textColor

```TypeScript
textColor?: ColorMetrics
```

Text color. Default value: $r('sys.color.font_primary').

**Type:** [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarMinimizeOptions-textColor?: ColorMetrics--><!--Device-ToolBarMinimizeOptions-textColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
