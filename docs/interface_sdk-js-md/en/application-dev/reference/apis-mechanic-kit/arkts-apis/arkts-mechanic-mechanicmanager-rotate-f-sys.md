# rotate (System API)

## Modules to Import

```TypeScript
import { mechanicManager } from '@kit.MechanicKit';
```

## rotate

```TypeScript
function rotate(mechId: int, angles: RotationAngles, duration: int): Promise<Result>
```

Rotates a mechanical device to the relative angles.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-mechanicManager-function rotate(mechId: int, angles: RotationAngles, duration: int): Promise<Result>--><!--Device-mechanicManager-function rotate(mechId: int, angles: RotationAngles, duration: int): Promise<Result>-End-->

**System capability:** SystemCapability.Mechanic.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mechId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | ID of the mechanical device. |
| angles | [RotationAngles](arkts-mechanic-mechanicmanager-rotationangles-i-sys.md) | Yes | Relative angles. |
| duration | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Rotation duration. Unit: millisecond. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Result&gt; | Promise that return the execution result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |
| [33300001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-mechanic-kit/errorcode-mechanic.md#33300001-system-error) | Service exception. |
| [33300002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-mechanic-kit/errorcode-mechanic.md#33300002-device-not-connected) | Device not connected. |

## Examples

```TypeScript
console.info('Start rotate');
let degree: mechanicManager.RotationAngles = {
  yaw: 0.1 * Math.PI,
  roll: 0.0,
  pitch: 0.0
}
mechanicManager.rotate(0, degree, 500)
  .then((result: mechanicManager.Result) => {
    console.info(`'Rotate result:' ${result}`);
  });
console.info('End rotation');
```

