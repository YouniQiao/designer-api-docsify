# OnListScrollIndexCallback

```TypeScript
declare type OnListScrollIndexCallback = (start: number, end: number, center: number) => void
```

Represents a callback for item changes in the visible area of the **List** component.

**Since:** 19

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

**Widget capability:** This API can be used in ArkTS widgets since API version 19.

<!--Device-unnamed-declare type OnListScrollIndexCallback = (start: number, end: number, center: number) => void--><!--Device-unnamed-declare type OnListScrollIndexCallback = (start: number, end: number, center: number) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| start | number | Yes |
| end | number | Yes |
| center | number | Yes |
