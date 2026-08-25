# getAppPowerPercent（系统接口）

## 导入模块

```TypeScript
import { batteryStats } from 'kits/@kit.BasicServicesKit';
```

## getAppPowerPercent

```TypeScript
function getAppPowerPercent(uid: number): number
```

获取应用的耗电百分比，该百分比表示应用耗电量占总耗电量的比例。

**起始版本：** 8

**系统能力：** SystemCapability.PowerManager.BatteryStatistics

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uid | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [4600101](../errorcode-batteryStatistics.md#4600101-连接服务失败) |
