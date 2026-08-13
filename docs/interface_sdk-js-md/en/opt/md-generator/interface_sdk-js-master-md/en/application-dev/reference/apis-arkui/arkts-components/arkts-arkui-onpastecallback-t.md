# OnPasteCallback

```TypeScript
declare type OnPasteCallback = (content: string, event: PasteEvent) => void
```

Defines the callback used to return the pasted text content.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-unnamed-declare type OnPasteCallback = (content: string, event: PasteEvent) => void--><!--Device-unnamed-declare type OnPasteCallback = (content: string, event: PasteEvent) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| content | string | Yes |
| event | [PasteEvent](arkts-arkui-pasteevent-i.md) | Yes |
