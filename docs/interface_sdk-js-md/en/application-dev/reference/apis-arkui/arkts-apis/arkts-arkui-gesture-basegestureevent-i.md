# BaseGestureEvent

Defines the gesture base event.

**Inheritance/Implementation:** BaseGestureEvent extends [BaseEvent](arkts-arkui-common-baseevent-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface BaseGestureEvent extends BaseEvent--><!--Device-unnamed-export interface BaseGestureEvent extends BaseEvent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fingerInfos

```TypeScript
fingerInfos?: FingerInfo[]
```

All finger information when the gesture event is triggered, the return value is one array, and the array length is just the total fingers count.

**Type:** [FingerInfo](arkts-arkui-gesture-fingerinfo-i.md)[]

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseGestureEvent-fingerInfos?: FingerInfo[]--><!--Device-BaseGestureEvent-fingerInfos?: FingerInfo[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fingerList

```TypeScript
fingerList: FingerInfo[]
```

All finger information.

**Type:** [FingerInfo](arkts-arkui-gesture-fingerinfo-i.md)[]

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseGestureEvent-fingerList: FingerInfo[]--><!--Device-BaseGestureEvent-fingerList: FingerInfo[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

