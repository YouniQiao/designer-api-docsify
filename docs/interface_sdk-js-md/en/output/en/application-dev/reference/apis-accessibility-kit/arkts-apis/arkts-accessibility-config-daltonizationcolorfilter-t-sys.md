# DaltonizationColorFilter (System API)

```TypeScript
type DaltonizationColorFilter = 'Normal' | 'Protanomaly' | 'Deuteranomaly' | 'Tritanomaly'
```

Enumerates the daltonization filters. The configuration of **DaltonizationColorFilter** takes effect only when [daltonizationState]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ is set to **true**; the normal type is used when [daltonizationState]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ is set to **false**.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-config-type DaltonizationColorFilter = 'Normal' | 'Protanomaly' | 'Deuteranomaly' | 'Tritanomaly'--><!--Device-config-type DaltonizationColorFilter = 'Normal' | 'Protanomaly' | 'Deuteranomaly' | 'Tritanomaly'-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

| Type | Description |
| --- | --- |
| 'Normal' | Filter for normal users. |
| 'Protanomaly' | Filter for protanomaly. |
| 'Deuteranomaly' | Filter for deuteranomaly. |
| 'Tritanomaly' | Filter for tritanomaly. |

