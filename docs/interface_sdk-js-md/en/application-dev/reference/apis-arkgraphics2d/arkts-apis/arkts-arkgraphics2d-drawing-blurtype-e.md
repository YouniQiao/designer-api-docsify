# BlurType

定义蒙版滤镜模糊中操作类型的枚举。蒙版用于定义图像的可绘制区域，滤镜用于应用模糊等视觉效果。该枚举控制模糊效果如何应用到蒙版定义的区域内。

| 名称 | 值 | 说明 | 示意图 |  
| ------ | - | ------------------ | -------- |  
| NORMAL | 0 | 全面模糊，外圈和内部实体一起模糊。 | ![NORMAL](../../../reference/apis-arkgraphics2d/figures/BlurType-Normal.png) |  
| SOLID | 1 | 内部实体不变，只模糊外圈边缘部分。 | ![SOLID](../../../reference/apis-arkgraphics2d/figures/BlurType-Solid.png) |  
| OUTER | 2 | 只有外圈边缘模糊，内部实体完全透明。 | ![OUTER](../../../reference/apis-arkgraphics2d/figures/BlurType-Outer.png) |  
| INNER | 3 | 只有内部实体模糊，外圈边缘清晰。 | ![INNER](../../../reference/apis-arkgraphics2d/figures/BlurType-Inner.png) |

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-drawing-enum BlurType--><!--Device-drawing-enum BlurType-End-->

**System capability:** SystemCapability.Graphics.Drawing

## NORMAL

```TypeScript
NORMAL = 0
```

Both the outer edges and the inner solid parts are blurred.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-BlurType-NORMAL = 0--><!--Device-BlurType-NORMAL = 0-End-->

**System capability:** SystemCapability.Graphics.Drawing

## SOLID

```TypeScript
SOLID = 1
```

The inner solid part remains unchanged, while only the outer edges are blurred.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-BlurType-SOLID = 1--><!--Device-BlurType-SOLID = 1-End-->

**System capability:** SystemCapability.Graphics.Drawing

## OUTER

```TypeScript
OUTER = 2
```

Only the outer edges are blurred, with the inner solid part being fully transparent.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-BlurType-OUTER = 2--><!--Device-BlurType-OUTER = 2-End-->

**System capability:** SystemCapability.Graphics.Drawing

## INNER

```TypeScript
INNER = 3
```

Only the inner solid part is blurred, while the outer edges remain sharp.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-BlurType-INNER = 3--><!--Device-BlurType-INNER = 3-End-->

**System capability:** SystemCapability.Graphics.Drawing

