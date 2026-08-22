# RawInputEventWrapper

Defines the raw input event wrapper.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

<!--Device-unnamed-export declare abstract class RawInputEventWrapper--><!--Device-unnamed-export declare abstract class RawInputEventWrapper-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## asKeyEvent

```TypeScript
asKeyEvent(): KeyEvent | null
```

Attempts to get the keyboard event.

Returns the event object if it is a keyboard event, otherwise returns null.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RawInputEventWrapper-asKeyEvent(): KeyEvent | null--><!--Device-RawInputEventWrapper-asKeyEvent(): KeyEvent | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [KeyEvent](arkts-common-keyevent-i.md) \| null | The keyboard event object or null. |

## asMouseEvent

```TypeScript
asMouseEvent(): MouseEvent | null
```

Attempts to get the mouse event.

Returns the event object if it is a mouse event, otherwise returns null.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RawInputEventWrapper-asMouseEvent(): MouseEvent | null--><!--Device-RawInputEventWrapper-asMouseEvent(): MouseEvent | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [MouseEvent](arkts-common-mouseevent-i.md) \| null | The mouse event object or null. |

## asTouchEvent

```TypeScript
asTouchEvent(): TouchEvent | null
```

Attempts to get the touch event.

Returns the event object if it is a touch event, otherwise returns null.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RawInputEventWrapper-asTouchEvent(): TouchEvent | null--><!--Device-RawInputEventWrapper-asTouchEvent(): TouchEvent | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [TouchEvent](arkts-common-touchevent-i.md) \| null | The touch event object or null. |

## isKeyEvent

```TypeScript
isKeyEvent(): boolean
```

Checks whether the event is a keyboard event.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RawInputEventWrapper-isKeyEvent(): boolean--><!--Device-RawInputEventWrapper-isKeyEvent(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the event is a keyboard event, otherwise returns false. |

## isMouseEvent

```TypeScript
isMouseEvent(): boolean
```

Checks whether the event is a mouse event.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RawInputEventWrapper-isMouseEvent(): boolean--><!--Device-RawInputEventWrapper-isMouseEvent(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the event is a mouse event, otherwise returns false. |

## isTouchEvent

```TypeScript
isTouchEvent(): boolean
```

Checks whether the event is a touch event.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RawInputEventWrapper-isTouchEvent(): boolean--><!--Device-RawInputEventWrapper-isTouchEvent(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the event is a touch event, otherwise returns false. |

