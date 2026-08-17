# RecoveryResult

RecoveryResult

**Since:** 26.1.0

<!--Device-unnamed-export declare class RecoveryResult--><!--Device-unnamed-export declare class RecoveryResult-End-->

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

## albumName

```TypeScript
albumName: string
```

Name of the restored album.

**Type:** string

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-RecoveryResult-albumName: string--><!--Device-RecoveryResult-albumName: string-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## albumUri

```TypeScript
albumUri: string
```

URI of the restored album.

**Type:** string

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-RecoveryResult-albumUri: string--><!--Device-RecoveryResult-albumUri: string-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

