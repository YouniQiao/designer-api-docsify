# GestureEvent

Defines event info for gesture.

**Inheritance/Implementation:** GestureEvent extends [BaseEvent](common-baseevent-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface GestureEvent extends BaseEvent--><!--Device-unnamed-export interface GestureEvent extends BaseEvent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## angle

```TypeScript
angle: double
```

Gesture event direction angle.The unit is deg.Used in RotationGesture and SwipeGesture.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureEvent-angle: double--><!--Device-GestureEvent-angle: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fingerInfos

```TypeScript
fingerInfos?: FingerInfo[]
```

All finger information when the gesture event is triggered, the return value is one array, and the array length is just the total fingers count.

**Type:** FingerInfo[]

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureEvent-fingerInfos?: FingerInfo[]--><!--Device-GestureEvent-fingerInfos?: FingerInfo[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fingerList

```TypeScript
fingerList: FingerInfo[]
```

All finger information.Used in LongPressGesture and TapGesture.

**Type:** FingerInfo[]

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureEvent-fingerList: FingerInfo[]--><!--Device-GestureEvent-fingerList: FingerInfo[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## offsetX

```TypeScript
offsetX: double
```

Gesture event offset X.The unit is vp.Used in PanGesture.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureEvent-offsetX: double--><!--Device-GestureEvent-offsetX: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## offsetY

```TypeScript
offsetY: double
```

Gesture event offset Y.The unit is vp.Used in PanGesture.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureEvent-offsetY: double--><!--Device-GestureEvent-offsetY: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## pinchCenterX

```TypeScript
pinchCenterX: double
```

X-axis coordinate of the kneading center point.The unit is vp.Used in PinchGesture.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureEvent-pinchCenterX: double--><!--Device-GestureEvent-pinchCenterX: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## pinchCenterY

```TypeScript
pinchCenterY: double
```

Y-axis coordinate of the kneading center point.The unit is vp.Used in PinchGesture.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureEvent-pinchCenterY: double--><!--Device-GestureEvent-pinchCenterY: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## repeat

```TypeScript
repeat: boolean
```

Indicates whether an event is triggered repeatedly.Used in LongPressGesture.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureEvent-repeat: boolean--><!--Device-GestureEvent-repeat: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scale

```TypeScript
scale: double
```

Scaling ratio.Used in PinchGesture.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureEvent-scale: double--><!--Device-GestureEvent-scale: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## speed

```TypeScript
speed: double
```

Gesture event slide speed.The unit is vp.Used in SwipeGesture.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureEvent-speed: double--><!--Device-GestureEvent-speed: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## tapLocation

```TypeScript
tapLocation?: EventLocationInfo
```

The tap location info used in tap gesture.

**Type:** EventLocationInfo

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureEvent-tapLocation?: EventLocationInfo--><!--Device-GestureEvent-tapLocation?: EventLocationInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## velocity

```TypeScript
velocity: double
```

velocity of the gesture.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureEvent-velocity: double--><!--Device-GestureEvent-velocity: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## velocityX

```TypeScript
velocityX: double
```

X-axis velocity of the gesture.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureEvent-velocityX: double--><!--Device-GestureEvent-velocityX: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## velocityY

```TypeScript
velocityY: double
```

Y-axis velocity of the gesture.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureEvent-velocityY: double--><!--Device-GestureEvent-velocityY: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

