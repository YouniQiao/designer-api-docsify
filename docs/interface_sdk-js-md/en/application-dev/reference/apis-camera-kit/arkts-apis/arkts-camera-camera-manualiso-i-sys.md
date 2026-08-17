# ManualIso (System API)

ManualIso object.

**Inheritance/Implementation:** ManualIso extends [ManualIsoQuery](arkts-camera-camera-manualisoquery-i.md#manualisoquery-system-api)

**Since:** 23

<!--Device-camera-interface ManualIso--><!--Device-camera-interface ManualIso-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { camera } from 'camera';
```

## getIso

```TypeScript
getIso(): int
```

Gets current ISO.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-ManualIso-getIso(): int--><!--Device-ManualIso-getIso(): int-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| int | The current ISO. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) | Operation not allowed, the inputDevice or the session is abnormal.<br>**Applicable version:** 24 and later |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application.<br>**Applicable version:** 12 - 23 |

**Examples**

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

```TypeScript
setIso(iso: int): void
```

Sets ISO sensitivity value, within the range of getSupportedIsoRange. This control can not be effective if ExposureMode is set to EXPOSURE_MODE_LOCKED.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-ManualIso-setIso(iso: int): void--><!--Device-ManualIso-setIso(iso: int): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| iso | int | Yes | ISO |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) | Parameter missing or parameter type incorrect.<br>**Applicable version:** 12 - 23 |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) | Operation not allowed, the inputDevice or the session is abnormal.<br>**Applicable version:** 24 and later |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application.<br>**Applicable version:** 12 - 23 |

**Examples**

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

