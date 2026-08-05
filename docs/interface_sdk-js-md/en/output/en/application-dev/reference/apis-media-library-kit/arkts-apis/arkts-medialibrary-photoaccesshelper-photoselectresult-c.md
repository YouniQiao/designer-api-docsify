# PhotoSelectResult

Defines information about the images or videos selected.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 26.0.0.

<!--Device-photoAccessHelper-class PhotoSelectResult--><!--Device-photoAccessHelper-class PhotoSelectResult-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## contextRecoveryInfo

```TypeScript
contextRecoveryInfo: ContextRecoveryInfo
```

Information about the context of exiting the PhotoPicker. This information is returned when the selection process is complete and is used by the application within **PhotoSelectOptions** during the subsequent launch of the PhotoPicker to restore the state from the previous exit.

**Type:** ContextRecoveryInfo

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-PhotoSelectResult-contextRecoveryInfo: ContextRecoveryInfo--><!--Device-PhotoSelectResult-contextRecoveryInfo: ContextRecoveryInfo-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## isOriginalPhoto

```TypeScript
isOriginalPhoto: boolean
```

Whether the selected media file is the original image. **true** if yes, **false** otherwise. The default value is **false**.

**Type:** boolean

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PhotoSelectResult-isOriginalPhoto: boolean--><!--Device-PhotoSelectResult-isOriginalPhoto: boolean-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## movingPhotoBadgeStates

```TypeScript
movingPhotoBadgeStates: Array<MovingPhotoBadgeStateType>
```

Array of moving photo badge states for the media files selected from Gallery. If **isMovingPhotoBadgeShown** is set to **true**, this array contains the moving photo badge states. Otherwise, it is empty.

**Type:** Array&lt;MovingPhotoBadgeStateType&gt;

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-PhotoSelectResult-movingPhotoBadgeStates: Array<MovingPhotoBadgeStateType>--><!--Device-PhotoSelectResult-movingPhotoBadgeStates: Array<MovingPhotoBadgeStateType>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## photoUris

```TypeScript
photoUris: Array<string>
```

URIs of the media files selected. This URI array can be used only by calling the [photoAccessHelper.getAssets]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ API through temporary authorization. For details, see \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Type:** Array&lt;string&gt;

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PhotoSelectResult-photoUris: Array<string>--><!--Device-PhotoSelectResult-photoUris: Array<string>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

