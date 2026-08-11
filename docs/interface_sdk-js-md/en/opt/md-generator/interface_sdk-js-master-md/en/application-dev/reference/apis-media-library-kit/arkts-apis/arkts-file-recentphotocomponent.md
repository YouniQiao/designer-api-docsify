# @ohos.file.RecentPhotoComponent(RecentPhotoComponent)

The RecentPhotoComponent embedded in the UI of an application allows the application to access the recent image or
 video in the user directory without the required permission. This component grants the application only the read
 permission.
 Note that **RecentPhotoComponent** does not support nesting. Additionally, prevent overlaying components with the
 **overlay** attribute or of higher levels on top it, as this will prevent it from receiving gesture events.
 > **NOTE**
 >
 > - This component does not support [same-layer rendering](../../../web/web-same-layer.md).
 ###### Properties
 The [universal properties](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md/arkts-app-ability-common.md) are supported.


## Modules to Import

```TypeScript
import { RecentPhotoComponent, RecentPhotoCheckResultCallback, RecentPhotoCheckInfoCallback, PhotoSource, RecentPhotoClickCallback, RecentPhotoOptions, RecentPhotoInfo } from 'kits/@kit.MediaLibraryKit';
```

## Summary

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [RecentPhotoInfo](arkts-medialibrary-file-recentphotocomponent-recentphotoinfo-c.md) |
| [RecentPhotoOptions](arkts-medialibrary-file-recentphotocomponent-recentphotooptions-c.md) |

### Structs

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [RecentPhotoComponent](arkts-medialibrary-file-recentphotocomponent-recentphotocomponent-s.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [PhotoSource](arkts-medialibrary-file-recentphotocomponent-photosource-e.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [RecentPhotoCheckInfoCallback](arkts-medialibrary-recentphotocheckinfocallback-t.md) |
| [RecentPhotoCheckResultCallback](arkts-medialibrary-recentphotocheckresultcallback-t.md) |
| [RecentPhotoClickCallback](arkts-medialibrary-recentphotoclickcallback-t.md) |
