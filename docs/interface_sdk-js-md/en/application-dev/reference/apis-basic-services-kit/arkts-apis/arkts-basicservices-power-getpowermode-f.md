# getPowerMode

## Modules to Import

```TypeScript
import { power } from '@kit.BasicServicesKit';
```

## getPowerMode

```TypeScript
function getPowerMode(): DevicePowerMode
```

Obtains the power mode of this device.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.PowerManager.PowerManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DevicePowerMode](arkts-basicservices-power-devicepowermode-e.md) |

**Examples**

```TypeScript
let mode = power.getPowerMode();
console.info('power mode: ' + mode);
```
