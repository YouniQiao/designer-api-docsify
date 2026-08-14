# @ohos.file.AlbumPickerComponent

## Modules to Import

```TypeScript
import { AlbumPickerComponent } from 'AlbumPickerComponent';
import { AlbumPickerOptions } from 'AlbumPickerOptions';
import { AlbumInfo } from 'AlbumInfo';
import { EmptyAreaClickCallback } from 'EmptyAreaClickCallback';
import { AlbumPickerController } from 'AlbumPickerController';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [AlbumInfo](arkts-medialibrary-file-albumpickercomponent-albuminfo-c.md) | Represents album information. |
| [AlbumPickerController](arkts-medialibrary-file-albumpickercomponent-albumpickercontroller-c.md) | A controller that enables applications to send data to the **AlbumPickerComponent**. |
| [AlbumPickerOptions](arkts-medialibrary-file-albumpickercomponent-albumpickeroptions-c.md) | Represents the **AlbumPicker** configuration. |

### Structs

| Name | Description |
| --- | --- |
| [AlbumPickerComponent](arkts-medialibrary-file-albumpickercomponent-albumpickercomponent-s.md) | AlbumPickerComponent( {albumPickerOptions?: AlbumPickerOptions, onAlbumClick?: (albumInfo: AlbumInfo) => boolean, onEmptyAreaClick?: EmptyAreaClickCallback, albumPickerController?: AlbumPickerController }) The **AlbumPickerComponent** embedded in the UI of an application allows the application to access the albums in the user directory without any permission. |

### Types

| Name | Description |
| --- | --- |
| [EmptyAreaClickCallback](arkts-medialibrary-emptyareaclickcallback-t.md) | Called when the blank area of the **AlbumPickerComponent** is tapped. |

