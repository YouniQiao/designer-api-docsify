# @ohos.batteryInfo

该模块主要提供电池状态和充放电状态的查询接口， 支持查询剩余电量、充电状态、健康状态、充电器类型、电压、电流、温度等电池信息， 适用于需要根据电池状态调整应用行为（如低电量时降低功耗、充电时启动高耗能任务）的场景， 可帮助开发者实时感知设备电池状况，优化应用功耗策略并提升用户体验。

**起始版本：** 6

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

## 导入模块

```TypeScript
import { batteryInfo } from 'kits/@kit.BasicServicesKit';
```

## 汇总

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [getBatteryConfig](arkts-basicservices-batteryinfo-getbatteryconfig-f-sys.md) |
| [isBatteryConfigSupported](arkts-basicservices-batteryinfo-isbatteryconfigsupported-f-sys.md) |
| [setBatteryConfig](arkts-basicservices-batteryinfo-setbatteryconfig-f-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [BatteryCapacityLevel](arkts-basicservices-batteryinfo-batterycapacitylevel-e.md) |
| [BatteryChargeState](arkts-basicservices-batteryinfo-batterychargestate-e.md) |
| [BatteryHealthState](arkts-basicservices-batteryinfo-batteryhealthstate-e.md) |
| [BatteryPluggedType](arkts-basicservices-batteryinfo-batterypluggedtype-e.md) |
| [CommonEventBatteryChangedKey](arkts-basicservices-batteryinfo-commoneventbatterychangedkey-e.md) |

### 常量

| 名称 |
| --- |
| [batteryCapacityLevel](arkts-basicservices-batteryinfo-con.md#batterycapacitylevel) |
| [batterySOC](arkts-basicservices-batteryinfo-con.md#batterysoc) |
| [batteryTemperature](arkts-basicservices-batteryinfo-con.md#batterytemperature) |
| [chargingStatus](arkts-basicservices-batteryinfo-con.md#chargingstatus) |
| [healthStatus](arkts-basicservices-batteryinfo-con.md#healthstatus) |
| [isBatteryPresent](arkts-basicservices-batteryinfo-con.md#isbatterypresent) |
| [nowCurrent](arkts-basicservices-batteryinfo-con.md#nowcurrent) |
| [pluggedType](arkts-basicservices-batteryinfo-con.md#pluggedtype) |
| [technology](arkts-basicservices-batteryinfo-con.md#technology) |
| [voltage](arkts-basicservices-batteryinfo-con.md#voltage) |

<!--Del-->
### 常量（系统接口）

| 名称 |
| --- |
| [estimatedRemainingChargeTime](arkts-basicservices-batteryinfo-con-sys.md#estimatedremainingchargetime) |
| [remainingEnergy](arkts-basicservices-batteryinfo-con-sys.md#remainingenergy) |
| [totalEnergy](arkts-basicservices-batteryinfo-con-sys.md#totalenergy) |
<!--DelEnd-->
