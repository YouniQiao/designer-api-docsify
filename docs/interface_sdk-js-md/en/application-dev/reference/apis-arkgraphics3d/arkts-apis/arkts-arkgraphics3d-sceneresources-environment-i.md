# Environment

环境资源.

**Inheritance/Implementation:** Environment extends [SceneResource](arkts-arkgraphics3d-sceneresources-sceneresource-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface Environment extends SceneResource--><!--Device-unnamed-export interface Environment extends SceneResource-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## backgroundType

```TypeScript
backgroundType: EnvironmentBackgroundType
```

环境背景类型.

**Type:** [EnvironmentBackgroundType](arkts-arkgraphics3d-sceneresources-environmentbackgroundtype-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Environment-backgroundType: EnvironmentBackgroundType--><!--Device-Environment-backgroundType: EnvironmentBackgroundType-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## environmentImage

```TypeScript
environmentImage?: Image | null
```

环境图像.

**Type:** [Image](arkts-arkgraphics3d-sceneresources-image-i.md) \| null

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Environment-environmentImage?: Image | null--><!--Device-Environment-environmentImage?: Image | null-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## environmentMapFactor

```TypeScript
environmentMapFactor: Vec4
```

环境贴图因子.

**Type:** [Vec4](arkts-arkgraphics3d-scenetypes-vec4-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Environment-environmentMapFactor: Vec4--><!--Device-Environment-environmentMapFactor: Vec4-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## environmentRotation

```TypeScript
environmentRotation?: Quaternion
```

环境旋转

**Type:** [Quaternion](arkts-arkgraphics3d-scenetypes-quaternion-i.md)

**Default:** Quaternion {x:0, y:0, z:0, w:1} 单位四元数（无旋转）

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Environment-environmentRotation?: Quaternion--><!--Device-Environment-environmentRotation?: Quaternion-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## indirectDiffuseFactor

```TypeScript
indirectDiffuseFactor: Vec4
```

环境间接漫反射因子.

**Type:** [Vec4](arkts-arkgraphics3d-scenetypes-vec4-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Environment-indirectDiffuseFactor: Vec4--><!--Device-Environment-indirectDiffuseFactor: Vec4-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## indirectSpecularFactor

```TypeScript
indirectSpecularFactor: Vec4
```

环境间接镜面反射因子.

**Type:** [Vec4](arkts-arkgraphics3d-scenetypes-vec4-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Environment-indirectSpecularFactor: Vec4--><!--Device-Environment-indirectSpecularFactor: Vec4-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## irradianceCoefficients

```TypeScript
irradianceCoefficients?: Vec3[]
```

辐射系数（九个Vec3的数组）.

**Type:** [Vec3](arkts-arkgraphics3d-scenetypes-vec3-i.md)[]

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Environment-irradianceCoefficients?: Vec3[]--><!--Device-Environment-irradianceCoefficients?: Vec3[]-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## radianceImage

```TypeScript
radianceImage?: Image | null
```

环境辐射图像.

**Type:** [Image](arkts-arkgraphics3d-sceneresources-image-i.md) \| null

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Environment-radianceImage?: Image | null--><!--Device-Environment-radianceImage?: Image | null-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

