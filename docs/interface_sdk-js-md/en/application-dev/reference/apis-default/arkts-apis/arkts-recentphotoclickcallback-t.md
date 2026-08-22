# RecentPhotoClickCallback

```TypeScript
export type RecentPhotoClickCallback = (recentPhotoInfo: BaseItemInfo) => boolean
```

The callback of onRecentPhotoClick event

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type RecentPhotoClickCallback = (recentPhotoInfo: BaseItemInfo) => boolean--><!--Device-unnamed-export type RecentPhotoClickCallback = (recentPhotoInfo: BaseItemInfo) => boolean-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| recentPhotoInfo | [BaseItemInfo](arkts-file-photopickercomponent-baseiteminfo-c.md) | Yes | The item information of recent photo |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | - |

