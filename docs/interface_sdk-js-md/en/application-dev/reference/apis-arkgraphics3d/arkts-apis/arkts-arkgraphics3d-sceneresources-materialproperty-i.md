# MaterialProperty

材质属性接口.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface MaterialProperty--><!--Device-unnamed-export interface MaterialProperty-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## factor

```TypeScript
factor: Vec4
```

纹理系数. 默认为{1,1,1,1}，表示无效果.

**Type:** [Vec4](arkts-arkgraphics3d-scenetypes-vec4-i.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-MaterialProperty-factor: Vec4--><!--Device-MaterialProperty-factor: Vec4-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## image

```TypeScript
image: Image | null
```

要使用的纹理. 如果未定义，factor定义漫反射颜色.

**Type:** [Image](arkts-arkgraphics3d-sceneresources-image-i.md) \| null

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-MaterialProperty-image: Image | null--><!--Device-MaterialProperty-image: Image | null-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## sampler

```TypeScript
sampler?: Sampler
```

纹理贴图采样器，默认使用放大、缩小和mipmap过滤模式为线性过滤（LINEAR），纹理贴图U、V、W方向的寻址模式为重复（REPEAT）。

**Type:** [Sampler](arkts-arkgraphics3d-sceneresources-sampler-i.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-MaterialProperty-sampler?: Sampler--><!--Device-MaterialProperty-sampler?: Sampler-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

