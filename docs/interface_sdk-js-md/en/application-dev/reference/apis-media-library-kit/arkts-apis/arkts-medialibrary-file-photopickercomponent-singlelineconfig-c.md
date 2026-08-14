# SingleLineConfig

Represents the single-line display mode. In single-line mode, the component does not provide functions for viewing a larger image. The component does not support callbacks related to large images, and the PickerController does not support APIs related to large images, making API calls ineffective.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Deprecated since:** -1

<!--Device-unnamed-export declare class SingleLineConfig--><!--Device-unnamed-export declare class SingleLineConfig-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
import { PhotoPickerComponent } from 'PhotoPickerComponent';
import { PickerController } from 'PickerController';
import { PickerOptions } from 'PickerOptions';
import { DataType } from 'DataType';
import { BaseItemInfo } from 'BaseItemInfo';
import { ItemInfo } from 'ItemInfo';
import { PhotoBrowserInfo } from 'PhotoBrowserInfo';
import { AnimatorParams } from 'AnimatorParams';
import { MaxSelected } from 'MaxSelected';
import { ItemType } from 'ItemType';
import { ClickType } from 'ClickType';
import { PickerOrientation } from 'PickerOrientation';
import { SelectMode } from 'SelectMode';
import { PickerColorMode } from 'PickerColorMode';
import { ReminderMode } from 'ReminderMode';
import { MaxCountType } from 'MaxCountType';
import { PhotoBrowserRange } from 'PhotoBrowserRange';
import { PhotoBrowserUIElement } from 'PhotoBrowserUIElement';
import { ItemsDeletedCallback } from 'ItemsDeletedCallback';
import { ExceedMaxSelectedCallback } from 'ExceedMaxSelectedCallback';
import { CurrentAlbumDeletedCallback } from 'CurrentAlbumDeletedCallback';
import { videoPlayStateChangedCallback } from 'videoPlayStateChangedCallback';
import { MovingPhotoBadgeStateChangedCallback } from 'MovingPhotoBadgeStateChangedCallback';
import { UpdatablePickerConfigs } from 'UpdatablePickerConfigs';
import { SingleLineConfig } from 'SingleLineConfig';
import { BadgeConfig } from 'BadgeConfig';
import { PreselectedInfo } from 'PreselectedInfo';
import { SaveMode } from 'SaveMode';
import { BadgeType } from 'BadgeType';
import { VideoPlayerState } from 'VideoPlayerState';
import { ItemDisplayRatio } from 'ItemDisplayRatio';
import { ScrollStopAtStartCallback } from 'ScrollStopAtStartCallback';
import { ItemClickedNotifyCallback } from 'ItemClickedNotifyCallback';
import { ScrollStopAtEndCallback } from 'ScrollStopAtEndCallback';
import { PhotoBrowserChangeStartCallback } from 'PhotoBrowserChangeStartCallback';
import { PinchGridSwitchedCallback } from 'PinchGridSwitchedCallback';
import { ErrorCallback } from 'ErrorCallback';
import { ClickResult } from 'ClickResult';
import { PickerError } from 'PickerError';
```

## itemBorderRadius

```TypeScript
itemBorderRadius?: Length | BorderRadiuses | LocalizedBorderRadiuses
```

Rounded corner radius for grid items.

**Type:** Length \| BorderRadiuses \| LocalizedBorderRadiuses

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-SingleLineConfig-itemBorderRadius?: Length | BorderRadiuses | LocalizedBorderRadiuses--><!--Device-SingleLineConfig-itemBorderRadius?: Length | BorderRadiuses | LocalizedBorderRadiuses-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## itemDisplayRatio

```TypeScript
itemDisplayRatio?: ItemDisplayRatio
```

Aspect ratio for grid display. Both 1:1 and the original image aspect ratio are supported. The default value is 1: 1.

**Type:** [ItemDisplayRatio](arkts-medialibrary-file-photopickercomponent-itemdisplayratio-e.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-SingleLineConfig-itemDisplayRatio?: ItemDisplayRatio--><!--Device-SingleLineConfig-itemDisplayRatio?: ItemDisplayRatio-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## itemGap

```TypeScript
itemGap?: Length
```

Spacing between grid items.

**Type:** Length

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-SingleLineConfig-itemGap?: Length--><!--Device-SingleLineConfig-itemGap?: Length-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

