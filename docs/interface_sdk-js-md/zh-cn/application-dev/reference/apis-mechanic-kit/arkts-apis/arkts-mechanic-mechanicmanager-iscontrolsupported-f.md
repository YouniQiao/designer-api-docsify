# isControlSupported

## 导入模块

```TypeScript
import { mechanicManager } from 'kits/@kit.MechanicKit';
```

## isControlSupported

```TypeScript
function isControlSupported(mechDeviceType?: MechDeviceType): boolean
```

判断当前设备是否支持某类设备的具身控制

**起始版本：** 26.0.0

**系统能力：** SystemCapability.Mechanic.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [mechDeviceType](arkts-mechanic-mechanicmanager-mechinfo-i.md) | [MechDeviceType](arkts-mechanic-mechanicmanager-mechdevicetype-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| boolean |
