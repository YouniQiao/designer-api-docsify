# PickerOptions

PickerOptions Object

**继承/实现关系：** PickerOptions extends [photoAccessHelper.BaseSelectOptions](arkts-medialibrary-photoaccesshelper-baseselectoptions-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export declare class PickerOptions extends photoAccessHelper.BaseSelectOptions--><!--Device-unnamed-export declare class PickerOptions extends photoAccessHelper.BaseSelectOptions-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { MaxCountType, PreselectedInfo, BaseItemInfo, ItemInfo, AnimatorParams, SelectMode, PhotoBrowserUIElement, ItemType, PinchGridSwitchedCallback, SingleLineConfig, ClickResult, ClickType, UpdatablePickerConfigs, DataType, VideoPlayerState, ItemDisplayRatio, ScrollStopAtStartCallback, ScrollStopAtEndCallback, PickerOrientation, videoPlayStateChangedCallback, PhotoBrowserChangeStartCallback, MovingPhotoBadgeStateChangedCallback, ErrorCallback, PickerOptions, ItemsDeletedCallback, PhotoBrowserRange, SaveMode, MaxSelected, PickerController, PickerError, PhotoPickerComponent, ExceedMaxSelectedCallback, ReminderMode, ItemClickedNotifyCallback, PickerColorMode, BadgeConfig, BadgeType, PhotoBrowserInfo, CurrentAlbumDeletedCallback } from 'kits/@kit.MediaLibraryKit';
```

## backgroundColor

```TypeScript
public backgroundColor?: string
```

Support set backgroundColor

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PickerOptions-public backgroundColor?: string--><!--Device-PickerOptions-public backgroundColor?: string-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## badgeConfig

```TypeScript
public badgeConfig?: BadgeConfig
```

Support to config special badge display.The picker component supports only one type of badge

**类型：** [BadgeConfig](arkts-medialibrary-file-photopickercomponent-badgeconfig-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PickerOptions-public badgeConfig?: BadgeConfig--><!--Device-PickerOptions-public badgeConfig?: BadgeConfig-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## checkBoxColor

```TypeScript
public checkBoxColor?: string
```

Support set checkBox color

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PickerOptions-public checkBoxColor?: string--><!--Device-PickerOptions-public checkBoxColor?: string-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## checkboxTextColor

```TypeScript
public checkboxTextColor?: string
```

Support to set checkbox text color

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PickerOptions-public checkboxTextColor?: string--><!--Device-PickerOptions-public checkboxTextColor?: string-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## contextRecoveryInfo

```TypeScript
public contextRecoveryInfo?: photoAccessHelper.ContextRecoveryInfo
```

Context recovery information for restoring the last selection session.

**类型：** photoAccessHelper.ContextRecoveryInfo

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PickerOptions-public contextRecoveryInfo?: photoAccessHelper.ContextRecoveryInfo--><!--Device-PickerOptions-public contextRecoveryInfo?: photoAccessHelper.ContextRecoveryInfo-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## gridEndOffset

```TypeScript
public gridEndOffset?: int
```

Support to set offset between last grid item and the bottom of the grid

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PickerOptions-public gridEndOffset?: int--><!--Device-PickerOptions-public gridEndOffset?: int-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## gridMargin

```TypeScript
public gridMargin?: Margin
```

Support set gridMargin

**类型：** [Margin](../../apis-arkui/arkts-apis/arkts-arkui-margin-t.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PickerOptions-public gridMargin?: Margin--><!--Device-PickerOptions-public gridMargin?: Margin-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## gridStartOffset

```TypeScript
public gridStartOffset?: int
```

Support to set offset between first grid item and the top of the grid

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PickerOptions-public gridStartOffset?: int--><!--Device-PickerOptions-public gridStartOffset?: int-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## isRepeatSelectSupported

```TypeScript
public isRepeatSelectSupported?: boolean
```

Support repeat select

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PickerOptions-public isRepeatSelectSupported?: boolean--><!--Device-PickerOptions-public isRepeatSelectSupported?: boolean-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## isSlidingSelectionSupported

```TypeScript
public isSlidingSelectionSupported?: boolean
```

Support to set sliding selection

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PickerOptions-public isSlidingSelectionSupported?: boolean--><!--Device-PickerOptions-public isSlidingSelectionSupported?: boolean-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## maxPhotoSelectNumber

```TypeScript
public maxPhotoSelectNumber?: int
```

Support to set max photo select number

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PickerOptions-public maxPhotoSelectNumber?: int--><!--Device-PickerOptions-public maxPhotoSelectNumber?: int-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## maxSelectedReminderMode

```TypeScript
public maxSelectedReminderMode?: ReminderMode
```

Support to set max select number remind mode.

**类型：** [ReminderMode](arkts-medialibrary-file-photopickercomponent-remindermode-e.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PickerOptions-public maxSelectedReminderMode?: ReminderMode--><!--Device-PickerOptions-public maxSelectedReminderMode?: ReminderMode-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## maxVideoSelectNumber

```TypeScript
public maxVideoSelectNumber?: int
```

Support to set max video select number

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PickerOptions-public maxVideoSelectNumber?: int--><!--Device-PickerOptions-public maxVideoSelectNumber?: int-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## orientation

```TypeScript
public orientation?: PickerOrientation
```

Support to set display orientation

**类型：** [PickerOrientation](arkts-medialibrary-file-photopickercomponent-pickerorientation-e.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PickerOptions-public orientation?: PickerOrientation--><!--Device-PickerOptions-public orientation?: PickerOrientation-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## photoBrowserBackgroundColorMode

```TypeScript
public photoBrowserBackgroundColorMode?: PickerColorMode
```

Support to set photo browser background color mode

**类型：** [PickerColorMode](arkts-medialibrary-file-photopickercomponent-pickercolormode-e.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PickerOptions-public photoBrowserBackgroundColorMode?: PickerColorMode--><!--Device-PickerOptions-public photoBrowserBackgroundColorMode?: PickerColorMode-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## photoBrowserCheckboxPosition

```TypeScript
public photoBrowserCheckboxPosition?: [
        double,
        double
    ]
```

Support to set photo browser checkbox position

**类型：** [         double,         double     ]

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PickerOptions-public photoBrowserCheckboxPosition?: [        double,        double    ]--><!--Device-PickerOptions-public photoBrowserCheckboxPosition?: [        double,        double    ]-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## photoBrowserMargin

```TypeScript
public photoBrowserMargin?: Margin
```

Support set photoBrowserMargin

**类型：** [Margin](../../apis-arkui/arkts-apis/arkts-arkui-margin-t.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PickerOptions-public photoBrowserMargin?: Margin--><!--Device-PickerOptions-public photoBrowserMargin?: Margin-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## pickerIndex

```TypeScript
public pickerIndex?: int
```

Support to set a serial number to distinguish different picker components. Default value is -1.

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PickerOptions-public pickerIndex?: int--><!--Device-PickerOptions-public pickerIndex?: int-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## preselectedInfos

```TypeScript
public preselectedInfos?: PreselectedInfo[]
```

Support automatically selecting the user-selected image/video on the PhotoPickerComponent at the specified picker index.

**类型：** [PreselectedInfo](arkts-medialibrary-file-photopickercomponent-preselectedinfo-c.md)[]

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PickerOptions-public preselectedInfos?: PreselectedInfo[]--><!--Device-PickerOptions-public preselectedInfos?: PreselectedInfo[]-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## selectMode

```TypeScript
public selectMode?: SelectMode
```

Support to set select mode

**类型：** [SelectMode](arkts-medialibrary-file-photopickercomponent-selectmode-e.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PickerOptions-public selectMode?: SelectMode--><!--Device-PickerOptions-public selectMode?: SelectMode-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## singleLineConfig

```TypeScript
public singleLineConfig?: SingleLineConfig
```

Single-line display mode for the PhotoPickerComponent.

**类型：** [SingleLineConfig](arkts-medialibrary-file-photopickercomponent-singlelineconfig-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PickerOptions-public singleLineConfig?: SingleLineConfig--><!--Device-PickerOptions-public singleLineConfig?: SingleLineConfig-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## uiComponentColorMode

```TypeScript
public uiComponentColorMode?: PickerColorMode
```

Support to set UIComponent color mode.

**类型：** [PickerColorMode](arkts-medialibrary-file-photopickercomponent-pickercolormode-e.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PickerOptions-public uiComponentColorMode?: PickerColorMode--><!--Device-PickerOptions-public uiComponentColorMode?: PickerColorMode-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

