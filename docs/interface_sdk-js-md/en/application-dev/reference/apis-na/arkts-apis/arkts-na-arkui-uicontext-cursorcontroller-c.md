# CursorController

class CursorController

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare class CursorController--><!--Device-unnamed-export declare class CursorController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## restoreDefault

```TypeScript
restoreDefault(): void
```

Restore default cursor.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-CursorController-restoreDefault(): void--><!--Device-CursorController-restoreDefault(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## setCursor

```TypeScript
setCursor(value: PointerStyle): void
```

Set cursor style.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-CursorController-setCursor(value: PointerStyle): void--><!--Device-CursorController-setCursor(value: PointerStyle): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [PointerStyle](../../apis-arkui/arkts-apis/arkts-arkui-pointerstyle-t.md) | Yes | cursor style enum. |

## setCustomCursor

```TypeScript
setCustomCursor(value: image.PixelMap, focusX?: int, focusY?: int): void
```

Sets the custom cursor style.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-CursorController-setCustomCursor(value: image.PixelMap, focusX?: int, focusY?: int): void--><!--Device-CursorController-setCustomCursor(value: image.PixelMap, focusX?: int, focusY?: int): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | image.PixelMap | Yes | custom cursor style. |
| focusX | int | No | Focus x of the custom cursor. The value is greater than or equal to 0. The default value is 0. |
| focusY | int | No | Focus y of the custom cursor. The value is greater than or equal to 0. The default value is 0. |

