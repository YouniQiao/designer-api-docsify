# LongPressRecognizer

Defines the long press gesture recognizer.

@extends GestureRecognizer

**Inheritance/Implementation:** LongPressRecognizer extends [GestureRecognizer](arkts-arkui-gesture-gesturerecognizer-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare class LongPressRecognizer--><!--Device-unnamed-export declare class LongPressRecognizer-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getAllowableMovement

```TypeScript
getAllowableMovement(): double
```

Returns the long press gesture's maximum moving distance. The unit is px.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LongPressRecognizer-getAllowableMovement(): double--><!--Device-LongPressRecognizer-getAllowableMovement(): double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| double | the maximum moving distance of the long press gesture. |

## getDuration

```TypeScript
getDuration(): int
```

Returns the long press gesture's duration. The unit is ms.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LongPressRecognizer-getDuration(): int--><!--Device-LongPressRecognizer-getDuration(): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| int | the duration of the long press gesture. |

## isRepeat

```TypeScript
isRepeat(): boolean
```

Returns the long press gesture's repeat state.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LongPressRecognizer-isRepeat(): boolean--><!--Device-LongPressRecognizer-isRepeat(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | the repeat state of the long press gesture. |

