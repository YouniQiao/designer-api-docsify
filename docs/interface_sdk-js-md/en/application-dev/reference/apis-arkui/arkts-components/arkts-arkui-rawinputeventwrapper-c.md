# RawInputEventWrapper

Raw input event wrapper class.Provides a unified interface to access different types of input events, ensuring type safety and backward compatibility.This class encapsulates either a raw **MouseEvent**, **TouchEvent**, or **KeyEvent** object and provides type-safe methods for access.This class is an abstract class. Developers cannot create instances on their own. The system automatically creates an instance and passes it to the callback when the input event listener is triggered.

> **NOTE：**&gt;
> Since the listener is executed before events are dispatched to specific components, some fields in the event will
> not provide valid values: the trigger object [target](arkts-arkui-eventtarget-i.md), coordinates relative to the component
> [x](arkts-arkui-mouseevent-i.md#x) and [y](arkts-arkui-mouseevent-i.md#y), [getCurrentLocalPosition](arkts-arkui-touchobject-i.md#getcurrentlocalposition)
> and [stopPropagation](arkts-arkui-touchevent-i.md#stoppropagation) methods, [preventDefault](arkts-arkui-touchevent-i.md#preventdefault) and
> [getHistoricalPoints](arkts-arkui-touchevent-i.md#gethistoricalpoints) methods of **TouchEvent**, as well as the [metaKey](arkts-arkui-keyevent-i.md#metakey)
> attribute and [getModifierKeyState](arkts-arkui-keyevent-i.md#getmodifierkeystate) method of **KeyEvent**.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## asKeyEvent

```TypeScript
asKeyEvent(): KeyEvent | null
```

Obtains the key event.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [KeyEvent](arkts-arkui-keyevent-i.md) \| null |

## asMouseEvent

```TypeScript
asMouseEvent(): MouseEvent | null
```

Obtains the mouse event.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MouseEvent](arkts-arkui-mouseevent-i.md) \| null |

## asTouchEvent

```TypeScript
asTouchEvent(): TouchEvent | null
```

Obtains the touch event.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TouchEvent](arkts-arkui-touchevent-i.md) \| null |

## isKeyEvent

```TypeScript
isKeyEvent(): boolean
```

Checks whether the event is a key event.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isMouseEvent

```TypeScript
isMouseEvent(): boolean
```

Checks whether the event is a mouse event.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isTouchEvent

```TypeScript
isTouchEvent(): boolean
```

Checks whether the event is a touch event.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |
