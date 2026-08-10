# BaseItemInfo

BaseItemInfo

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare class BaseItemInfo--><!--Device-unnamed-export declare class BaseItemInfo-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
import { MaxCountType, PreselectedInfo, BaseItemInfo, ItemInfo, AnimatorParams, SelectMode, PhotoBrowserUIElement, ItemType, PinchGridSwitchedCallback, SingleLineConfig, ClickResult, ClickType, UpdatablePickerConfigs, DataType, VideoPlayerState, ItemDisplayRatio, ScrollStopAtStartCallback, ScrollStopAtEndCallback, PickerOrientation, videoPlayStateChangedCallback, PhotoBrowserChangeStartCallback, MovingPhotoBadgeStateChangedCallback, ErrorCallback, PickerOptions, ItemsDeletedCallback, PhotoBrowserRange, SaveMode, MaxSelected, PickerController, PickerError, PhotoPickerComponent, ExceedMaxSelectedCallback, ReminderMode, ItemClickedNotifyCallback, PickerColorMode, BadgeConfig, BadgeType, PhotoBrowserInfo, CurrentAlbumDeletedCallback } from 'kits/@kit.MediaLibraryKit';
```

## duration

```TypeScript
public duration?: int
```

Duration. if the itemType is CAMERA, it will be null; if photos, return -1

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseItemInfo-public duration?: int--><!--Device-BaseItemInfo-public duration?: int-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## dynamicRangeType

```TypeScript
public dynamicRangeType?: photoAccessHelper.DynamicRangeType
```

DynamicRangeType. Dynamic range type of media files. For movingPhoto, this specifically refers to the dynamic range type of the cover image.

**Type:** photoAccessHelper.DynamicRangeType

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseItemInfo-public dynamicRangeType?: photoAccessHelper.DynamicRangeType--><!--Device-BaseItemInfo-public dynamicRangeType?: photoAccessHelper.DynamicRangeType-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## height

```TypeScript
public height?: int
```

Height. if the itemType is CAMERA, it will be null

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseItemInfo-public height?: int--><!--Device-BaseItemInfo-public height?: int-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## mimeType

```TypeScript
public mimeType?: string
```

MimeType. if the itemType is CAMERA, it will be null

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseItemInfo-public mimeType?: string--><!--Device-BaseItemInfo-public mimeType?: string-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## size

```TypeScript
public size?: int
```

Size. if the itemType is CAMERA, it will be null

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseItemInfo-public size?: int--><!--Device-BaseItemInfo-public size?: int-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## uri

```TypeScript
public uri?: string
```

Uri. if the itemType is CAMERA, it will be null

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseItemInfo-public uri?: string--><!--Device-BaseItemInfo-public uri?: string-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## width

```TypeScript
public width?: int
```

Width. if the itemType is CAMERA, it will be null

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseItemInfo-public width?: int--><!--Device-BaseItemInfo-public width?: int-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

