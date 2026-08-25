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
 The universal properties are supported.


## Modules to Import

```TypeScript
import { RecentPhotoComponent, RecentPhotoCheckResultCallback, RecentPhotoInfo, RecentPhotoCheckInfoCallback, RecentPhotoClickCallback, RecentPhotoOptions, PhotoSource } from '@kit.MediaLibraryKit';
```

## Summary

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [RecentPhotoInfo(RecentPhotoComponent)](arkts-medialibrary-file-recentphotocomponent-recentphotoinfo-c.md) |
| [RecentPhotoOptions(RecentPhotoComponent)](arkts-medialibrary-file-recentphotocomponent-recentphotooptions-c.md) |

### Structs

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [RecentPhotoComponent(RecentPhotoComponent)](arkts-medialibrary-file-recentphotocomponent-recentphotocomponent-s.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [PhotoSource(RecentPhotoComponent)](arkts-medialibrary-file-recentphotocomponent-photosource-e.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [RecentPhotoCheckInfoCallback(RecentPhotoComponent)](arkts-medialibrary-recentphotocheckinfocallback-t.md) |
| [RecentPhotoCheckResultCallback(RecentPhotoComponent)](arkts-medialibrary-recentphotocheckresultcallback-t.md) |
| [RecentPhotoClickCallback(RecentPhotoComponent)](arkts-medialibrary-recentphotoclickcallback-t.md) |
