# getHardwareUnitPowerValue（系统接口）

## getHardwareUnitPowerValue

```TypeScript
function getHardwareUnitPowerValue(type: ConsumptionType): number
```

根据耗电类型获取硬件单元的耗电量，单位毫安时。

**起始版本：** 23

**废弃版本：** -1

<!--Device-batteryStats-function getHardwareUnitPowerValue(type: ConsumptionType): double--><!--Device-batteryStats-function getHardwareUnitPowerValue(type: ConsumptionType): double-End-->

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [4600101](../../apis-basic-services-kit/errorcode-batteryStatistics.md#4600101-连接服务失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
try {
    let powerValue = batteryStats.getHardwareUnitPowerValue(batteryStats.ConsumptionType.CONSUMPTION_TYPE_SCREEN);
    console.info('battery statistics value of hardware is: ' + powerValue);
} catch (err) {
    console.error(`Failed to get battery statistics value of hardware. Code: ${err.code}, message: ${err.message}`);
}
```
