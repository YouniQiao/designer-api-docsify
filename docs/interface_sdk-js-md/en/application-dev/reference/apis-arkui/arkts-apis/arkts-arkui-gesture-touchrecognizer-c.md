# TouchRecognizer

Defines the touch recognizer.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export declare class TouchRecognizer--><!--Device-unnamed-export declare class TouchRecognizer-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## cancelTouch

```TypeScript
cancelTouch(): void
```

Dispatch touch cancel to the touch recognizer.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TouchRecognizer-cancelTouch(): void--><!--Device-TouchRecognizer-cancelTouch(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getEventTargetInfo

```TypeScript
getEventTargetInfo(): EventTargetInfo
```

Returns the event target information of the component.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TouchRecognizer-getEventTargetInfo(): EventTargetInfo--><!--Device-TouchRecognizer-getEventTargetInfo(): EventTargetInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [EventTargetInfo](arkts-arkui-gesture-eventtargetinfo-c.md) | the event target information of the component. |

## isHostBelongsTo

```TypeScript
isHostBelongsTo(uniqueId: int): boolean
```

Check whether the current gesture binding node is a descendant of the passed-in component.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TouchRecognizer-isHostBelongsTo(uniqueId: int): boolean--><!--Device-TouchRecognizer-isHostBelongsTo(uniqueId: int): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uniqueId | int | Yes | the unique id of the component. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | the query result. |

