# getLevel

## getLevel

```TypeScript
function getLevel(): ThermalLevel
```

Obtains the current thermal level.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-thermal-function getLevel(): ThermalLevel--><!--Device-thermal-function getLevel(): ThermalLevel-End-->

**System capability:** SystemCapability.PowerManager.ThermalManager

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Thermal level. |

**Example**

```TypeScript
let level = thermal.getLevel();
console.info('thermal level is: ' + level);
```

