# PickerController

The class for PickerController

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**装饰器类型：** @Observed

<!--Device-unnamed-export declare class PickerController--><!--Device-unnamed-export declare class PickerController-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { MaxCountType, PreselectedInfo, BaseItemInfo, ItemInfo, AnimatorParams, SelectMode, PhotoBrowserUIElement, ItemType, PinchGridSwitchedCallback, SingleLineConfig, ClickResult, ClickType, UpdatablePickerConfigs, DataType, VideoPlayerState, ItemDisplayRatio, ScrollStopAtStartCallback, ScrollStopAtEndCallback, PickerOrientation, videoPlayStateChangedCallback, PhotoBrowserChangeStartCallback, MovingPhotoBadgeStateChangedCallback, ErrorCallback, PickerOptions, ItemsDeletedCallback, PhotoBrowserRange, SaveMode, MaxSelected, PickerController, PickerError, PhotoPickerComponent, ExceedMaxSelectedCallback, ReminderMode, ItemClickedNotifyCallback, PickerColorMode, BadgeConfig, BadgeType, PhotoBrowserInfo, CurrentAlbumDeletedCallback } from 'kits/@kit.MediaLibraryKit';
```

## addData

```TypeScript
public addData(dataType: DataType, data: Object): void
```

Add data to picker component

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PickerController-public addData(dataType: DataType, data: Object): void--><!--Device-PickerController-public addData(dataType: DataType, data: Object): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataType | [DataType](arkts-medialibrary-file-photopickercomponent-datatype-e.md) | 是 | data type |
| data | Object | 是 | data |

## completed

```TypeScript
public completed(): Promise<CompletedResult>
```

Call this method to obtain the complete data after a selection operation has finished.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PickerController-public completed(): Promise<CompletedResult>--><!--Device-PickerController-public completed(): Promise<CompletedResult>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;CompletedResult&gt; | Promise&lt;CompletedResult&gt; |

## deleteData

```TypeScript
public deleteData(dataType: DataType, data: Object): void
```

Delete data to picker component

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PickerController-public deleteData(dataType: DataType, data: Object): void--><!--Device-PickerController-public deleteData(dataType: DataType, data: Object): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataType | [DataType](arkts-medialibrary-file-photopickercomponent-datatype-e.md) | 是 | data type |
| data | Object | 是 | data |

## exitPhotoBrowser

```TypeScript
public exitPhotoBrowser(): void
```

Exit photo browser.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PickerController-public exitPhotoBrowser(): void--><!--Device-PickerController-public exitPhotoBrowser(): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## replacePhotoPickerPreview

```TypeScript
public replacePhotoPickerPreview(originalUri: string, newUri: string, callback: AsyncCallback<void>): void
```

Display the photo after edit.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PickerController-public replacePhotoPickerPreview(originalUri: string, newUri: string, callback: AsyncCallback<void>): void--><!--Device-PickerController-public replacePhotoPickerPreview(originalUri: string, newUri: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| originalUri | string | 是 | Original uri |
| newUri | string | 是 | New uri after replacement |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | Returns void |

## saveTrustedPhotoAssets

```TypeScript
public saveTrustedPhotoAssets(trustedUris: string[], callback: AsyncCallback<string[]>,
    configs?: photoAccessHelper.PhotoCreationConfig[], saveMode?: SaveMode): void
```

Save the photo assets of uris.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PickerController-public saveTrustedPhotoAssets(trustedUris: string[], callback: AsyncCallback<string[]>,    configs?: photoAccessHelper.PhotoCreationConfig[], saveMode?: SaveMode): void--><!--Device-PickerController-public saveTrustedPhotoAssets(trustedUris: string[], callback: AsyncCallback<string[]>,    configs?: photoAccessHelper.PhotoCreationConfig[], saveMode?: SaveMode): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| trustedUris | string[] | 是 | Uris need to be saved |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string[]&gt; | 是 | Returns the uri list |
| configs | photoAccessHelper.PhotoCreationConfig[] | 否 | Photo asset creation configs |
| saveMode | [SaveMode](arkts-medialibrary-file-photopickercomponent-savemode-e.md) | 否 | Mode of save |

## setData

```TypeScript
public setData(dataType: DataType, data: Object): void
```

Set data to picker component

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PickerController-public setData(dataType: DataType, data: Object): void--><!--Device-PickerController-public setData(dataType: DataType, data: Object): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataType | [DataType](arkts-medialibrary-file-photopickercomponent-datatype-e.md) | 是 | data type |
| data | Object | 是 | data |

## setMaxSelected

```TypeScript
public setMaxSelected(maxSelected: MaxSelected): void
```

Set max select count to picker component, include max_total_count, max_photo_count and max_video_count.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PickerController-public setMaxSelected(maxSelected: MaxSelected): void--><!--Device-PickerController-public setMaxSelected(maxSelected: MaxSelected): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| maxSelected | [MaxSelected](arkts-medialibrary-file-photopickercomponent-maxselected-c.md) | 是 | max select count data |

## setPhotoBrowserItem

```TypeScript
public setPhotoBrowserItem(uri: string, photoBrowserRange?: PhotoBrowserRange): void
```

Set photo browser item to picker component.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PickerController-public setPhotoBrowserItem(uri: string, photoBrowserRange?: PhotoBrowserRange): void--><!--Device-PickerController-public setPhotoBrowserItem(uri: string, photoBrowserRange?: PhotoBrowserRange): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | specify image uri for photo browsing |
| photoBrowserRange | [PhotoBrowserRange](arkts-medialibrary-file-photopickercomponent-photobrowserrange-e.md) | 否 | photo browser slide range |

## setPhotoBrowserUIElementVisibility

```TypeScript
public setPhotoBrowserUIElementVisibility(elements: PhotoBrowserUIElement[], isVisible: boolean): void
```

Sets whether other elements on the photo browser page are visible.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PickerController-public setPhotoBrowserUIElementVisibility(elements: PhotoBrowserUIElement[], isVisible: boolean): void--><!--Device-PickerController-public setPhotoBrowserUIElementVisibility(elements: PhotoBrowserUIElement[], isVisible: boolean): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| elements | [PhotoBrowserUIElement](arkts-medialibrary-file-photopickercomponent-photobrowseruielement-e.md)[] | 是 | other elements on the photo browser page |
| isVisible | boolean | 是 | visible or not |

