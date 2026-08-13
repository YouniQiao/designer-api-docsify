# FlashQuery

FlashQuery provides APIs to query the flash status and mode of a camera device. > **NOTE：**> > - This interface was first introduced in API version 12. In this version, a compatibility change was made that > preserved the initial version information of inner elements. As a result, you might see outer element's @since > version number being higher than that of the inner elements. However, this discrepancy does not affect the > functionality of the interface.

**Since:** 23

**Deprecated since:** -1

<!--Device-camera-interface FlashQuery--><!--Device-camera-interface FlashQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

## hasFlash

```TypeScript
hasFlash(): boolean
```

Checks whether the camera device has flash.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-FlashQuery-hasFlash(): boolean--><!--Device-FlashQuery-hasFlash(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |

## isFlashModeSupported

```TypeScript
isFlashModeSupported(flashMode: FlashMode): boolean
```

Checks whether a flash mode is supported.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-FlashQuery-isFlashModeSupported(flashMode: FlashMode): boolean--><!--Device-FlashQuery-isFlashModeSupported(flashMode: FlashMode): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| flashMode | [FlashMode](arkts-camera-camera-flashmode-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |
