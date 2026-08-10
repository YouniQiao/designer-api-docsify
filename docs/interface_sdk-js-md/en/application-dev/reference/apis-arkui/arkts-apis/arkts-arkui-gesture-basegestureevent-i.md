# BaseGestureEvent

基础手势事件类型。继承自[BaseEvent](arkts-arkui-common-baseevent-i.md)。

**Inheritance/Implementation:** BaseGestureEvent extends [BaseEvent](arkts-arkui-common-baseevent-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface BaseGestureEvent extends BaseEvent--><!--Device-unnamed-export interface BaseGestureEvent extends BaseEvent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fingerInfos

```TypeScript
fingerInfos?: FingerInfo[]
```

参与触发事件的所有有效触点信息。默认值为空数组[]，返回空数组时，表示当前无有效触点信息。

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

触发事件的所有手指信息。

**Type:** [FingerInfo](arkts-arkui-gesture-fingerinfo-i.md)[]

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseGestureEvent-fingerList: FingerInfo[]--><!--Device-BaseGestureEvent-fingerList: FingerInfo[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

