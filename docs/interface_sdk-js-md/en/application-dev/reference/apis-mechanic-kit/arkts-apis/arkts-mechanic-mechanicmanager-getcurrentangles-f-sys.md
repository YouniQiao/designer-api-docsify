# getCurrentAngles (System API)

## Modules to Import

```TypeScript
import { mechanicManager } from 'kits/@kit.MechanicKit';
```

## getCurrentAngles

```TypeScript
function getCurrentAngles(mechId: int): EulerAngles
```

获取机械设备的当前角度

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-mechanicManager-function getCurrentAngles(mechId: int): EulerAngles--><!--Device-mechanicManager-function getCurrentAngles(mechId: int): EulerAngles-End-->

**System capability:** SystemCapability.Mechanic.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mechId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 机械设备ID |

**Return value:**

| Type | Description |
| --- | --- |
| [EulerAngles](arkts-mechanic-mechanicmanager-eulerangles-i-sys.md) | 返回当前角度 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | Not system application. |
| 33300001 | Service exception. |
| 33300002 | Device not connected. |

## Examples

```TypeScript
console.info('Query current location');
let currentAngles: mechanicManager.EulerAngles = mechanicManager.getCurrentAngles(0);
console.info(`'Query current location, location:' ${currentAngles}`);
```

