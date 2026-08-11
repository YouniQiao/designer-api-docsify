# getPowerMode

## Modules to Import

```TypeScript
import { power } from 'kits/@kit.BasicServicesKit';
```

## getPowerMode

```TypeScript
function getPowerMode(): DevicePowerMode
```

Obtains the power mode of this device.

**Since:** 9

<!--Device-power-function getPowerMode(): DevicePowerMode--><!--Device-power-function getPowerMode(): DevicePowerMode-End-->

**System capability:** SystemCapability.PowerManager.PowerManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DevicePowerMode](arkts-basicservices-power-devicepowermode-e.md) |

## Examples

```TypeScript
let mode = power.getPowerMode();
console.info('power mode: ' + mode);
```
