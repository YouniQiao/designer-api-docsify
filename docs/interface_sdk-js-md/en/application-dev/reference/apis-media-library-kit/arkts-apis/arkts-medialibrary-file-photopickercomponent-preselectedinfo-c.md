# PreselectedInfo

Describes the information about the preselected files and their corresponding **PhotoPickerComponent** index.

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

**Deprecated since:** -1

<!--Device-unnamed-export declare class PreselectedInfo--><!--Device-unnamed-export declare class PreselectedInfo-End-->

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

## preselectablePickerIndex

```TypeScript
preselectablePickerIndex?: number
```

Index of the **PhotoPickerComponent** that can be used in automatic selection. The default value is **-1**, which allows automatic selection in any **PhotoPickerComponent**.

**Type:** number

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

**Deprecated since:** -1

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

**ArkTS mode:** ArkTS-Dyn only, since version 21.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-PreselectedInfo-uri: string--><!--Device-PreselectedInfo-uri: string-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

