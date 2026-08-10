# QuickImageDataHandler

QuickImageDataHandler is a media asset handler used to customize the media asset processing logic in   
**onDataPrepared**.

**起始版本：** 13

**ArkTS模式：** ArkTS-Dyn起始版本为13；ArkTS-Sta起始版本为23。

<!--Device-photoAccessHelper-interface QuickImageDataHandler<T>--><!--Device-photoAccessHelper-interface QuickImageDataHandler<T>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## onDataPrepared

```TypeScript
onDataPrepared(data: T, imageSource: image.ImageSource, map: Map<string, string>): void
```

Called when the requested image is ready. If an error occurs, **data** returned by the callback is **undefined**.

Information returned by **map**:

| Map Key | **Description**|  
|----------|-------|  
| 'quality' | Image quality. The value **high** means high quality, and **low** means poor quality.|

**起始版本：** 13

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为13。

<!--Device-QuickImageDataHandler-onDataPrepared(data: T, imageSource: image.ImageSource, map: Map<string, string>): void--><!--Device-QuickImageDataHandler-onDataPrepared(data: T, imageSource: image.ImageSource, map: Map<string, string>): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | T | 是 | Data of the image asset that is ready. It is of the generic type and supports the [Picture](../../apis-image-kit/arkts-apis/arkts-image-image-picture-i.md/arkts-image-image-picture-i.md) type. |
| imageSource | image.ImageSource | 是 | Data of the image asset that is ready. |
| map | Map&lt;string, string&gt; | 是 | Additional information about the image asset, such as the image quality. Currently, only **quality** is supported. |

## onDataPrepared

```TypeScript
onDataPrepared(data: T | undefined, imageSource: image.ImageSource | null, map: Map<string, string>): void
```

Indicates required media asset data quickly is prepared

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-QuickImageDataHandler-onDataPrepared(data: T | undefined, imageSource: image.ImageSource | null, map: Map<string, string>): void--><!--Device-QuickImageDataHandler-onDataPrepared(data: T | undefined, imageSource: image.ImageSource | null, map: Map<string, string>): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | T \| undefined | 是 | the returned data of picture if data of media asset is invalid, return undefined. |
| imageSource | image.ImageSource \| null | 是 | the returned data of imageSource if data of imageSource is invalid, return null. |
| map | Map&lt;string, string&gt; | 是 | additional information for the data |

