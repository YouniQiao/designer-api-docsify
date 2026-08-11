# TouchRecognizer

Represents a touch gesture recognizer.

**Since:** 20

<!--Device-unnamed-declare class TouchRecognizer--><!--Device-unnamed-declare class TouchRecognizer-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## cancelTouch

```TypeScript
cancelTouch(): void
```

Sends a touch cancellation event to this touch gesture recognizer.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TouchRecognizer-cancelTouch(): void--><!--Device-TouchRecognizer-cancelTouch(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getEventTargetInfo

```TypeScript
getEventTargetInfo(): EventTargetInfo
```

Obtains the information about the component corresponding to this touch gesture recognizer.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TouchRecognizer-getEventTargetInfo(): EventTargetInfo--><!--Device-TouchRecognizer-getEventTargetInfo(): EventTargetInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [EventTargetInfo](arkts-arkui-eventtargetinfo-c.md) |

## isHostBelongsTo

```TypeScript
isHostBelongsTo(uniqueId: number): boolean
```

Returns whether the node bound to the current touch gesture recognizer is a descendant of the specified component.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-TouchRecognizer-isHostBelongsTo(uniqueId: int): boolean--><!--Device-TouchRecognizer-isHostBelongsTo(uniqueId: int): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uniqueId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |
