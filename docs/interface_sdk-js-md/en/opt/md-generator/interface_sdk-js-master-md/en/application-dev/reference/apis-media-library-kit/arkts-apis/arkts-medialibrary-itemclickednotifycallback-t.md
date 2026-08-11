# ItemClickedNotifyCallback

```TypeScript
export type ItemClickedNotifyCallback = (itemInfo: ItemInfo, clickType: ClickType) => void
```

Callback to be invoked when an item in a **PhotoPickerComponent** is clicked.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-export type ItemClickedNotifyCallback = (itemInfo: ItemInfo, clickType: ClickType) => void--><!--Device-unnamed-export type ItemClickedNotifyCallback = (itemInfo: ItemInfo, clickType: ClickType) => void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| itemInfo | [ItemInfo](arkts-medialibrary-file-photopickercomponent-iteminfo-c.md) | Yes |
| clickType | [ClickType](arkts-medialibrary-file-photopickercomponent-clicktype-e.md) | Yes |
