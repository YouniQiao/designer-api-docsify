# PCFConfig

PCF软阴影配置参数

**Inheritance/Implementation:** PCFConfig extends [SoftShadowConfig](arkts-arkgraphics3d-scene-softshadowconfig-c.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export declare class PCFConfig extends SoftShadowConfig--><!--Device-unnamed-export declare class PCFConfig extends SoftShadowConfig-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## shadowSampleCount

```TypeScript
set shadowSampleCount(value: int | undefined)
```

设置用于渲染阴影像素的阴影图采样数量.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Default:** 16

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PCFConfig-set shadowSampleCount(value: int | undefined)--><!--Device-PCFConfig-set shadowSampleCount(value: int | undefined)-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## shadowSampleRadius

```TypeScript
set shadowSampleRadius(value: double | undefined)
```

设置像素级阴影边缘周围的采样半径.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Default:** 5.0

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PCFConfig-set shadowSampleRadius(value: double | undefined)--><!--Device-PCFConfig-set shadowSampleRadius(value: double | undefined)-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

