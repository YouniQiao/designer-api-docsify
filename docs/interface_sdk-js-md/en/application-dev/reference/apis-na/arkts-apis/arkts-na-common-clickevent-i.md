# ClickEvent

The tap action triggers this method invocation.

**Inheritance/Implementation:** ClickEvent extends [BaseEvent](arkts-na-common-baseevent-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface ClickEvent--><!--Device-unnamed-export declare interface ClickEvent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getCurrentLocalPosition

```TypeScript
getCurrentLocalPosition(): Coordinate2D
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-ClickEvent-getCurrentLocalPosition(): Coordinate2D--><!--Device-ClickEvent-getCurrentLocalPosition(): Coordinate2D-End-->

**Return value:**

| Type | Description |
| --- | --- |
## preventDefault

```TypeScript
preventDefault(): void
```

Prevent the default function.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ClickEvent-preventDefault(): void--><!--Device-ClickEvent-preventDefault(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100017](../../apis-arkui/errorcode-event.md#100017-component-does-not-support-default-event-prevention) | Component does not support prevent function. |

## default

```TypeScript
default
```

Gets the coordinates of the top-left corner of the current component based on its real-time position.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ClickEvent-default--><!--Device-ClickEvent-default-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## displayX

```TypeScript
displayX: double
```

X coordinate of the click relative to the upper left corner of the application screen.

**Type:** double

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ClickEvent-displayX: double--><!--Device-ClickEvent-displayX: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## displayY

```TypeScript
displayY: double
```

Y coordinate of the click relative to the upper left corner of the application screen.

**Type:** double

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ClickEvent-displayY: double--><!--Device-ClickEvent-displayY: double-End-->

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

<!--Device-ClickEvent-globalDisplayX?: double--><!--Device-ClickEvent-globalDisplayX?: double-End-->

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

<!--Device-ClickEvent-globalDisplayY?: double--><!--Device-ClickEvent-globalDisplayY?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## hand

```TypeScript
hand?: InteractionHand
```

Whether the event is triggered by a left-hand or right-hand tap.

**Type:** [InteractionHand](../../apis-arkui/arkts-apis/arkts-arkui-interactionhand-e.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ClickEvent-hand?: InteractionHand--><!--Device-ClickEvent-hand?: InteractionHand-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## windowX

```TypeScript
windowX: double
```

X coordinate of the click relative to the upper left corner of the application window.

**Type:** double

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ClickEvent-windowX: double--><!--Device-ClickEvent-windowX: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## windowY

```TypeScript
windowY: double
```

Y coordinate of the click relative to the upper left corner of the application window.

**Type:** double

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ClickEvent-windowY: double--><!--Device-ClickEvent-windowY: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## x

```TypeScript
x: double
```

X coordinate of the click point relative to the left edge of the clicked element.

**Type:** double

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ClickEvent-x: double--><!--Device-ClickEvent-x: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## y

```TypeScript
y: double
```

Y coordinate of the click point relative to the left edge of the clicked element.

**Type:** double

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ClickEvent-y: double--><!--Device-ClickEvent-y: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

