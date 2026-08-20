# MouseEvent

The mouse click action triggers this method invocation.

@extends BaseEvent

**Inheritance/Implementation:** MouseEvent extends [BaseEvent](arkts-common-baseevent-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface MouseEvent--><!--Device-unnamed-export declare interface MouseEvent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getCurrentLocalPosition

```TypeScript
getCurrentLocalPosition(): Coordinate2D
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-MouseEvent-getCurrentLocalPosition(): Coordinate2D--><!--Device-MouseEvent-getCurrentLocalPosition(): Coordinate2D-End-->

**Return value:**

| Type | Description |
| --- | --- |
## getHistoricalPoints

```TypeScript
getHistoricalPoints(): MouseHistoricalPoint[] | undefined
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-MouseEvent-getHistoricalPoints(): MouseHistoricalPoint[] | undefined--><!--Device-MouseEvent-getHistoricalPoints(): MouseHistoricalPoint[] | undefined-End-->

**Return value:**

| Type | Description |
| --- | --- |
## stopPropagation

```TypeScript
stopPropagation(): void
```

Stops the event from bubbling upwards or downwards.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MouseEvent-stopPropagation(): void--><!--Device-MouseEvent-stopPropagation(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## action

```TypeScript
action: MouseAction
```

Mouse action of the click event.

**Type:** [MouseAction](../../apis-arkui/arkts-apis/arkts-arkui-mouseaction-e.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MouseEvent-action: MouseAction--><!--Device-MouseEvent-action: MouseAction-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## button

```TypeScript
button: MouseButton
```

Mouse button of the click event.

**Type:** [MouseButton](../../apis-arkui/arkts-apis/arkts-arkui-mousebutton-e.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MouseEvent-button: MouseButton--><!--Device-MouseEvent-button: MouseButton-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## default

```TypeScript
default
```

Obtains all historical points of the current frame.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MouseEvent-default--><!--Device-MouseEvent-default-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## displayX

```TypeScript
displayX: double
```

X coordinate of the mouse pointer relative to the upper left corner of the application screen.

**Type:** double

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MouseEvent-displayX: double--><!--Device-MouseEvent-displayX: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## displayY

```TypeScript
displayY: double
```

Y coordinate of the mouse pointer relative to the upper left corner of the application screen.

**Type:** double

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MouseEvent-displayY: double--><!--Device-MouseEvent-displayY: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## eventHandleId

```TypeScript
eventHandleId?: int
```

The unique handle for the event processing session. This handle must be used for any further operations on the event. The system ensures that for a given finger, only one event with this handle can be active at a time.

**Type:** int

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MouseEvent-eventHandleId?: int--><!--Device-MouseEvent-eventHandleId?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## globalDisplayX

```TypeScript
globalDisplayX?: double
```

X coordinate of the point relative to the global display.

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MouseEvent-globalDisplayX?: double--><!--Device-MouseEvent-globalDisplayX?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## globalDisplayY

```TypeScript
globalDisplayY?: double
```

Y coordinate of the point relative to the global display.

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MouseEvent-globalDisplayY?: double--><!--Device-MouseEvent-globalDisplayY?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## pressedButtons

```TypeScript
pressedButtons?: MouseButton[]
```

Array of all mouse buttons that are currently pressed.

**Type:** [MouseButton](../../apis-arkui/arkts-apis/arkts-arkui-mousebutton-e.md)[]

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MouseEvent-pressedButtons?: MouseButton[]--><!--Device-MouseEvent-pressedButtons?: MouseButton[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## rawDeltaX

```TypeScript
rawDeltaX?: double
```

X axis offset relative to the previous reported mouse pointer position. When the mouse pointer is at the edge of the screen, the value may be less than the difference of the X coordinate reported twice.

**Type:** double

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MouseEvent-rawDeltaX?: double--><!--Device-MouseEvent-rawDeltaX?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## rawDeltaY

```TypeScript
rawDeltaY?: double
```

Y axis offset relative to the previous reported mouse pointer position. When the mouse pointer is at the edge of the screen, the value may be less than the difference of the Y coordinate reported twice.

**Type:** double

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MouseEvent-rawDeltaY?: double--><!--Device-MouseEvent-rawDeltaY?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## windowX

```TypeScript
windowX: double
```

X coordinate of the mouse pointer relative to the upper left corner of the application window.

**Type:** double

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MouseEvent-windowX: double--><!--Device-MouseEvent-windowX: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## windowY

```TypeScript
windowY: double
```

Y coordinate of the mouse pointer relative to the upper left corner of the application window.

**Type:** double

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MouseEvent-windowY: double--><!--Device-MouseEvent-windowY: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## x

```TypeScript
x: double
```

X coordinate of the mouse pointer relative to the upper left corner of the component being clicked.

**Type:** double

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MouseEvent-x: double--><!--Device-MouseEvent-x: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## y

```TypeScript
y: double
```

Y coordinate of the mouse pointer relative to the upper left corner of the component being clicked.

**Type:** double

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MouseEvent-y: double--><!--Device-MouseEvent-y: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

