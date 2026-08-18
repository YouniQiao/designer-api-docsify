# TapGestureHandlerOptions

Defines the TapGestureHandler options.

**Inheritance/Implementation:** TapGestureHandlerOptions extends [BaseHandlerOptions](arkts-arkui-gesture-basehandleroptions-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export interface TapGestureHandlerOptions--><!--Device-unnamed-export interface TapGestureHandlerOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## count

```TypeScript
count?: int
```

Indicates the number of consecutive clicks recognized. If the value is less than 1, the default value is used. The default value is 1.

**Type:** int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TapGestureHandlerOptions-count?: int--><!--Device-TapGestureHandlerOptions-count?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## distanceThreshold

```TypeScript
distanceThreshold?: double
```

The limited move distance of click. If the value is less than 0, the default value is used.

**Type:** double

**Default:** Infinity

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TapGestureHandlerOptions-distanceThreshold?: double--><!--Device-TapGestureHandlerOptions-distanceThreshold?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fingers

```TypeScript
fingers?: int
```

Indicates the hand index that triggers the click. If the value is less than 1, the default value is used. The default value is 1.

**Type:** int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TapGestureHandlerOptions-fingers?: int--><!--Device-TapGestureHandlerOptions-fingers?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

