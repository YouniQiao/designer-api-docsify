# LongPressRecognizer

Implements a number press gesture recognizer. Inherits from [GestureRecognizer](arkts-arkui-gesturerecognizer-c.md).

**Inheritance/Implementation:** LongPressRecognizer extends [GestureRecognizer](arkts-arkui-gesturerecognizer-c.md)

**Since:** 18

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## getAllowableMovement

```TypeScript
getAllowableMovement(): number
```

Obtains the maximum movement distance allowed for gesture recognition by the number press gesture recognizer.

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| number | Maximum movement distance recognized by the number press gesture recognizer, in px. |

## getDuration

```TypeScript
getDuration(): number
```

Obtains the minimum duration required for the number press gesture to be recognized.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| number | Minimum duration, in ms. |

## isRepeat

```TypeScript
isRepeat(): boolean
```

Checks whether the number press gesture recognizer is set to trigger repeated callbacks.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether the number press gesture recognizer is set to trigger repeated callbacks. **false**: Repeated callbacks are not triggered. **true**: Repeated callbacks are triggered. |
