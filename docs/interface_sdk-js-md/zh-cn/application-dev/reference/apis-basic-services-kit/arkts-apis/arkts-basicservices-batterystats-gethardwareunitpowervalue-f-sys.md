# getHardwareUnitPowerValue（系统接口）

## 导入模块

```TypeScript
import { batteryStats } from 'kits/@kit.BasicServicesKit';
```

## getHardwareUnitPowerValue

```TypeScript
function getHardwareUnitPowerValue(type: ConsumptionType): number
```

根据耗电类型获取硬件单元的耗电量，单位毫安时。适用于需要精确耗电数值的场景。如需比较不同硬件单元耗电占比，请使用[getHardwareUnitPowerPercent](arkts-basicservices-batterystats-gethardwareunitpowerpercent-f-sys.md)获取相对百分比。

**起始版本：** 8

**系统能力：** SystemCapability.PowerManager.BatteryStatistics

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [ConsumptionType](arkts-basicservices-batterystats-consumptiontype-e-sys.md) | 是 |

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
