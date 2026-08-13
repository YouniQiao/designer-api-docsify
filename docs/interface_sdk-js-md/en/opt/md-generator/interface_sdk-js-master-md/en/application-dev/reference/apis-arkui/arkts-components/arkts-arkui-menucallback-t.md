# MenuCallback

```TypeScript
declare type MenuCallback = (start: number, end: number) => void
```

Represents the callback invoked when the custom context menu on selection is shown or hidden.

**Since:** 15

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-unnamed-declare type MenuCallback = (start: number, end: number) => void--><!--Device-unnamed-declare type MenuCallback = (start: number, end: number) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| start | number | Yes |
| end | number | Yes |
