# MediaAssetDataHandler

MediaAssetDataHandler is a media asset handler used to customize the media asset processing logic in   
**onDataPrepared**.

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-photoAccessHelper-interface MediaAssetDataHandler<T>--><!--Device-photoAccessHelper-interface MediaAssetDataHandler<T>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## onDataPrepared

```TypeScript
onDataPrepared(data: T, map?: Map<string, string>): void
```

Called when the requested media asset is ready. If an error occurs, **data** returned by the callback is   
**undefined**. Each media asset request corresponds to a callback.

T supports the following data types: ArrayBuffer, [ImageSource](../../apis-image-kit/arkts-apis/arkts-image-image-imagesource-i.md/arkts-image-image-imagesource-i.md),   
[MovingPhoto](arkts-file-photoaccesshelper.md), and boolean. ArrayBuffer indicates the image or video asset data, [ImageSource](../../apis-image-kit/arkts-apis/arkts-image-image-imagesource-i.md/arkts-image-image-imagesource-i.md) indicates the image source,   
[MovingPhoto](arkts-file-photoaccesshelper.md) indicates a moving photo object, and boolean indicates whether the image or video is successfully written to the application sandbox directory.

Information returned by **map**:

| Map Key | Description|  
|----------|-------|  
| 'quality' | Image quality. The value **high** means high quality, and **low** means poor quality.|

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

<!--Device-MediaAssetDataHandler-onDataPrepared(data: T, map?: Map<string, string>): void--><!--Device-MediaAssetDataHandler-onDataPrepared(data: T, map?: Map<string, string>): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | T | 是 | Data of the image asset that is ready. It is of the generic type and supports the following data types: ArrayBuffer, [ImageSource](../../apis-image-kit/arkts-apis/arkts-image-image-imagesource-i.md/arkts-image-image-imagesource-i.md), [MovingPhoto](arkts-file-photoaccesshelper.md), and boolean. |
| map | Map&lt;string, string&gt; | 否 | Additional information about the image asset, such as the image quality. Currently, only **quality** is supported.<br>**起始版本：** 12 |

## onDataPrepared

```TypeScript
onDataPrepared(data: T | undefined, map?: Map<string, string>): void
```

Indicates required media asset data is prepared

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-MediaAssetDataHandler-onDataPrepared(data: T | undefined, map?: Map<string, string>): void--><!--Device-MediaAssetDataHandler-onDataPrepared(data: T | undefined, map?: Map<string, string>): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | T \| undefined | 是 | the returned data of media asset if data of media asset is invalid, return undefined. |
| map | Map&lt;string, string&gt; | 否 | additional information for the data |

