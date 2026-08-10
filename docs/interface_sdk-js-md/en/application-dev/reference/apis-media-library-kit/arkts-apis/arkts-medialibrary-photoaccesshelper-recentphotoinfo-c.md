# RecentPhotoInfo

Recent photo info

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 26.0.0.

<!--Device-photoAccessHelper-export class RecentPhotoInfo--><!--Device-photoAccessHelper-export class RecentPhotoInfo-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## dateTaken

```TypeScript
dateTaken?: long
```

Time when the recent image or video was shot (in milliseconds since January 1, 1970). The unit is ms.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-RecentPhotoInfo-dateTaken?: long--><!--Device-RecentPhotoInfo-dateTaken?: long-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## identifier

```TypeScript
identifier?: string
```

Hash value of the name of the recent image or video, which is used to help the application determine whether the image or video to be displayed is the same as the one displayed before.

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-RecentPhotoInfo-identifier?: string--><!--Device-RecentPhotoInfo-identifier?: string-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

