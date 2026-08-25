# @ohos.batteryStatistics

该模块提供软硬件耗电统计信息的查询接口，支持查询应用和硬件单元的耗电量与耗电百分比，适用于开发者需要监控和分析设备耗电情况的场景，便于定位高耗电应用或硬件组件，从而优化应用的能耗表现。

> **说明：**&gt;
> - 本模块接口为系统接口。

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.PowerManager.BatteryStatistics

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { batteryStats } from '@kit.BasicServicesKit';
```

## 汇总

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [getAppPowerPercent](arkts-basicservices-batterystats-getapppowerpercent-f-sys.md) |
| [getAppPowerValue](arkts-basicservices-batterystats-getapppowervalue-f-sys.md) |
| [getBatteryStats](arkts-basicservices-batterystats-getbatterystats-f-sys.md) |
| [getBatteryStats](arkts-basicservices-batterystats-getbatterystats-f-sys.md) |
| [getHardwareUnitPowerPercent](arkts-basicservices-batterystats-gethardwareunitpowerpercent-f-sys.md) |
| [getHardwareUnitPowerValue](arkts-basicservices-batterystats-gethardwareunitpowervalue-f-sys.md) |
<!--DelEnd-->

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [BatteryStatsInfo](arkts-basicservices-batterystats-batterystatsinfo-i-sys.md) |
<!--DelEnd-->

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [ConsumptionType](arkts-basicservices-batterystats-consumptiontype-e-sys.md) |
<!--DelEnd-->
