# PickerController

Defines an instance used to send data to the **PhotoPickerComponent**.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

<!--Device-unnamed-export declare class PickerController--><!--Device-unnamed-export declare class PickerController-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
import { MaxCountType, PreselectedInfo, BaseItemInfo, ItemInfo, AnimatorParams, SelectMode, PhotoBrowserUIElement, ItemType, PinchGridSwitchedCallback, SingleLineConfig, ClickResult, ClickType, UpdatablePickerConfigs, DataType, VideoPlayerState, ItemDisplayRatio, ScrollStopAtStartCallback, ScrollStopAtEndCallback, PickerOrientation, videoPlayStateChangedCallback, PhotoBrowserChangeStartCallback, MovingPhotoBadgeStateChangedCallback, ErrorCallback, PickerOptions, ItemsDeletedCallback, PhotoBrowserRange, SaveMode, MaxSelected, PickerController, PickerError, PhotoPickerComponent, ExceedMaxSelectedCallback, ReminderMode, ItemClickedNotifyCallback, PickerColorMode, BadgeConfig, BadgeType, PhotoBrowserInfo, CurrentAlbumDeletedCallback } from '@kit.MediaLibraryKit';
```

## addData

```TypeScript
addData(dataType: DataType, data: Object): void
```

Sends additional configuration data to the **PhotoPickerComponent**. The [DataType](arkts-medialibrary-file-photopickercomponent-datatype-e.md#DataType) parameter identifies the type of data to send. In versions earlier than API version 23, only the **SET_BADGE_CONFIGS** type is supported.

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-PickerController-addData(dataType: DataType, data: Object): void--><!--Device-PickerController-addData(dataType: DataType, data: Object): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dataType | [DataType](arkts-medialibrary-file-photopickercomponent-datatype-e.md) | Yes | Type of additional configuration data to send. |
| data | Object | Yes | Additional configuration data to send. |

## completed

```TypeScript
completed(): Promise<CompletedResult>
```

This API is used by an application to obtain the complete data after a selection operation is completed on the Picker page. The data can be used to restore the scene when the Picker is started next time.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-PickerController-completed(): Promise<CompletedResult>--><!--Device-PickerController-completed(): Promise<CompletedResult>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[CompletedResult](arkts-medialibrary-file-photopickercomponent-completedresult-c.md)&gt; | Promise used to return the information about the restored scene. |

## deleteData

```TypeScript
deleteData(dataType: DataType, data: Object): void
```

Sends removal configuration data to the **PhotoPickerComponent**. The [DataType](arkts-medialibrary-file-photopickercomponent-datatype-e.md#DataType) parameter identifies the type of data to send, and only the **SET_BADGE_CONFIGS** type is supported currently.

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-PickerController-deleteData(dataType: DataType, data: Object): void--><!--Device-PickerController-deleteData(dataType: DataType, data: Object): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dataType | [DataType](arkts-medialibrary-file-photopickercomponent-datatype-e.md) | Yes | Type of removal configuration data to send. |
| data | Object | Yes | Removal configuration data to send. |

## exitPhotoBrowser

```TypeScript
exitPhotoBrowser(): void
```

Exits the photo browser page.

**Since:** 13

**ArkTS mode:** ArkTS-Dyn only, since version 13.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-PickerController-exitPhotoBrowser(): void--><!--Device-PickerController-exitPhotoBrowser(): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## replacePhotoPickerPreview

```TypeScript
replacePhotoPickerPreview(originalUri: string, newUri: string, callback: AsyncCallback<void>): void
```

Replaces the image selected by the user in the **PhotoPickerComponent** with the image edited by the application.

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-PickerController-replacePhotoPickerPreview(originalUri: string, newUri: string, callback: AsyncCallback<void>): void--><!--Device-PickerController-replacePhotoPickerPreview(originalUri: string, newUri: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| originalUri | string | Yes | URI of the original image, which will be replaced. |
| newUri | string | Yes | URI of the new image. The new image is temporarily stored in the application sandbox path. Therefore, this URI specifies a directory in the application sandbox path. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback invoked when image replacement is complete. |

## saveTrustedPhotoAssets

```TypeScript
saveTrustedPhotoAssets(trustedUris: Array<string>, callback: AsyncCallback<Array<string>>,
    configs?: Array<photoAccessHelper.PhotoCreationConfig>, saveMode?: SaveMode): void
