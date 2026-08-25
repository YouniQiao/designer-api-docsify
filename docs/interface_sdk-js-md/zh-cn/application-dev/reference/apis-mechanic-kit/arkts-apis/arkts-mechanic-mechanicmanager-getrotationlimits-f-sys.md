# getRotationLimits（系统接口）

## 导入模块

```TypeScript
import { mechanicManager } from 'kits/@kit.MechanicKit';
```

## getRotationLimits

```TypeScript
function getRotationLimits(mechId: number): RotationLimits
```

Obtains the maximum rotation angles relative to the reference point for the specified mechanical device.

**起始版本：** 20

**系统能力：** SystemCapability.Mechanic.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mechId | number | 是 |

**返回值：**

| 类型 |
| --- |
| [RotationLimits](arkts-mechanic-mechanicmanager-rotationlimits-i-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [33300001](../errorcode-mechanic.md#33300001-系统错误) |
| [33300002](../errorcode-mechanic.md#33300002-设备未连接) |
