# ManualExposure (System API)

ManualExposure extends [ManualExposureQuery](arkts-camera-camera-manualexposurequery-i.md#ManualExposureQuery-(System-API)) Provides APIs to obtain and set the exposure duration.

**Inheritance/Implementation:** ManualExposure extends [ManualExposureQuery](arkts-camera-camera-manualexposurequery-i.md#ManualExposureQuery-(System-API))

**Since:** 23

**Deprecated since:** -1

<!--Device-camera-interface ManualExposure--><!--Device-camera-interface ManualExposure-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

## getExposureDuration

```TypeScript
getExposureDuration(): number
```

Gets current exposure value.

**Since:** 24

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-ManualExposure-getExposureDuration(): int--><!--Device-ManualExposure-getExposureDuration(): int-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |

## setExposureDuration

```TypeScript
setExposureDuration(exposureDuration: number): void
```

Sets Exposure duration value, units: microseconds.This control is only effective if ExposureMode is set to EXPOSURE_MODE_MANUAL.

**Since:** 24

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-ManualExposure-setExposureDuration(exposureDuration: int): void--><!--Device-ManualExposure-setExposureDuration(exposureDuration: int): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| exposureDuration | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |
