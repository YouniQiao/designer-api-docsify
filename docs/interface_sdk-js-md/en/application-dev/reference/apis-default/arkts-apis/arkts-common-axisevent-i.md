# AxisEvent

The axis event triggers this method invocation.

@extends BaseEvent

**Inheritance/Implementation:** AxisEvent extends [BaseEvent](arkts-common-baseevent-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface AxisEvent--><!--Device-unnamed-export declare interface AxisEvent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getCurrentLocalPosition

```TypeScript
getCurrentLocalPosition(): Coordinate2D
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-AxisEvent-getCurrentLocalPosition(): Coordinate2D--><!--Device-AxisEvent-getCurrentLocalPosition(): Coordinate2D-End-->

**Return value:**

| Type | Description |
| --- | --- |
## getHorizontalAxisValue

```TypeScript
getHorizontalAxisValue(): double
```

Obtains the value of the horizontal scroll axis for this axis event.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AxisEvent-getHorizontalAxisValue(): double--><!--Device-AxisEvent-getHorizontalAxisValue(): double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| double |  |

## getPinchAxisScaleValue

```TypeScript
getPinchAxisScaleValue(): double
```

Obtains the value of the pinch axis for this axis event.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AxisEvent-getPinchAxisScaleValue(): double--><!--Device-AxisEvent-getPinchAxisScaleValue(): double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| double |  |

## getVerticalAxisValue

```TypeScript
getVerticalAxisValue(): double
```

Obtains the value of the vertical scroll axis for this axis event.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AxisEvent-getVerticalAxisValue(): double--><!--Device-AxisEvent-getVerticalAxisValue(): double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| double |  |

## hasAxis

```TypeScript
hasAxis(axisType: AxisType): boolean
```

Checks whether this event contains a specified axis type.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AxisEvent-hasAxis(axisType: AxisType): boolean--><!--Device-AxisEvent-hasAxis(axisType: AxisType): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| axisType | [AxisType](../../apis-arkui/arkts-apis/arkts-arkui-axistype-e.md) | Yes | Indicates the axis type. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean |  |

## propagation

```TypeScript
propagation(): void
```

Active event bubbling.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AxisEvent-propagation(): void--><!--Device-AxisEvent-propagation(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## action

```TypeScript
action: AxisAction
```

Axis action of the axis event.

**Type:** [AxisAction](../../apis-arkui/arkts-apis/arkts-arkui-axisaction-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AxisEvent-action: AxisAction--><!--Device-AxisEvent-action: AxisAction-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## default

```TypeScript
default
```

Gets the coordinates of the top-left corner of the current component based on its real-time position.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AxisEvent-default--><!--Device-AxisEvent-default-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## displayX

```TypeScript
displayX: double
```

X coordinate of the mouse cursor relative to the left edge of the device screen.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AxisEvent-displayX: double--><!--Device-AxisEvent-displayX: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## displayY

```TypeScript
displayY: double
```

Y coordinate of the mouse cursor relative to the upper edge of the device screen.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AxisEvent-displayY: double--><!--Device-AxisEvent-displayY: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## eventHandleId

```TypeScript
eventHandleId?: int
```

The unique handle for the event processing session. This handle must be used for any further operations on the event. The system ensures that for a given finger, only one event with this handle can be active at a time.

**Type:** int

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AxisEvent-eventHandleId?: int--><!--Device-AxisEvent-eventHandleId?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## globalDisplayX

```TypeScript
globalDisplayX?: double
```

X coordinate of the point relative to the global display.

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AxisEvent-globalDisplayX?: double--><!--Device-AxisEvent-globalDisplayX?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## globalDisplayY

```TypeScript
globalDisplayY?: double
```

Y coordinate of the point relative to the global display.

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AxisEvent-globalDisplayY?: double--><!--Device-AxisEvent-globalDisplayY?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scrollStep

```TypeScript
scrollStep?: int
```

Scroll step configuration which is only mouse wheel has.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AxisEvent-scrollStep?: int--><!--Device-AxisEvent-scrollStep?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## windowX

```TypeScript
windowX: double
```

X coordinate of the mouse cursor relative to the left edge of the current window.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AxisEvent-windowX: double--><!--Device-AxisEvent-windowX: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## windowY

```TypeScript
windowY: double
```

Y coordinate of the mouse cursor relative to the upper edge of the current window.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AxisEvent-windowY: double--><!--Device-AxisEvent-windowY: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## x

```TypeScript
x: double
```

X coordinate of the mouse cursor relative to the left edge of the axis event hit element.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AxisEvent-x: double--><!--Device-AxisEvent-x: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## y

```TypeScript
y: double
```

Y coordinate of the mouse cursor relative to the upper edge of the axis event hit element.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AxisEvent-y: double--><!--Device-AxisEvent-y: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

