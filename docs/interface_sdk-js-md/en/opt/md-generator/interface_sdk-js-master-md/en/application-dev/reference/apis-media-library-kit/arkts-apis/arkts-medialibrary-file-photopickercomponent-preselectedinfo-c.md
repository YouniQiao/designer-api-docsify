# PreselectedInfo

Describes the information about the preselected files and their corresponding **PhotoPickerComponent** index.

**Since:** 21

<!--Device-unnamed-export declare class PreselectedInfo--><!--Device-unnamed-export declare class PreselectedInfo-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
import { MaxCountType, PreselectedInfo, BaseItemInfo, ItemInfo, AnimatorParams, SelectMode, PhotoBrowserUIElement, ItemType, PinchGridSwitchedCallback, SingleLineConfig, ClickResult, ClickType, UpdatablePickerConfigs, DataType, VideoPlayerState, ItemDisplayRatio, ScrollStopAtStartCallback, ScrollStopAtEndCallback, PickerOrientation, videoPlayStateChangedCallback, PhotoBrowserChangeStartCallback, MovingPhotoBadgeStateChangedCallback, ErrorCallback, PickerOptions, ItemsDeletedCallback, PhotoBrowserRange, SaveMode, MaxSelected, PickerController, PickerError, PhotoPickerComponent, ExceedMaxSelectedCallback, ReminderMode, ItemClickedNotifyCallback, PickerColorMode, BadgeConfig, BadgeType, PhotoBrowserInfo, CurrentAlbumDeletedCallback } from 'kits/@kit.MediaLibraryKit';
```

## preselectablePickerIndex

```TypeScript
preselectablePickerIndex?: number
```

Index of the **PhotoPickerComponent** that can be used in automatic selection. The default value is **-1**, which allows automatic selection in any **PhotoPickerComponent**.

**Type:** number

**Since:** 21

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-PreselectedInfo-preselectablePickerIndex?: number--><!--Device-PreselectedInfo-preselectablePickerIndex?: number-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## uri

```TypeScript
uri: string
```

URI of the preselected media file.

**Type:** string

**Since:** 21

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-PreselectedInfo-uri: string--><!--Device-PreselectedInfo-uri: string-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core
