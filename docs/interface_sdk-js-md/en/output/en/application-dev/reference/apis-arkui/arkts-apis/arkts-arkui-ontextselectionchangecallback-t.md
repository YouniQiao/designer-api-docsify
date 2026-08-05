# OnTextSelectionChangeCallback

```TypeScript
export type OnTextSelectionChangeCallback = (selectionStart: int, selectionEnd: int) => void
```

Defines a TextInput callback when onTextSelectionChange. Anonymous Object Rectification.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnTextSelectionChangeCallback = (selectionStart: int, selectionEnd: int) => void--><!--Device-unnamed-export type OnTextSelectionChangeCallback = (selectionStart: int, selectionEnd: int) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| selectionStart | int | Yes | The starting position of the selected text, the starting position of the text is 0. \_\_\_HTML\_TAG\_USD\_0\_\_\_The value should be an integer.  |
| selectionEnd | int | Yes | The end location of the selected text. \_\_\_HTML\_TAG\_USD\_0\_\_\_The value should be an integer.  |

