# MovingPhotoViewAttribute

Defines the moving photo view attribute functions.

**Inheritance/Implementation:** MovingPhotoViewAttribute extends [CommonMethod](CommonMethod)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare interface MovingPhotoViewAttribute extends CommonMethod--><!--Device-unnamed-export declare interface MovingPhotoViewAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## setPlaybackStrategy

```TypeScript
setPlaybackStrategy(strategy: media.PlaybackStrategy): MovingPhotoViewAttribute
```

Sets playback strategy.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MovingPhotoViewAttribute-setPlaybackStrategy(strategy: media.PlaybackStrategy): MovingPhotoViewAttribute--><!--Device-MovingPhotoViewAttribute-setPlaybackStrategy(strategy: media.PlaybackStrategy): MovingPhotoViewAttribute-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| strategy | media.PlaybackStrategy | Yes | playback strategy |

**Return value:**

| Type | Description |
| --- | --- |
| [MovingPhotoViewAttribute](arkts-medialibrary-multimedia-movingphotoview-movingphotoviewattribute-i.md) |  |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications are not allowed to use system APIs. |

