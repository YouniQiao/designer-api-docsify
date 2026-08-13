# getRotationLimits (System API)

## Modules to Import

```TypeScript
import { mechanicManager } from '@kit.MechanicKit';
```

## getRotationLimits

```TypeScript
function getRotationLimits(mechId: number): RotationLimits
```

Obtains the maximum rotation angles relative to the reference point for the specified mechanical device.

**Since:** 23

**Deprecated since:** -1

<!--Device-mechanicManager-function getRotationLimits(mechId: int): RotationLimits--><!--Device-mechanicManager-function getRotationLimits(mechId: int): RotationLimits-End-->

**System capability:** SystemCapability.Mechanic.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mechId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RotationLimits](arkts-mechanic-mechanicmanager-rotationlimits-i-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [33300001](../errorcode-mechanic.md#33300001-system-error) |
| [33300002](../errorcode-mechanic.md#33300002-device-not-connected) |

## Examples

```TypeScript
console.info('Query rotation limit information');
let degreeLimit: mechanicManager.RotationLimits = mechanicManager.getRotationLimits(0);
console.info(`'Query the rotation limit information successfully, limit information:' ${degreeLimit}`);
```
