# CompletedResult

Defines the information about the Picker's state from the last exit.

**Since:** 26.0.0

<!--Device-unnamed-export declare class CompletedResult--><!--Device-unnamed-export declare class CompletedResult-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
import { MaxCountType, PreselectedInfo, BaseItemInfo, ItemInfo, AnimatorParams, SelectMode, PhotoBrowserUIElement, ItemType, PinchGridSwitchedCallback, SingleLineConfig, ClickResult, ClickType, UpdatablePickerConfigs, DataType, VideoPlayerState, ItemDisplayRatio, ScrollStopAtStartCallback, ScrollStopAtEndCallback, PickerOrientation, videoPlayStateChangedCallback, PhotoBrowserChangeStartCallback, MovingPhotoBadgeStateChangedCallback, ErrorCallback, PickerOptions, ItemsDeletedCallback, PhotoBrowserRange, SaveMode, MaxSelected, PickerController, PickerError, PhotoPickerComponent, ExceedMaxSelectedCallback, ReminderMode, ItemClickedNotifyCallback, PickerColorMode, BadgeConfig, BadgeType, PhotoBrowserInfo, CurrentAlbumDeletedCallback } from 'kits/@kit.MediaLibraryKit';
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

Moving photo badge states of the selected media files. When **isMovingPhotoBadgeShown** is set to **true**,  
**movingPhotoBadgeStates** contains the moving photo status. Otherwise, the value is empty.

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
