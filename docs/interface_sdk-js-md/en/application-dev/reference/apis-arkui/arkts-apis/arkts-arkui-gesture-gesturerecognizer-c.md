# GestureRecognizer

Defines the gesture recognizer.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class GestureRecognizer--><!--Device-unnamed-export declare class GestureRecognizer-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getEventTargetInfo

```TypeScript
getEventTargetInfo(): EventTargetInfo
```

Returns the event target information of the component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureRecognizer-getEventTargetInfo(): EventTargetInfo--><!--Device-GestureRecognizer-getEventTargetInfo(): EventTargetInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [EventTargetInfo](arkts-arkui-gesture-eventtargetinfo-c.md) | the event target information of the component. |

## getFingerCount

```TypeScript
getFingerCount(): int
```

Returns the tap gesture's finger count.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureRecognizer-getFingerCount(): int--><!--Device-GestureRecognizer-getFingerCount(): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| int | the finger count of the tap gesture. |

## getState

```TypeScript
getState(): GestureRecognizerState
```

Returns the gesture recognizer's state.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureRecognizer-getState(): GestureRecognizerState--><!--Device-GestureRecognizer-getState(): GestureRecognizerState-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [GestureRecognizerState](arkts-arkui-gesture-gesturerecognizerstate-e.md) | the gesture recognizer's state |

## getTag

```TypeScript
getTag(): string
```

Returns the gesture's tag.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureRecognizer-getTag(): string--><!--Device-GestureRecognizer-getTag(): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| string | the gesture's tag |

## getType

```TypeScript
getType(): GestureControl.GestureType
```

Returns the gesture's type.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureRecognizer-getType(): GestureControl.GestureType--><!--Device-GestureRecognizer-getType(): GestureControl.GestureType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [GestureControl.GestureType](arkts-arkui-gesturecontrol-gesturetype-e.md) | the gesture's type |

## isBuiltIn

```TypeScript
isBuiltIn(): boolean
```

Returns whether the gesture recognizer is built in recognizer.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureRecognizer-isBuiltIn(): boolean--><!--Device-GestureRecognizer-isBuiltIn(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true is built in recognizer, false is not built in recognizer |

## isEnabled

```TypeScript
isEnabled(): boolean
```

Returns whether the gesture recognizer is enabled.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureRecognizer-isEnabled(): boolean--><!--Device-GestureRecognizer-isEnabled(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true is enabled, false is not enabled |

## isFingerCountLimit

```TypeScript
isFingerCountLimit(): boolean
```

Returns the tap gesture's limitFingerCount.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureRecognizer-isFingerCountLimit(): boolean--><!--Device-GestureRecognizer-isFingerCountLimit(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | the limitFingerCount of the tap gesture. |

## isHostBelongsTo

```TypeScript
isHostBelongsTo(uniqueId: int): boolean
```

Check whether the current gesture binding node is a descendant of the passed-in component.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureRecognizer-isHostBelongsTo(uniqueId: int): boolean--><!--Device-GestureRecognizer-isHostBelongsTo(uniqueId: int): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uniqueId | int | Yes | the unique id of the component. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | the query result. |

## isValid

```TypeScript
isValid(): boolean
```

Returns whether the gesture recognizer is valid.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureRecognizer-isValid(): boolean--><!--Device-GestureRecognizer-isValid(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true is valid, false is invalid |

## preventBegin

```TypeScript
preventBegin(): void
```

Prevent the gesture recognizer from participating in this gesture recognition until all fingers are lifted. If the system has already made out the result of this gesture recognizer (success and failure), calling this function will have no any effect.

[Note]: This method is different from GestureRecognizer.setEnabled(isEnabled: boolean), setEnabled does not prevent a gesture recognizer object from participating in the gesture recognition process, but only affects whether the gesture's corresponding callback function is executed.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureRecognizer-preventBegin(): void--><!--Device-GestureRecognizer-preventBegin(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## setEnabled

```TypeScript
setEnabled(isEnabled: boolean): void
```

set the enabled state of the gesture recognizer.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureRecognizer-setEnabled(isEnabled: boolean): void--><!--Device-GestureRecognizer-setEnabled(isEnabled: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isEnabled | boolean | Yes | Indicates the enabled state. |

