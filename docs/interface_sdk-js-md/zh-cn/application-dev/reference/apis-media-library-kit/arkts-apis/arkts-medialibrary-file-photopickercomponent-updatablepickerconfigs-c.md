# UpdatablePickerConfigs

Describes the updatable attributes of the **PhotoPickerComponent**. These attributes are a subset of  
[PickerOptions](arkts-medialibrary-file-photopickercomponent-pickeroptions-c.md).

**起始版本：** 22

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为22。

<!--Device-unnamed-export declare class UpdatablePickerConfigs--><!--Device-unnamed-export declare class UpdatablePickerConfigs-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { MaxCountType, PreselectedInfo, BaseItemInfo, ItemInfo, AnimatorParams, SelectMode, PhotoBrowserUIElement, ItemType, PinchGridSwitchedCallback, SingleLineConfig, ClickResult, ClickType, UpdatablePickerConfigs, DataType, VideoPlayerState, ItemDisplayRatio, ScrollStopAtStartCallback, ScrollStopAtEndCallback, PickerOrientation, videoPlayStateChangedCallback, PhotoBrowserChangeStartCallback, MovingPhotoBadgeStateChangedCallback, ErrorCallback, PickerOptions, ItemsDeletedCallback, PhotoBrowserRange, SaveMode, MaxSelected, PickerController, PickerError, PhotoPickerComponent, ExceedMaxSelectedCallback, ReminderMode, ItemClickedNotifyCallback, PickerColorMode, BadgeConfig, BadgeType, PhotoBrowserInfo, CurrentAlbumDeletedCallback } from 'kits/@kit.MediaLibraryKit';
```

## appAlbumFilters

```TypeScript
appAlbumFilters?: Array<string>
```

Used to display only the album content corresponding to the specified bundle name.

**类型：** Array&lt;string&gt;

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-UpdatablePickerConfigs-appAlbumFilters?: Array<string>--><!--Device-UpdatablePickerConfigs-appAlbumFilters?: Array<string>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## autoPlayScenes

```TypeScript
autoPlayScenes?: Array<photoAccessHelper.AutoPlayScene>
```

Playback mode of the moving photo. The maximum array length is 2. If this limit is exceeded, the first two elements are used, and the extra ones are automatically ignored.

**类型：** Array&lt;photoAccessHelper.AutoPlayScene&gt;

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-UpdatablePickerConfigs-autoPlayScenes?: Array<photoAccessHelper.AutoPlayScene>--><!--Device-UpdatablePickerConfigs-autoPlayScenes?: Array<photoAccessHelper.AutoPlayScene>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## backgroundColor

```TypeScript
backgroundColor?: string
```

Background color of the Picker grid page.

The value is an 8-digit hexadecimal color code.

**类型：** string

**起始版本：** 22

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为22。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-UpdatablePickerConfigs-backgroundColor?: string--><!--Device-UpdatablePickerConfigs-backgroundColor?: string-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## backgroundOpacity

```TypeScript
backgroundOpacity?: number
```

Background opacity of the picker. The value range is [0, 1]. **0** indicates completely transparent, and **1**indicates completely opaque.

**类型：** number

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-UpdatablePickerConfigs-backgroundOpacity?: number--><!--Device-UpdatablePickerConfigs-backgroundOpacity?: number-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## checkBoxColor

```TypeScript
checkBoxColor?: string
```

Background color of the check box.

The value is an 8-digit hexadecimal color code.

**类型：** string

**起始版本：** 22

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为22。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-UpdatablePickerConfigs-checkBoxColor?: string--><!--Device-UpdatablePickerConfigs-checkBoxColor?: string-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## checkboxTextColor

```TypeScript
checkboxTextColor?: string
```

Text color in the check box.

The value is an 8-digit hexadecimal color code.

**类型：** string

**起始版本：** 22

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为22。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-UpdatablePickerConfigs-checkboxTextColor?: string--><!--Device-UpdatablePickerConfigs-checkboxTextColor?: string-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## edgeEffect

```TypeScript
edgeEffect?: EdgeEffect
```

Scrolling effect when the Picker grid page reaches the edge.

The default value is [EdgeEffect.Spring](../../apis-arkui/arkts-apis/arkts-arkui-enums-edgeeffect-e.md/arkts-arkui-enums-edgeeffect-e.md).

**类型：** [EdgeEffect](../../apis-arkui/arkts-apis/arkts-arkui-edgeeffect-e.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-UpdatablePickerConfigs-edgeEffect?: EdgeEffect--><!--Device-UpdatablePickerConfigs-edgeEffect?: EdgeEffect-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## gridMargin

```TypeScript
gridMargin?: Margin
```

Margin of the component grid.

**类型：** [Margin](../../apis-arkui/arkts-apis/arkts-arkui-margin-t.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-UpdatablePickerConfigs-gridMargin?: Margin--><!--Device-UpdatablePickerConfigs-gridMargin?: Margin-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## isRepeatSelectSupported

```TypeScript
isRepeatSelectSupported?: boolean
```

Whether a single image can be repeatedly selected.

**true** if supported, **false** otherwise. The default value is **false**.

**类型：** boolean

**起始版本：** 22

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为22。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-UpdatablePickerConfigs-isRepeatSelectSupported?: boolean--><!--Device-UpdatablePickerConfigs-isRepeatSelectSupported?: boolean-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## isSlidingSupported

```TypeScript
isSlidingSupported?: boolean
```

Whether scrolling in the **PhotoPickerComponent** is enabled. The value **true** means that scrolling is not blocked and the component responds to user scroll gestures. The value **false** means that scrolling is blocked and the component does not respond to user scroll gestures.

The default value is **true**.

**类型：** boolean

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-UpdatablePickerConfigs-isSlidingSupported?: boolean--><!--Device-UpdatablePickerConfigs-isSlidingSupported?: boolean-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## maxPhotoSelectNumber

```TypeScript
maxPhotoSelectNumber?: number
```

Maximum number of images that can be selected (unit: number).

The maximum value is **500**, which is limited by **MaxSelected**. The default value is **500**.

**类型：** number

**起始版本：** 22

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为22。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-UpdatablePickerConfigs-maxPhotoSelectNumber?: number--><!--Device-UpdatablePickerConfigs-maxPhotoSelectNumber?: number-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## maxSelectNumber

```TypeScript
maxSelectNumber?: number
```

Maximum number of media files that can be selected.

The maximum value is 500, and the default value is 50.

**类型：** number

**起始版本：** 22

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为22。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-UpdatablePickerConfigs-maxSelectNumber?: number--><!--Device-UpdatablePickerConfigs-maxSelectNumber?: number-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## maxVideoSelectNumber

```TypeScript
maxVideoSelectNumber?: number
```

Maximum number of videos that can be selected (unit: number).

The maximum value is **500**, and it is restricted by the maximum number of media files that can be selected in the system. The default value is **500**.

**类型：** number

**起始版本：** 22

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为22。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-UpdatablePickerConfigs-maxVideoSelectNumber?: number--><!--Device-UpdatablePickerConfigs-maxVideoSelectNumber?: number-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## mimeType

```TypeScript
mimeType?: photoAccessHelper.PhotoViewMIMETypes
```

MIME types.

If this parameter is not specified, **IMAGE_VIDEO_TYPE** is used by default.

**类型：** photoAccessHelper.PhotoViewMIMETypes

**起始版本：** 22

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为22。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-UpdatablePickerConfigs-mimeType?: photoAccessHelper.PhotoViewMIMETypes--><!--Device-UpdatablePickerConfigs-mimeType?: photoAccessHelper.PhotoViewMIMETypes-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## mimeTypeFilter

```TypeScript
mimeTypeFilter?: photoAccessHelper.MimeTypeFilter
```

Configuration for file type filtering. Multiple types can be specified.

- When this parameter is set, the **mimeType** configuration automatically becomes invalid.  
- When this parameter is set, only media files of the configured filter type are displayed. You are advised to  
notify users that only images or videos of the specified type can be selected.

**类型：** photoAccessHelper.MimeTypeFilter

**起始版本：** 22

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为22。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-UpdatablePickerConfigs-mimeTypeFilter?: photoAccessHelper.MimeTypeFilter--><!--Device-UpdatablePickerConfigs-mimeTypeFilter?: photoAccessHelper.MimeTypeFilter-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## photoBrowserBackgroundColorMode

```TypeScript
photoBrowserBackgroundColorMode?: PickerColorMode
```

Background color of the photo browser page.

The options are **AUTO**, **LIGHT**, and **DARK**. The default value is **AUTO**.

**类型：** [PickerColorMode](arkts-medialibrary-file-photopickercomponent-pickercolormode-e.md)

**起始版本：** 22

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为22。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-UpdatablePickerConfigs-photoBrowserBackgroundColorMode?: PickerColorMode--><!--Device-UpdatablePickerConfigs-photoBrowserBackgroundColorMode?: PickerColorMode-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## photoBrowserMargin

```TypeScript
photoBrowserMargin?: Margin
```

Margin of the component large image.

**类型：** [Margin](../../apis-arkui/arkts-apis/arkts-arkui-margin-t.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-UpdatablePickerConfigs-photoBrowserMargin?: Margin--><!--Device-UpdatablePickerConfigs-photoBrowserMargin?: Margin-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## preselectedUris

```TypeScript
preselectedUris?: Array<string>
```

URIs of the selected images.

**类型：** Array&lt;string&gt;

**起始版本：** 22

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为22。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-UpdatablePickerConfigs-preselectedUris?: Array<string>--><!--Device-UpdatablePickerConfigs-preselectedUris?: Array<string>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## selectMode

```TypeScript
selectMode?: SelectMode
```

Picker selection mode.

**SINGLE_SELECT** or **MULTI_SELECT**. The default value is **MULTI_SELECT**.

**类型：** [SelectMode](arkts-medialibrary-file-photopickercomponent-selectmode-e.md)

**起始版本：** 22

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为22。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-UpdatablePickerConfigs-selectMode?: SelectMode--><!--Device-UpdatablePickerConfigs-selectMode?: SelectMode-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## singleSelectionMode

```TypeScript
singleSelectionMode?: photoAccessHelper.SingleSelectionMode
```

Single selection mode. The default value is **SingleSelectionMode.BROWSER_MODE**.

**类型：** photoAccessHelper.SingleSelectionMode

**起始版本：** 22

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为22。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-UpdatablePickerConfigs-singleSelectionMode?: photoAccessHelper.SingleSelectionMode--><!--Device-UpdatablePickerConfigs-singleSelectionMode?: photoAccessHelper.SingleSelectionMode-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## uiComponentColorMode

```TypeScript
uiComponentColorMode?: PickerColorMode
```

Color mode of the Picker UI component.

Dark/Light color mode (excluding the background color) of other components on the Picker grid page, including the search box, camera entry, safety tips for using Gallery, and recommendation bubble. This attribute is usually used together with **backgroundColor**. The default value is **PickerColorMode.AUTO**, which follows the system's dark/light color mode.

When setting this attribute, avoid using **PickerColorMode.LIGHT** with a dark background color, as it may make components or text hard to see. Avoid using **PickerColorMode.DARK** with a light background color for the same reason.

**类型：** [PickerColorMode](arkts-medialibrary-file-photopickercomponent-pickercolormode-e.md)

**起始版本：** 22

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为22。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-UpdatablePickerConfigs-uiComponentColorMode?: PickerColorMode--><!--Device-UpdatablePickerConfigs-uiComponentColorMode?: PickerColorMode-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

