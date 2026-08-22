# MediaAssetDataHandler

MediaAssetDataHandler is a media asset handler used to customize the media asset processing logic in **onDataPrepared**.

**Since:** 23

<!--Device-photoAccessHelper-interface MediaAssetDataHandler--><!--Device-photoAccessHelper-interface MediaAssetDataHandler-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

## onDataPrepared

```TypeScript
onDataPrepared(data: T, map?: Map<string, string>): void
```

Called when the requested media asset is ready. If an error occurs, **data** returned by the callback is **undefined**. Each media asset request corresponds to a callback.

T supports the following data types: ArrayBuffer, [ImageSource](../../apis-image-kit/arkts-apis/arkts-image-image-imagesource-i.md), [MovingPhoto](arkts-file-photoaccesshelper.md), and boolean. ArrayBuffer indicates the image or video asset data, [ImageSource](../../apis-image-kit/arkts-apis/arkts-image-image-imagesource-i.md) indicates the image source, [MovingPhoto](arkts-file-photoaccesshelper.md) indicates a moving photo object, and boolean indicates whether the image or video is successfully written to the application sandbox directory.

Information returned by **map**:

| Map Key | Description| |----------|-------| | 'quality' | Image quality. The value **high** means high quality, and **low** means poor quality.|

**Since:** 11

<!--Device-MediaAssetDataHandler-onDataPrepared(data: T, map?: Map<string, string>): void--><!--Device-MediaAssetDataHandler-onDataPrepared(data: T, map?: Map<string, string>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | T | Yes | Data of the image asset that is ready. It is of the generic type and supports the following data types: ArrayBuffer, [ImageSource](../../apis-image-kit/arkts-apis/arkts-image-image-imagesource-i.md), [MovingPhoto](arkts-file-photoaccesshelper.md), and boolean. |
| map | Map&lt;string, string&gt; | No | Additional information about the image asset, such as the image quality. Currently, only **quality** is supported.<br>**Since:** 12 |

**Examples**

```TypeScript
import { image } from '@kit.ImageKit';

class MediaHandler implements photoAccessHelper.MediaAssetDataHandler<image.ImageSource> {
  onDataPrepared = (data: image.ImageSource, map: Map<string, string>) => {
    if (data === undefined) {
      console.error('Error occurred when preparing data');
      return;
    }
    // Customize the processing logic for ImageSource.
    console.info('on image data prepared, photo quality is ' + map['quality']);
  }
}

class MediaDataHandler implements photoAccessHelper.MediaAssetDataHandler<ArrayBuffer> {
  onDataPrepared = (data: ArrayBuffer, map: Map<string, string>) => {
    if (data === undefined) {
      console.error('Error occurred when preparing data');
      return;
    }
    // Customize the processing logic for ArrayBuffer.
    console.info('on image data prepared, photo quality is ' + map['quality']);
  }
}

class MovingPhotoHandler implements photoAccessHelper.MediaAssetDataHandler<photoAccessHelper.MovingPhoto> {
  onDataPrepared = (data: photoAccessHelper.MovingPhoto, map: Map<string, string>) => {
    if (data === undefined) {
      console.error('Error occurred when preparing data');
      return;
    }
    // Customize the processing logic for MovingPhoto.
    console.info('on image data prepared, photo quality is ' + map['quality']);
  }
}
```

```TypeScript
import { image } from '@kit.ImageKit';

class MediaHandler implements photoAccessHelper.QuickImageDataHandler<image.Picture> {
  onDataPrepared(data: image.Picture, imageSource: image.ImageSource, map: Map<string, string>) {
    console.info('on image data prepared');
  }
}
```

## onDataPrepared

```TypeScript
onDataPrepared(data: T | undefined, map?: Map<string, string>): void
```

Indicates required media asset data is prepared

**Since:** 23

<!--Device-MediaAssetDataHandler-onDataPrepared(data: T | undefined, map?: Map<string, string>): void--><!--Device-MediaAssetDataHandler-onDataPrepared(data: T | undefined, map?: Map<string, string>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | T \| undefined | Yes | the returned data of media asset if data of media asset is invalid, return undefined. |
| map | Map&lt;string, string&gt; | No | additional information for the data |

**Examples**

See [onDataPrepared](#ondataprepared)

