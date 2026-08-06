# getThermalLevel

## getThermalLevel

```TypeScript
function getThermalLevel(): ThermalLevel
```

Obtains the current thermal level.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [thermal.getLevel](arkts-basicservices-thermal-getlevel-f.md#getlevel)

<!--Device-thermal-function getThermalLevel(): ThermalLevel--><!--Device-thermal-function getThermalLevel(): ThermalLevel-End-->

**System capability:** SystemCapability.PowerManager.ThermalManager

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Thermal level. |

**Example**

```TypeScript
let level = thermal.getThermalLevel();
console.info('thermal level is: ' + level);
```

