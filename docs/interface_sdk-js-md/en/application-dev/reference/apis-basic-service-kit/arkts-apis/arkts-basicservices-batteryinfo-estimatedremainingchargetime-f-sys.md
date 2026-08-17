# estimatedRemainingChargeTime (System API)

## Modules to Import

```TypeScript
import { batteryInfo } from 'batteryInfo';
```

## estimatedRemainingChargeTime

```TypeScript
function estimatedRemainingChargeTime(): long
```

Estimated time for fully charging the current device, in unit of milliseconds. This is a system API.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-batteryInfo-function estimatedRemainingChargeTime(): long--><!--Device-batteryInfo-function estimatedRemainingChargeTime(): long-End-->

**System capability:** SystemCapability.PowerManager.BatteryManager.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| long | Returns the estimated remaining time for the current device to be fully charged, in ms. |

