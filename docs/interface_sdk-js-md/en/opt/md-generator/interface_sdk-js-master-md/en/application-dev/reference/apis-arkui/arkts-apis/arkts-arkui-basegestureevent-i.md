# BaseGestureEvent

Defines the basic gesture event type. Inherits from [BaseEvent](../arkts-components/arkts-arkui-baseevent-i.md#baseevent).

**Inheritance/Implementation:** BaseGestureEvent extends [BaseEvent](../arkts-components/arkts-arkui-baseevent-i.md#baseevent)

**Since:** 11

<!--Device-unnamed-interface BaseGestureEvent--><!--Device-unnamed-interface BaseGestureEvent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## fingerInfos

```TypeScript
fingerInfos?: FingerInfo[]
```

Information about touch points of the gesture event. For gesture events initiated by a touchscreen, **fingerInfos** includes information about all touch points. For gesture events initiated by a mouse or touchpad, **fingerInfos** contains only one touch point. **NOTE：****fingerInfos** only records information about effective fingers that participate in the touch. Fingers that are pressed first but do not participate in triggering of the current gesture will not be shown in **fingerInfos**. The default value is an empty array **[]**, and an empty array indicates no effective touch point information.

**Type:** [FingerInfo](arkts-arkui-fingerinfo-i.md)[]

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-BaseGestureEvent-fingerInfos?: FingerInfo[]--><!--Device-BaseGestureEvent-fingerInfos?: FingerInfo[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fingerList

```TypeScript
fingerList: FingerInfo[]
```

Information about all fingers triggering the event.

**Type:** [FingerInfo](arkts-arkui-fingerinfo-i.md)[]

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BaseGestureEvent-fingerList: FingerInfo[]--><!--Device-BaseGestureEvent-fingerList: FingerInfo[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
