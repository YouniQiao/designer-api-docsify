# RecentPhotoCheckInfoCallback

```TypeScript
export type RecentPhotoCheckInfoCallback = (recentPhotoExists: boolean, info: RecentPhotoInfo) => void
```

The callback of onRecentPhotoCheckInfo event

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type RecentPhotoCheckInfoCallback = (recentPhotoExists: boolean, info: RecentPhotoInfo) => void--><!--Device-unnamed-export type RecentPhotoCheckInfoCallback = (recentPhotoExists: boolean, info: RecentPhotoInfo) => void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| recentPhotoExists | boolean | Yes | Does the recent photo exist? |
| info | [RecentPhotoInfo](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-file-recentphotocomponent-recentphotoinfo-c.md) | Yes | the recent photo info |

