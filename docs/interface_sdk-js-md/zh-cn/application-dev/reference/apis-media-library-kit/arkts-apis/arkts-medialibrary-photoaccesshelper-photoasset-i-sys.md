# PhotoAsset

提供封装文件属性的方法。

**起始版本：** 10

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## cancelPhotoRequest

```TypeScript
cancelPhotoRequest(requestId: string): void
```

根据id取消指定的获取媒体缩略图的任务。

**起始版本：** 11

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| requestId | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## commitEditedAsset

```TypeScript
commitEditedAsset(editData: string, uri: string, callback: AsyncCallback<void>): void
```

提交编辑数据以及编辑后的图片或视频。使用callback异步回调。通过uri将编辑后的文件传递给媒体库，uri是编辑后的文件在应用沙箱下的FileUri，可参考 [FileUri](../../apis-core-file-kit/arkts-apis/arkts-file-fileuri.md)。

> **注意：**&gt;
> 新的编辑数据提交后，将覆盖掉原来的编辑数据。

**起始版本：** 11

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| editData | string | 是 |
| uri | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## commitEditedAsset

```TypeScript
commitEditedAsset(editData: string, uri: string): Promise<void>
```

提交编辑数据以及编辑后的图片或视频。使用Promise异步回调。通过uri将编辑后的文件传递给媒体库，uri是编辑后的文件在应用沙箱下的FileUri，可参考 [FileUri](../../apis-core-file-kit/arkts-apis/arkts-file-fileuri.md)。

> **注意：**&gt;
> 新的编辑数据提交后，将覆盖掉原来的编辑数据。

**起始版本：** 11

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| editData | string | 是 |
| uri | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## convertImageFormat

```TypeScript
convertImageFormat(title: string, imageFormat: SupportedImageFormat): Promise<PhotoAsset>
```

复制同一相册（用户创建的相册或应用相册）中的图片，并转换为指定格式。使用Promise异步回调。

