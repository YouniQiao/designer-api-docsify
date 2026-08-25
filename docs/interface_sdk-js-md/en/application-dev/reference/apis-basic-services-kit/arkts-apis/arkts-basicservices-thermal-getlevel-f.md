# getLevel

## Modules to Import

```TypeScript
import { thermal } from '@kit.BasicServicesKit';
```

## getLevel

```TypeScript
function getLevel(): ThermalLevel
```

Obtains the current thermal level.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.PowerManager.ThermalManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ThermalLevel](arkts-basicservices-thermal-thermallevel-e.md) |

**Examples**

```TypeScript
let level = thermal.getLevel();
console.info('thermal level is: ' + level);
```
