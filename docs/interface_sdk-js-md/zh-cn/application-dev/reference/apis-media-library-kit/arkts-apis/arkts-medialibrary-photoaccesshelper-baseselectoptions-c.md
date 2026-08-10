# BaseSelectOptions

Defines the basic options for selecting media files from Gallery.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为26.0.0。

<!--Device-photoAccessHelper-export class BaseSelectOptions--><!--Device-photoAccessHelper-export class BaseSelectOptions-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## MIMEType

```TypeScript
MIMEType?: PhotoViewMIMETypes
```

Available media file types. **IMAGE_VIDEO_TYPE** is used by default.

**类型：** [PhotoViewMIMETypes](../../apis-core-file-kit/arkts-apis/arkts-corefile-picker-photoviewmimetypes-e.md)

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-BaseSelectOptions-MIMEType?: PhotoViewMIMETypes--><!--Device-BaseSelectOptions-MIMEType?: PhotoViewMIMETypes-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## assetCompatibleCapability

```TypeScript
assetCompatibleCapability?: AssetCompatibleCapability
```

Configuration for asset compatibility capabilities.

**类型：** [AssetCompatibleCapability](arkts-medialibrary-photoaccesshelper-assetcompatiblecapability-i.md)

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为24；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-BaseSelectOptions-assetCompatibleCapability?: AssetCompatibleCapability--><!--Device-BaseSelectOptions-assetCompatibleCapability?: AssetCompatibleCapability-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## assetFilter

```TypeScript
assetFilter?: Array<OperationItem>
```

Media asset filter, with a maximum length of 50 items. If the limit is exceeded, only the first 50 items are used.

**NOTE：**

1. When this filter is applied, other filters become invalid.2. When setting multiple conditions, enclose the filter conditions in parentheses to prevent conflicts with  internal filter items.

**类型：** Array&lt;OperationItem&gt;

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-BaseSelectOptions-assetFilter?: Array<OperationItem>--><!--Device-BaseSelectOptions-assetFilter?: Array<OperationItem>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## autoPlayScenes

```TypeScript
autoPlayScenes?: Array<AutoPlayScene>
```

Playback mode of the moving photo. The maximum array length is 2. If this limit is exceeded, the first two elements are used, and the extra ones are automatically ignored.

**类型：** Array&lt;AutoPlayScene&gt;

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-BaseSelectOptions-autoPlayScenes?: Array<AutoPlayScene>--><!--Device-BaseSelectOptions-autoPlayScenes?: Array<AutoPlayScene>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## combinedMediaTypeFilter

```TypeScript
combinedMediaTypeFilter?: Array<string>
```

A string array of filter criteria, supporting combinations of various types.

The string format is as follows: **photoType | photoSubType1,photoSubType2, ... | mimeType1,mimeType2, ...**

- The first part specifies a single **photoType**, which is fixed at **image** or **video**.  
- The second part lists 1 to *N* photoSubTypes, separated by commas, with an OR relationship. Currently, the   
maximum value of *N* is **1**. Options include **movingPhoto** or "*" (ignore).  
- The third part lists 1 to *N* mimeTypes, separated by commas, with an OR relationship. Currently, the maximum   
value of *N* is **10**. The format is similar to [MimeTypeFilter](arkts-medialibrary-photoaccesshelper-mimetypefilter-c.md).

Filters are combined using intersection logic.

The NOT logic is supported. To exclude types, use parentheses. Each string can have only one set.

If the filter string does not match the specifications, the result is empty.

Only the first three array elements are used; **MIMETypes** and **mimeTypeFilter** are ignored.

**类型：** Array&lt;string&gt;

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-BaseSelectOptions-combinedMediaTypeFilter?: Array<string>--><!--Device-BaseSelectOptions-combinedMediaTypeFilter?: Array<string>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## fileSizeFilter

```TypeScript
fileSizeFilter?: FileSizeFilter
```

Configuration for file size filtering.

