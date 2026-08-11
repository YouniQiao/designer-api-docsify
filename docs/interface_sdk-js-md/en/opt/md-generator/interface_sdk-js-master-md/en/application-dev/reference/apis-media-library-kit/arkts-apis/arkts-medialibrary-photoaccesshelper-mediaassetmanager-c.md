# MediaAssetManager

The MediaAssetManager class is used for manipulating the read and write operations of media assets.

**Since:** 11

<!--Device-photoAccessHelper-class MediaAssetManager--><!--Device-photoAccessHelper-class MediaAssetManager-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## cancelRequest

```TypeScript
static cancelRequest(context: Context, requestId: string): Promise<void>
```

Cancels a request for the asset, the callback of which has not been triggered yet. This API uses a promise to return the result.

**Since:** 12

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-MediaAssetManager-static cancelRequest(context: Context, requestId: string): Promise<void>--><!--Device-MediaAssetManager-static cancelRequest(context: Context, requestId: string): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |
| requestId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 14000011 |

## loadMovingPhoto

```TypeScript
static loadMovingPhoto(
      context: Context,
      imageFileUri: string,
      videoFileUri: string
    ): Promise<MovingPhoto>
```

Loads a moving photo in the application sandbox. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-MediaAssetManager-static loadMovingPhoto(      context: Context,      imageFileUri: string,      videoFileUri: string    ): Promise<MovingPhoto>--><!--Device-MediaAssetManager-static loadMovingPhoto(      context: Context,      imageFileUri: string,      videoFileUri: string    ): Promise<MovingPhoto>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |
| imageFileUri | string | Yes |
| videoFileUri | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;MovingPhoto&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 14000011 |

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

**Since:** 13

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-MediaAssetManager-static quickRequestImage(      context: Context,      asset: PhotoAsset,      requestOptions: RequestOptions,      dataHandler: QuickImageDataHandler<image.Picture>    ): Promise<string>--><!--Device-MediaAssetManager-static quickRequestImage(      context: Context,      asset: PhotoAsset,      requestOptions: RequestOptions,      dataHandler: QuickImageDataHandler<image.Picture>    ): Promise<string>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |
| asset | [PhotoAsset](arkts-medialibrary-sendablephotoaccesshelper-photoasset-i.md) | Yes |
| requestOptions | [RequestOptions](arkts-medialibrary-photoaccesshelper-requestoptions-i.md) | Yes |
| dataHandler | [QuickImageDataHandler](arkts-medialibrary-photoaccesshelper-quickimagedatahandler-i.md)&lt;image.Picture&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;string&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 14000011 |

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

**Since:** 11

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-MediaAssetManager-static requestImage(      context: Context,      asset: PhotoAsset,      requestOptions: RequestOptions,      dataHandler: MediaAssetDataHandler<image.ImageSource>    ): Promise<string>--><!--Device-MediaAssetManager-static requestImage(      context: Context,      asset: PhotoAsset,      requestOptions: RequestOptions,      dataHandler: MediaAssetDataHandler<image.ImageSource>    ): Promise<string>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |
| asset | [PhotoAsset](arkts-medialibrary-sendablephotoaccesshelper-photoasset-i.md) | Yes |
| requestOptions | [RequestOptions](arkts-medialibrary-photoaccesshelper-requestoptions-i.md) | Yes |
| dataHandler | [MediaAssetDataHandler](arkts-medialibrary-photoaccesshelper-mediaassetdatahandler-i.md)&lt;image.ImageSource&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;string&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 14000011 |

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

**Since:** 11

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-MediaAssetManager-static requestImageData(      context: Context,      asset: PhotoAsset,      requestOptions: RequestOptions,      dataHandler: MediaAssetDataHandler<ArrayBuffer>    ): Promise<string>--><!--Device-MediaAssetManager-static requestImageData(      context: Context,      asset: PhotoAsset,      requestOptions: RequestOptions,      dataHandler: MediaAssetDataHandler<ArrayBuffer>    ): Promise<string>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |
| asset | [PhotoAsset](arkts-medialibrary-sendablephotoaccesshelper-photoasset-i.md) | Yes |
| requestOptions | [RequestOptions](arkts-medialibrary-photoaccesshelper-requestoptions-i.md) | Yes |
| dataHandler | [MediaAssetDataHandler](arkts-medialibrary-photoaccesshelper-mediaassetdatahandler-i.md)&lt;ArrayBuffer&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;string&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 14000011 |

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

**Since:** 12

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-MediaAssetManager-static requestMovingPhoto(      context: Context,      asset: PhotoAsset,      requestOptions: RequestOptions,      dataHandler: MediaAssetDataHandler<MovingPhoto>    ): Promise<string>--><!--Device-MediaAssetManager-static requestMovingPhoto(      context: Context,      asset: PhotoAsset,      requestOptions: RequestOptions,      dataHandler: MediaAssetDataHandler<MovingPhoto>    ): Promise<string>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |
| asset | [PhotoAsset](arkts-medialibrary-sendablephotoaccesshelper-photoasset-i.md) | Yes |
| requestOptions | [RequestOptions](arkts-medialibrary-photoaccesshelper-requestoptions-i.md) | Yes |
| dataHandler | [MediaAssetDataHandler](arkts-medialibrary-photoaccesshelper-mediaassetdatahandler-i.md)&lt;MovingPhoto&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;string&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 14000011 |

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

**Since:** 12

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-MediaAssetManager-static requestVideoFile(      context: Context,      asset: PhotoAsset,      requestOptions: RequestOptions,      fileUri: string,      dataHandler: MediaAssetDataHandler<boolean>    ): Promise<string>--><!--Device-MediaAssetManager-static requestVideoFile(      context: Context,      asset: PhotoAsset,      requestOptions: RequestOptions,      fileUri: string,      dataHandler: MediaAssetDataHandler<boolean>    ): Promise<string>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |
| asset | [PhotoAsset](arkts-medialibrary-sendablephotoaccesshelper-photoasset-i.md) | Yes |
| requestOptions | [RequestOptions](arkts-medialibrary-photoaccesshelper-requestoptions-i.md) | Yes |
| fileUri | string | Yes |
| dataHandler | [MediaAssetDataHandler](arkts-medialibrary-photoaccesshelper-mediaassetdatahandler-i.md)&lt;boolean&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;string&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 14000011 |
