# MovingPhotoBadgeStateChangedCallback

```TypeScript
export type MovingPhotoBadgeStateChangedCallback = 
  (uri: string, state: photoAccessHelper.MovingPhotoBadgeStateType) => void
```

Callback to be invoked when the moving photo effect of the **PhotoPickerComponent** is enabled or disabled.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-unnamed-export type MovingPhotoBadgeStateChangedCallback =   (uri: string, state: photoAccessHelper.MovingPhotoBadgeStateType) => void--><!--Device-unnamed-export type MovingPhotoBadgeStateChangedCallback =   (uri: string, state: photoAccessHelper.MovingPhotoBadgeStateType) => void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | URI of the moving photo. |
| state | photoAccessHelper.MovingPhotoBadgeStateType | Yes | State of the moving photo badge. |

