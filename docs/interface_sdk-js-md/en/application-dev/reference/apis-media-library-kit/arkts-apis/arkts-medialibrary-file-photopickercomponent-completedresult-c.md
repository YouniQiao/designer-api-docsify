# CompletedResult

Defines the information about the Picker's state from the last exit.

**Since:** 26.0.0

<!--Device-unnamed-export declare class CompletedResult--><!--Device-unnamed-export declare class CompletedResult-End-->

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

## contextRecoveryInfo

```TypeScript
contextRecoveryInfo: photoAccessHelper.ContextRecoveryInfo
```

Context information of the PhotoPicker exit status.

**Type:** photoAccessHelper.ContextRecoveryInfo

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CompletedResult-contextRecoveryInfo: photoAccessHelper.ContextRecoveryInfo--><!--Device-CompletedResult-contextRecoveryInfo: photoAccessHelper.ContextRecoveryInfo-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## movingPhotoBadgeStates

```TypeScript
movingPhotoBadgeStates: Array<photoAccessHelper.MovingPhotoBadgeStateType>
```

Moving photo badge states of the selected media files. When **isMovingPhotoBadgeShown** is set to **true**, **movingPhotoBadgeStates** contains the moving photo status. Otherwise, the value is empty.

**Type:** Array&lt;photoAccessHelper.MovingPhotoBadgeStateType&gt;

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CompletedResult-movingPhotoBadgeStates: Array<photoAccessHelper.MovingPhotoBadgeStateType>--><!--Device-CompletedResult-movingPhotoBadgeStates: Array<photoAccessHelper.MovingPhotoBadgeStateType>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## photoUris

```TypeScript
photoUris: Array<string>
```

URI of the selected image or video. The URI array can be used only by calling **photoAccessHelper.getAssets** in temporary authorization mode.

**Type:** Array&lt;string&gt;

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CompletedResult-photoUris: Array<string>--><!--Device-CompletedResult-photoUris: Array<string>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

