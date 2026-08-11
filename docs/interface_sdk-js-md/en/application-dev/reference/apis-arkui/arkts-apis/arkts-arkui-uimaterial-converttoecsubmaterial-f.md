# convertToECSubMaterial

## Modules to Import

```TypeScript
import { uiMaterial } from 'kits/@kit.ArkUI';
```

## convertToECSubMaterial

```TypeScript
export function convertToECSubMaterial(material: uiMaterial.ImmersiveMaterial) : uiMaterial.ImmersiveMaterial
```

Convert from ImmersiveMaterial to another ImmersiveMaterial set on sub component of EffectComponent.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-uiMaterial-export function convertToECSubMaterial(material: uiMaterial.ImmersiveMaterial) : uiMaterial.ImmersiveMaterial--><!--Device-uiMaterial-export function convertToECSubMaterial(material: uiMaterial.ImmersiveMaterial) : uiMaterial.ImmersiveMaterial-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| material | uiMaterial.ImmersiveMaterial | Yes | The ImmersiveMaterial. |

**Return value:**

| Type | Description |
| --- | --- |
| uiMaterial.ImmersiveMaterial | The ImmersiveMaterial set on sub component of EffectComponent. |