When this parameter is set, only media files within the specified size range are displayed. You are advised to notify users that only images or videos of the specified size can be selected.

**类型：** [FileSizeFilter](arkts-medialibrary-photoaccesshelper-filesizefilter-c.md)

**起始版本：** 19

**ArkTS模式：** ArkTS-Dyn起始版本为19；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-BaseSelectOptions-fileSizeFilter?: FileSizeFilter--><!--Device-BaseSelectOptions-fileSizeFilter?: FileSizeFilter-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## globalMovingPhotoState

```TypeScript
globalMovingPhotoState?: MovingPhotoBadgeStateType
```

Global effect of the moving photo. Currently, only **MOVING_PHOTO_ENABLED** and **MOVING_PHOTO_DISABLED** are supported. The default value is **MOVING_PHOTO_ENABLED**.

**类型：** [MovingPhotoBadgeStateType](arkts-medialibrary-photoaccesshelper-movingphotobadgestatetype-e.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-BaseSelectOptions-globalMovingPhotoState?: MovingPhotoBadgeStateType--><!--Device-BaseSelectOptions-globalMovingPhotoState?: MovingPhotoBadgeStateType-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## gridPinchMode

```TypeScript
gridPinchMode?: GridPinchMode
```

Pinch mode of the grid in the picker.

**类型：** [GridPinchMode](arkts-medialibrary-photoaccesshelper-gridpinchmode-c.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-BaseSelectOptions-gridPinchMode?: GridPinchMode--><!--Device-BaseSelectOptions-gridPinchMode?: GridPinchMode-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## isMovingPhotoBadgeShown

```TypeScript
isMovingPhotoBadgeShown?: boolean
```

Whether the moving photo badge is displayed in the photo browser page. **true** to display the badge, **false** to hide it. The default is **false**.

If this parameter is set to **true**, [Photoselectresult](arkts-medialibrary-photoaccesshelper-photoselectresult-c.md) returns the   
**movingPhotoBadgeStates** array. The default status of a moving photo is   
[MOVING_PHOTO_ENABLED](arkts-medialibrary-photoaccesshelper-movingphotobadgestatetype-e.md).

Note: Use both **isMovingPhotoBadgeShown** and **MovingPhotoBadgeStateType** to determine whether a photo is a moving photo.

**类型：** boolean

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-BaseSelectOptions-isMovingPhotoBadgeShown?: boolean--><!--Device-BaseSelectOptions-isMovingPhotoBadgeShown?: boolean-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## isPhotoTakingSupported

```TypeScript
isPhotoTakingSupported?: boolean
```

Whether photo taking is supported. **true** if supported, **false** otherwise.

**类型：** boolean

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-BaseSelectOptions-isPhotoTakingSupported?: boolean--><!--Device-BaseSelectOptions-isPhotoTakingSupported?: boolean-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## isPreviewForSingleSelectionSupported

```TypeScript
isPreviewForSingleSelectionSupported?: boolean
```

Whether to enable full image preview if a single image is selected. **true** to enable, **false** otherwise. The default value is **true**.

**类型：** boolean

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-BaseSelectOptions-isPreviewForSingleSelectionSupported?: boolean--><!--Device-BaseSelectOptions-isPreviewForSingleSelectionSupported?: boolean-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## isSearchSupported

```TypeScript
isSearchSupported?: boolean
```

Whether the image is searchable. **true** if searchable, **false** otherwise.

**类型：** boolean

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-BaseSelectOptions-isSearchSupported?: boolean--><!--Device-BaseSelectOptions-isSearchSupported?: boolean-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## maxSelectNumber

```TypeScript
maxSelectNumber?: int
```

Maximum number of media files that can be selected. The maximum value is **500**, and the default value is **50**.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-BaseSelectOptions-maxSelectNumber?: int--><!--Device-BaseSelectOptions-maxSelectNumber?: int-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## mimeTypeFilter

```TypeScript
mimeTypeFilter?: MimeTypeFilter
```

Configuration for file type filtering. Multiple types can be specified.

When this parameter is set, the **MIMEType** configuration automatically becomes invalid.

When this parameter is set, only media files of the configured filter type are displayed. You are advised to notify users that only images or videos of the specified type can be selected.

**类型：** [MimeTypeFilter](arkts-medialibrary-photoaccesshelper-mimetypefilter-c.md)

**起始版本：** 19

**ArkTS模式：** ArkTS-Dyn起始版本为19；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-BaseSelectOptions-mimeTypeFilter?: MimeTypeFilter--><!--Device-BaseSelectOptions-mimeTypeFilter?: MimeTypeFilter-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## photoViewMimeTypeFileSizeFilters

```TypeScript
photoViewMimeTypeFileSizeFilters?: Array<PhotoViewMimeTypeFileSizeFilter>
```

An array used to filter media files by type and size.

Only the first three array elements are used; **MIMETypes** and **fileSizeFilter** are ignored.

**类型：** Array&lt;PhotoViewMimeTypeFileSizeFilter&gt;

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-BaseSelectOptions-photoViewMimeTypeFileSizeFilters?: Array<PhotoViewMimeTypeFileSizeFilter>--><!--Device-BaseSelectOptions-photoViewMimeTypeFileSizeFilters?: Array<PhotoViewMimeTypeFileSizeFilter>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## preferredCompatibleMode

```TypeScript
preferredCompatibleMode?: PreferredCompatibleMode
```

Preferred compatibility mode.

**类型：** [PreferredCompatibleMode](arkts-medialibrary-photoaccesshelper-preferredcompatiblemode-e.md)

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-BaseSelectOptions-preferredCompatibleMode?: PreferredCompatibleMode--><!--Device-BaseSelectOptions-preferredCompatibleMode?: PreferredCompatibleMode-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## preselectedUris

```TypeScript
preselectedUris?: Array<string>
```

URI of the preselected image.

**类型：** Array&lt;string&gt;

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-BaseSelectOptions-preselectedUris?: Array<string>--><!--Device-BaseSelectOptions-preselectedUris?: Array<string>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## recommendationOptions

```TypeScript
recommendationOptions?: RecommendationOptions
```

Image recommendation parameters.

**类型：** [RecommendationOptions](arkts-medialibrary-photoaccesshelper-recommendationoptions-c.md)

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-BaseSelectOptions-recommendationOptions?: RecommendationOptions--><!--Device-BaseSelectOptions-recommendationOptions?: RecommendationOptions-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## showDateOnScrollbar

```TypeScript
showDateOnScrollbar?: boolean
```

Whether to display the date group information when the scroll bar is dragged. **true**: yes; **false**: no. The default value is **false**.

**类型：** boolean

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为24；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-BaseSelectOptions-showDateOnScrollbar?: boolean--><!--Device-BaseSelectOptions-showDateOnScrollbar?: boolean-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## singleSelectionMode

```TypeScript
singleSelectionMode?: SingleSelectionMode
```

Single selection mode. The default value is **SingleSelectionMode.BROWSER_MODE**.

**类型：** [SingleSelectionMode](arkts-medialibrary-photoaccesshelper-singleselectionmode-e.md)

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-BaseSelectOptions-singleSelectionMode?: SingleSelectionMode--><!--Device-BaseSelectOptions-singleSelectionMode?: SingleSelectionMode-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## videoDurationFilter

```TypeScript
videoDurationFilter?: VideoDurationFilter
```

Configuration for video duration filtering.

When this parameter is set, only media files within the specified duration range are displayed. You are advised to notify users that only videos of the specified length can be selected.

**类型：** [VideoDurationFilter](arkts-medialibrary-photoaccesshelper-videodurationfilter-c.md)

**起始版本：** 19

**ArkTS模式：** ArkTS-Dyn起始版本为19；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-BaseSelectOptions-videoDurationFilter?: VideoDurationFilter--><!--Device-BaseSelectOptions-videoDurationFilter?: VideoDurationFilter-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

