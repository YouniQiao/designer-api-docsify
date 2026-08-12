# TapGestureEvent

Inherits from [BaseGestureEvent](arkts-arkui-basegestureevent-i.md#BaseGestureEvent). This object can be passed as the **event** parameter of   
[onGestureJudgeBegin](CommonMethod#onGestureJudgeBegin).

**Inheritance/Implementation:** TapGestureEvent extends [BaseGestureEvent](arkts-arkui-basegestureevent-i.md#BaseGestureEvent)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-unnamed-interface TapGestureEvent extends BaseGestureEvent--><!--Device-unnamed-interface TapGestureEvent extends BaseGestureEvent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## tapLocation

```TypeScript
tapLocation?: EventLocationInfo
```

Coordinate information of the current tap gesture. For non-tap gestures, the return value of **tapLocation** is   
**undefined**.

**Type:** [EventLocationInfo](arkts-arkui-eventlocationinfo-i.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TapGestureEvent-tapLocation?: EventLocationInfo--><!--Device-TapGestureEvent-tapLocation?: EventLocationInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

