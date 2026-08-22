# MovingPhotoBadgeStateChangedCallback

```TypeScript
export type MovingPhotoBadgeStateChangedCallback =
  (uri: string, state: photoAccessHelper.MovingPhotoBadgeStateType) => void
```

The callback of onMovingPhotoBadgeStateChanged event

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type MovingPhotoBadgeStateChangedCallback =  (uri: string, state: photoAccessHelper.MovingPhotoBadgeStateType) => void--><!--Device-unnamed-export type MovingPhotoBadgeStateChangedCallback =  (uri: string, state: photoAccessHelper.MovingPhotoBadgeStateType) => void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes |  |
| state | photoAccessHelper.MovingPhotoBadgeStateType | Yes |  |

