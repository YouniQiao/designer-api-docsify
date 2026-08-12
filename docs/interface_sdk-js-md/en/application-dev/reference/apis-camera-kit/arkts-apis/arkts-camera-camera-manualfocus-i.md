# ManualFocus

ManualFocus object.

**Inheritance/Implementation:** ManualFocus extends [ManualFocusQuery](arkts-camera-camera-manualfocusquery-i.md#ManualFocusQuery)

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-camera-interface ManualFocus extends ManualFocusQuery--><!--Device-camera-interface ManualFocus extends ManualFocusQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

## getFocusDistance

ArkTS-Dyn:
```TypeScript
getFocusDistance(): number
```

ArkTS-Sta:
```TypeScript
getFocusDistance(): double
```

Gets current focus distance, ranging from 0.0 to 1.0, with 0.0 being shortest distance at which the lens can focus and 1.0 the furthest. The default value is 1.0.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-ManualFocus-getFocusDistance(): double--><!--Device-ManualFocus-getFocusDistance(): double-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：double | The current focus distance. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400102](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400102-invalid-operation) | Operation not allowed, the inputDevice or the session is abnormal.<br>**Applicable version:** 24 and later |
| [7400103](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-session-not-configured) | Session not config. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application.<br>**Applicable version:** 12 - 23 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function getFocusDistance(professionalPhotoSession: camera.ProfessionalPhotoSession): number {
  let distance: number = 0;
  try {
    distance = professionalPhotoSession.getFocusDistance();
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(`The getFocusDistance call failed. error code: ${err.code}`);
  }
  return distance;
}
```

## setFocusDistance

ArkTS-Dyn:
```TypeScript
setFocusDistance(distance: number): void
```

ArkTS-Sta:
```TypeScript
setFocusDistance(distance: double): void
```

Sets focus distance. Possible distance values range from 0.0 to 1.0, with 0.0 being shortest distance at which the lens can focus and 1.0 the furthest. The default value is 1.0.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-ManualFocus-setFocusDistance(distance: double): void--><!--Device-ManualFocus-setFocusDistance(distance: double): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| distance | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Focus distance. |

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

function setFocusDistance(professionalPhotoSession: camera.ProfessionalPhotoSession): void {
  try {
    let distance: number = 0.5;
    professionalPhotoSession.setFocusDistance(distance);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(`The setFocusDistance call failed. error code: ${err.code}`);
  }
}
```

