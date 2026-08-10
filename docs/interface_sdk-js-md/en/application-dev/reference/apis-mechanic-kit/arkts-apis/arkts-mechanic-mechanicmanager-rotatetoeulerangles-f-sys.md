# rotateToEulerAngles (System API)

## Modules to Import

```TypeScript
import { mechanicManager } from 'kits/@kit.MechanicKit';
```

## rotateToEulerAngles

```TypeScript
function rotateToEulerAngles(mechId: int, angles: EulerAngles, duration: int): Promise<Result>
```

将机械设备旋转到绝对角度

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-mechanicManager-function rotateToEulerAngles(mechId: int, angles: EulerAngles, duration: int): Promise<Result>--><!--Device-mechanicManager-function rotateToEulerAngles(mechId: int, angles: EulerAngles, duration: int): Promise<Result>-End-->

**System capability:** SystemCapability.Mechanic.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mechId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 机械设备ID |
| angles | [EulerAngles](arkts-mechanic-mechanicmanager-eulerangles-i-sys.md) | Yes | 绝对角度位置 |
| duration | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 执行时间 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Result&gt; | 返回执行结果 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | Not system application. |
| 33300001 | Service exception. |
| 33300002 | Device not connected. |

## Examples

```TypeScript
let degree: mechanicManager.EulerAngles = {
  yaw: 0.9 * Math.PI,
  roll: 0.9 * Math.PI,
  pitch: 0.9 * Math.PI
}
mechanicManager.rotateToEulerAngles(0, degree, 500)
  .then((result: mechanicManager.Result) => {
    console.info(`'Rotate result:' ${result}`);
  });
console.info('End rotation');
```

