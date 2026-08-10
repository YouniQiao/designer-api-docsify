# batterySOC

## Modules to Import

```TypeScript
import { batteryInfo } from 'kits/@kit.BasicServicesKit';
```

## batterySOC

```TypeScript
function batterySOC(): int
```

表示当前设备剩余电池电量百分比，取值范围是[0，100]。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-batteryInfo-function batterySOC(): int--><!--Device-batteryInfo-function batterySOC(): int-End-->

**System capability:** SystemCapability.PowerManager.BatteryManager.Core

**Return value:**

| Type | Description |
| --- | --- |
| int | 返回当前设备剩余电池电量百分比，取值范围是[0，100]。 |

