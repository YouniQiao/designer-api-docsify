# isBatteryPresent

## Modules to Import

```TypeScript
import { batteryInfo } from 'kits/@kit.BasicServicesKit';
```

## isBatteryPresent

```TypeScript
function isBatteryPresent(): boolean
```

表示当前设备是否支持电池或者电池是否在位。true表示支持电池或电池在位，false表示不支持电池或电池不在位，默认为false。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-batteryInfo-function isBatteryPresent(): boolean--><!--Device-batteryInfo-function isBatteryPresent(): boolean-End-->

**System capability:** SystemCapability.PowerManager.BatteryManager.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回true表示支持电池或电池在位，返回false表示不支持电池或电池不在位。 |

