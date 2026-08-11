# ManualExposure

ManualExposure extends [ManualExposureQuery](arkts-camera-camera-manualexposurequery-i.md)Provides APIs to obtain and set the exposure duration.

**Inheritance/Implementation:** ManualExposure extends [ManualExposureQuery](arkts-camera-camera-manualexposurequery-i.md)

**Since:** 24

<!--Device-camera-interface ManualExposure extends ManualExposureQuery--><!--Device-camera-interface ManualExposure extends ManualExposureQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## getExposure

```TypeScript
getExposure(): number
```

Obtains the manual exposure duration in use.

**Since:** 11

<!--Device-ManualExposure-getExposure(): int--><!--Device-ManualExposure-getExposure(): int-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
function getExposure(nightPhotoSession: camera.NightPhotoSession): number | undefined {
  let exposureRange: Array<number> = nightPhotoSession.getSupportedExposureRange();
  if (exposureRange === undefined || exposureRange.length <= 0) {
    return undefined;
  }
  let exposure: number = nightPhotoSession.getExposure();
  return exposure;
}
```

## getExposureDuration

```TypeScript
getExposureDuration(): number
```

Gets current exposure value.

**Since:** 24

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

## setExposure

```TypeScript
setExposure(exposure: number): void
```

Sets the manual exposure duration. Before using this API, call  
[getSupportedExposureRange](arkts-camera-camera-manualexposurequery-i.md#getsupportedexposurerange) to obtain the supported manual exposure durations, in ms.

**Since:** 11

<!--Device-ManualExposure-setExposure(exposure: int): void--><!--Device-ManualExposure-setExposure(exposure: int): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| exposure | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## setExposureDuration

```TypeScript
setExposureDuration(exposureDuration: number): void
```

Sets Exposure duration value, units: microseconds.This control is only effective if ExposureMode is set to EXPOSURE_MODE_MANUAL.

**Since:** 24

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
