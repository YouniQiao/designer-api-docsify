# PhotoAccessHelper

Helper functions to access photos and albums.

**Since:** 10

<!--Device-photoAccessHelper-interface PhotoAccessHelper--><!--Device-photoAccessHelper-interface PhotoAccessHelper-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## applyChanges

```TypeScript
applyChanges(mediaChangeRequest: MediaChangeRequest): Promise<void>
```

Applies media changes. This API uses a promise to return the result.

**Since:** 11

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PhotoAccessHelper-applyChanges(mediaChangeRequest: MediaChangeRequest): Promise<void>--><!--Device-PhotoAccessHelper-applyChanges(mediaChangeRequest: MediaChangeRequest): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mediaChangeRequest | [MediaChangeRequest](arkts-medialibrary-photoaccesshelper-mediachangerequest-i.md) | Yes |

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

## checkPhotoUrisReadPermission

```TypeScript
checkPhotoUrisReadPermission(uris: string[]): Promise<Map<string, MediaAssetPermissionState>>
```

Query whether the assets exist and whether the invoker has read permission on the assets without permission.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoAccessHelper-checkPhotoUrisReadPermission(uris: string[]): Promise<Map<string, MediaAssetPermissionState>>--><!--Device-PhotoAccessHelper-checkPhotoUrisReadPermission(uris: string[]): Promise<Map<string, MediaAssetPermissionState>>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uris | string[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Map&lt;string, MediaAssetPermissionState&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-system-internal-error) |
| [23800151](../errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## createAsset

```TypeScript
createAsset(photoType: PhotoType, extension: string, options: CreateOptions, callback: AsyncCallback<string>): void
```

Creates an image or video asset with the specified file type, file name extension, and options. This API uses an asynchronous callback to return the result.

If you do not have the **ohos.permission.WRITE_IMAGEVIDEO** permission, you can create a media asset by using a security component or an authorization pop-up. For details, see   
[Saving Media Assets](../../../media/medialibrary/photoAccessHelper-savebutton.md).

**Since:** 10

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PhotoAccessHelper-createAsset(photoType: PhotoType, extension: string, options: CreateOptions, callback: AsyncCallback<string>): void--><!--Device-PhotoAccessHelper-createAsset(photoType: PhotoType, extension: string, options: CreateOptions, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| photoType | [PhotoType](arkts-medialibrary-sendablephotoaccesshelper-phototype-e.md) | Yes |
| extension | string | Yes |
| options | [CreateOptions](arkts-medialibrary-photoaccesshelper-createoptions-i.md) | Yes | Options used for creation. Currently, only **title** is supported, for example , **{title: 'testPhoto'}**. &lt;br&gt;**NOTE：**&lt;br&gt;If a **subtype** option is passed, the configuration does not take effect. Only DEFAULT images can be saved. &lt;br&gt;The file name must not contain any invalid characters, which are:.. \ / : ? " ' ` &lt; &gt; \|
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 13900012 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 14000011 |

## createAsset

```TypeScript
createAsset(photoType: PhotoType, extension: string, callback: AsyncCallback<string>): void
```

Creates an image or video asset with the specified file type and file name extension. This API uses an asynchronous callback to return the result.

If you do not have the **ohos.permission.WRITE_IMAGEVIDEO** permission, you can create a media asset by using a security component or an authorization pop-up. For details, see   
[Saving Media Assets](../../../media/medialibrary/photoAccessHelper-savebutton.md).

**Since:** 10

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PhotoAccessHelper-createAsset(photoType: PhotoType, extension: string, callback: AsyncCallback<string>): void--><!--Device-PhotoAccessHelper-createAsset(photoType: PhotoType, extension: string, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| photoType | [PhotoType](arkts-medialibrary-sendablephotoaccesshelper-phototype-e.md) | Yes |
| extension | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 13900012 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 14000011 |

## createAsset

```TypeScript
createAsset(photoType: PhotoType, extension: string, options?: CreateOptions): Promise<string>
```

Creates an image or video asset with the specified file type, file name extension, and options. This API uses a promise to return the result.

If you do not have the **ohos.permission.WRITE_IMAGEVIDEO** permission, you can create a media asset by using a security component or an authorization pop-up. For details, see   
[Saving Media Assets](../../../media/medialibrary/photoAccessHelper-savebutton.md).

**Since:** 10

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PhotoAccessHelper-createAsset(photoType: PhotoType, extension: string, options?: CreateOptions): Promise<string>--><!--Device-PhotoAccessHelper-createAsset(photoType: PhotoType, extension: string, options?: CreateOptions): Promise<string>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| photoType | [PhotoType](arkts-medialibrary-sendablephotoaccesshelper-phototype-e.md) | Yes |
| extension | string | Yes |
| options | [CreateOptions](arkts-medialibrary-photoaccesshelper-createoptions-i.md) | No | Options used for creation. Currently, only **title** is supported, for example, **{title: 'testPhoto'}**. &lt;br&gt;**NOTE：**&lt;br&gt;If a **subtype** option is passed, the configuration does not take effect. Only DEFAULT images can be saved. &lt;br&gt;The file name must not contain any invalid characters, which are:.. \ / : ? " ' ` &lt; &gt; \|

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;string&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 13900012 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 14000011 |

## createAssetWithShortTermPermission

```TypeScript
createAssetWithShortTermPermission(photoCreationConfig: PhotoCreationConfig): Promise<string>
```

Creates an asset with a temporary permission of the given period. When this API is called by an application for the first time, a dialog box will be displayed for the user to confirm whether to save the asset. If the user agrees to save the asset, the asset instance will be created and the file URI granted with the save permission will be returned. The application can write the asset based on the URI.

Within 5 minutes after the user agrees to save the asset, if the same application calls this API again, the authorized URI can be automatically returned without the need to display the confirmation dialog box. Exiting the application will terminate the authorization, and the user need to re-trigger the dialog box for authorization confirmation when the application is re-launched.

**Since:** 12

**Required permissions:** ohos.permission.SHORT_TERM_WRITE_IMAGEVIDEO

<!--Device-PhotoAccessHelper-createAssetWithShortTermPermission(photoCreationConfig: PhotoCreationConfig): Promise<string>--><!--Device-PhotoAccessHelper-createAssetWithShortTermPermission(photoCreationConfig: PhotoCreationConfig): Promise<string>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| photoCreationConfig | [PhotoCreationConfig](arkts-medialibrary-photoaccesshelper-photocreationconfig-i.md) | Yes |

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

## createAssetWithShortTermPermissionEx

```TypeScript
createAssetWithShortTermPermissionEx(creationSetting: CreationSetting): Promise<string>
```

Displays the dialog box for the first time for the user to confirm whether to save the asset. This API uses a promise to return the result.

> **NOTE：**
> 
> - After the user agrees to save the asset, the API returns the URI of the created asset that has the save
> permission. The application can use the URI to write the image or video.
> 
> - Within 5 minutes after the user agrees to save the asset, if the same application calls this API again, the
> system directly returns the authorized URI for the application to save the image or video without displaying a
> confirmation dialog box. Exiting the application will terminate the authorization, and the user need to re-
> trigger the dialog box for authorization confirmation when the application is re-launched.

**Since:** 23

**Required permissions:** ohos.permission.SHORT_TERM_WRITE_IMAGEVIDEO

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoAccessHelper-createAssetWithShortTermPermissionEx(creationSetting: CreationSetting): Promise<string>--><!--Device-PhotoAccessHelper-createAssetWithShortTermPermissionEx(creationSetting: CreationSetting): Promise<string>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| creationSetting | [CreationSetting](arkts-medialibrary-photoaccesshelper-creationsetting-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;string&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 14000011 |

## createDeleteRequest

```TypeScript
createDeleteRequest(uriList: Array<string>, callback: AsyncCallback<void>): void
```

Creates a dialog box for deleting media files. This API uses an asynchronous callback to return the result. The deleted media files are moved to the trash.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [photoAccessHelper.MediaAssetChangeRequest.deleteAssets](arkts-medialibrary-photoaccesshelper-mediaassetchangerequest-c.md#deleteassets)

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-PhotoAccessHelper-createDeleteRequest(uriList: Array<string>, callback: AsyncCallback<void>): void--><!--Device-PhotoAccessHelper-createDeleteRequest(uriList: Array<string>, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uriList | Array&lt;string&gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 13900012 |
| 14000011 |

## createDeleteRequest

```TypeScript
createDeleteRequest(uriList: Array<string>): Promise<void>
```

Creates a dialog box for deleting media files. This API uses a promise to return the result. The deleted media files are moved to the trash.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [photoAccessHelper.MediaAssetChangeRequest.deleteAssets](arkts-medialibrary-photoaccesshelper-mediaassetchangerequest-c.md#deleteassets)

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-PhotoAccessHelper-createDeleteRequest(uriList: Array<string>): Promise<void>--><!--Device-PhotoAccessHelper-createDeleteRequest(uriList: Array<string>): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uriList | Array&lt;string&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 13900012 |
| 14000011 |

## createPhotoAsset

```TypeScript
createPhotoAsset(photoType: PhotoType, extension: string, title?: string): Promise<string>
```

Creates an image or video resource with the specified file type, extension, and title. This API uses a promise to return the result.

If you do not have the **ohos.permission.WRITE_IMAGEVIDEO** permission, you can create a media asset by using a security component or an authorization pop-up. For details, see   
[Saving Media Assets](../../../media/medialibrary/photoAccessHelper-savebutton.md).

**Since:** 23

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-PhotoAccessHelper-createPhotoAsset(photoType: PhotoType, extension: string, title?: string): Promise<string>--><!--Device-PhotoAccessHelper-createPhotoAsset(photoType: PhotoType, extension: string, title?: string): Promise<string>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| photoType | [PhotoType](arkts-medialibrary-sendablephotoaccesshelper-phototype-e.md) | Yes |
| extension | string | Yes |
| title | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;string&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [23800151](../errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) | The scenario parameter verification fails. Possible causes: &lt;br&gt;1. The extension format is unsupported &lt;br&gt;2. Title contains unsupported character, such as . .. \ / : ? " ' ` &lt; &gt; \|

## getAlbumIdByLpath

```TypeScript
getAlbumIdByLpath(lpath: string): Promise<number>
```

Obtains the album ID in the media library based on the album's virtual path. This API uses a promise to return the result.

This API supports the following albums: camera application album, screenshot application album,and screen recording application album.

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoAccessHelper-getAlbumIdByLpath(lpath: string): Promise<int>--><!--Device-PhotoAccessHelper-getAlbumIdByLpath(lpath: string): Promise<int>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| lpath | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-system-internal-error) |
| [23800151](../errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## getAlbums

```TypeScript
getAlbums(
      type: AlbumType,
      subtype: AlbumSubtype,
      options: FetchOptions,
      callback: AsyncCallback<FetchResult<Album>>
    ): void
```

Obtains albums based on the specified options and album type. This API uses an asynchronous callback to return the result.

Before the operation, ensure that the albums to obtain exist.

**Since:** 10

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAccessHelper-getAlbums(      type: AlbumType,      subtype: AlbumSubtype,      options: FetchOptions,      callback: AsyncCallback<FetchResult<Album>>    ): void--><!--Device-PhotoAccessHelper-getAlbums(      type: AlbumType,      subtype: AlbumSubtype,      options: FetchOptions,      callback: AsyncCallback<FetchResult<Album>>    ): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [AlbumType](arkts-medialibrary-photoaccesshelper-albumtype-e.md) | Yes |
| subtype | [AlbumSubtype](arkts-medialibrary-sendablephotoaccesshelper-albumsubtype-e.md) | Yes |
| options | [FetchOptions](arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FetchResult&lt;Album&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 13900012 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 14000011 |

## getAlbums

```TypeScript
getAlbums(type: AlbumType, subtype: AlbumSubtype, callback: AsyncCallback<FetchResult<Album>>): void
```

Obtains albums by type. This API uses an asynchronous callback to return the result.

Before the operation, ensure that the albums to obtain exist.

**Since:** 10

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAccessHelper-getAlbums(type: AlbumType, subtype: AlbumSubtype, callback: AsyncCallback<FetchResult<Album>>): void--><!--Device-PhotoAccessHelper-getAlbums(type: AlbumType, subtype: AlbumSubtype, callback: AsyncCallback<FetchResult<Album>>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [AlbumType](arkts-medialibrary-photoaccesshelper-albumtype-e.md) | Yes |
| subtype | [AlbumSubtype](arkts-medialibrary-sendablephotoaccesshelper-albumsubtype-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FetchResult&lt;Album&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 13900012 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 14000011 |

## getAlbums

```TypeScript
getAlbums(type: AlbumType, subtype: AlbumSubtype, options?: FetchOptions): Promise<FetchResult<Album>>
```

Obtains albums based on the specified options and album type. This API uses a promise to return the result.

Before the operation, ensure that the albums to obtain exist.

**Since:** 10

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAccessHelper-getAlbums(type: AlbumType, subtype: AlbumSubtype, options?: FetchOptions): Promise<FetchResult<Album>>--><!--Device-PhotoAccessHelper-getAlbums(type: AlbumType, subtype: AlbumSubtype, options?: FetchOptions): Promise<FetchResult<Album>>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [AlbumType](arkts-medialibrary-photoaccesshelper-albumtype-e.md) | Yes |
| subtype | [AlbumSubtype](arkts-medialibrary-sendablephotoaccesshelper-albumsubtype-e.md) | Yes |
| options | [FetchOptions](arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;FetchResult&lt;Album&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 13900012 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 14000011 |

## getAssets

```TypeScript
getAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<PhotoAsset>>): void
```

Obtains image and video assets. This API uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAccessHelper-getAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<PhotoAsset>>): void--><!--Device-PhotoAccessHelper-getAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<PhotoAsset>>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [FetchOptions](arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FetchResult&lt;PhotoAsset&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 13900012 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 14000011 |

## getAssets

```TypeScript
getAssets(options: FetchOptions): Promise<FetchResult<PhotoAsset>>
```

Obtains image and video assets. This API uses a promise to return the result.

**Since:** 10

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-PhotoAccessHelper-getAssets(options: FetchOptions): Promise<FetchResult<PhotoAsset>>--><!--Device-PhotoAccessHelper-getAssets(options: FetchOptions): Promise<FetchResult<PhotoAsset>>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [FetchOptions](arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;FetchResult&lt;PhotoAsset&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900012 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 14000011 |

## getBurstAssets

```TypeScript
getBurstAssets(burstKey: string, options: FetchOptions): Promise<FetchResult<PhotoAsset>>
```

Obtains burst assets. This API uses a promise to return the result.

**Since:** 12

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-PhotoAccessHelper-getBurstAssets(burstKey: string, options: FetchOptions): Promise<FetchResult<PhotoAsset>>--><!--Device-PhotoAccessHelper-getBurstAssets(burstKey: string, options: FetchOptions): Promise<FetchResult<PhotoAsset>>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| burstKey | string | Yes |
| options | [FetchOptions](arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;FetchResult&lt;PhotoAsset&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 14000011 |

## getPhotoPickerComponentDefaultAlbumName

```TypeScript
getPhotoPickerComponentDefaultAlbumName(): Promise<string>
```

Obtains the name of the album that the **PhotoPickerComponent** shows by default. The name string is localized to match the current system language. This API uses a promise to return the result.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-PhotoAccessHelper-getPhotoPickerComponentDefaultAlbumName(): Promise<string>--><!--Device-PhotoAccessHelper-getPhotoPickerComponentDefaultAlbumName(): Promise<string>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;string&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-system-internal-error) |

## getRecentPhotoInfo

```TypeScript
getRecentPhotoInfo(options?: RecentPhotoOptions): Promise<RecentPhotoInfo>
```

Obtains the information about the recent image or video when the application uses the **RecentPhotoComponent** to view recent images or videos. This API uses a promise to return the result.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-PhotoAccessHelper-getRecentPhotoInfo(options?: RecentPhotoOptions): Promise<RecentPhotoInfo>--><!--Device-PhotoAccessHelper-getRecentPhotoInfo(options?: RecentPhotoOptions): Promise<RecentPhotoInfo>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [RecentPhotoOptions](arkts-medialibrary-photoaccesshelper-recentphotooptions-c.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;RecentPhotoInfo&gt; |

## getSupportedPhotoFormats

```TypeScript
getSupportedPhotoFormats(photoType: PhotoType): Promise<Array<string>>
```

Obtains the list of image or video file name extensions supported by the media library.

**Since:** 18

<!--Device-PhotoAccessHelper-getSupportedPhotoFormats(photoType: PhotoType): Promise<Array<string>>--><!--Device-PhotoAccessHelper-getSupportedPhotoFormats(photoType: PhotoType): Promise<Array<string>>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| photoType | [PhotoType](arkts-medialibrary-sendablephotoaccesshelper-phototype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;string&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 14000011 |

## off('photoChange')

```TypeScript
off(type: 'photoChange', callback?: Callback<PhotoAssetChangeInfos>): void
```

Unregisters the listener for the **'photoChange'** event to stop monitoring media asset changes. If multiple listeners are registered, you can unregister a specific listener by specifying **callback**. Alternatively, you can unregister all of them without specifying **callback**.

**Since:** 20

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAccessHelper-off(type: 'photoChange', callback?: Callback<PhotoAssetChangeInfos>): void--><!--Device-PhotoAccessHelper-off(type: 'photoChange', callback?: Callback<PhotoAssetChangeInfos>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'photoChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;PhotoAssetChangeInfos&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [23800151](../errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## off('photoAlbumChange')

```TypeScript
off(type: 'photoAlbumChange', callback?: Callback<AlbumChangeInfos>): void
```

Unregisters a listener for the **'photoAlbumChange'** event to stop monitoring album changes. If multiple listeners are registered, you can unregister a specific listener by specifying **callback**. Alternatively, you can unregister all of them without specifying **callback**.

**Since:** 20

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAccessHelper-off(type: 'photoAlbumChange', callback?: Callback<AlbumChangeInfos>): void--><!--Device-PhotoAccessHelper-off(type: 'photoAlbumChange', callback?: Callback<AlbumChangeInfos>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'photoAlbumChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AlbumChangeInfos&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [23800151](../errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## offMediaLibraryAvailability

```TypeScript
offMediaLibraryAvailability(callback?: Callback<MediaLibraryAvailability>): void
```

Unsubscribes to changes of medialibrary availability.

**Since:** 26.0.0

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoAccessHelper-offMediaLibraryAvailability(callback?: Callback<MediaLibraryAvailability>): void--><!--Device-PhotoAccessHelper-offMediaLibraryAvailability(callback?: Callback<MediaLibraryAvailability>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;MediaLibraryAvailability&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## offSinglePhotoAlbumChange

```TypeScript
offSinglePhotoAlbumChange(album?: Album, callback?: Callback<AlbumChangeInfos>): void
```

Unregisters a listener for a single album. Note the following:

1. If no parameter is specified, all listeners for the single albums are unregistered.2. If **album** is specified but **callback** is not specified, all callback listeners of the album are unregistered.3. If both **album** and **callback** are specified, only the specified callback listener is unregistered.

**Since:** 23

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAccessHelper-offSinglePhotoAlbumChange(album?: Album, callback?: Callback<AlbumChangeInfos>): void--><!--Device-PhotoAccessHelper-offSinglePhotoAlbumChange(album?: Album, callback?: Callback<AlbumChangeInfos>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| album | [Album](arkts-medialibrary-sendablephotoaccesshelper-album-i.md) | No |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AlbumChangeInfos&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [23800151](../errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## offSinglePhotoChange

```TypeScript
offSinglePhotoChange(asset?: PhotoAsset, callback?: Callback<PhotoAssetChangeInfos>): void
```

Unregisters the listener for a single asset. Note the following:

1. If no parameter is specified, all listeners for the single assets are unregistered.2. If **asset** is specified but **callback** is not specified, all callback listeners of the **asset** are unregistered.3. If both **asset** and **callback** are specified, only the specified callback listener is unregistered.

**Since:** 23

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAccessHelper-offSinglePhotoChange(asset?: PhotoAsset, callback?: Callback<PhotoAssetChangeInfos>): void--><!--Device-PhotoAccessHelper-offSinglePhotoChange(asset?: PhotoAsset, callback?: Callback<PhotoAssetChangeInfos>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| asset | [PhotoAsset](arkts-medialibrary-sendablephotoaccesshelper-photoasset-i.md) | No |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;PhotoAssetChangeInfos&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [23800151](../errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## on('photoChange')

```TypeScript
on(type: 'photoChange', callback: Callback<PhotoAssetChangeInfos>): void
```

Registers a listener for the **'photoChange'** event to monitor media asset changes. This API uses a callback to return the result, and it accepts multiple callbacks.

**Since:** 20

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAccessHelper-on(type: 'photoChange', callback: Callback<PhotoAssetChangeInfos>): void--><!--Device-PhotoAccessHelper-on(type: 'photoChange', callback: Callback<PhotoAssetChangeInfos>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'photoChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;PhotoAssetChangeInfos&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [23800151](../errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## on('photoAlbumChange')

```TypeScript
on(type: 'photoAlbumChange', callback: Callback<AlbumChangeInfos>): void
```

Registers a listener for the **'photoAlbumChange'** event to monitor album changes. This API uses a callback to return the result, and it accepts multiple callbacks.

**Since:** 20

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAccessHelper-on(type: 'photoAlbumChange', callback: Callback<AlbumChangeInfos>): void--><!--Device-PhotoAccessHelper-on(type: 'photoAlbumChange', callback: Callback<AlbumChangeInfos>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'photoAlbumChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AlbumChangeInfos&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [23800151](../errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## onMediaLibraryAvailability

```TypeScript
onMediaLibraryAvailability(callback: Callback<MediaLibraryAvailability>): void
```

Subscribes to changes of medialibrary availability.

**Since:** 26.0.0

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoAccessHelper-onMediaLibraryAvailability(callback: Callback<MediaLibraryAvailability>): void--><!--Device-PhotoAccessHelper-onMediaLibraryAvailability(callback: Callback<MediaLibraryAvailability>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;MediaLibraryAvailability&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [23800151](../errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## onSinglePhotoAlbumChange

```TypeScript
onSinglePhotoAlbumChange(album: Album, callback: Callback<AlbumChangeInfos>): void
```

Registers a listener for changes of a single common asset. This API uses an asynchronous callback to return the result.

**Since:** 23

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAccessHelper-onSinglePhotoAlbumChange(album: Album, callback: Callback<AlbumChangeInfos>): void--><!--Device-PhotoAccessHelper-onSinglePhotoAlbumChange(album: Album, callback: Callback<AlbumChangeInfos>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| album | [Album](arkts-medialibrary-sendablephotoaccesshelper-album-i.md) | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AlbumChangeInfos&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [23800151](../errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## onSinglePhotoChange

```TypeScript
onSinglePhotoChange(asset: PhotoAsset, callback: Callback<PhotoAssetChangeInfos>): void
```

Registers a listener for changes of a single common asset. This API uses an asynchronous callback to return the result.

**Since:** 23

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAccessHelper-onSinglePhotoChange(asset: PhotoAsset, callback: Callback<PhotoAssetChangeInfos>): void--><!--Device-PhotoAccessHelper-onSinglePhotoChange(asset: PhotoAsset, callback: Callback<PhotoAssetChangeInfos>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| asset | [PhotoAsset](arkts-medialibrary-sendablephotoaccesshelper-photoasset-i.md) | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;PhotoAssetChangeInfos&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [23800151](../errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## registerChange

```TypeScript
registerChange(uri: string, forChildUris: boolean, callback: Callback<ChangeData>): void
```

Registers listening for the specified URI. This API uses a callback to return the result.

**Since:** 10

<!--Device-PhotoAccessHelper-registerChange(uri: string, forChildUris: boolean, callback: Callback<ChangeData>): void--><!--Device-PhotoAccessHelper-registerChange(uri: string, forChildUris: boolean, callback: Callback<ChangeData>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| forChildUris | boolean | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ChangeData&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 13900012 |

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

Releases the **PhotoAccessHelper** instance. This API uses an asynchronous callback to return the result.

Call this API when the APIs of the PhotoAccessHelper instance are no longer used.

**Since:** 10

<!--Device-PhotoAccessHelper-release(callback: AsyncCallback<void>): void--><!--Device-PhotoAccessHelper-release(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 14000011 |

## release

```TypeScript
release(): Promise<void>
```

Releases the **PhotoAccessHelper** instance. This API uses a promise to return the result.

Call this API when the APIs of the PhotoAccessHelper instance are no longer used.

**Since:** 10

<!--Device-PhotoAccessHelper-release(): Promise<void>--><!--Device-PhotoAccessHelper-release(): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 14000011 |

## requestPhotoUrisReadPermission

```TypeScript
requestPhotoUrisReadPermission(srcFileUris: Array<string>): Promise<Array<string>>
```

&lt;!--RP1--&gt;&lt;!--RP1End--&gt;Grants the read permission for unauthorized URIs, returning a list of URIs that have been created and granted the permission.

**Since:** 14

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-PhotoAccessHelper-requestPhotoUrisReadPermission(srcFileUris: Array<string>): Promise<Array<string>>--><!--Device-PhotoAccessHelper-requestPhotoUrisReadPermission(srcFileUris: Array<string>): Promise<Array<string>>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| srcFileUris | Array&lt;string&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;string&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 14000011 |

## requestPhotoUrisReadPermissionEx

```TypeScript
requestPhotoUrisReadPermissionEx(srcFileUris: Array<string>): Promise<RequestReadPermissionResult>
```

Grants the read permission for unauthorized URIs. This API uses a promise to return the authorization result.

It contains the list of URIs that have been created and granted the save permission and the list of invalid URIs.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-PhotoAccessHelper-requestPhotoUrisReadPermissionEx(srcFileUris: Array<string>): Promise<RequestReadPermissionResult>--><!--Device-PhotoAccessHelper-requestPhotoUrisReadPermissionEx(srcFileUris: Array<string>): Promise<RequestReadPermissionResult>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| srcFileUris | Array&lt;string&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;RequestReadPermissionResult&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-system-internal-error) |

## setAssetCompatibleCapability

```TypeScript
setAssetCompatibleCapability(capability: AssetCompatibleCapability): Promise<void>
```

Sets the asset compatibility capability. The system performs compatibility processing on special assets (such as high-resolution assets). If you want to obtain the original assets, you need to register the compatibility capability with the system.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoAccessHelper-setAssetCompatibleCapability(capability: AssetCompatibleCapability): Promise<void>--><!--Device-PhotoAccessHelper-setAssetCompatibleCapability(capability: AssetCompatibleCapability): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| capability | [AssetCompatibleCapability](arkts-medialibrary-photoaccesshelper-assetcompatiblecapability-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-system-internal-error) |
| [23800151](../errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## showAssetsCreationDialog

```TypeScript
showAssetsCreationDialog(srcFileUris: Array<string>, photoCreationConfigs: Array<PhotoCreationConfig>): Promise<Array<string>>
```

Displays a dialog box for the user to confirm whether to save the images or videos. If the user agrees to save the images or videos, this API returns a list of URIs that have been created and granted save permissions (this list is permanent), and the application can use these URIs to write the images or videos. If the user declines to save the images or videos, this API returns an empty list.

The dialog box must display the application name, but this cannot be directly obtained. Therefore, before calling this API, ensure that the **label** and **icon** items are configured in the **abilities** tag in the   
[module.json5 configuration file](../../../quick-start/module-configuration-file.md). Note that the icon is not affected by the **icon** item in the **abilities** tag and cannot be modified.

> **NOTE：**
> 
> If the passed URI is a sandbox path, images or videos can be saved but cannot be previewed.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PhotoAccessHelper-showAssetsCreationDialog(srcFileUris: Array<string>, photoCreationConfigs: Array<PhotoCreationConfig>): Promise<Array<string>>--><!--Device-PhotoAccessHelper-showAssetsCreationDialog(srcFileUris: Array<string>, photoCreationConfigs: Array<PhotoCreationConfig>): Promise<Array<string>>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| srcFileUris | Array&lt;string&gt; | Yes |
| photoCreationConfigs | Array&lt;PhotoCreationConfig&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;string&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 14000011 |

## showAssetsCreationDialogEx

```TypeScript
showAssetsCreationDialogEx(srcFileUris: Array<string>, creationSettings: Array<CreationSetting>): Promise<Array<string>>
```

Displays a dialog box for the user to confirm whether to save the images or videos. This API uses a promise to return the result.

> **NOTE：**
> 
> - If the user agrees, the list of created URIs with the save permission granted is returned. The list is
> permanently valid and supports image or video writing. If the user rejects, an empty list is returned.
> 
> - The application name and icon need to be displayed in the dialog box. The name and icon need to be configured
> in the **label** and **icon** items in the **abilities** tag of the
> [module.json5 configuration file](../../../quick-start/module-configuration-file.md).
> 
> - When the passed URI is a sandbox path, images or videos can be saved properly, but the preview is not
> displayed.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-PhotoAccessHelper-showAssetsCreationDialogEx(srcFileUris: Array<string>, creationSettings: Array<CreationSetting>): Promise<Array<string>>--><!--Device-PhotoAccessHelper-showAssetsCreationDialogEx(srcFileUris: Array<string>, creationSettings: Array<CreationSetting>): Promise<Array<string>>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| srcFileUris | Array&lt;string&gt; | Yes |
| creationSettings | Array&lt;CreationSetting&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;string&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-system-internal-error) |

## showSingleAssetCreationDialogEx

```TypeScript
showSingleAssetCreationDialogEx(srcFileUri: string, creationSetting: CreationSetting, isImageFullyDisplayed: boolean): Promise<string>
```

Displays a dialog box for the user to confirm whether to save an image or video. This API uses a promise to return the result.

> **NOTE：**
> 
> - If the user agrees to save the images or videos, this API returns a URI that has been created and granted
> with the save permission (this URI is permanent), and the application can use this URI to write the image or
> video. If the user declines to save the image or video, this API returns an empty string.
> 
> - The dialog box must display the application name, but this cannot be directly obtained. Therefore, before
> calling this API, ensure that the **label** and **icon** items are configured in the **abilities** tag in the
> [module.json5 configuration file](../../../quick-start/module-configuration-file.md). Note that the icon is
> not affected by the **icon** item in the **abilities** tag and cannot be modified.
> 
> - If the passed URI is a sandbox path, images or videos can be saved but cannot be previewed.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-PhotoAccessHelper-showSingleAssetCreationDialogEx(srcFileUri: string, creationSetting: CreationSetting, isImageFullyDisplayed: boolean): Promise<string>--><!--Device-PhotoAccessHelper-showSingleAssetCreationDialogEx(srcFileUri: string, creationSetting: CreationSetting, isImageFullyDisplayed: boolean): Promise<string>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| srcFileUri | string | Yes |
| creationSetting | [CreationSetting](arkts-medialibrary-photoaccesshelper-creationsetting-i.md) | Yes |
| isImageFullyDisplayed | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;string&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-system-internal-error) |

## unRegisterChange

```TypeScript
unRegisterChange(uri: string, callback?: Callback<ChangeData>): void
```

Unregisters listening for the specified URI. Multiple callbacks can be registered for a URI for listening. You can use this API to unregister the listening of the specified callbacks or all callbacks.

**Since:** 10

<!--Device-PhotoAccessHelper-unRegisterChange(uri: string, callback?: Callback<ChangeData>): void--><!--Device-PhotoAccessHelper-unRegisterChange(uri: string, callback?: Callback<ChangeData>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ChangeData&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 13900012 |
