# OnPasteCallback

```TypeScript
declare type OnPasteCallback = (pasteValue: string, event: PasteEvent) => void
```

Called when a paste operation is performed.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-unnamed-declare type OnPasteCallback = (pasteValue: string, event: PasteEvent) => void--><!--Device-unnamed-declare type OnPasteCallback = (pasteValue: string, event: PasteEvent) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pasteValue | string | Yes |
| event | [PasteEvent](../arkts-components/arkts-arkui-pasteevent-i.md) | Yes |
