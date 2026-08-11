# FocusQuery

FocusQuery provides APIs to check whether a focus mode is supported.

> **NOTE：**
> 
> - This interface was first introduced in API version 12. In this version, a compatibility change was made that
> preserved the initial version information of inner elements. As a result, you might see outer element's @since
> version number being higher than that of the inner elements. However, this discrepancy does not affect the
> functionality of the interface.

**Since:** 12

<!--Device-camera-interface FocusQuery--><!--Device-camera-interface FocusQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## isFocusModeSupported

```TypeScript
isFocusModeSupported(afMode: FocusMode): boolean
```

Checks whether a focus mode is supported.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-FocusQuery-isFocusModeSupported(afMode: FocusMode): boolean--><!--Device-FocusQuery-isFocusModeSupported(afMode: FocusMode): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| afMode | [FocusMode](arkts-camera-camera-focusmode-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |

## isLockFocusTrackingSupported

```TypeScript
isLockFocusTrackingSupported(): boolean
```

Checks whether lock focus tracking is supported.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-FocusQuery-isLockFocusTrackingSupported(): boolean--><!--Device-FocusQuery-isLockFocusTrackingSupported(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |
