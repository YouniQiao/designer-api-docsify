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
import { AlbumPickerComponent, AlbumPickerOptions, AlbumInfo, EmptyAreaClickCallback, AlbumPickerController } from '@kit.MediaLibraryKit';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [AlbumInfo(AlbumPickerComponent)](arkts-medialibrary-file-albumpickercomponent-albuminfo-c.md) | Represents album information. |
| [AlbumPickerController(AlbumPickerComponent)](arkts-medialibrary-file-albumpickercomponent-albumpickercontroller-c.md) | A controller that enables applications to send data to the **AlbumPickerComponent**. |
| [AlbumPickerOptions(AlbumPickerComponent)](arkts-medialibrary-file-albumpickercomponent-albumpickeroptions-c.md) | Represents the **AlbumPicker** configuration. |

### Structs

| Name | Description |
| --- | --- |
| [AlbumPickerComponent(AlbumPickerComponent)](arkts-medialibrary-file-albumpickercomponent-albumpickercomponent-s.md) | AlbumPickerComponent( {albumPickerOptions?: AlbumPickerOptions, onAlbumClick?: (albumInfo: AlbumInfo) = & gt; boolean, onEmptyAreaClick?: EmptyAreaClickCallback, albumPickerController?: AlbumPickerController })The **AlbumPickerComponent** embedded in the UI of an application allows the application to access the albums in the user directory without any permission. |

### Types

| Name | Description |
| --- | --- |
| [EmptyAreaClickCallback(AlbumPickerComponent)](arkts-medialibrary-emptyareaclickcallback-t.md) | Called when the blank area of the **AlbumPickerComponent** is tapped. |
