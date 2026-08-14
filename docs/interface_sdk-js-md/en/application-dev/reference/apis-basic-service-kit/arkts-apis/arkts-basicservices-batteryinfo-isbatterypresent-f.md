# isBatteryPresent

## Modules to Import

```TypeScript
import { batteryInfo } from 'batteryInfo';
```

## isBatteryPresent

```TypeScript
function isBatteryPresent(): boolean
```

Whether the battery is supported or present. The value **true** means that the battery is supported or present; **false** means the opposite. Default value: **false**.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-batteryInfo-function isBatteryPresent(): boolean--><!--Device-batteryInfo-function isBatteryPresent(): boolean-End-->

**System capability:** SystemCapability.PowerManager.BatteryManager.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the battery is supported or present; returns false if the battery is not supported or absent. |

