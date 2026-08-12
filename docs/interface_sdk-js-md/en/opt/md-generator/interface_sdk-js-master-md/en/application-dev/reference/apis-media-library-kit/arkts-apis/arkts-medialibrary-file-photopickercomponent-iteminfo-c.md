# ItemInfo

It inherits from [BaseItemInfo](arkts-medialibrary-file-photopickercomponent-baseiteminfo-c.md#BaseItemInfo), adding the parameter **itemType**.

Represents basic image and video information.

**Inheritance/Implementation:** ItemInfo extends [BaseItemInfo](arkts-medialibrary-file-photopickercomponent-baseiteminfo-c.md#BaseItemInfo)

**Since:** 12

<!--Device-unnamed-export declare class ItemInfo extends BaseItemInfo--><!--Device-unnamed-export declare class ItemInfo extends BaseItemInfo-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
import { MaxCountType, PreselectedInfo, BaseItemInfo, ItemInfo, AnimatorParams, SelectMode, PhotoBrowserUIElement, ItemType, PinchGridSwitchedCallback, SingleLineConfig, ClickResult, ClickType, UpdatablePickerConfigs, DataType, VideoPlayerState, ItemDisplayRatio, ScrollStopAtStartCallback, ScrollStopAtEndCallback, PickerOrientation, videoPlayStateChangedCallback, PhotoBrowserChangeStartCallback, MovingPhotoBadgeStateChangedCallback, ErrorCallback, PickerOptions, ItemsDeletedCallback, PhotoBrowserRange, SaveMode, MaxSelected, PickerController, PickerError, PhotoPickerComponent, ExceedMaxSelectedCallback, ReminderMode, ItemClickedNotifyCallback, PickerColorMode, BadgeConfig, BadgeType, PhotoBrowserInfo, CurrentAlbumDeletedCallback } from '@kit.MediaLibraryKit';
```

## itemType

```TypeScript
itemType?: ItemType
```

Type of the item, which can be **THUMBNAIL** or **CAMERA**.

**Type:** [ItemType](arkts-medialibrary-file-photopickercomponent-itemtype-e.md)

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ItemInfo-itemType?: ItemType--><!--Device-ItemInfo-itemType?: ItemType-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core
