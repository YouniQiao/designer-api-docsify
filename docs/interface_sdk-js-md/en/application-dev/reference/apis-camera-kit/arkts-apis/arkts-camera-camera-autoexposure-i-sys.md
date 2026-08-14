# AutoExposure

**AutoExposure** inherits from [AutoExposureQuery](arkts-camera-camera-autoexposurequery-i.md#AutoExposureQuery). It provides APIs related to auto exposure.

**Inheritance/Implementation:** AutoExposure extends [AutoExposureQuery](arkts-camera-camera-autoexposurequery-i.md#AutoExposureQuery)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-camera-interface AutoExposure--><!--Device-camera-interface AutoExposure-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from 'camera';
```

## getExposureMeteringMode

```TypeScript
getExposureMeteringMode(): ExposureMeteringMode
```

Obtains the exposure metering mode in use.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-AutoExposure-getExposureMeteringMode(): ExposureMeteringMode--><!--Device-AutoExposure-getExposureMeteringMode(): ExposureMeteringMode-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| [ExposureMeteringMode](arkts-camera-camera-exposuremeteringmode-e-sys.md) | Exposure metering mode obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) | Operation not allowed, the inputDevice or the session is abnormal.<br>**Applicable version:** 24 and later |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config, only throw in session usage. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application.<br>**Applicable version:** 12 - 23 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function getExposureMeteringMode(professionalPhotoSession: camera.ProfessionalPhotoSession): camera.ExposureMeteringMode | undefined {
  let exposureMeteringMode: camera.ExposureMeteringMode | undefined = undefined;
  try {
    exposureMeteringMode = professionalPhotoSession.getExposureMeteringMode();
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(`The getExposureMeteringMode call failed. error code: ${err.code}`);
  }
  return exposureMeteringMode;
}
```

## setExposureMeteringMode

```TypeScript
setExposureMeteringMode(aeMeteringMode: ExposureMeteringMode): void
```

Sets exposure metering mode.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-AutoExposure-setExposureMeteringMode(aeMeteringMode: ExposureMeteringMode): void--><!--Device-AutoExposure-setExposureMeteringMode(aeMeteringMode: ExposureMeteringMode): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| aeMeteringMode | [ExposureMeteringMode](arkts-camera-camera-exposuremeteringmode-e-sys.md) | Yes | Exposure metering mode. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) | Parameter missing or parameter type incorrect.<br>**Applicable version:** 12 - 23 |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) | Operation not allowed, the inputDevice or the session is abnormal.<br>**Applicable version:** 24 and later |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config, only throw in session usage. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application.<br>**Applicable version:** 12 - 23 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function setExposureMeteringMode(professionalPhotoSession: camera.ProfessionalPhotoSession): void {
  try {
    professionalPhotoSession.setExposureMeteringMode(camera.ExposureMeteringMode.CENTER);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(`The setExposureMeteringMode call failed. error code: ${err.code}`);
  }
}
```

