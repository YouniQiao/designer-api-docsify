# getRotationLimits (System API)

## Modules to Import

```TypeScript
import { mechanicManager } from 'kits/@kit.MechanicKit';
```

## getRotationLimits

```TypeScript
function getRotationLimits(mechId: int): RotationLimits
```

Obtains the maximum rotation angles relative to the reference point for the specified mechanical device.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-mechanicManager-function getRotationLimits(mechId: int): RotationLimits--><!--Device-mechanicManager-function getRotationLimits(mechId: int): RotationLimits-End-->

**System capability:** SystemCapability.Mechanic.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mechId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | ID of the mechanical device. |

**Return value:**

| Type | Description |
| --- | --- |
| [RotationLimits](arkts-mechanic-mechanicmanager-rotationlimits-i-sys.md) | Maximum rotation angles. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |
| [33300001](../errorcode-mechanic.md#33300001-system-error) | Service exception. |
| [33300002](../errorcode-mechanic.md#33300002-device-not-connected) | Device not connected. |

## Examples

```TypeScript
console.info('Query rotation limit information');
let degreeLimit: mechanicManager.RotationLimits = mechanicManager.getRotationLimits(0);
console.info(`'Query the rotation limit information successfully, limit information:' ${degreeLimit}`);
```

