# TouchEvent

Touch Action Function Parameters

**Inheritance/Implementation:** TouchEvent extends [BaseEvent](../arkts-components/arkts-arkui-baseevent-i.md/arkts-arkui-baseevent-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface TouchEvent extends BaseEvent--><!--Device-unnamed-export declare interface TouchEvent extends BaseEvent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getHistoricalPoints

```TypeScript
getHistoricalPoints(): Array<HistoricalPoint> | undefined
```

Obtains all historical points of the current frame.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TouchEvent-getHistoricalPoints(): Array<HistoricalPoint> | undefined--><!--Device-TouchEvent-getHistoricalPoints(): Array<HistoricalPoint> | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;HistoricalPoint&gt; | return all historical points. Undefined will be returned if the internal runtime environment is broken. |

## preventDefault

```TypeScript
preventDefault(): void
```

Blocks the default event.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TouchEvent-preventDefault(): void--><!--Device-TouchEvent-preventDefault(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100017](../errorcode-event.md#100017-component-does-not-support-default-event-prevention) | Component does not support prevent function. |

## stopPropagation

```TypeScript
stopPropagation(): void
```

Stops the event from bubbling upwards or downwards.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TouchEvent-stopPropagation(): void--><!--Device-TouchEvent-stopPropagation(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## changedTouches

```TypeScript
changedTouches: TouchObject[]
```

Finger information changed.

**Type:** [TouchObject](arkts-arkui-common-touchobject-i.md)[]

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TouchEvent-changedTouches: TouchObject[]--><!--Device-TouchEvent-changedTouches: TouchObject[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## eventHandleId

```TypeScript
eventHandleId?: int
```

The unique handle for the event processing session. This handle must be used for any further operations on the event. The system ensures that for a given finger, only one event with this handle can be active at a time.

**Type:** int

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TouchEvent-eventHandleId?: int--><!--Device-TouchEvent-eventHandleId?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## touches

```TypeScript
touches: TouchObject[]
```

All finger information.

**Type:** [TouchObject](arkts-arkui-common-touchobject-i.md)[]

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TouchEvent-touches: TouchObject[]--><!--Device-TouchEvent-touches: TouchObject[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type: TouchType
```

Type of the touch event.

**Type:** [TouchType](arkts-arkui-touchtype-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TouchEvent-type: TouchType--><!--Device-TouchEvent-type: TouchType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

