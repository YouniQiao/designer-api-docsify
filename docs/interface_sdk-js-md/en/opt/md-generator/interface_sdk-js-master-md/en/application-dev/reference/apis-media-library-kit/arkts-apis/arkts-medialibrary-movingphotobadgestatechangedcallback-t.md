# MovingPhotoBadgeStateChangedCallback

```TypeScript
export type MovingPhotoBadgeStateChangedCallback = 
  (uri: string, state: photoAccessHelper.MovingPhotoBadgeStateType) => void
```

Callback to be invoked when the moving photo effect of the **PhotoPickerComponent** is enabled or disabled.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-unnamed-export type MovingPhotoBadgeStateChangedCallback =   (uri: string, state: photoAccessHelper.MovingPhotoBadgeStateType) => void--><!--Device-unnamed-export type MovingPhotoBadgeStateChangedCallback =   (uri: string, state: photoAccessHelper.MovingPhotoBadgeStateType) => void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| state | photoAccessHelper.MovingPhotoBadgeStateType | Yes |
