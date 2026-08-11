# getAttachedMechDevices

## Modules to Import

```TypeScript
import { mechanicManager } from 'kits/@kit.MechanicKit';
```

## getAttachedMechDevices

```TypeScript
function getAttachedMechDevices(): MechInfo[]
```

Obtain the list of connected mechanical devices.

**Since:** 20

<!--Device-mechanicManager-function getAttachedMechDevices(): MechInfo[]--><!--Device-mechanicManager-function getAttachedMechDevices(): MechInfo[]-End-->

**System capability:** SystemCapability.Mechanic.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MechInfo](arkts-mechanic-mechanicmanager-mechinfo-i.md)[] |

**Error codes:**

| Error Code ID |
| --- |
| [33300001](../errorcode-mechanic.md#33300001-system-error) |

## Examples

```TypeScript
console.info('Query device list');
// Call getAttachedMechDevices to obtain the list of attached mechanic devices.
let mechanicInfos = mechanicManager.getAttachedMechDevices();
console.info(`'device list:' ${mechanicInfos}`);
```
