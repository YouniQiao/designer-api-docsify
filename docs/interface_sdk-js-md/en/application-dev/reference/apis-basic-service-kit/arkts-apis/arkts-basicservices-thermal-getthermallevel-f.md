# getThermalLevel

## Modules to Import

```TypeScript
import { thermal } from 'kits/@kit.BasicServicesKit';
```

## getThermalLevel

```TypeScript
function getThermalLevel(): ThermalLevel
```

获取当前热档位信息。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [thermal.getLevel](arkts-basicservices-thermal-getlevel-f.md#getlevel)

<!--Device-thermal-function getThermalLevel(): ThermalLevel--><!--Device-thermal-function getThermalLevel(): ThermalLevel-End-->

**System capability:** SystemCapability.PowerManager.ThermalManager

**Return value:**

| Type | Description |
| --- | --- |
| [ThermalLevel](arkts-basicservices-thermal-thermallevel-e.md) | 热档位信息。 |

## Examples

```TypeScript
let level = thermal.getThermalLevel();
console.info('thermal level is: ' + level);
```

