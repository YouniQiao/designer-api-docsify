# RecentPhotoCheckResultCallback

```TypeScript
export type RecentPhotoCheckResultCallback = (recentPhotoExists: boolean) => void
```

Called to return the query result of the recent image or video.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-unnamed-export type RecentPhotoCheckResultCallback = (recentPhotoExists: boolean) => void--><!--Device-unnamed-export type RecentPhotoCheckResultCallback = (recentPhotoExists: boolean) => void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| recentPhotoExists | boolean | Yes | Whether the recent image or video exists. **true** if it exists, **false** otherwise. The default value is **true**. |

