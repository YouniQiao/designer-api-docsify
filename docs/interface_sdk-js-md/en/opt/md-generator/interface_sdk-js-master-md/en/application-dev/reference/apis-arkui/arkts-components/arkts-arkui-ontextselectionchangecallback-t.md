# OnTextSelectionChangeCallback

```TypeScript
declare type OnTextSelectionChangeCallback = (selectionStart: number, selectionEnd: number) => void
```

Defines the callback for text selection changes or caret position changes.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-unnamed-declare type OnTextSelectionChangeCallback = (selectionStart: number, selectionEnd: number) => void--><!--Device-unnamed-declare type OnTextSelectionChangeCallback = (selectionStart: number, selectionEnd: number) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| selectionStart | number | Yes |
| selectionEnd | number | Yes |
