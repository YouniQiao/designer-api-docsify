# getRotationAxesStatus (System API)

## Modules to Import

```TypeScript
import { mechanicManager } from 'kits/@kit.MechanicKit';
```

## getRotationAxesStatus

```TypeScript
function getRotationAxesStatus(mechId: number): RotationAxesStatus
```

Obtains the status of the rotation axes.

**Since:** 20

<!--Device-mechanicManager-function getRotationAxesStatus(mechId: int): RotationAxesStatus--><!--Device-mechanicManager-function getRotationAxesStatus(mechId: int): RotationAxesStatus-End-->

**System capability:** SystemCapability.Mechanic.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mechId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RotationAxesStatus](arkts-mechanic-mechanicmanager-rotationaxesstatus-i-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [33300001](../errorcode-mechanic.md#33300001-system-error) |
| [33300002](../errorcode-mechanic.md#33300002-device-not-connected) |

## Examples

```TypeScript
console.info('Query the rotation axis status');
let axisStatus: mechanicManager.RotationAxesStatus = mechanicManager.getRotationAxesStatus(0);
console.info(`'Query the rotation axis status successfully, axis state:' ${axisStatus}`);
```