```

Saves files in a URI list. Generally, this API is used together with [replacePhotoPickerPreview](#replacePhotoPickerPreview) to save the new images or videos in the application sandbox path to Gallery.

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-PickerController-saveTrustedPhotoAssets(trustedUris: Array<string>, callback: AsyncCallback<Array<string>>,    configs?: Array<photoAccessHelper.PhotoCreationConfig>, saveMode?: SaveMode): void--><!--Device-PickerController-saveTrustedPhotoAssets(trustedUris: Array<string>, callback: AsyncCallback<Array<string>>,    configs?: Array<photoAccessHelper.PhotoCreationConfig>, saveMode?: SaveMode): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| trustedUris | Array&lt;string&gt; | Yes | URIs of the images or videos in the application sandbox path. Generally, **trustedUris** comes from **newUri** of new images generated by [replacePhotoPickerPreview](#replacePhotoPickerPreview). |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | Yes | URIs of the new files in Gallery. |
| configs | Array&lt;photoAccessHelper.PhotoCreationConfig&gt; | No | Configuration parameters corresponding to the original files. &lt;br&gt;**NOTE：**&lt;br&gt;1. If a **subtype** option is passed, the configuration does not take effect. Only **DEFAULT** images can be saved. &lt;br&gt;By default, the values of **title**, **fileNameExtension**, and **photoType** of **mediaItem** corresponding to **trustedUris** are used, and the value of **subtype** is fixed to **DEFAULT**. &lt;br&gt;2. This parameter does not take effect when [SaveMode](arkts-medialibrary-file-photopickercomponent-savemode-e.md#SaveMode) is set to **OVERWRITE**. |
| saveMode | [SaveMode](arkts-medialibrary-file-photopickercomponent-savemode-e.md) | No | Mode for saving the files. &lt;br&gt;By default, the **SAVE_AS** mode is used to save the files as new files. |

## saveTrustedPhotoAssetsEx

```TypeScript
saveTrustedPhotoAssetsEx(trustedUris: Array<string>,settings?: Array<photoAccessHelper.CreationSetting>,
    saveMode?: SaveMode): Promise<Array<string>>
```

Saves files in a URI list. This API uses a promise to return the result. > **NOTE：**> > This API is usually used together with > [replacePhotoPickerPreview](#replacePhotoPickerPreview) to save the new images or videos in > the application sandbox path to Gallery.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-PickerController-saveTrustedPhotoAssetsEx(trustedUris: Array<string>,settings?: Array<photoAccessHelper.CreationSetting>,    saveMode?: SaveMode): Promise<Array<string>>--><!--Device-PickerController-saveTrustedPhotoAssetsEx(trustedUris: Array<string>,settings?: Array<photoAccessHelper.CreationSetting>,    saveMode?: SaveMode): Promise<Array<string>>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| trustedUris | Array&lt;string&gt; | Yes | URIs of the images or videos in the application sandbox path. &lt;br&gt;**trustedUris** is usually the **newUri** of the images or videos in the application sandbox path that are successfully replaced by [replacePhotoPickerPreview](#replacePhotoPickerPreview). |
| settings | Array&lt;photoAccessHelper.CreationSetting&gt; | No | Configuration parameters corresponding to the original files. &lt;br&gt;By default, the **title**, **fileNameExtension**, and **photoType** values of **mediaItem** corresponding to **trustedUris** are used. |
| saveMode | [SaveMode](arkts-medialibrary-file-photopickercomponent-savemode-e.md) | No | Mode for saving images or videos. &lt;br&gt;By default, the **SAVE_AS** mode is used to save the files as new files. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;string&gt;&gt; | Promise used to return the URI of the new asset. |

## setData

```TypeScript
setData(dataType: DataType, data: Object): void
```

Sends data of the specified type to the **PhotoPickerComponent**.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PickerController-setData(dataType: DataType, data: Object): void--><!--Device-PickerController-setData(dataType: DataType, data: Object): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dataType | [DataType](arkts-medialibrary-file-photopickercomponent-datatype-e.md) | Yes | Type of the data to send. |
| data | Object | Yes | Data to send. |

## setMaxSelected

```TypeScript
setMaxSelected(maxSelected: MaxSelected): void
```

Sets the maximum number of images, videos, or images and videos that can be selected in real time.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PickerController-setMaxSelected(maxSelected: MaxSelected): void--><!--Device-PickerController-setMaxSelected(maxSelected: MaxSelected): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| maxSelected | [MaxSelected](arkts-medialibrary-file-photopickercomponent-maxselected-c.md) | Yes | Maximum number of media assets that can be selected at a time. |

## setMovingPhotoState

```TypeScript
setMovingPhotoState(movingPhotoState: photoAccessHelper.MovingPhotoBadgeStateType): Promise<void>
```

Sets the state of the moving photo on the photo browser page. This API uses a promise to return the result. This parameter takes effect only on the photo browser page. **NOT_MOVING_PHOTO** cannot be set.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-PickerController-setMovingPhotoState(movingPhotoState: photoAccessHelper.MovingPhotoBadgeStateType): Promise<void>--><!--Device-PickerController-setMovingPhotoState(movingPhotoState: photoAccessHelper.MovingPhotoBadgeStateType): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| movingPhotoState | photoAccessHelper.MovingPhotoBadgeStateType | Yes | State of the moving photo on the photo browser page. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [23800202](../errorcode-medialibrary.md#23800202-invalid-scenario-call) | Invalid call context. Possible causes: 1. The API is called outside the photo browsing scenario. 2. The API is called when isMovingPhotoBadgeShown is already set to true. |
| [23800151](../errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) | Scene parameters validate failed, possible causes: 1. An invalid enumeration value was passed. Only MOVING_PHOTO_ENABLED and MOVING_PHOTO_DISABLED are supported for configuration; |

## setPhotoBrowserItem

```TypeScript
setPhotoBrowserItem(uri: string, photoBrowserRange?: PhotoBrowserRange): void
```

Switches from the **PhotoPickerComponent** to the photo browser page or from the photo browser page to the image to be viewed.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PickerController-setPhotoBrowserItem(uri: string, photoBrowserRange?: PhotoBrowserRange): void--><!--Device-PickerController-setPhotoBrowserItem(uri: string, photoBrowserRange?: PhotoBrowserRange): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | URI of the image to view. Only the images selected by the user are supported. |
| photoBrowserRange | [PhotoBrowserRange](arkts-medialibrary-file-photopickercomponent-photobrowserrange-e.md) | No | View range on the photo browser page. The value can be **ALL** or **SELECTED_ONLY**. The default value is **ALL**, which means to view all images and videos. |

## setPhotoBrowserUIElementVisibility

```TypeScript
setPhotoBrowserUIElementVisibility(elements: Array<PhotoBrowserUIElement>, isVisible: boolean): void
```

Sets whether other UI elements are visible on the photo browser page. By default, other UI elements are visible.

**Since:** 13

**ArkTS mode:** ArkTS-Dyn only, since version 13.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-PickerController-setPhotoBrowserUIElementVisibility(elements: Array<PhotoBrowserUIElement>, isVisible: boolean): void--><!--Device-PickerController-setPhotoBrowserUIElementVisibility(elements: Array<PhotoBrowserUIElement>, isVisible: boolean): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| elements | Array&lt;[PhotoBrowserUIElement](arkts-medialibrary-file-photopickercomponent-photobrowseruielement-e.md)&gt; | Yes | Other UI elements on the photo browser page. |
| isVisible | boolean | Yes | Whether the specified elements are visible. **true**: visible; **false**: not visible. The default value is **false**. |

## updatePickerOptions

```TypeScript
updatePickerOptions(updateConfig: UpdatablePickerConfigs): Promise<void>
```

Updates the attributes of the **PhotoPickerComponent**. This API uses a promise to return the result.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-PickerController-updatePickerOptions(updateConfig: UpdatablePickerConfigs): Promise<void>--><!--Device-PickerController-updatePickerOptions(updateConfig: UpdatablePickerConfigs): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| updateConfig | [UpdatablePickerConfigs](arkts-medialibrary-file-photopickercomponent-updatablepickerconfigs-c.md) | Yes | New attributes, which are a subset of [PickerOptions](arkts-medialibrary-file-photopickercomponent-pickeroptions-c.md#PickerOptions). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

