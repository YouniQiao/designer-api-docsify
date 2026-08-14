# RecentPhotoComponent

RecentPhotoComponent({ recentPhotoOptions?: RecentPhotoOptions, onRecentPhotoCheckResult?: RecentPhotoCheckResultCallback, onRecentPhotoClick: RecentPhotoClickCallback, onRecentPhotoCheckInfo?: RecentPhotoCheckInfoCallback, }) Allows an application to access the latest image or video file in the public directory to access the recent image or video in the user directory without the media access permission.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

<!--Device-unnamed-export declare struct RecentPhotoComponent--><!--Device-unnamed-export declare struct RecentPhotoComponent-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
import { RecentPhotoComponent } from 'RecentPhotoComponent';
import { RecentPhotoCheckResultCallback } from 'RecentPhotoCheckResultCallback';
import { RecentPhotoInfo } from 'RecentPhotoInfo';
import { RecentPhotoCheckInfoCallback } from 'RecentPhotoCheckInfoCallback';
import { RecentPhotoClickCallback } from 'RecentPhotoClickCallback';
import { RecentPhotoOptions } from 'RecentPhotoOptions';
import { PhotoSource } from 'PhotoSource';
```

## onRecentPhotoCheckInfo

```TypeScript
onRecentPhotoCheckInfo?: RecentPhotoCheckInfoCallback
```

Callback when check whether photos or videos exists and return the recent photo info

**Type:** [RecentPhotoCheckInfoCallback](../../apis-na/arkts-apis/arkts-na-recentphotocheckinfocallback-t.md)

**Since:** 13

**ArkTS mode:** ArkTS-Dyn only, since version 13.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-RecentPhotoComponent-onRecentPhotoCheckInfo?: RecentPhotoCheckInfoCallback--><!--Device-RecentPhotoComponent-onRecentPhotoCheckInfo?: RecentPhotoCheckInfoCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onRecentPhotoCheckResult

```TypeScript
onRecentPhotoCheckResult?: RecentPhotoCheckResultCallback
```

Callback when check whether photos or videos exists

**Type:** [RecentPhotoCheckResultCallback](../../apis-na/arkts-apis/arkts-na-recentphotocheckresultcallback-t.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RecentPhotoComponent-onRecentPhotoCheckResult?: RecentPhotoCheckResultCallback--><!--Device-RecentPhotoComponent-onRecentPhotoCheckResult?: RecentPhotoCheckResultCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onRecentPhotoClick

```TypeScript
onRecentPhotoClick: RecentPhotoClickCallback
```

Callback when select photos or videos

**Type:** [RecentPhotoClickCallback](../../apis-na/arkts-apis/arkts-na-recentphotoclickcallback-t.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RecentPhotoComponent-onRecentPhotoClick: RecentPhotoClickCallback--><!--Device-RecentPhotoComponent-onRecentPhotoClick: RecentPhotoClickCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## recentPhotoOptions

```TypeScript
recentPhotoOptions?: RecentPhotoOptions
```

recentPhotoOptions

**Type:** [RecentPhotoOptions](../../apis-na/arkts-apis/arkts-na-file-recentphotocomponent-recentphotooptions-c.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RecentPhotoComponent-recentPhotoOptions?: RecentPhotoOptions--><!--Device-RecentPhotoComponent-recentPhotoOptions?: RecentPhotoOptions-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

