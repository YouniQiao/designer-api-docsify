# QuickImageDataHandler

QuickImageDataHandler is a media asset handler used to customize the media asset processing logic in   
**onDataPrepared**.

**Since:** 13

<!--Device-photoAccessHelper-interface QuickImageDataHandler<T>--><!--Device-photoAccessHelper-interface QuickImageDataHandler<T>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

## onDataPrepared

```TypeScript
onDataPrepared(data: T, imageSource: image.ImageSource, map: Map<string, string>): void
```

Called when the requested image is ready. If an error occurs, **data** returned by the callback is **undefined**.

Information returned by **map**:

| Map Key | **Description**|
|----------|-------|
| 'quality' |

**Since:** 13

<!--Device-QuickImageDataHandler-onDataPrepared(data: T, imageSource: image.ImageSource, map: Map<string, string>): void--><!--Device-QuickImageDataHandler-onDataPrepared(data: T, imageSource: image.ImageSource, map: Map<string, string>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | T | Yes |
| imageSource | image.ImageSource | Yes |
| map | Map & lt;string, string & gt; | Yes |
