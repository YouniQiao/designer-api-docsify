# MediaAssetChangeRequest

Represents a media asset change request.

**Inheritance/Implementation:** MediaAssetChangeRequest implements [MediaChangeRequest](arkts-medialibrary-photoaccesshelper-mediachangerequest-i.md#MediaChangeRequest)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-photoAccessHelper-class MediaAssetChangeRequest--><!--Device-photoAccessHelper-class MediaAssetChangeRequest-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
import { photoAccessHelper } from 'photoAccessHelper';
```

## addResource

```TypeScript
addResource(type: ResourceType, fileUri: string): void
```

Adds resources from the application sandbox based on the file URI. For details about the data source, see [@ohos.file.fileuri (File URI)](../../apis-core-file-kit/arkts-apis/arkts-file-fileuri.md#@ohos.file.fileuri). > **NOTE：**> > For the same asset change request, this API cannot be repeatedly called after the resource is successfully > added. For a moving photo, you can call this API twice to add the image and video resources.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-MediaAssetChangeRequest-addResource(type: ResourceType, fileUri: string): void--><!--Device-MediaAssetChangeRequest-addResource(type: ResourceType, fileUri: string): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | ResourceType | Yes | Type of the resource to add. |
| fileUri | string | Yes | Data source of the resource to be added, which is specified by a URI in the application sandbox directory. Example: **'file://com.example.temptest/data/storage/el2/base/haps/entry/files/test.jpg'**. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| 14000016 | Operation Not Support |
| 13900002 | The file corresponding to the URI is not in the app sandbox. |
| 14000011 | System inner fail |

## addResource

```TypeScript
addResource(type: ResourceType, data: ArrayBuffer): void
```

Adds a resource using **ArrayBuffer** data. > **NOTE：**> > For the same asset change request, this API cannot be repeatedly called after the resource is successfully > added. For a moving photo, you can call this API twice to add the image and video resources.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-MediaAssetChangeRequest-addResource(type: ResourceType, data: ArrayBuffer): void--><!--Device-MediaAssetChangeRequest-addResource(type: ResourceType, data: ArrayBuffer): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | ResourceType | Yes | Type of the resource to add. |
| data | ArrayBuffer | Yes | Data of the resource to add. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| 14000016 | Operation Not Support |
| 14000011 | System inner fail |

## constructor

```TypeScript
constructor(asset: PhotoAsset)
```

Constructor used to initialize an asset change request.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MediaAssetChangeRequest-constructor(asset: PhotoAsset)--><!--Device-MediaAssetChangeRequest-constructor(asset: PhotoAsset)-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| asset | PhotoAsset | Yes | Assets to change. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| 14000011 | System inner fail |

## createAssetRequest

```TypeScript
static createAssetRequest(context: Context, photoType: PhotoType, extension: string, options?: CreateOptions): MediaAssetChangeRequest
```

Create an asset change request based on the file type and filename extension.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-MediaAssetChangeRequest-static createAssetRequest(context: Context, photoType: PhotoType, extension: string, options?: CreateOptions): MediaAssetChangeRequest--><!--Device-MediaAssetChangeRequest-static createAssetRequest(context: Context, photoType: PhotoType, extension: string, options?: CreateOptions): MediaAssetChangeRequest-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes | Context of the ability instance. |
| photoType | PhotoType | Yes | Type of the file to create, which can be **IMAGE** or **VIDEO**. |
| extension | string | Yes | File name extension, for example, **'jpg'**. |
| options | [CreateOptions](arkts-medialibrary-photoaccesshelper-createoptions-i.md) | No | Options for creating the image or video asset, for example, **{title: 'testPhoto'}**. <br>The file name must not contain any invalid characters, which are:.. \ / : ? " ' ` &lt; &gt; \| { } [ ] |

**Return value:**

| Type | Description |
| --- | --- |
| [MediaAssetChangeRequest](arkts-medialibrary-photoaccesshelper-mediaassetchangerequest-c.md) | MediaAssetChangeRequest** created. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| 14000011 | System inner fail |

## createAssetRequest

```TypeScript
static createAssetRequest(context: Context, photoType: PhotoType, extension: string, options?: CreateOptions): MediaAssetChangeRequest | null
```

Create an asset change request based on the file type and filename extension.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-MediaAssetChangeRequest-static createAssetRequest(context: Context, photoType: PhotoType, extension: string, options?: CreateOptions): MediaAssetChangeRequest | null--><!--Device-MediaAssetChangeRequest-static createAssetRequest(context: Context, photoType: PhotoType, extension: string, options?: CreateOptions): MediaAssetChangeRequest | null-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes | Context of the ability instance. |
| photoType | PhotoType | Yes | Type of the file to create, which can be IMAGE or VIDEO. |
| extension | string | Yes | File name extension, for example, 'jpg'. |
| options | [CreateOptions](arkts-medialibrary-photoaccesshelper-createoptions-i.md) | No | Options for creating the image or video asset, for example, {title: 'testPhoto'}. |

**Return value:**

| Type | Description |
| --- | --- |
| [MediaAssetChangeRequest](arkts-medialibrary-photoaccesshelper-mediaassetchangerequest-c.md) | Returns a MediaAssetChangeRequest instance, if the operation fails, returns null |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [23800301](../errorcode-medialibrary.md#23800301-system-internal-error) | Internal system error. It is recommended to retry and check the logs. Possible causes: <br>1. Database corrupted; <br>2. The file system is abnormal; <br>3. The IPC request timed out. |

## createImageAssetRequest

```TypeScript
static createImageAssetRequest(context: Context, fileUri: string): MediaAssetChangeRequest
```

Creates an image asset change request. For details about data source of the asset to be created, see [@ohos.file.fileuri (File URI)](../../apis-core-file-kit/arkts-apis/arkts-file-fileuri.md#@ohos.file.fileuri).

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MediaAssetChangeRequest-static createImageAssetRequest(context: Context, fileUri: string): MediaAssetChangeRequest--><!--Device-MediaAssetChangeRequest-static createImageAssetRequest(context: Context, fileUri: string): MediaAssetChangeRequest-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes | Context of the ability instance. |
| fileUri | string | Yes | Data source of the image asset, which is specified by a URI in the application sandbox directory. Example: **'file://com.example.temptest/data/storage/el2/base/haps/entry/files/test.jpg'** . |

**Return value:**

| Type | Description |
| --- | --- |
| [MediaAssetChangeRequest](arkts-medialibrary-photoaccesshelper-mediaassetchangerequest-c.md) | MediaAssetChangeRequest** created. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| 13900002 | The file corresponding to the URI is not in the app sandbox. |
| 14000011 | System inner fail |

## createImageAssetRequest

```TypeScript
static createImageAssetRequest(context: Context, fileUri: string): MediaAssetChangeRequest | null
```

Creates an image asset change request.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-MediaAssetChangeRequest-static createImageAssetRequest(context: Context, fileUri: string): MediaAssetChangeRequest | null--><!--Device-MediaAssetChangeRequest-static createImageAssetRequest(context: Context, fileUri: string): MediaAssetChangeRequest | null-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes | Context of the ability instance. |
| fileUri | string | Yes | Data source of the image asset, which is specified by a URI in the application sandbox directory. |

**Return value:**

| Type | Description |
| --- | --- |
| [MediaAssetChangeRequest](arkts-medialibrary-photoaccesshelper-mediaassetchangerequest-c.md) | Returns a MediaAssetChangeRequest instance, if the operation fails, returns null |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [23800301](../errorcode-medialibrary.md#23800301-system-internal-error) | Internal system error. It is recommended to retry and check the logs. Possible causes: <br>1. Database corrupted; <br>2. The file system is abnormal; <br>3. The IPC request timed out. |
| 23800101 | The file corresponding to the URI is not in the app sandbox. |

## createVideoAssetRequest

```TypeScript
static createVideoAssetRequest(context: Context, fileUri: string): MediaAssetChangeRequest
```

Creates a video asset change request. For details about data source of the asset to be created, see [@ohos.file.fileuri (File URI)](../../apis-core-file-kit/arkts-apis/arkts-file-fileuri.md#@ohos.file.fileuri).

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

<!--Device-MediaAssetChangeRequest-static createVideoAssetRequest(context: Context, fileUri: string): MediaAssetChangeRequest--><!--Device-MediaAssetChangeRequest-static createVideoAssetRequest(context: Context, fileUri: string): MediaAssetChangeRequest-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes | Context of the ability instance. |
| fileUri | string | Yes | Data source of the video asset, which is specified by a URI in the application sandbox directory. Example: **'file://com.example.temptest/data/storage/el2/base/haps/entry/files/test.mp4'** . |

**Return value:**

| Type | Description |
| --- | --- |
| [MediaAssetChangeRequest](arkts-medialibrary-photoaccesshelper-mediaassetchangerequest-c.md) | MediaAssetChangeRequest** created. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| 13900002 | The file corresponding to the URI is not in the app sandbox. |
| 14000011 | System inner fail |

## createVideoAssetRequest

```TypeScript
static createVideoAssetRequest(context: Context, fileUri: string): MediaAssetChangeRequest | null
```

Creates a video asset change request.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-MediaAssetChangeRequest-static createVideoAssetRequest(context: Context, fileUri: string): MediaAssetChangeRequest | null--><!--Device-MediaAssetChangeRequest-static createVideoAssetRequest(context: Context, fileUri: string): MediaAssetChangeRequest | null-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes | Context of the ability instance. |
| fileUri | string | Yes | Data source of the video asset, which is specified by a URI in the application sandbox directory. |

**Return value:**

| Type | Description |
| --- | --- |
| [MediaAssetChangeRequest](arkts-medialibrary-photoaccesshelper-mediaassetchangerequest-c.md) | Returns a MediaAssetChangeRequest instance. if the operation fails, returns null. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [23800301](../errorcode-medialibrary.md#23800301-system-internal-error) | Internal system error. It is recommended to retry and check the logs. Possible causes: <br>1. Database corrupted; <br>2. The file system is abnormal; <br>3. The IPC request timed out. |
| 23800101 | The file corresponding to the URI is not in the app sandbox. |

## deleteAssets

```TypeScript
static deleteAssets(context: Context, assets: Array<PhotoAsset>): Promise<void>
```

Deletes media assets. The deleted assets are moved to the trash. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-MediaAssetChangeRequest-static deleteAssets(context: Context, assets: Array<PhotoAsset>): Promise<void>--><!--Device-MediaAssetChangeRequest-static deleteAssets(context: Context, assets: Array<PhotoAsset>): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes | Context of the ability instance. |
| assets | Array&lt;PhotoAsset&gt; | Yes | Array of media assets to delete. The array can contain a maximum of 300 elements. &lt;!--Del--&gt;System applications are not subject to this limitation.&lt;!--DelEnd--&gt; |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied |
| 14000011 | System inner fail |

## deleteAssets

```TypeScript
static deleteAssets(context: Context, uriList: Array<string>): Promise<void>
```

Deletes media assets. The deleted assets are moved to the trash. This API uses a promise to return the result.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-MediaAssetChangeRequest-static deleteAssets(context: Context, uriList: Array<string>): Promise<void>--><!--Device-MediaAssetChangeRequest-static deleteAssets(context: Context, uriList: Array<string>): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes | Context of the ability instance. |
| uriList | Array&lt;string&gt; | Yes | URIs of the media assets to delete. The array can contain a maximum of 300 elements. &lt;!--Del--&gt;System applications are not subject to this limitation.&lt;!--DelEnd--&gt; |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| 14000002 | The uri format is incorrect or does not exist. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied |
| 14000011 | System inner fail |

## deleteAssetsToTrashWithUris

```TypeScript
static deleteAssetsToTrashWithUris(context: Context, uriList: Array<string>): Promise<void>
```

Deletes media assets. This API uses a promise to return the result. The deleted assets are moved to the trash.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-MediaAssetChangeRequest-static deleteAssetsToTrashWithUris(context: Context, uriList: Array<string>): Promise<void>--><!--Device-MediaAssetChangeRequest-static deleteAssetsToTrashWithUris(context: Context, uriList: Array<string>): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes | Context of the ability instance. |
| uriList | Array&lt;string&gt; | Yes | URIs of the media files to delete. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Returns void |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [23800301](../errorcode-medialibrary.md#23800301-system-internal-error) | Internal system error. It is recommended to retry and check the logs. Possible causes: <br>1. Database corrupted; <br>2. The file system is abnormal; <br>3. The IPC request timed out. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied |
| [23800151](../errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) | The scenario parameter verification fails. Possible causes: <br>1. context is null or invalid; <br>2. The uri format is incorrect or does not exist. |

## discardCameraPhoto

```TypeScript
discardCameraPhoto(): void
```

Discards the photo taken by the camera.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-MediaAssetChangeRequest-discardCameraPhoto(): void--><!--Device-MediaAssetChangeRequest-discardCameraPhoto(): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14000016 | Operation Not Support |
| 14000011 | Internal system error |

## getAsset

```TypeScript
getAsset(): PhotoAsset
```

Obtains the asset in this asset change request. > **NOTE：**> > For the change request used to create an asset, this API returns **null** before > [applyChanges](arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md#applyChanges) is called > to apply the changes.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MediaAssetChangeRequest-getAsset(): PhotoAsset--><!--Device-MediaAssetChangeRequest-getAsset(): PhotoAsset-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Return value:**

| Type | Description |
| --- | --- |
| PhotoAsset | Asset obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |
| 14000011 | System inner fail |

## getAsset

```TypeScript
getAsset(): PhotoAsset | null
```

Obtains the asset in this asset change request.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-MediaAssetChangeRequest-getAsset(): PhotoAsset | null--><!--Device-MediaAssetChangeRequest-getAsset(): PhotoAsset | null-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Return value:**

| Type | Description |
| --- | --- |
| PhotoAsset | Returns the asset. if the operation fails, returns null. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [23800301](../errorcode-medialibrary.md#23800301-system-internal-error) | Internal system error. It is recommended to retry and check the logs. Possible causes: <br>1. Database corrupted; <br>2. The file system is abnormal; <br>3. The IPC request timed out. |

## getWriteCacheHandler

```TypeScript
getWriteCacheHandler(): Promise<int>
```

Obtains the handler used for writing a file to cache. This API uses a promise to return the result. > **NOTE：**> > For the same asset change request, this API cannot be repeatedly called after a temporary file write handle is > successfully obtained.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-MediaAssetChangeRequest-getWriteCacheHandler(): Promise<int>--><!--Device-MediaAssetChangeRequest-getWriteCacheHandler(): Promise<int>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;int&gt; | Promise used to return the write handle obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |
| 14000016 | Operation Not Support |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied |
| 14000011 | System inner fail. Possible causes: <br>1. The database is corrupted; <br>2. The file system is abnormal; <br>3. The IPC request timed out. |

## saveCameraPhoto

```TypeScript
saveCameraPhoto(): void
```

Saves the photo taken by the camera.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-MediaAssetChangeRequest-saveCameraPhoto(): void--><!--Device-MediaAssetChangeRequest-saveCameraPhoto(): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14000016 | Operation Not Support |
| 14000011 | System inner fail |

## saveCameraPhoto

```TypeScript
saveCameraPhoto(imageFileType: ImageFileType): void
```

Saves the photo taken by the camera.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-MediaAssetChangeRequest-saveCameraPhoto(imageFileType: ImageFileType): void--><!--Device-MediaAssetChangeRequest-saveCameraPhoto(imageFileType: ImageFileType): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| imageFileType | [ImageFileType](arkts-medialibrary-photoaccesshelper-imagefiletype-e.md) | Yes | File type of the photo to save. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14000016 | Operation Not Support |
| 14000011 | System inner fail |

## setOrientation

```TypeScript
setOrientation(orientation: int): void
```

Sets the orientation of this image.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-MediaAssetChangeRequest-setOrientation(orientation: int): void--><!--Device-MediaAssetChangeRequest-setOrientation(orientation: int): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| orientation | int | Yes | Rotation angle of the image to set. The value can only be **0**, **90**, **180**, or **270**. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| 14000011 | Internal system error |

## setTitle

```TypeScript
setTitle(title: string): void
```

Sets the media asset title.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MediaAssetChangeRequest-setTitle(title: string): void--><!--Device-MediaAssetChangeRequest-setTitle(title: string): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| title | string | Yes | Title to set. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| 14000011 | System inner fail |

## comment

```TypeScript
readonly comment: string
```

A readonly member for type checking.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-MediaAssetChangeRequest-readonly comment: string--><!--Device-MediaAssetChangeRequest-readonly comment: string-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

