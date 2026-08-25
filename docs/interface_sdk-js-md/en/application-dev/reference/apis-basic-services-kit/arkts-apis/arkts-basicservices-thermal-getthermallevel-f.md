# getThermalLevel

## Modules to Import

```TypeScript
import { thermal } from '@kit.BasicServicesKit';
```

## getThermalLevel

```TypeScript
function getThermalLevel(): ThermalLevel
```

Obtains the current thermal level.

**Since:** 8

**ArkTS mode:** Supports only ArkTS-Dyn, since version 8.

**Deprecated since:** 9

**Substitutes:** [getLevel](arkts-basicservices-thermal-getlevel-f.md)

**System capability:** SystemCapability.PowerManager.ThermalManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ThermalLevel](arkts-basicservices-thermal-thermallevel-e.md) |

**Examples**

```TypeScript
let level = thermal.getThermalLevel();
console.info('thermal level is: ' + level);
```
