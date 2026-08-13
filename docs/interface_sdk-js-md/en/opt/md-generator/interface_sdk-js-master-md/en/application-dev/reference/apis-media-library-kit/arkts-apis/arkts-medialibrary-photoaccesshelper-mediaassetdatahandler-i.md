# MediaAssetDataHandler

MediaAssetDataHandler is a media asset handler used to customize the media asset processing logic in **onDataPrepared**.

**Since:** 23

**Deprecated since:** -1

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

Called when the requested media asset is ready. If an error occurs, **data** returned by the callback is **undefined**. Each media asset request corresponds to a callback. T supports the following data types: ArrayBuffer, [ImageSource](../../apis-image-kit/arkts-apis/arkts-image-image-imagesource-i.md#ImageSource), [MovingPhoto](arkts-file-photoaccesshelper.md#@ohos.file.photoAccessHelper), and boolean. ArrayBuffer indicates the image or video asset data, [ImageSource](../../apis-image-kit/arkts-apis/arkts-image-image-imagesource-i.md#ImageSource) indicates the image source, [MovingPhoto](arkts-file-photoaccesshelper.md#@ohos.file.photoAccessHelper) indicates a moving photo object, and boolean indicates whether the image or video is successfully written to the application sandbox directory. Information returned by **map**: | Map Key | Description| |----------|-------| | 'quality' | Image quality. The value **high** means high quality, and **low** means poor quality.|

**Since:** 11

**Deprecated since:** -1

<!--Device-MediaAssetDataHandler-onDataPrepared(data: T, map?: Map<string, string>): void--><!--Device-MediaAssetDataHandler-onDataPrepared(data: T, map?: Map<string, string>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | T | Yes |
| map | Map & lt;string, string & gt; | No |

## onDataPrepared

```TypeScript
onDataPrepared(data: T | undefined, map?: Map<string, string>): void
```

Indicates required media asset data is prepared

**Since:** 23

**Deprecated since:** -1

<!--Device-MediaAssetDataHandler-onDataPrepared(data: T | undefined, map?: Map<string, string>): void--><!--Device-MediaAssetDataHandler-onDataPrepared(data: T | undefined, map?: Map<string, string>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | T \| undefined | Yes |
| map | Map & lt;string, string & gt; | No |
