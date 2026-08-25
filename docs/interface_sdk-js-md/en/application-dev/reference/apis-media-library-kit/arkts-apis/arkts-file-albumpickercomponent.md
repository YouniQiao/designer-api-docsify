# @ohos.file.AlbumPickerComponent(AlbumPickerComponent)

The **AlbumPickerComponent** embedded in the UI of an application allows the application to access the albums in the
 user directory without any permission.
 Note that **AlbumPickerComponent** does not support nesting. Additionally, prevent overlaying components with the
 **overlay** attribute or of higher levels on top it, as this will prevent it from receiving gesture events.
 This component must be used together with [PhotoPickerComponent](arkts-medialibrary-file-photopickercomponent-photopickercomponent-s.md). When a user
 selects an album by using the **AlbumPickerComponent**, the **PhotoPickerComponent** is instructed to update the
 images and videos in the album.
 > **NOTE**
 >
 > - This component does not support [same-layer rendering](../../../web/web-same-layer.md).
 ###### Attributes
 The universal attributes are supported.


## Modules to Import

```TypeScript
import { AlbumPickerComponent, AlbumPickerOptions, AlbumInfo, EmptyAreaClickCallback, AlbumPickerController } from 'kits/@kit.MediaLibraryKit';
```

## Summary

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AlbumInfo(AlbumPickerComponent)](arkts-medialibrary-file-albumpickercomponent-albuminfo-c.md) |
| [AlbumPickerController(AlbumPickerComponent)](arkts-medialibrary-file-albumpickercomponent-albumpickercontroller-c.md) |
| [AlbumPickerOptions(AlbumPickerComponent)](arkts-medialibrary-file-albumpickercomponent-albumpickeroptions-c.md) |

### Structs

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AlbumPickerComponent(AlbumPickerComponent)](arkts-medialibrary-file-albumpickercomponent-albumpickercomponent-s.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [EmptyAreaClickCallback(AlbumPickerComponent)](arkts-medialibrary-emptyareaclickcallback-t.md) |
