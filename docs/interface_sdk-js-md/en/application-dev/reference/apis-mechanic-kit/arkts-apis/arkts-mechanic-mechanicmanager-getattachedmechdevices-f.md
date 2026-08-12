# getAttachedMechDevices

## Modules to Import

```TypeScript
import { mechanicManager } from '@kit.MechanicKit';
```

## getAttachedMechDevices

```TypeScript
function getAttachedMechDevices(): MechInfo[]
```

Obtain the list of connected mechanical devices.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-mechanicManager-function getAttachedMechDevices(): MechInfo[]--><!--Device-mechanicManager-function getAttachedMechDevices(): MechInfo[]-End-->

**System capability:** SystemCapability.Mechanic.Core

**Return value:**

| Type | Description |
| --- | --- |
| [MechInfo](arkts-mechanic-mechanicmanager-mechinfo-i.md)[] | List of connected mechanical devices. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [33300001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-mechanic-kit/errorcode-mechanic.md#33300001-system-error) | Service exception. |

## Examples

```TypeScript
console.info('Query device list');
let mechanicInfos = mechanicManager.getAttachedMechDevices();
console.info(`'device list:' ${mechanicInfos}`);
```

