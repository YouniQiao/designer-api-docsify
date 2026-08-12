# ManualIso

ManualIso object.

**Inheritance/Implementation:** ManualIso extends [ManualIsoQuery](arkts-camera-camera-manualisoquery-i.md#ManualIsoQuery)

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-camera-interface ManualIso extends ManualIsoQuery--><!--Device-camera-interface ManualIso extends ManualIsoQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

## getIso

ArkTS-Dyn:
```TypeScript
getIso(): number
```

ArkTS-Sta:
```TypeScript
getIso(): int
```

Gets current ISO.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-ManualIso-getIso(): int--><!--Device-ManualIso-getIso(): int-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | The current ISO. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400102](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400102-invalid-operation) | Operation not allowed, the inputDevice or the session is abnormal.<br>**Applicable version:** 24 and later |
| [7400103](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-session-not-configured) | Session not config. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application.<br>**Applicable version:** 12 - 23 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function getIso(professionalPhotoSession: camera.ProfessionalPhotoSession): number {
  let iso: number = 0;
  try {
    iso = professionalPhotoSession.getIso();
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(`The getIso call failed. error code: ${err.code}`);
  }
  return iso;
}
```

## setIso

ArkTS-Dyn:
```TypeScript
setIso(iso: number): void
```

ArkTS-Sta:
```TypeScript
setIso(iso: int): void
```

Sets ISO sensitivity value, within the range of getSupportedIsoRange. This control can not be effective if ExposureMode is set to EXPOSURE_MODE_LOCKED.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-ManualIso-setIso(iso: int): void--><!--Device-ManualIso-setIso(iso: int): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| iso | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | ISO |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400101](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400101-invalid-parameter) | Parameter missing or parameter type incorrect.<br>**Applicable version:** 12 - 23 |
| [7400102](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400102-invalid-operation) | Operation not allowed, the inputDevice or the session is abnormal.<br>**Applicable version:** 24 and later |
| [7400103](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-session-not-configured) | Session not config. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application.<br>**Applicable version:** 12 - 23 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function setIso(professionalPhotoSession: camera.ProfessionalPhotoSession): void {
  try {
    let iso: number = 200;
    professionalPhotoSession.setIso(iso);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(`The setIso call failed. error code: ${err.code}`);
  }
}
```

