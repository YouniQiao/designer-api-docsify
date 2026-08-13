# getMaxRotationTime (System API)

## Modules to Import

```TypeScript
import { mechanicManager } from '@kit.MechanicKit';
```

## getMaxRotationTime

```TypeScript
function getMaxRotationTime(mechId: int): int
```

Obtains the maximum continuous rotation duration of a mechanical device.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-mechanicManager-function getMaxRotationTime(mechId: int): int--><!--Device-mechanicManager-function getMaxRotationTime(mechId: int): int-End-->

**System capability:** SystemCapability.Mechanic.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mechId | int | Yes | ID of the mechanical device. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Maximum rotation duration. Unit: millisecond. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |
| [33300001](../errorcode-mechanic.md#33300001-system-error) | Service exception. |
| [33300002](../errorcode-mechanic.md#33300002-device-not-connected) | Device not connected. |

## Examples

```TypeScript
console.info('Query maximum rotation time');
let maxTime = mechanicManager.getMaxRotationTime(0);
console.info(`'Query maximum rotation time successful, maximum time:' ${maxTime}`);
```