**起始版本：** 20

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| title | string | 是 |
| imageFormat | [SupportedImageFormat](arkts-medialibrary-photoaccesshelper-supportedimageformat-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;PhotoAsset & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## createTemporaryCompatibleDuplicate

```TypeScript
createTemporaryCompatibleDuplicate(): Promise<void>
```

为不支持HEIF/HEIC图片编码格式的第三方应用创建JPEG格式的兼容副本。使用Promise异步回调。

**起始版本：** 21

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## getAnalysisData

```TypeScript
getAnalysisData(analysisType: AnalysisType): Promise<string>
```

根据智慧分析类型获取指定分析结果数据。使用Promise异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| analysisType | [AnalysisType](arkts-medialibrary-photoaccesshelper-analysistype-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## getEditData

```TypeScript
getEditData(): Promise<MediaAssetEditData>
```

获得资产编辑数据。使用Promise异步回调。如果资源未编辑过，则返回的编辑数据的内容为空字符串。

**起始版本：** 11

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;[MediaAssetEditData](arkts-medialibrary-photoaccesshelper-mediaasseteditdata-c-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## getExif

```TypeScript
getExif(callback: AsyncCallback<string>): void
```

读取jpg格式图片的Exif标签，并返回json格式的字符串。使用callback异步回调。此接口中获取的Exif标签信息是由 [image](../../apis-image-kit/arkts-apis/arkts-multimedia-image.md)模块提供。Exif标签详细信息请参考 [image.PropertyKey](../../apis-image-kit/arkts-apis/arkts-image-image-propertykey-e.md)。

> **注意：**&gt;
> 此接口返回的是Exif标签组成的json格式的字符串，完整Exif信息由all_exif与
> [PhotoKeys.USER_COMMENT](arkts-medialibrary-photoaccesshelper-photokeys-e.md)组成，
> [FetchOptions](arkts-medialibrary-photoaccesshelper-fetchoptions-i.md).fetchColumns需要传入这两个字段。

**起始版本：** 10

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900012 |
| 13900020 |
| 14000011 |

## getExif

```TypeScript
getExif(): Promise<string>
```

读取jpg格式图片的Exif标签，并返回json格式的字符串。使用Promise异步回调。此接口中获取的Exif标签信息是由[image](../../apis-image-kit/arkts-apis/arkts-multimedia-image.md) 模块提供。Exif标签详细信息请参考 [image.PropertyKey](../../apis-image-kit/arkts-apis/arkts-image-image-propertykey-e.md).

> **注意：**&gt;
> 此接口返回的是Exif标签组成的json格式的字符串，完整Exif信息由all_exif与
> [PhotoKeys.USER_COMMENT](arkts-medialibrary-photoaccesshelper-photokeys-e.md)组成，
> [FetchOptions](arkts-medialibrary-photoaccesshelper-fetchoptions-i.md).fetchColumns需要传入这两个字段。

**起始版本：** 10

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900012 |
| 13900020 |
| 14000011 |

## getKeyFrameThumbnail

```TypeScript
getKeyFrameThumbnail(beginFrameTimeMs: number, type: ThumbnailType): Promise<image.PixelMap>
```

获取视频中关键视频帧位置的指定类型缩略图。使用Promise异步回调。

**起始版本：** 18

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| beginFrameTimeMs | number | 是 |
| type | [ThumbnailType](arkts-medialibrary-photoaccesshelper-thumbnailtype-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;image.PixelMap & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## getReadOnlyFdWithCached

```TypeScript
getReadOnlyFdWithCached(): Promise<number>
```

打开文件，当从云端流读视频文件时会在图库沙箱进行缓存。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |
| [23800302](../errorcode-medialibrary.md#23800302-打开文件失败) |

## getThumbnailData

```TypeScript
getThumbnailData(type: ThumbnailType): Promise<ArrayBuffer>
```

获取文件缩略图的ArrayBuffer，传入缩略图的类型。使用Promise异步回调。

**起始版本：** 18

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [ThumbnailType](arkts-medialibrary-photoaccesshelper-thumbnailtype-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;ArrayBuffer & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## isEdited

```TypeScript
isEdited(callback: AsyncCallback<boolean>): void
```

查询图片或视频资源是否被编辑过。使用callback异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## isEdited

```TypeScript
isEdited(): Promise<boolean>
```

查询图片或视频资源是否被编辑过。使用Promise异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## open

```TypeScript
open(mode: string, callback: AsyncCallback<number>): void
```

打开当前文件。使用callback异步回调。该接口返回的文件描述符在使用完毕后需要调用close进行释放。

> **说明：**&gt;
> 从API version 10开始支持，从API version 11开始废弃。出于安全考量，不再提供获取正式媒体文件句柄的接口。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** open

**需要权限：** ohos.permission.READ_IMAGEVIDEO or ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900012 |
| 13900020 |
| 14000011 |

## open

```TypeScript
open(mode: string): Promise<number>
```

打开当前文件。使用Promise异步回调。该接口返回的文件描述符在使用完毕后需要调用close进行释放。

> **说明：**&gt;
> 从API version 10开始支持，从API version 11开始废弃。出于安全考量，不再提供获取正式媒体文件句柄的接口。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** open

**需要权限：** ohos.permission.READ_IMAGEVIDEO or ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900012 |
| 13900020 |
| 14000011 |

## requestEditData

```TypeScript
requestEditData(callback: AsyncCallback<string>): void
```

获得图片或视频资源的编辑数据。使用callback异步回调。如果资源未编辑过，则返回一个空字符串。

**起始版本：** 11

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## requestEditData

```TypeScript
requestEditData(): Promise<string>
```

获得图片或视频资源的编辑数据。使用Promise异步回调。如果资源未编辑过，则返回一个空字符串。

**起始版本：** 11

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## requestPhoto

```TypeScript
requestPhoto(callback: AsyncCallback<image.PixelMap>): string
```

通过callback的形式，获取资源的快速缩略图和普通缩略图。快速缩略图尺寸为128*128，普通缩略图尺寸为256*256。应用调用接口后，callback将返回两次缩略图对象，第一次为快速缩略图， 第二次为普通缩略图。

**起始版本：** 11

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;image.PixelMap&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## requestPhoto

```TypeScript
requestPhoto(options: RequestPhotoOptions, callback: AsyncCallback<image.PixelMap>): string
```

通过callback的形式，根据传入的选项，获取资源的缩略图。

**起始版本：** 11

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [RequestPhotoOptions](arkts-medialibrary-photoaccesshelper-requestphotooptions-i-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;image.PixelMap&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## requestSource

```TypeScript
requestSource(callback: AsyncCallback<number>): void
```

打开源文件并返回fd（文件描述符）。使用callback异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## requestSource

```TypeScript
requestSource(): Promise<number>
```

打开源文件并返回fd（文件描述符）。使用Promise异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## revertToOriginal

```TypeScript
revertToOriginal(callback: AsyncCallback<void>): void
```

回退到编辑前的状态。使用callback异步回调。

> **注意：**&gt;
> 调用该接口后，编辑数据和编辑后的图片或视频资源都将被删除，无法恢复，请谨慎调用。

**起始版本：** 11

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## revertToOriginal

```TypeScript
revertToOriginal(): Promise<void>
```

回退到编辑前的状态。使用Promise异步回调。

> **注意：**&gt;
> 调用该接口后，编辑数据和编辑后的图片或视频资源都将被删除，无法恢复，请谨慎调用。

**起始版本：** 11

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## setFavorite

```TypeScript
setFavorite(favoriteState: boolean, callback: AsyncCallback<void>): void
```

将文件设置为收藏文件。使用callback异步回调。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [setFavorite](arkts-medialibrary-photoaccesshelper-mediaassetchangerequest-c.md#setfavorite)

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| favoriteState | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900020 |
| 14000011 |

## setFavorite

```TypeScript
setFavorite(favoriteState: boolean): Promise<void>
```

将文件设置为收藏文件。使用Promise异步回调。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [setFavorite](arkts-medialibrary-photoaccesshelper-mediaassetchangerequest-c.md#setfavorite)

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| favoriteState | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900020 |
| 14000011 |

## setHidden

```TypeScript
setHidden(hiddenState: boolean, callback: AsyncCallback<void>): void
```

将文件设置为隐私文件。使用callback异步回调。隐私文件存在隐私相册中，用户通过隐私相册去获取隐私文件后可以通过设置hiddenState为false来从隐私相册中移除。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [setHidden](arkts-medialibrary-photoaccesshelper-mediaassetchangerequest-c-sys.md#sethidden)

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| hiddenState | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900020 |
| 14000011 |

## setHidden

```TypeScript
setHidden(hiddenState: boolean): Promise<void>
```

将文件设置为隐私文件。使用Promise异步回调。隐私文件存在隐私相册中，用户通过隐私相册去获取隐私文件后可以通过设置hiddenState为false来从隐私相册中移除。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [setHidden](arkts-medialibrary-photoaccesshelper-mediaassetchangerequest-c-sys.md#sethidden)

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| hiddenState | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900020 |
| 14000011 |

## setPending

```TypeScript
setPending(pendingState: boolean, callback: AsyncCallback<void>): void
```

为图片或视频资源设置pending状态。使用callback异步回调。将文件通过`setPending(true)`设置为pending状态后，只能通过`setPending(false)`解除pending状态。 可以通过`photoAsset.get(photoAccessHelper.PhotoKeys.PENDING)`的方式获取是否为pending状态，pending状态下返回true， 否则返回false。

> **注意：**&gt;
> setPending只能在文件的创建期使用，在文件的首次创建流程的close之后，无法通过setPending(true)将文件设置为pending状态。

**起始版本：** 11

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pendingState | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## setPending

```TypeScript
setPending(pendingState: boolean): Promise<void>
```

为图片或视频资源设置pending状态。使用Promise异步回调。将文件通过`setPending(true)`设置为pending状态后，只能通过`setPending(false)`解除pending状态。 可以通过`photoAsset.get(photoAccessHelper.PhotoKeys.PENDING)`的方式获取是否为pending状态，pending状态下返回true， 否则返回false。

> **注意：**&gt;
> setPending只能在文件的创建期使用，在文件的首次创建流程的close之后，无法通过setPending(true)将文件设置为pending状态。

**起始版本：** 11

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pendingState | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## setUserComment

```TypeScript
setUserComment(userComment: string, callback: AsyncCallback<void>): void
```

修改图片或者视频的备注信息。使用callback异步回调。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [setUserComment](arkts-medialibrary-photoaccesshelper-mediaassetchangerequest-c-sys.md#setusercomment)

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userComment | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900020 |
| 14000011 |

## setUserComment

```TypeScript
setUserComment(userComment: string): Promise<void>
```

修改图片或者视频的备注信息。使用Promise异步回调。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [setUserComment](arkts-medialibrary-photoaccesshelper-mediaassetchangerequest-c-sys.md#setusercomment)

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userComment | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900020 |
| 14000011 |
