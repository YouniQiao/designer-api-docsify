# BaseItemInfo

BaseItemInfo

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export declare class BaseItemInfo--><!--Device-unnamed-export declare class BaseItemInfo-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { MaxCountType, PreselectedInfo, BaseItemInfo, ItemInfo, AnimatorParams, SelectMode, PhotoBrowserUIElement, ItemType, PinchGridSwitchedCallback, SingleLineConfig, ClickResult, ClickType, UpdatablePickerConfigs, DataType, VideoPlayerState, ItemDisplayRatio, ScrollStopAtStartCallback, ScrollStopAtEndCallback, PickerOrientation, videoPlayStateChangedCallback, PhotoBrowserChangeStartCallback, MovingPhotoBadgeStateChangedCallback, ErrorCallback, PickerOptions, ItemsDeletedCallback, PhotoBrowserRange, SaveMode, MaxSelected, PickerController, PickerError, PhotoPickerComponent, ExceedMaxSelectedCallback, ReminderMode, ItemClickedNotifyCallback, PickerColorMode, BadgeConfig, BadgeType, PhotoBrowserInfo, CurrentAlbumDeletedCallback } from 'kits/@kit.MediaLibraryKit';
```

## duration

```TypeScript
public duration?: int
```

Duration. if the itemType is CAMERA, it will be null; if photos, return -1

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BaseItemInfo-public duration?: int--><!--Device-BaseItemInfo-public duration?: int-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## dynamicRangeType

```TypeScript
public dynamicRangeType?: photoAccessHelper.DynamicRangeType
```

DynamicRangeType. Dynamic range type of media files. For movingPhoto, this specifically refers to the dynamic range type of the cover image.

**类型：** photoAccessHelper.DynamicRangeType

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BaseItemInfo-public dynamicRangeType?: photoAccessHelper.DynamicRangeType--><!--Device-BaseItemInfo-public dynamicRangeType?: photoAccessHelper.DynamicRangeType-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## height

```TypeScript
public height?: int
```

Height. if the itemType is CAMERA, it will be null

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BaseItemInfo-public height?: int--><!--Device-BaseItemInfo-public height?: int-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## mimeType

```TypeScript
public mimeType?: string
```

MimeType. if the itemType is CAMERA, it will be null

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BaseItemInfo-public mimeType?: string--><!--Device-BaseItemInfo-public mimeType?: string-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## size

```TypeScript
public size?: int
```

Size. if the itemType is CAMERA, it will be null

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BaseItemInfo-public size?: int--><!--Device-BaseItemInfo-public size?: int-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## uri

```TypeScript
public uri?: string
```

Uri. if the itemType is CAMERA, it will be null

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BaseItemInfo-public uri?: string--><!--Device-BaseItemInfo-public uri?: string-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## width

```TypeScript
public width?: int
```

Width. if the itemType is CAMERA, it will be null

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BaseItemInfo-public width?: int--><!--Device-BaseItemInfo-public width?: int-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

