# isControlSupported

## Modules to Import

```TypeScript
import { mechanicManager } from '@kit.MechanicKit';
```

## isControlSupported

```TypeScript
function isControlSupported(mechDeviceType?: MechDeviceType): boolean
```

Checks whether the current device supports embodied control for a specific type of device.

**Since:** 26.0.0

<!--Device-mechanicManager-function isControlSupported(mechDeviceType?: MechDeviceType): boolean--><!--Device-mechanicManager-function isControlSupported(mechDeviceType?: MechDeviceType): boolean-End-->

**System capability:** SystemCapability.Mechanic.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [mechDeviceType](arkts-mechanic-mechanicmanager-mechinfo-i.md) | [MechDeviceType](arkts-mechanic-mechanicmanager-mechdevicetype-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
console.info('Check whether control is supported');
// Call the isControlSupported method and pass MechDeviceType.GIMBAL_DEVICE to check whether gimbal device control is supported.
let isSupported = mechanicManager.isControlSupported(mechanicManager.MechDeviceType.GIMBAL_DEVICE);
console.info(`isSupported: ${isSupported}`);
```
