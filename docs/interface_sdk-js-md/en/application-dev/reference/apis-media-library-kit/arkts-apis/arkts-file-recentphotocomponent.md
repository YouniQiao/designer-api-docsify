# @ohos.file.RecentPhotoComponent

## Modules to Import

```TypeScript
import { RecentPhotoComponent, RecentPhotoCheckResultCallback, RecentPhotoInfo, RecentPhotoCheckInfoCallback, RecentPhotoClickCallback, RecentPhotoOptions, PhotoSource } from '@kit.MediaLibraryKit';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [RecentPhotoInfo](arkts-medialibrary-file-recentphotocomponent-recentphotoinfo-c.md) | Represents information about the recent image or video. |
| [RecentPhotoOptions](arkts-medialibrary-file-recentphotocomponent-recentphotooptions-c.md) | Represents the configuration of the recent image or video. |

### Structs

| Name | Description |
| --- | --- |
| [RecentPhotoComponent](arkts-medialibrary-file-recentphotocomponent-recentphotocomponent-s.md) | RecentPhotoComponent({ recentPhotoOptions?: RecentPhotoOptions, onRecentPhotoCheckResult?: RecentPhotoCheckResultCallback, onRecentPhotoClick: RecentPhotoClickCallback, onRecentPhotoCheckInfo?: RecentPhotoCheckInfoCallback, })Allows an application to access the latest image or video file in the public directory to access the recent image or video in the user directory without the media access permission. |

### Enums

| Name | Description |
| --- | --- |
| [PhotoSource](arkts-medialibrary-file-recentphotocomponent-photosource-e.md) | Enumerates the sources of the image or video data. |

### Types

| Name | Description |
| --- | --- |
| [RecentPhotoCheckInfoCallback](arkts-medialibrary-recentphotocheckinfocallback-t.md) | Called to return whether the recent image or video exists and the information about it. |
| [RecentPhotoCheckResultCallback](arkts-medialibrary-recentphotocheckresultcallback-t.md) | Called to return the query result of the recent image or video. |
| [RecentPhotoClickCallback](arkts-medialibrary-recentphotoclickcallback-t.md) | Called when the recent image or video is selected. No special processing is performed on the return value. |

