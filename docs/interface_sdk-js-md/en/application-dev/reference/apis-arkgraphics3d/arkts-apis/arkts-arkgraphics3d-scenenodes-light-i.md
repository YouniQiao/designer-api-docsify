# Light

定义Light接口.

**Inheritance/Implementation:** Light extends [Node](arkts-arkgraphics3d-scenenodes-node-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface Light extends Node--><!--Device-unnamed-export interface Light extends Node-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## color

```TypeScript
color: Color
```

光源颜色.

**Type:** [Color](arkts-arkgraphics3d-scenetypes-color-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Light-color: Color--><!--Device-Light-color: Color-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## enabled

```TypeScript
enabled: boolean
```

是否启用光源.

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Light-enabled: boolean--><!--Device-Light-enabled: boolean-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## intensity

```TypeScript
intensity: double
```

光照强度，单位为坎德拉（cd），取值范围是大于0的实数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Light-intensity: double--><!--Device-Light-intensity: double-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## lightType

```TypeScript
readonly lightType: LightType
```

光源类型.

**Type:** [LightType](arkts-arkgraphics3d-scenenodes-lighttype-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Light-readonly lightType: LightType--><!--Device-Light-readonly lightType: LightType-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## shadowEnabled

```TypeScript
shadowEnabled: boolean
```

是否投射阴影.

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Light-shadowEnabled: boolean--><!--Device-Light-shadowEnabled: boolean-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

