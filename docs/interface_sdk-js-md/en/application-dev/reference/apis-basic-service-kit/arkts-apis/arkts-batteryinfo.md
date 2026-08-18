# @ohos.batteryInfo

/*
 Copyright (c) 2025 Huawei Device Co., Ltd.
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
 http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 /


**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

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
| [batteryCapacityLevel](arkts-basicservices-batteryinfo-batterycapacitylevel-f.md#batterycapacitylevel) | Battery level of the device. |
| [batterySOC](arkts-basicservices-batteryinfo-batterysoc-f.md#batterysoc) | Battery state of charge (SoC) of the device, in unit of percentage, which ranges from 0 to 100. |
| [batteryTemperature](arkts-basicservices-batteryinfo-batterytemperature-f.md#batterytemperature) | Battery temperature of the device, in unit of 0.1°C. |
| [chargingStatus](arkts-basicservices-batteryinfo-chargingstatus-f.md#chargingstatus) | Battery charging state of the current device. |
| [healthStatus](arkts-basicservices-batteryinfo-healthstatus-f.md#healthstatus) | Battery health status of the device. |
| [isBatteryPresent](arkts-basicservices-batteryinfo-isbatterypresent-f.md#isbatterypresent) | Whether the battery is supported or present. The value **true** means that the battery is supported or present; **false** means the opposite. Default value: **false**. |
| [nowCurrent](arkts-basicservices-batteryinfo-nowcurrent-f.md#nowcurrent) | Battery current of the device, in unit of mA. |
| [pluggedType](arkts-basicservices-batteryinfo-pluggedtype-f.md#pluggedtype) | Charger type of the device. |
| [technology](arkts-basicservices-batteryinfo-technology-f.md#technology) | Battery technology of the device. |
| [voltage](arkts-basicservices-batteryinfo-voltage-f.md#voltage) | Battery voltage of the device, in unit of microvolt. |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [estimatedRemainingChargeTime](arkts-basicservices-batteryinfo-estimatedremainingchargetime-f-sys.md#estimatedremainingchargetime-system-api) | Estimated time for fully charging the current device, in unit of milliseconds. This is a system API. |
| [getBatteryConfig](arkts-basicservices-batteryinfo-getbatteryconfig-f-sys.md#getbatteryconfig) | Obtains the battery configuration based on the specified scenario. |
| [isBatteryConfigSupported](arkts-basicservices-batteryinfo-isbatteryconfigsupported-f-sys.md#isbatteryconfigsupported) | Checks whether the battery configuration is enabled based on the specified scenario. |
| [remainingEnergy](arkts-basicservices-batteryinfo-remainingenergy-f-sys.md#remainingenergy-system-api) | Remaining battery capacity of the device, in unit of mAh. This is a system API. |
| [setBatteryConfig](arkts-basicservices-batteryinfo-setbatteryconfig-f-sys.md#setbatteryconfig) | Sets the battery configuration based on the specified scenario. |
| [totalEnergy](arkts-basicservices-batteryinfo-totalenergy-f-sys.md#totalenergy-system-api) | Total battery capacity of the device, in unit of mAh. This is a system API. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [BatteryCapacityLevel](arkts-basicservices-batteryinfo-batterycapacitylevel-e.md) | Enumerates battery levels. |
| [BatteryChargeState](arkts-basicservices-batteryinfo-batterychargestate-e.md) | Enumerates charging states. |
| [BatteryHealthState](arkts-basicservices-batteryinfo-batteryhealthstate-e.md) | Enumerates battery health states. |
| [BatteryPluggedType](arkts-basicservices-batteryinfo-batterypluggedtype-e.md) | Enumerates charger types. |
| [CommonEventBatteryChangedKey](arkts-basicservices-batteryinfo-commoneventbatterychangedkey-e.md) | Enumerates keys for querying the additional information about the **COMMON_EVENT_BATTERY_CHANGED** event. |

