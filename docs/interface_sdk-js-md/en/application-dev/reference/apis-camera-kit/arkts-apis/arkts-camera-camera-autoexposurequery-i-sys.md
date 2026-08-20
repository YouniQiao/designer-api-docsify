# AutoExposureQuery

AutoExposureQuery provides APIs to query the automatic exposure feature of a camera device.   
> 
> - In this version, a compatibility change was made that preserved the initial version information of inner &gt; elements. As a result, you might see outer element's

**Since:** 23

<!--Device-camera-interface AutoExposureQuery--><!--Device-camera-interface AutoExposureQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
import { cameraPicker } from '@kit.CameraKit';
```

## isExposureMeteringModeSupported

```TypeScript
isExposureMeteringModeSupported(aeMeteringMode: ExposureMeteringMode): boolean
```

Checks whether the specified exposure metering mode is supported.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-AutoExposureQuery-isExposureMeteringModeSupported(aeMeteringMode: ExposureMeteringMode): boolean--><!--Device-AutoExposureQuery-isExposureMeteringModeSupported(aeMeteringMode: ExposureMeteringMode): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| aeMeteringMode | [ExposureMeteringMode](arkts-camera-camera-exposuremeteringmode-e-sys.md) | Yes | Exposure metering mode. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether the exposure metering mode is supported. **true** if supported, **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application.<br>**Applicable version:** 12 - 23 |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) | Parameter missing or parameter type incorrect.<br>**Applicable version:** 12 - 23 |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config, only throw in session usage. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function isExposureMeteringModeSupported(professionalPhotoSession: camera.ProfessionalPhotoSession): boolean {
  let isSupported: boolean = false;
  try {
    isSupported = professionalPhotoSession.isExposureMeteringModeSupported(camera.ExposureMeteringMode.CENTER);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(`The isExposureMeteringModeSupported call failed. error code: ${err.code}`);
  }
  return isSupported;
}
```

