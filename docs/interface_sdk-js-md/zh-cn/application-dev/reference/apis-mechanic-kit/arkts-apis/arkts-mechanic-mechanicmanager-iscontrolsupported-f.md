# isControlSupported

## 导入模块

```TypeScript
import { mechanicManager } from '@kit.MechanicKit';
```

## isControlSupported

```TypeScript
function isControlSupported(mechDeviceType?: MechDeviceType): boolean
```

判断当前设备是否支持某类设备的具身控制

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**系统能力：** SystemCapability.Mechanic.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [mechDeviceType](arkts-mechanic-mechanicmanager-mechinfo-i.md) | [MechDeviceType](arkts-mechanic-mechanicmanager-mechdevicetype-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| boolean |

**示例**

```TypeScript
console.info('Check whether control is supported');
// 调用isControlSupported方法，传入MechDeviceType.GIMBAL_DEVICE类型，判断是否支持云台设备控制
let isSupported = mechanicManager.isControlSupported(mechanicManager.MechDeviceType.GIMBAL_DEVICE);
console.info(`isSupported: ${isSupported}`);
```
