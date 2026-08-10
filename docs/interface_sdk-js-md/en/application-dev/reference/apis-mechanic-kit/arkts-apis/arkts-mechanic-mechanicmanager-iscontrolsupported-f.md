# isControlSupported

## Modules to Import

```TypeScript
import { mechanicManager } from 'kits/@kit.MechanicKit';
```

## isControlSupported

```TypeScript
function isControlSupported(mechDeviceType?: MechDeviceType): boolean
```

判断当前设备是否支持某类设备的具身控制

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-mechanicManager-function isControlSupported(mechDeviceType?: MechDeviceType): boolean--><!--Device-mechanicManager-function isControlSupported(mechDeviceType?: MechDeviceType): boolean-End-->

**System capability:** SystemCapability.Mechanic.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mechDeviceType | [MechDeviceType](arkts-mechanic-mechanicmanager-mechdevicetype-e.md) | No | 关联的设备类型 &lt;br&gt;默认值:如果未提供该参数，则代表所有类型设备，只要支持其中一种以上则返回支持 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns whether control is supported. |

## Examples

```TypeScript
console.info('Check whether control is supported');
// Call the isControlSupported method and pass MechDeviceType.GIMBAL_DEVICE to check whether gimbal device control is supported.
let isSupported = mechanicManager.isControlSupported(mechanicManager.MechDeviceType.GIMBAL_DEVICE);
console.info(`isSupported: ${isSupported}`);
```

