# OnTabsContentWillChangeCallback

```TypeScript
declare type OnTabsContentWillChangeCallback = (currentIndex: number, comingIndex: number) => boolean
```

Defines the callback invoked when a new page is about to be displayed.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-unnamed-declare type OnTabsContentWillChangeCallback = (currentIndex: number, comingIndex: number) => boolean--><!--Device-unnamed-declare type OnTabsContentWillChangeCallback = (currentIndex: number, comingIndex: number) => boolean-End-->

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
