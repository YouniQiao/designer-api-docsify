# @ohos.batteryStatistics

该模块提供软硬件耗电统计信息的查询接口。

> **说明：**
> 
> - 本模块接口为系统接口。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-unnamed-declare namespace batteryStats--><!--Device-unnamed-declare namespace batteryStats-End-->

**System capability:** SystemCapability.PowerManager.BatteryStatistics

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { batteryStats } from 'kits/@kit.BasicServicesKit';
```

## Summary

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [getAppPowerPercent](arkts-basicservices-batterystats-getapppowerpercent-f-sys.md#getapppowerpercent) | 获取应用的耗电百分比。 |
| [getAppPowerValue](arkts-basicservices-batterystats-getapppowervalue-f-sys.md#getapppowervalue) | 获取应用的耗电量，单位毫安时。 |
| [getBatteryStats](arkts-basicservices-batterystats-getbatterystats-f-sys.md#getbatterystats) | 获取耗电信息列表。使用Promise异步回调。 |
| [getBatteryStats](arkts-basicservices-batterystats-getbatterystats-f-sys.md#getbatterystats-1) | 获取耗电信息列表。使用callback异步回调。 |
| [getHardwareUnitPowerPercent](arkts-basicservices-batterystats-gethardwareunitpowerpercent-f-sys.md#gethardwareunitpowerpercent) | 根据耗电类型获取硬件单元的耗电百分比。 |
| [getHardwareUnitPowerValue](arkts-basicservices-batterystats-gethardwareunitpowervalue-f-sys.md#gethardwareunitpowervalue) | 根据耗电类型获取硬件单元的耗电量，单位毫安时。 |
<!--DelEnd-->

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [BatteryStatsInfo](arkts-basicservices-batterystats-batterystatsinfo-i-sys.md) | 设备的耗电信息。 |
<!--DelEnd-->

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [ConsumptionType](arkts-basicservices-batterystats-consumptiontype-e-sys.md) | 表示电量消耗类型的枚举值。 |
<!--DelEnd-->

