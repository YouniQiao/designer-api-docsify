# BatteryResponse

包含充电状态及剩余电量的对象。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 6

<!--Device-unnamed-export interface BatteryResponse--><!--Device-unnamed-export interface BatteryResponse-End-->

**System capability:** SystemCapability.PowerManager.BatteryManager.Lite

## Modules to Import

```TypeScript
import { GetStatusOptions, BatteryResponse } from 'kits/@kit.BasicServicesKit';
```

## charging

```TypeScript
charging: boolean
```

当前电池是否在充电中。true表示在充电，false表示没有充电，默认为false。

**说明：** 除Lite Wearable外，从API Version 6开始不再维护，建议使用
[`batteryInfo.chargingStatus`](../../../reference/apis-basic-services-kit/js-apis-battery-info.md#常量)替代。

**Type:** boolean

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 6

**Substitutes:** [@ohos.batteryInfo:batteryInfo.chargingStatus](arkts-basicservices-batteryinfo-con.md#chargingstatus)

<!--Device-BatteryResponse-charging: boolean--><!--Device-BatteryResponse-charging: boolean-End-->

**System capability:** SystemCapability.PowerManager.BatteryManager.Lite

## level

```TypeScript
level: number
```

当前电池的电量百分比，取值范围：0.00~1.00。

**说明：** 除Lite Wearable外，从API Version 6开始不再维护，建议使用
[`batteryInfo.batterySOC`](../../../reference/apis-basic-services-kit/js-apis-battery-info.md#常量)替代。

**Type:** number

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 6

**Substitutes:** [@ohos.batteryInfo:batteryInfo.batterySOC](arkts-basicservices-batteryinfo-con.md#batterysoc)

<!--Device-BatteryResponse-level: number--><!--Device-BatteryResponse-level: number-End-->

**System capability:** SystemCapability.PowerManager.BatteryManager.Lite

