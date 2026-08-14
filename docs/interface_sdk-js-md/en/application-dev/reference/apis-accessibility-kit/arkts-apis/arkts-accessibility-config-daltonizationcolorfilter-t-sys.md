# DaltonizationColorFilter (System API)

```TypeScript
type DaltonizationColorFilter = 'Normal' | 'Protanomaly' | 'Deuteranomaly' | 'Tritanomaly'
```

The configuration takes effect when the daltonization feature is enabled ( [daltonizationState](arkts-accessibility-config-con-sys.md#daltonizationState) is set to **true**). When the daltonization feature is disabled ([daltonizationState](arkts-accessibility-config-con-sys.md#daltonizationState) is set to **false**), the standard type is displayed.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-config-type DaltonizationColorFilter = 'Normal' | 'Protanomaly' | 'Deuteranomaly' | 'Tritanomaly'--><!--Device-config-type DaltonizationColorFilter = 'Normal' | 'Protanomaly' | 'Deuteranomaly' | 'Tritanomaly'-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

| Type | Description |
| --- | --- |
| 'Normal' | Standard color vision. |
| 'Protanomaly' | Red-weak color vision deficiency. |
| 'Deuteranomaly' | Green-weak color vision deficiency. |
| 'Tritanomaly' | Blue-weak color vision deficiency. |

