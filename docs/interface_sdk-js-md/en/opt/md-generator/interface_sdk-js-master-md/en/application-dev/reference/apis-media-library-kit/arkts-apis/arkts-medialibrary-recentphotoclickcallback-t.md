# RecentPhotoClickCallback

```TypeScript
export type RecentPhotoClickCallback = (recentPhotoInfo: BaseItemInfo) => boolean
```

Called when the recent image or video is selected. No special processing is performed on the return value.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-unnamed-export type RecentPhotoClickCallback = (recentPhotoInfo: BaseItemInfo) => boolean--><!--Device-unnamed-export type RecentPhotoClickCallback = (recentPhotoInfo: BaseItemInfo) => boolean-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| recentPhotoInfo | [BaseItemInfo](arkts-medialibrary-file-photopickercomponent-baseiteminfo-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |
