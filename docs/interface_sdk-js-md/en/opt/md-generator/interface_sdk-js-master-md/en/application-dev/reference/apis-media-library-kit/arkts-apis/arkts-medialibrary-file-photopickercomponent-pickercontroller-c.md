# PickerController

Defines an instance used to send data to the **PhotoPickerComponent**.

**Since:** 12

**Decorator:** @Observed

<!--Device-unnamed-export declare class PickerController--><!--Device-unnamed-export declare class PickerController-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
import { MaxCountType, PreselectedInfo, BaseItemInfo, ItemInfo, AnimatorParams, SelectMode, PhotoBrowserUIElement, ItemType, PinchGridSwitchedCallback, SingleLineConfig, ClickResult, ClickType, UpdatablePickerConfigs, DataType, VideoPlayerState, ItemDisplayRatio, ScrollStopAtStartCallback, ScrollStopAtEndCallback, PickerOrientation, videoPlayStateChangedCallback, PhotoBrowserChangeStartCallback, MovingPhotoBadgeStateChangedCallback, ErrorCallback, PickerOptions, ItemsDeletedCallback, PhotoBrowserRange, SaveMode, MaxSelected, PickerController, PickerError, PhotoPickerComponent, ExceedMaxSelectedCallback, ReminderMode, ItemClickedNotifyCallback, PickerColorMode, BadgeConfig, BadgeType, PhotoBrowserInfo, CurrentAlbumDeletedCallback } from 'kits/@kit.MediaLibraryKit';
```

## addData

```TypeScript
addData(dataType: DataType, data: Object): void
```

Sends additional configuration data to the **PhotoPickerComponent**. The [DataType](arkts-medialibrary-file-photopickercomponent-datatype-e.md) parameter identifies the type of data to send. In versions earlier than API version 23, only the **SET_BADGE_CONFIGS** type is supported.

**Since:** 21

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-PickerController-addData(dataType: DataType, data: Object): void--><!--Device-PickerController-addData(dataType: DataType, data: Object): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dataType | [DataType](arkts-medialibrary-file-photopickercomponent-datatype-e.md) | Yes |
| data | Object | Yes |

## completed

```TypeScript
completed(): Promise<CompletedResult>
```

This API is used by an application to obtain the complete data after a selection operation is completed on the Picker page. The data can be used to restore the scene when the Picker is started next time.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-PickerController-completed(): Promise<CompletedResult>--><!--Device-PickerController-completed(): Promise<CompletedResult>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;CompletedResult&gt; |

## deleteData

```TypeScript
deleteData(dataType: DataType, data: Object): void
```

Sends removal configuration data to the **PhotoPickerComponent**. The [DataType](arkts-medialibrary-file-photopickercomponent-datatype-e.md) parameter identifies the type of data to send, and only the **SET_BADGE_CONFIGS** type is supported currently.

**Since:** 21

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-PickerController-deleteData(dataType: DataType, data: Object): void--><!--Device-PickerController-deleteData(dataType: DataType, data: Object): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dataType | [DataType](arkts-medialibrary-file-photopickercomponent-datatype-e.md) | Yes |
| data | Object | Yes |

## exitPhotoBrowser

```TypeScript
exitPhotoBrowser(): void
```

Exits the photo browser page.

**Since:** 13

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-PickerController-exitPhotoBrowser(): void--><!--Device-PickerController-exitPhotoBrowser(): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## replacePhotoPickerPreview

```TypeScript
replacePhotoPickerPreview(originalUri: string, newUri: string, callback: AsyncCallback<void>): void
```

Replaces the image selected by the user in the **PhotoPickerComponent** with the image edited by the application.

**Since:** 15

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-PickerController-replacePhotoPickerPreview(originalUri: string, newUri: string, callback: AsyncCallback<void>): void--><!--Device-PickerController-replacePhotoPickerPreview(originalUri: string, newUri: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| originalUri | string | Yes |
| newUri | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## saveTrustedPhotoAssets

```TypeScript
saveTrustedPhotoAssets(trustedUris: Array<string>, callback: AsyncCallback<Array<string>>,
    configs?: Array<photoAccessHelper.PhotoCreationConfig>, saveMode?: SaveMode): void
```

Saves files in a URI list. Generally, this API is used together with  
[replacePhotoPickerPreview](arkts-medialibrary-file-photopickercomponent-pickercontroller-c.md#replacephotopickerpreview) to save the new images or videos in the application sandbox path to Gallery.

**Since:** 15

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-PickerController-saveTrustedPhotoAssets(trustedUris: Array<string>, callback: AsyncCallback<Array<string>>,    configs?: Array<photoAccessHelper.PhotoCreationConfig>, saveMode?: SaveMode): void--><!--Device-PickerController-saveTrustedPhotoAssets(trustedUris: Array<string>, callback: AsyncCallback<Array<string>>,    configs?: Array<photoAccessHelper.PhotoCreationConfig>, saveMode?: SaveMode): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| trustedUris | Array&lt;string&gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | Yes |
| configs | Array&lt;photoAccessHelper.PhotoCreationConfig&gt; | No |
| saveMode | [SaveMode](arkts-medialibrary-file-photopickercomponent-savemode-e.md) | No |

## saveTrustedPhotoAssetsEx

```TypeScript
saveTrustedPhotoAssetsEx(trustedUris: Array<string>,settings?: Array<photoAccessHelper.CreationSetting>,
    saveMode?: SaveMode): Promise<Array<string>>
```

Saves files in a URI list. This API uses a promise to return the result.

> **NOTE：**
> 
> This API is usually used together with
> [replacePhotoPickerPreview](arkts-medialibrary-file-photopickercomponent-pickercontroller-c.md#replacephotopickerpreview) to save the new images or videos in
> the application sandbox path to Gallery.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-PickerController-saveTrustedPhotoAssetsEx(trustedUris: Array<string>,settings?: Array<photoAccessHelper.CreationSetting>,    saveMode?: SaveMode): Promise<Array<string>>--><!--Device-PickerController-saveTrustedPhotoAssetsEx(trustedUris: Array<string>,settings?: Array<photoAccessHelper.CreationSetting>,    saveMode?: SaveMode): Promise<Array<string>>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| trustedUris | Array&lt;string&gt; | Yes |
| settings | Array&lt;photoAccessHelper.CreationSetting&gt; | No |
| saveMode | [SaveMode](arkts-medialibrary-file-photopickercomponent-savemode-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;string&gt;&gt; |

## setData

```TypeScript
setData(dataType: DataType, data: Object): void
```

Sends data of the specified type to the **PhotoPickerComponent**.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PickerController-setData(dataType: DataType, data: Object): void--><!--Device-PickerController-setData(dataType: DataType, data: Object): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dataType | [DataType](arkts-medialibrary-file-photopickercomponent-datatype-e.md) | Yes |
| data | Object | Yes |

## setMaxSelected

```TypeScript
setMaxSelected(maxSelected: MaxSelected): void
```

Sets the maximum number of images, videos, or images and videos that can be selected in real time.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PickerController-setMaxSelected(maxSelected: MaxSelected): void--><!--Device-PickerController-setMaxSelected(maxSelected: MaxSelected): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| maxSelected | [MaxSelected](arkts-medialibrary-file-photopickercomponent-maxselected-c.md) | Yes |

## setMovingPhotoState

```TypeScript
setMovingPhotoState(movingPhotoState: photoAccessHelper.MovingPhotoBadgeStateType): Promise<void>
```

Sets the state of the moving photo on the photo browser page. This API uses a promise to return the result.

This parameter takes effect only on the photo browser page. **NOT_MOVING_PHOTO** cannot be set.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-PickerController-setMovingPhotoState(movingPhotoState: photoAccessHelper.MovingPhotoBadgeStateType): Promise<void>--><!--Device-PickerController-setMovingPhotoState(movingPhotoState: photoAccessHelper.MovingPhotoBadgeStateType): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| movingPhotoState | photoAccessHelper.MovingPhotoBadgeStateType | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800202](../errorcode-medialibrary.md#23800202-invalid-scenario-call) |
| [23800151](../errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## setPhotoBrowserItem

```TypeScript
setPhotoBrowserItem(uri: string, photoBrowserRange?: PhotoBrowserRange): void
```

Switches from the **PhotoPickerComponent** to the photo browser page or from the photo browser page to the image to be viewed.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PickerController-setPhotoBrowserItem(uri: string, photoBrowserRange?: PhotoBrowserRange): void--><!--Device-PickerController-setPhotoBrowserItem(uri: string, photoBrowserRange?: PhotoBrowserRange): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| photoBrowserRange | [PhotoBrowserRange](arkts-medialibrary-file-photopickercomponent-photobrowserrange-e.md) | No |

## setPhotoBrowserUIElementVisibility

```TypeScript
setPhotoBrowserUIElementVisibility(elements: Array<PhotoBrowserUIElement>, isVisible: boolean): void
```

Sets whether other UI elements are visible on the photo browser page. By default, other UI elements are visible.

**Since:** 13

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-PickerController-setPhotoBrowserUIElementVisibility(elements: Array<PhotoBrowserUIElement>, isVisible: boolean): void--><!--Device-PickerController-setPhotoBrowserUIElementVisibility(elements: Array<PhotoBrowserUIElement>, isVisible: boolean): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| elements | Array&lt;PhotoBrowserUIElement&gt; | Yes |
| isVisible | boolean | Yes |

## updatePickerOptions

```TypeScript
updatePickerOptions(updateConfig: UpdatablePickerConfigs): Promise<void>
```

Updates the attributes of the **PhotoPickerComponent**. This API uses a promise to return the result.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-PickerController-updatePickerOptions(updateConfig: UpdatablePickerConfigs): Promise<void>--><!--Device-PickerController-updatePickerOptions(updateConfig: UpdatablePickerConfigs): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| updateConfig | [UpdatablePickerConfigs](arkts-medialibrary-file-photopickercomponent-updatablepickerconfigs-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |
