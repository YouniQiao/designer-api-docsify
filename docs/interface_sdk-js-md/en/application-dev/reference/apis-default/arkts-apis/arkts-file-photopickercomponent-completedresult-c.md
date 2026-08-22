# CompletedResult

CompletedResult

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

<!--Device-unnamed-export declare class CompletedResult--><!--Device-unnamed-export declare class CompletedResult-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
```

## contextRecoveryInfo

```TypeScript
contextRecoveryInfo: photoAccessHelper.ContextRecoveryInfo
```

Contextual information about the PhotoPicker's exit state.

**Type:** photoAccessHelper.ContextRecoveryInfo

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CompletedResult-contextRecoveryInfo: photoAccessHelper.ContextRecoveryInfo--><!--Device-CompletedResult-contextRecoveryInfo: photoAccessHelper.ContextRecoveryInfo-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## movingPhotoBadgeStates

```TypeScript
movingPhotoBadgeStates: Array<photoAccessHelper.MovingPhotoBadgeStateType>
```

M​oving photo badge states for the selected media files in the gallery. When isMovingPhotoBadgeShown is true, movingPhotoBadgeStates contains the moving photo states; otherwise, it is empty.

**Type:** Array&lt;photoAccessHelper.MovingPhotoBadgeStateType&gt;

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CompletedResult-movingPhotoBadgeStates: Array<photoAccessHelper.MovingPhotoBadgeStateType>--><!--Device-CompletedResult-movingPhotoBadgeStates: Array<photoAccessHelper.MovingPhotoBadgeStateType>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## photoUris

```TypeScript
photoUris: Array<string>
```

URIs of the images or videos selected. The URI array can be used only by calling photoAccessHelper.getAssets with temporary authorization. For details about how to use the media file URI, see Using a Media File URI.

**Type:** Array&lt;string&gt;

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CompletedResult-photoUris: Array<string>--><!--Device-CompletedResult-photoUris: Array<string>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

