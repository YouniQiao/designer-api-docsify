# QuickImageDataHandler

QuickImageDataHandler is a media asset handler used to customize the media asset processing logic in **onDataPrepared**.

**Since:** 23

<!--Device-photoAccessHelper-interface QuickImageDataHandler--><!--Device-photoAccessHelper-interface QuickImageDataHandler-End-->

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

| Map Key | **Description**| |----------|-------| | 'quality' | Image quality. The value **high** means high quality, and **low** means poor quality.|

**Since:** 13

<!--Device-QuickImageDataHandler-onDataPrepared(data: T, imageSource: image.ImageSource, map: Map<string, string>): void--><!--Device-QuickImageDataHandler-onDataPrepared(data: T, imageSource: image.ImageSource, map: Map<string, string>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | T | Yes | Data of the image asset that is ready. It is of the generic type and supports the [Picture](../../apis-image-kit/arkts-apis/arkts-image-image-picture-i.md) type. |
| imageSource | image.ImageSource | Yes | Data of the image asset that is ready. |
| map | Map&lt;string, string&gt; | Yes | Additional information about the image asset, such as the image quality. Currently, only **quality** is supported. |

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
onDataPrepared(data: T | undefined, imageSource: image.ImageSource | null, map: Map<string, string>): void
```

Indicates required media asset data quickly is prepared

**Since:** 23

<!--Device-QuickImageDataHandler-onDataPrepared(data: T | undefined, imageSource: image.ImageSource | null, map: Map<string, string>): void--><!--Device-QuickImageDataHandler-onDataPrepared(data: T | undefined, imageSource: image.ImageSource | null, map: Map<string, string>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | T \| undefined | Yes | the returned data of picture if data of media asset is invalid, return undefined. |
| imageSource | image.ImageSource \| null | Yes | the returned data of imageSource if data of imageSource is invalid, return null. |
| map | Map&lt;string, string&gt; | Yes | additional information for the data |

**Examples**

See [onDataPrepared](#ondataprepared)

