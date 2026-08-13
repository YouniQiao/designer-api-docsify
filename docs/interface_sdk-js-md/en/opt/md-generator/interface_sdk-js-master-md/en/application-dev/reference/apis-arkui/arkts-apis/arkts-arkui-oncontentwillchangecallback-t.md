# OnContentWillChangeCallback

```TypeScript
export type OnContentWillChangeCallback = (currentIndex: number, comingIndex: number) => boolean
```

Defines the callback function triggered when the page content changes.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-unnamed-export type OnContentWillChangeCallback = (currentIndex: number, comingIndex: number) => boolean--><!--Device-unnamed-export type OnContentWillChangeCallback = (currentIndex: number, comingIndex: number) => boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| currentIndex | number | Yes |
| comingIndex | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |
