# GestureRecognizer

Gesture recognizer object.

**Since:** 12

<!--Device-unnamed-declare class GestureRecognizer--><!--Device-unnamed-declare class GestureRecognizer-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## getEventTargetInfo

```TypeScript
getEventTargetInfo(): EventTargetInfo
```

Obtains the information about the component corresponding to this gesture recognizer.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-GestureRecognizer-getEventTargetInfo(): EventTargetInfo--><!--Device-GestureRecognizer-getEventTargetInfo(): EventTargetInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [EventTargetInfo](arkts-arkui-eventtargetinfo-c.md) |

## getFingerCount

```TypeScript
getFingerCount(): number
```

Obtains the number of fingers required to trigger the preset gesture.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-GestureRecognizer-getFingerCount(): number--><!--Device-GestureRecognizer-getFingerCount(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getState

```TypeScript
getState(): GestureRecognizerState
```

Obtains the state of this gesture recognizer.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-GestureRecognizer-getState(): GestureRecognizerState--><!--Device-GestureRecognizer-getState(): GestureRecognizerState-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [GestureRecognizerState](arkts-arkui-gesturerecognizerstate-e.md) |

## getTag

```TypeScript
getTag(): string
```

Obtains the tag of this gesture recognizer.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-GestureRecognizer-getTag(): string--><!--Device-GestureRecognizer-getTag(): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getType

```TypeScript
getType(): GestureControl.GestureType
```

Obtains the type of this gesture recognizer.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-GestureRecognizer-getType(): GestureControl.GestureType--><!--Device-GestureRecognizer-getType(): GestureControl.GestureType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [GestureControl.GestureType](arkts-arkui-gesturecontrol-gesturetype-e.md) |

## isBuiltIn

```TypeScript
isBuiltIn(): boolean
```

Obtains whether this gesture recognizer is a built-in gesture.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-GestureRecognizer-isBuiltIn(): boolean--><!--Device-GestureRecognizer-isBuiltIn(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isEnabled

```TypeScript
isEnabled(): boolean
```

Obtains the enabled state of this gesture recognizer.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-GestureRecognizer-isEnabled(): boolean--><!--Device-GestureRecognizer-isEnabled(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isFingerCountLimit

```TypeScript
isFingerCountLimit(): boolean
```

Checks whether the preset gesture detects the number of fingers on the screen.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-GestureRecognizer-isFingerCountLimit(): boolean--><!--Device-GestureRecognizer-isFingerCountLimit(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isHostBelongsTo

```TypeScript
isHostBelongsTo(uniqueId: number): boolean
```

Returns whether the node bound to the current gesture recognizer is a descendant of the specified component.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-GestureRecognizer-isHostBelongsTo(uniqueId: int): boolean--><!--Device-GestureRecognizer-isHostBelongsTo(uniqueId: int): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uniqueId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isValid

```TypeScript
isValid(): boolean
```

Whether the current gesture recognizer is valid.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureRecognizer-isValid(): boolean--><!--Device-GestureRecognizer-isValid(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## preventBegin

```TypeScript
preventBegin(): void
```

Prevents a gesture recognizer from participating in the current gesture recognition before all fingers are lifted. If the system has already determined the result of the gesture recognizer (regardless of success or failure), calling this API will be ineffective. Unlike GestureRecognizer.[setEnabled](#setenabled)(isEnabled: boolean), which only affects callback execution, this API prevents the recognizer from participating in the recognition process entirely.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-GestureRecognizer-preventBegin(): void--><!--Device-GestureRecognizer-preventBegin(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## setEnabled

```TypeScript
setEnabled(isEnabled: boolean): void
```

Sets the enabled state of this gesture recognizer.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-GestureRecognizer-setEnabled(isEnabled: boolean): void--><!--Device-GestureRecognizer-setEnabled(isEnabled: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [isEnabled](#isenabled) | boolean | Yes |
