# PanGestureHandlerOptions

Defines the PanGestureHandler options.

**Inheritance/Implementation:** PanGestureHandlerOptions extends [BaseHandlerOptions](arkts-arkui-gesture-basehandleroptions-i.md#BaseHandlerOptions)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export interface PanGestureHandlerOptions--><!--Device-unnamed-export interface PanGestureHandlerOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## direction

```TypeScript
direction?: PanDirection
```

Indicates the move direction of the pan gesture. The default value is PanDirection.All.

**Type:** [PanDirection](arkts-arkui-gesture-pandirection-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PanGestureHandlerOptions-direction?: PanDirection--><!--Device-PanGestureHandlerOptions-direction?: PanDirection-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## distance

```TypeScript
distance?: double
```

Indicates minimum move distance. The default value is 5vp.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PanGestureHandlerOptions-distance?: double--><!--Device-PanGestureHandlerOptions-distance?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## distanceMap

```TypeScript
distanceMap?: Map<SourceTool, double>
```

Indicates minimum move distance map.

**Type:** Map&lt;[SourceTool](../arkts-components/arkts-arkui-sourcetool-e.md), double&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PanGestureHandlerOptions-distanceMap?: Map<SourceTool, double>--><!--Device-PanGestureHandlerOptions-distanceMap?: Map<SourceTool, double>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fingers

```TypeScript
fingers?: int
```

Indicates the hand index that triggers the pan. If the value is less than 1, the default value is used. The default value is 1.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PanGestureHandlerOptions-fingers?: int--><!--Device-PanGestureHandlerOptions-fingers?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

