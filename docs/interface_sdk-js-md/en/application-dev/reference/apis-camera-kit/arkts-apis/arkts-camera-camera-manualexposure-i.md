# ManualExposure

ManualExposure extends [ManualExposureQuery](arkts-camera-camera-manualexposurequery-i.md)Provides APIs to obtain and set the exposure duration.

**Inheritance/Implementation:** ManualExposure extends [ManualExposureQuery](arkts-camera-camera-manualexposurequery-i.md)

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-camera-interface ManualExposure extends ManualExposureQuery--><!--Device-camera-interface ManualExposure extends ManualExposureQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## getExposure

ArkTS-Dyn:
```TypeScript
getExposure(): number
```

ArkTS-Sta:
```TypeScript
getExposure(): int
```

Obtains the manual exposure duration in use.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-ManualExposure-getExposure(): int--><!--Device-ManualExposure-getExposure(): int-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | The current exposure value, in units of ms |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect.<br>**Applicable version:** 12 and later |
| 7400103 | Session not config. |
| 202 | Not System Application. |

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

ArkTS-Dyn:
```TypeScript
getExposureDuration(): number
```

ArkTS-Sta:
```TypeScript
getExposureDuration(): int
```

Gets current exposure value.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-ManualExposure-getExposureDuration(): int--><!--Device-ManualExposure-getExposureDuration(): int-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | The current exposure value, in units of microsecond |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400102 | Operation not allowed, session or inputdevice maybe abnormal. |
| 7400103 | Session not config. |

## setExposure

ArkTS-Dyn:
```TypeScript
setExposure(exposure: number): void
```

ArkTS-Sta:
```TypeScript
setExposure(exposure: int): void
```

Sets the manual exposure duration. Before using this API, call  
[getSupportedExposureRange](arkts-camera-camera-manualexposurequery-i.md#getsupportedexposurerange) to obtain the supported manual exposure durations, in ms.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-ManualExposure-setExposure(exposure: int): void--><!--Device-ManualExposure-setExposure(exposure: int): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| exposure | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Manual exposure duration, which must be one of the supported durations obtained by running [getSupportedExposureRange](arkts-camera-camera-manualexposurequery-i.md#getsupportedexposurerange). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400102 | Operation not allowed.<br>**Applicable version:** 12 and later |
| 7400103 | Session not config. |
| 202 | Not System Application. |

## setExposureDuration

ArkTS-Dyn:
```TypeScript
setExposureDuration(exposureDuration: number): void
```

ArkTS-Sta:
```TypeScript
setExposureDuration(exposureDuration: int): void
```

Sets Exposure duration value, units: microseconds.This control is only effective if ExposureMode is set to EXPOSURE_MODE_MANUAL.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-ManualExposure-setExposureDuration(exposureDuration: int): void--><!--Device-ManualExposure-setExposureDuration(exposureDuration: int): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| exposureDuration | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Exposure duration value |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400103 | Session not config. |

