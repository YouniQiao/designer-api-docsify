# PhotoViewPicker

PhotoViewPicker provides APIs for the user to select images and videos. Before using the APIs of PhotoViewPicker, you need to create a PhotoViewPicker instance.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 26.0.0.

<!--Device-photoAccessHelper-class PhotoViewPicker--><!--Device-photoAccessHelper-class PhotoViewPicker-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## select

```TypeScript
select(option?: PhotoSelectOptions): Promise<PhotoSelectResult>
```

Starts a **photoPicker** page for the user to select one or more images or videos. This API uses a promise to return the result. You can pass in **PhotoSelectOptions** to specify the type and maximum number of the files to select. A **PhotoSelectResult** object is returned.

> **NOTE：**
> 
> **photoUris** in the PhotoSelectResult object returned by this API has permanent authorization and can be used
> only by calling
> [photoAccessHelper.getAssets](arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md#getassets)
> . For details, see
> [Using a Media File URI](../../../file-management/user-file-uri-intro.md#using-a-media-file-uri).

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PhotoViewPicker-select(option?: PhotoSelectOptions): Promise<PhotoSelectResult>--><!--Device-PhotoViewPicker-select(option?: PhotoSelectOptions): Promise<PhotoSelectResult>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| option | [PhotoSelectOptions](../../apis-core-file-kit/arkts-apis/arkts-corefile-picker-photoselectoptions-c.md) | No | Options for selecting files. If this parameter is not specified, up to 5 0 images and videos are selected by default. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;PhotoSelectResult&gt; | Promise used to return information about the images or videos selected. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| [23800151](../errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) | Scene parameters validate failed, possible causes: &lt;br&gt;1. An illegal enumeration value was passed to PhotoSelectOptions.globalMovingPhotoState. Only MOVING_PHOTO_ENABLED and MOVING_PHOTO_DISABLED are supported for configuration; &lt;br&gt;2. An illegal enumeration value was passed to PhotoSelectOptions.assetCompatibleAbility.<br>**Applicable version:** 12 and later |
| 13900042 | Unknown error |

## select

```TypeScript
select(option: PhotoSelectOptions, callback: AsyncCallback<PhotoSelectResult>): void
```

Starts a **photoPicker** page for the user to select one or more images or videos. This API uses an asynchronous callback to return the result. You can pass in **PhotoSelectOptions** to specify the media file type and the maximum number of files to select.

> **NOTE：**
> 
> **photoUris** in the PhotoSelectResult object returned by this API has permanent authorization and can be used
> only by calling
> [photoAccessHelper.getAssets](arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md#getassets)
> . For details, see
> [Using a Media File URI](../../../file-management/user-file-uri-intro.md#using-a-media-file-uri).

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PhotoViewPicker-select(option: PhotoSelectOptions, callback: AsyncCallback<PhotoSelectResult>): void--><!--Device-PhotoViewPicker-select(option: PhotoSelectOptions, callback: AsyncCallback<PhotoSelectResult>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| option | [PhotoSelectOptions](../../apis-core-file-kit/arkts-apis/arkts-corefile-picker-photoselectoptions-c.md) | Yes | Options for selecting images or videos. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;PhotoSelectResult&gt; | Yes | Callback used to return information about the images or videos selected. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| [23800151](../errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) | Scene parameters validate failed, possible causes: &lt;br&gt;1. An illegal enumeration value was passed to PhotoSelectOptions.globalMovingPhotoState. Only MOVING_PHOTO_ENABLED and MOVING_PHOTO_DISABLED are supported for configuration;<br>**Applicable version:** 12 and later |
| 13900042 | Unknown error |

## select

```TypeScript
select(callback: AsyncCallback<PhotoSelectResult>): void
```

Starts a **photoPicker** page for the user to select one or more images or videos. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> **photoUris** in the PhotoSelectResult object returned by this API has permanent authorization and can be used
> only by calling
> [photoAccessHelper.getAssets](arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md#getassets)
> . For details, see
> [Using a Media File URI](../../../file-management/user-file-uri-intro.md#using-a-media-file-uri).

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PhotoViewPicker-select(callback: AsyncCallback<PhotoSelectResult>): void--><!--Device-PhotoViewPicker-select(callback: AsyncCallback<PhotoSelectResult>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;PhotoSelectResult&gt; | Yes | Callback used to return information about the images or videos selected. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |
| 13900042 | Unknown error |

