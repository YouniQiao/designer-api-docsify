# OnTextSelectionChangeCallback

```TypeScript
declare type OnTextSelectionChangeCallback = (selectionStart: number, selectionEnd: number) => void
```

Called when the position of the text selection changes or when the cursor position changes during the editing state.

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-unnamed-declare type OnTextSelectionChangeCallback = (selectionStart: number, selectionEnd: number) => void--><!--Device-unnamed-declare type OnTextSelectionChangeCallback = (selectionStart: number, selectionEnd: number) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| selectionStart | number | Yes |
| selectionEnd | number | Yes |
