# @ohos.batteryInfo

该模块主要提供电池状态和充放电状态的查询接口。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-declare namespace batteryInfo--><!--Device-unnamed-declare namespace batteryInfo-End-->

**System capability:** SystemCapability.PowerManager.BatteryManager.Core

## Modules to Import

```TypeScript
import { batteryInfo } from 'kits/@kit.BasicServicesKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [batteryCapacityLevel](arkts-basicservices-batteryinfo-batterycapacitylevel-f.md#batterycapacitylevel) | 表示当前设备电池电量的等级。 |
| [batterySOC](arkts-basicservices-batteryinfo-batterysoc-f.md#batterysoc) | 表示当前设备剩余电池电量百分比，取值范围是[0，100]。 |
| [batteryTemperature](arkts-basicservices-batteryinfo-batterytemperature-f.md#batterytemperature) | 表示当前设备电池的温度，单位0.1摄氏度。 |
| [chargingStatus](arkts-basicservices-batteryinfo-chargingstatus-f.md#chargingstatus) | 表示当前设备电池的充电状态。 |
| [healthStatus](arkts-basicservices-batteryinfo-healthstatus-f.md#healthstatus) | 表示当前设备电池的健康状态。 |
| [isBatteryPresent](arkts-basicservices-batteryinfo-isbatterypresent-f.md#isbatterypresent) | 表示当前设备是否支持电池或者电池是否在位。true表示支持电池或电池在位，false表示不支持电池或电池不在位，默认为false。 |
| [nowCurrent](arkts-basicservices-batteryinfo-nowcurrent-f.md#nowcurrent) | 表示当前设备电池的电流，单位毫安。 |
| [pluggedType](arkts-basicservices-batteryinfo-pluggedtype-f.md#pluggedtype) | 表示当前设备连接的充电器类型。 |
| [technology](arkts-basicservices-batteryinfo-technology-f.md#technology) | 表示当前设备电池的技术型号。 |
| [voltage](arkts-basicservices-batteryinfo-voltage-f.md#voltage) | 表示当前设备电池的电压，单位微伏。 |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [estimatedRemainingChargeTime](arkts-basicservices-batteryinfo-estimatedremainingchargetime-f-sys.md#estimatedremainingchargetime) | 获取当前设备充满电的预估时间，单位毫秒。 |
| [getBatteryConfig](arkts-basicservices-batteryinfo-getbatteryconfig-f-sys.md#getbatteryconfig) | 按场景名称查询电池配置。 |
| [isBatteryConfigSupported](arkts-basicservices-batteryinfo-isbatteryconfigsupported-f-sys.md#isbatteryconfigsupported) | 检查是否按场景名称启用电池配置。 |
| [remainingEnergy](arkts-basicservices-batteryinfo-remainingenergy-f-sys.md#remainingenergy) | 获取当前设备电池的剩余容量，单位毫安时。 |
| [setBatteryConfig](arkts-basicservices-batteryinfo-setbatteryconfig-f-sys.md#setbatteryconfig) | 按场景名称设置电池配置。 |
| [totalEnergy](arkts-basicservices-batteryinfo-totalenergy-f-sys.md#totalenergy) | 获取当前设备电池的总容量，单位毫安时。 |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [BatteryCapacityLevel](arkts-basicservices-batteryinfo-batterycapacitylevel-e.md) | 表示电池电量等级的枚举。 |
| [BatteryChargeState](arkts-basicservices-batteryinfo-batterychargestate-e.md) | 表示电池充电状态的枚举。 |
| [BatteryHealthState](arkts-basicservices-batteryinfo-batteryhealthstate-e.md) | 表示电池健康状态的枚举。 |
| [BatteryPluggedType](arkts-basicservices-batteryinfo-batterypluggedtype-e.md) | 表示连接的充电器类型的枚举。 |
| [CommonEventBatteryChangedKey](arkts-basicservices-batteryinfo-commoneventbatterychangedkey-e.md) | 表示COMMON_EVENT_BATTERY_CHANGED通用事件附加信息的查询键。 |

