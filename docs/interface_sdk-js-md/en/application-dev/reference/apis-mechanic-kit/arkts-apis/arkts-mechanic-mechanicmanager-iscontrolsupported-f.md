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

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-mechanicManager-function isControlSupported(mechDeviceType?: MechDeviceType): boolean--><!--Device-mechanicManager-function isControlSupported(mechDeviceType?: MechDeviceType): boolean-End-->

**System capability:** SystemCapability.Mechanic.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mechDeviceType | [MechDeviceType](arkts-mechanic-mechanicmanager-mechdevicetype-e.md) | No | Associated device type. &lt;br&gt;Default: If this parameter is not provided, it represents all device types. As long as one or more types are supported, the result returned will be supported. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns whether embodied control is supported. |

