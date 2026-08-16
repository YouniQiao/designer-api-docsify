# ItemClickedNotifyCallback

```TypeScript
export type ItemClickedNotifyCallback = (itemInfo: ItemInfo, clickType: ClickType) => void
```

The callback of onItemClickedNotify event

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type ItemClickedNotifyCallback = (itemInfo: ItemInfo, clickType: ClickType) => void--><!--Device-unnamed-export type ItemClickedNotifyCallback = (itemInfo: ItemInfo, clickType: ClickType) => void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| itemInfo | [ItemInfo](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-file-photopickercomponent-iteminfo-c.md) | Yes |  |
| clickType | [ClickType](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-file-photopickercomponent-clicktype-e.md) | Yes |  |

