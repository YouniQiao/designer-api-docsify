# healthStatus

## Modules to Import

```TypeScript
import { batteryInfo } from '@kit.BasicServicesKit';
```

## healthStatus

```TypeScript
function healthStatus(): BatteryHealthState
```

Battery health status of the device.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-batteryInfo-function healthStatus(): BatteryHealthState--><!--Device-batteryInfo-function healthStatus(): BatteryHealthState-End-->

**System capability:** SystemCapability.PowerManager.BatteryManager.Core

**Return value:**

| Type | Description |
| --- | --- |
| [BatteryHealthState](arkts-basicservices-batteryinfo-batteryhealthstate-e.md) | Returns the battery health status of the device. |

