# OnTextSelectionChangeCallback

```TypeScript
export type OnTextSelectionChangeCallback = (selectionStart: int, selectionEnd: int) => void
```

文本选择变化回调或光标位置变化回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnTextSelectionChangeCallback = (selectionStart: int, selectionEnd: int) => void--><!--Device-unnamed-export type OnTextSelectionChangeCallback = (selectionStart: int, selectionEnd: int) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| selectionStart | int | Yes | 所选文本的起始位置，文字的起始位置为0。 |
| selectionEnd | int | Yes | 所选文本的结束位置。 |

