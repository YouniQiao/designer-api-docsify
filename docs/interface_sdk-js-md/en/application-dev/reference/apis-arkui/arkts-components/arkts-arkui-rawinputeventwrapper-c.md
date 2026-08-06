# RawInputEventWrapper

Raw input event wrapper class.

Provides a unified interface to access different types of input events, ensuring type safety and backward compatibility.

This class encapsulates either a raw **MouseEvent**, **TouchEvent**, or **KeyEvent** object and provides type-safe methods for access.

This class is an abstract class. Developers cannot create instances on their own. The system automatically creates an instance and passes it to the callback when the input event listener is triggered.
    **NOTE**  
    
    Since the listener is executed before events are dispatched to specific components, some fields in the event will  
    not provide valid values: the trigger object [target]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_, coordinates relative to the component  
    [x]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ and [y]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_, [getCurrentLocalPosition]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_  
    and [stopPropagation]\_\_\_JSDOC\_LINK\_DESC\_USD\_4\_\_\_ methods, [preventDefault]\_\_\_JSDOC\_LINK\_DESC\_USD\_5\_\_\_ and  
    [getHistoricalPoints]\_\_\_JSDOC\_LINK\_DESC\_USD\_6\_\_\_ methods of **TouchEvent**, as well as the [metaKey]\_\_\_JSDOC\_LINK\_DESC\_USD\_7\_\_\_  
    attribute and [getModifierKeyState]\_\_\_JSDOC\_LINK\_DESC\_USD\_8\_\_\_ method of **KeyEvent**.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

<!--Device-unnamed-declare abstract class RawInputEventWrapper--><!--Device-unnamed-declare abstract class RawInputEventWrapper-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## asKeyEvent

```TypeScript
asKeyEvent(): KeyEvent | null
```

Obtains the key event.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-RawInputEventWrapper-asKeyEvent(): KeyEvent | null--><!--Device-RawInputEventWrapper-asKeyEvent(): KeyEvent | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Key event object if it is a key event, or **null** otherwise. |

## asMouseEvent

```TypeScript
asMouseEvent(): MouseEvent | null
```

Obtains the mouse event.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-RawInputEventWrapper-asMouseEvent(): MouseEvent | null--><!--Device-RawInputEventWrapper-asMouseEvent(): MouseEvent | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Mouse event object if it is a mouse event, or **null** otherwise. |

## asTouchEvent

```TypeScript
asTouchEvent(): TouchEvent | null
```

Obtains the touch event.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-RawInputEventWrapper-asTouchEvent(): TouchEvent | null--><!--Device-RawInputEventWrapper-asTouchEvent(): TouchEvent | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Touch event object if it is a touch event, or **null** otherwise. |

## isKeyEvent

```TypeScript
isKeyEvent(): boolean
```

Checks whether the event is a key event.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-RawInputEventWrapper-isKeyEvent(): boolean--><!--Device-RawInputEventWrapper-isKeyEvent(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether it is a key event. Returns **true** if it is a key event, and **false** otherwise. |

## isMouseEvent

```TypeScript
isMouseEvent(): boolean
```

Checks whether the event is a mouse event.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-RawInputEventWrapper-isMouseEvent(): boolean--><!--Device-RawInputEventWrapper-isMouseEvent(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether it is a mouse event. Returns **true** if it is a mouse event, and **false** otherwise. |

## isTouchEvent

```TypeScript
isTouchEvent(): boolean
```

Checks whether the event is a touch event.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-RawInputEventWrapper-isTouchEvent(): boolean--><!--Device-RawInputEventWrapper-isTouchEvent(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether it is a touch event. Returns **true** if it is a touch event, and **false** otherwise. |

