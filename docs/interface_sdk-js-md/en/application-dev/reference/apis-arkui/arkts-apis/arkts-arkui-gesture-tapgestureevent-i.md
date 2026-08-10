# TapGestureEvent

继承自[BaseGestureEvent](arkts-arkui-basegestureevent-i.md)。可将该对象作为[onGestureJudgeBegin](arkts-arkui-common-commonmethod-i.md#ongesturejudgebegin)的event参数来传递。

**Inheritance/Implementation:** TapGestureEvent extends [BaseGestureEvent](arkts-arkui-basegestureevent-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface TapGestureEvent extends BaseGestureEvent--><!--Device-unnamed-export interface TapGestureEvent extends BaseGestureEvent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## tapLocation

```TypeScript
tapLocation?: EventLocationInfo
```

获取点击手势的坐标信息。

**Type:** [EventLocationInfo](arkts-arkui-eventlocationinfo-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TapGestureEvent-tapLocation?: EventLocationInfo--><!--Device-TapGestureEvent-tapLocation?: EventLocationInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

