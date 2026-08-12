# AutoExposureQuery

AutoExposureQuery provides APIs to query the automatic exposure feature of a camera device.  
> 
> - In this version, a compatibility change was made that preserved the initial version information of inner
> elements. As a result, you might see outer element's @since version number being higher than that of the inner
> elements. However, this discrepancy does not affect the functionality of the interface.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-camera-interface AutoExposureQuery--><!--Device-camera-interface AutoExposureQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

## getExposureBiasRange

ArkTS-Dyn:
```TypeScript
getExposureBiasRange(): Array<number>
```

ArkTS-Sta:
```TypeScript
getExposureBiasRange(): Array<double>
```

Obtains the exposure compensation values of the camera device.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-AutoExposureQuery-getExposureBiasRange(): Array<double>--><!--Device-AutoExposureQuery-getExposureBiasRange(): Array<double>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;double&gt; | Array of compensation values. If the operation fails, an error code defined in [CameraErrorCode]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400103](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-session-not-configured) | Session not config, only throw in session usage. |

## isExposureMeteringModeSupported

```TypeScript
isExposureMeteringModeSupported(aeMeteringMode: ExposureMeteringMode): boolean
```

Checks whether the specified exposure metering mode is supported.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-AutoExposureQuery-isExposureMeteringModeSupported(aeMeteringMode: ExposureMeteringMode): boolean--><!--Device-AutoExposureQuery-isExposureMeteringModeSupported(aeMeteringMode: ExposureMeteringMode): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| aeMeteringMode | [ExposureMeteringMode](arkts-camera-camera-exposuremeteringmode-e.md) | Yes | Exposure metering mode. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether the exposure metering mode is supported. **true** if supported, **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400101](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400101-invalid-parameter) | Parameter missing or parameter type incorrect.<br>**Applicable version:** 12 - 23 |
| [7400103](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-session-not-configured) | Session not config, only throw in session usage. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application.<br>**Applicable version:** 12 - 23 |

## Examples

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

## isExposureModeSupported

```TypeScript
isExposureModeSupported(aeMode: ExposureMode): boolean
```

Checks whether an exposure mode is supported.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-AutoExposureQuery-isExposureModeSupported(aeMode: ExposureMode): boolean--><!--Device-AutoExposureQuery-isExposureModeSupported(aeMode: ExposureMode): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| aeMode | [ExposureMode](arkts-camera-camera-exposuremode-e.md) | Yes | Exposure mode. If the input parameter is null or undefined, it is treated as 0 and exposure is locked. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result for the support of the exposure mode. **true** if supported, **false** otherwise. If the operation fails, undefined is returned and an error code defined in [CameraErrorCode]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400103](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-session-not-configured) | Session not config, only throw in session usage. |

