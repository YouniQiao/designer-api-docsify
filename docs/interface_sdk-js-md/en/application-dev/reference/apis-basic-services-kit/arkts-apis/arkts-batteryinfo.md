# @ohos.batteryInfo

The **batteryInfo** module provides APIs for querying the charger type, battery health status, and battery charging status.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-declare namespace batteryInfo--><!--Device-unnamed-declare namespace batteryInfo-End-->

**System capability:** SystemCapability.PowerManager.BatteryManager.Core

## Modules to Import

```TypeScript
import { batteryInfo } from '@kit.BasicServicesKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [batteryCapacityLevel](arkts-basicservices-batteryinfo-batterycapacitylevel-f.md) | Battery level of the device. |
| [batterySOC](arkts-basicservices-batteryinfo-batterysoc-f.md) | Battery state of charge (SoC) of the device, in unit of percentage, which ranges from 0 to 100. |
| [batteryTemperature](arkts-basicservices-batteryinfo-batterytemperature-f.md) | Battery temperature of the device, in unit of 0.1°C. |
| [chargingStatus](arkts-basicservices-batteryinfo-chargingstatus-f.md) | Battery charging state of the current device. |
| [healthStatus](arkts-basicservices-batteryinfo-healthstatus-f.md) | Battery health status of the device. |
| [isBatteryPresent](arkts-basicservices-batteryinfo-isbatterypresent-f.md) | Whether the battery is supported or present. The value **true** means that the battery is supported or present; **false** means the opposite.Default value: **false**. |
| [nowCurrent](arkts-basicservices-batteryinfo-nowcurrent-f.md) | Battery current of the device, in unit of mA. |
| [pluggedType](arkts-basicservices-batteryinfo-pluggedtype-f.md) | Charger type of the device. |
| [technology](arkts-basicservices-batteryinfo-technology-f.md) | Battery technology of the device. |
| [voltage](arkts-basicservices-batteryinfo-voltage-f.md) | Battery voltage of the device, in unit of microvolt. |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [estimatedRemainingChargeTime](arkts-basicservices-batteryinfo-estimatedremainingchargetime-f-sys.md) | Estimated time for fully charging the current device, in unit of milliseconds. This is a system API. |
| [getBatteryConfig](arkts-basicservices-batteryinfo-getbatteryconfig-f-sys.md) | Obtains the battery configuration based on the specified scenario. |
| [isBatteryConfigSupported](arkts-basicservices-batteryinfo-isbatteryconfigsupported-f-sys.md) | Checks whether the battery configuration is enabled based on the specified scenario. |
| [remainingEnergy](arkts-basicservices-batteryinfo-remainingenergy-f-sys.md) | Remaining battery capacity of the device, in unit of mAh. This is a system API. |
| [setBatteryConfig](arkts-basicservices-batteryinfo-setbatteryconfig-f-sys.md) | Sets the battery configuration based on the specified scenario. |
| [totalEnergy](arkts-basicservices-batteryinfo-totalenergy-f-sys.md) | Total battery capacity of the device, in unit of mAh. This is a system API. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [BatteryCapacityLevel](arkts-basicservices-batteryinfo-batterycapacitylevel-e.md) | Enumerates battery levels.@enum { int } |
| [BatteryChargeState](arkts-basicservices-batteryinfo-batterychargestate-e.md) | Enumerates charging states.@enum { int } |
| [BatteryHealthState](arkts-basicservices-batteryinfo-batteryhealthstate-e.md) | Enumerates battery health states.@enum { int } |
| [BatteryPluggedType](arkts-basicservices-batteryinfo-batterypluggedtype-e.md) | Enumerates charger types.@enum { int } |
| [CommonEventBatteryChangedKey](arkts-basicservices-batteryinfo-commoneventbatterychangedkey-e.md) | Enumerates keys for querying the additional information about the **COMMON_EVENT_BATTERY_CHANGED** event.@enum { string } |

