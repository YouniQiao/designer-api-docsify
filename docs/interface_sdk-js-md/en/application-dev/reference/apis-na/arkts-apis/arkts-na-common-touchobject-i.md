# TouchObject

Type of the touch event.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare interface TouchObject--><!--Device-unnamed-export declare interface TouchObject-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getCurrentLocalPosition

```TypeScript
getCurrentLocalPosition(): Coordinate2D
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta only, since version -1.

**Deprecated since:** -1

<!--Device-TouchObject-getCurrentLocalPosition(): Coordinate2D--><!--Device-TouchObject-getCurrentLocalPosition(): Coordinate2D-End-->

**Return value:**

| Type | Description |
| --- | --- |
| [Coordinate2D](../../apis-arkui/arkts-apis/arkts-arkui-coordinate2d-i.md) |  |

## default

```TypeScript
default
```

Gets the coordinates of the top-left corner of the current component based on its real-time position.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-TouchObject-default--><!--Device-TouchObject-default-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## displayX

```TypeScript
displayX: double
```

X coordinate of the touch point relative to the upper left corner of the application screen.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-TouchObject-displayX: double--><!--Device-TouchObject-displayX: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## displayY

```TypeScript
displayY: double
```

Y coordinate of the touch point relative to the upper left corner of the application screen.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-TouchObject-displayY: double--><!--Device-TouchObject-displayY: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## globalDisplayX

```TypeScript
globalDisplayX?: double
```

X coordinate of the point relative to the global display.

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-TouchObject-globalDisplayX?: double--><!--Device-TouchObject-globalDisplayX?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## globalDisplayY

```TypeScript
globalDisplayY?: double
```

Y coordinate of the point relative to the global display.

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-TouchObject-globalDisplayY?: double--><!--Device-TouchObject-globalDisplayY?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## hand

```TypeScript
hand?: InteractionHand
```

Whether the event is triggered by a left-hand or right-hand tap.

**Type:** [InteractionHand](../../apis-arkui/arkts-apis/arkts-arkui-interactionhand-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-TouchObject-hand?: InteractionHand--><!--Device-TouchObject-hand?: InteractionHand-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## height

```TypeScript
height?: double
```

Height of the area pressed by the finger.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-TouchObject-height?: double--><!--Device-TouchObject-height?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## id

```TypeScript
id: int
```

Unique identifier of a finger.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-TouchObject-id: int--><!--Device-TouchObject-id: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## pressedTime

```TypeScript
pressedTime?: long
```

Time when the finger is pressed.

**Type:** long

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-TouchObject-pressedTime?: long--><!--Device-TouchObject-pressedTime?: long-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## pressure

```TypeScript
pressure?: double
```

Pressure value of the finger press.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-TouchObject-pressure?: double--><!--Device-TouchObject-pressure?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type: TouchType
```

Type of the touch event.

**Type:** [TouchType](../../apis-arkui/arkts-apis/arkts-arkui-touchtype-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-TouchObject-type: TouchType--><!--Device-TouchObject-type: TouchType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## width

```TypeScript
width?: double
```

Width of the area pressed by the finger.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-TouchObject-width?: double--><!--Device-TouchObject-width?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## windowX

```TypeScript
windowX: double
```

X coordinate of the touch point relative to the upper left corner of the application window.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-TouchObject-windowX: double--><!--Device-TouchObject-windowX: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## windowY

```TypeScript
windowY: double
```

Y coordinate of the touch point relative to the upper left corner of the application window.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-TouchObject-windowY: double--><!--Device-TouchObject-windowY: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## x

```TypeScript
x: double
```

X coordinate of the touch point relative to the upper left corner of the event responding component.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-TouchObject-x: double--><!--Device-TouchObject-x: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## y

```TypeScript
y: double
```

Y coordinate of the touch point relative to the upper left corner of the event responding component.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-TouchObject-y: double--><!--Device-TouchObject-y: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

