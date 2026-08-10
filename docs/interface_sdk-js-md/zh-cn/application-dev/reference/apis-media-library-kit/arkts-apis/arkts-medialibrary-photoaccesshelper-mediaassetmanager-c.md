# MediaAssetManager

The MediaAssetManager class is used for manipulating the read and write operations of media assets.

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-photoAccessHelper-class MediaAssetManager--><!--Device-photoAccessHelper-class MediaAssetManager-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## cancelRequest

```TypeScript
static cancelRequest(context: Context, requestId: string): Promise<void>
```

Cancels a request for the asset, the callback of which has not been triggered yet. This API uses a promise to return the result.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.READ_IMAGEVIDEO

<!--Device-MediaAssetManager-static cancelRequest(context: Context, requestId: string): Promise<void>--><!--Device-MediaAssetManager-static cancelRequest(context: Context, requestId: string): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 | Context of the ability instance. |
| requestId | string | 是 | ID of the request to cancel. It is a valid request ID returned by **requestImage**. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| 201 | Permission denied |
| 14000011 | System inner fail |

## loadMovingPhoto

```TypeScript
static loadMovingPhoto(
      context: Context,
      imageFileUri: string,
      videoFileUri: string
    ): Promise<MovingPhoto>
```

Loads a moving photo in the application sandbox. This API uses a promise to return the result.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-MediaAssetManager-static loadMovingPhoto(      context: Context,      imageFileUri: string,      videoFileUri: string    ): Promise<MovingPhoto>--><!--Device-MediaAssetManager-static loadMovingPhoto(      context: Context,      imageFileUri: string,      videoFileUri: string    ): Promise<MovingPhoto>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 | AbilityContext or UIExtensionContext instance. |
| imageFileUri | string | 是 | URI of the image file of the moving photo in the application sandbox. &lt;br&gt;Example: **'file://com.example.temptest/data/storage/el2/base/haps/ImageFile.jpg'**. |
| videoFileUri | string | 是 | URI of the video file of the moving photo in the application sandbox. &lt;br&gt;Example: **'file://com.example.temptest/data/storage/el2/base/haps/VideoFile.mp4'**. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;MovingPhoto&gt; | Promise used to return the [MovingPhoto]{ |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| 14000011 | Internal system error |

## quickRequestImage

```TypeScript
static quickRequestImage(
      context: Context,
      asset: PhotoAsset,
      requestOptions: RequestOptions,
      dataHandler: QuickImageDataHandler<image.Picture>
    ): Promise<string>
```

Requests an image quickly. This API uses a promise to return the result.

**起始版本：** 13

**ArkTS模式：** ArkTS-Dyn起始版本为13；ArkTS-Sta起始版本为26.0.0。

**需要权限：** ohos.permission.READ_IMAGEVIDEO

<!--Device-MediaAssetManager-static quickRequestImage(      context: Context,      asset: PhotoAsset,      requestOptions: RequestOptions,      dataHandler: QuickImageDataHandler<image.Picture>    ): Promise<string>--><!--Device-MediaAssetManager-static quickRequestImage(      context: Context,      asset: PhotoAsset,      requestOptions: RequestOptions,      dataHandler: QuickImageDataHandler<image.Picture>    ): Promise<string>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 | Context of the ability instance. |
| asset | [PhotoAsset](arkts-medialibrary-sendablephotoaccesshelper-photoasset-i.md) | 是 | Image to request. |
| requestOptions | [RequestOptions](arkts-medialibrary-photoaccesshelper-requestoptions-i.md) | 是 | Options for requesting the image. |
| dataHandler | [QuickImageDataHandler](arkts-medialibrary-photoaccesshelper-quickimagedatahandler-i.md)&lt;image.Picture&gt; | 是 | Media asset handler, which invokes a callback to return the image when the requested image is ready. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Promise used to return the request ID, which can be used in [cancelRequest]{ |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| 201 | Permission denied |
| 14000011 | Internal system error |

## requestImage

```TypeScript
static requestImage(
      context: Context,
      asset: PhotoAsset,
      requestOptions: RequestOptions,
      dataHandler: MediaAssetDataHandler<image.ImageSource>
    ): Promise<string>
```

Requests an image. This API uses a promise to return the result.

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.READ_IMAGEVIDEO

<!--Device-MediaAssetManager-static requestImage(      context: Context,      asset: PhotoAsset,      requestOptions: RequestOptions,      dataHandler: MediaAssetDataHandler<image.ImageSource>    ): Promise<string>--><!--Device-MediaAssetManager-static requestImage(      context: Context,      asset: PhotoAsset,      requestOptions: RequestOptions,      dataHandler: MediaAssetDataHandler<image.ImageSource>    ): Promise<string>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 | Context of the ability instance. |
| asset | [PhotoAsset](arkts-medialibrary-sendablephotoaccesshelper-photoasset-i.md) | 是 | Image to request. |
| requestOptions | [RequestOptions](arkts-medialibrary-photoaccesshelper-requestoptions-i.md) | 是 | Options for requesting the image. |
| dataHandler | [MediaAssetDataHandler](arkts-medialibrary-photoaccesshelper-mediaassetdatahandler-i.md)&lt;image.ImageSource&gt; | 是 | Media asset handler, which invokes a callback to return the image when the requested image is ready. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Promise used to return the request ID, which can be used in [cancelRequest]{ |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| 201 | Permission denied |
| 14000011 | System inner fail. Possible causes: &lt;br&gt;1. The database is corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |

## requestImageData

```TypeScript
static requestImageData(
      context: Context,
      asset: PhotoAsset,
      requestOptions: RequestOptions,
      dataHandler: MediaAssetDataHandler<ArrayBuffer>
    ): Promise<string>
```

Requests image data. This API uses a promise to return the result.

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.READ_IMAGEVIDEO

<!--Device-MediaAssetManager-static requestImageData(      context: Context,      asset: PhotoAsset,      requestOptions: RequestOptions,      dataHandler: MediaAssetDataHandler<ArrayBuffer>    ): Promise<string>--><!--Device-MediaAssetManager-static requestImageData(      context: Context,      asset: PhotoAsset,      requestOptions: RequestOptions,      dataHandler: MediaAssetDataHandler<ArrayBuffer>    ): Promise<string>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 | Context of the ability instance. |
| asset | [PhotoAsset](arkts-medialibrary-sendablephotoaccesshelper-photoasset-i.md) | 是 | Image to request. |
| requestOptions | [RequestOptions](arkts-medialibrary-photoaccesshelper-requestoptions-i.md) | 是 | Options for requesting the image. |
| dataHandler | [MediaAssetDataHandler](arkts-medialibrary-photoaccesshelper-mediaassetdatahandler-i.md)&lt;ArrayBuffer&gt; | 是 | Media asset handler, which invokes a callback to return the image when the requested image is ready. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Promise used to return the request ID, which can be used in [cancelRequest]{ |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| 201 | Permission denied |
| 14000011 | System inner fail. Possible causes: &lt;br&gt;1. The database is corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |

## requestMovingPhoto

```TypeScript
static requestMovingPhoto(
      context: Context,
      asset: PhotoAsset,
      requestOptions: RequestOptions,
      dataHandler: MediaAssetDataHandler<MovingPhoto>
    ): Promise<string>
```

Requests a moving photo object, which can be used to request the asset data of the moving photo. This API uses a promise to return the result.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.READ_IMAGEVIDEO

<!--Device-MediaAssetManager-static requestMovingPhoto(      context: Context,      asset: PhotoAsset,      requestOptions: RequestOptions,      dataHandler: MediaAssetDataHandler<MovingPhoto>    ): Promise<string>--><!--Device-MediaAssetManager-static requestMovingPhoto(      context: Context,      asset: PhotoAsset,      requestOptions: RequestOptions,      dataHandler: MediaAssetDataHandler<MovingPhoto>    ): Promise<string>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 | Context of the ability instance. |
| asset | [PhotoAsset](arkts-medialibrary-sendablephotoaccesshelper-photoasset-i.md) | 是 | Image to request. |
| requestOptions | [RequestOptions](arkts-medialibrary-photoaccesshelper-requestoptions-i.md) | 是 | Options for requesting the image. |
| dataHandler | [MediaAssetDataHandler](arkts-medialibrary-photoaccesshelper-mediaassetdatahandler-i.md)&lt;MovingPhoto&gt; | 是 | Media asset handler, which invokes a callback to return the image when the requested image is ready. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Promise used to return the request ID, which can be used in [cancelRequest]{ |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| 801 | Capability not supported.<br>**适用版本：** 18+ |
| 201 | Permission denied |
| 14000011 | System inner fail |

## requestVideoFile

```TypeScript
static requestVideoFile(
      context: Context,
      asset: PhotoAsset,
      requestOptions: RequestOptions,
      fileUri: string,
      dataHandler: MediaAssetDataHandler<boolean>
    ): Promise<string>
```

Requests a video and saves it to the specified sandbox directory. This API uses a promise to return the result.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.READ_IMAGEVIDEO

<!--Device-MediaAssetManager-static requestVideoFile(      context: Context,      asset: PhotoAsset,      requestOptions: RequestOptions,      fileUri: string,      dataHandler: MediaAssetDataHandler<boolean>    ): Promise<string>--><!--Device-MediaAssetManager-static requestVideoFile(      context: Context,      asset: PhotoAsset,      requestOptions: RequestOptions,      fileUri: string,      dataHandler: MediaAssetDataHandler<boolean>    ): Promise<string>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 | Context of the ability instance. |
| asset | [PhotoAsset](arkts-medialibrary-sendablephotoaccesshelper-photoasset-i.md) | 是 | Image to request. |
| requestOptions | [RequestOptions](arkts-medialibrary-photoaccesshelper-requestoptions-i.md) | 是 | Options for requesting the video asset. |
| fileUri | string | 是 | URI of the sandbox directory, to which the requested video asset is to be saved. Example: **'file://com.example.temptest/data/storage/el2/base/haps/entry/files/test.mp4'**. |
| dataHandler | [MediaAssetDataHandler](arkts-medialibrary-photoaccesshelper-mediaassetdatahandler-i.md)&lt;boolean&gt; | 是 | Media asset handler. When the requested video is written to the specified directory, a callback is triggered. &lt;br&gt;If the video is successfully written, **true** is returned. Otherwise, **false** is returned. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Promise used to return the request ID, which can be used in [cancelRequest]{ |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| 801 | Capability not supported.<br>**适用版本：** 15+ |
| 201 | Permission denied |
| 14000011 | System inner fail. Possible causes: &lt;br&gt;1. The database is corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |

