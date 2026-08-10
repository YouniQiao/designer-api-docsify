# PrimitiveTopology

顶点序列如何构成三角形.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-unnamed-export enum PrimitiveTopology--><!--Device-unnamed-export enum PrimitiveTopology-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## TRIANGLE_LIST

```TypeScript
TRIANGLE_LIST = 0
```

顶点形成一组独立的三角形. 顶点(0, 1, 2)、(3, 4, 5)、...定义独立的三角形.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-PrimitiveTopology-TRIANGLE_LIST = 0--><!--Device-PrimitiveTopology-TRIANGLE_LIST = 0-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## TRIANGLE_STRIP

```TypeScript
TRIANGLE_STRIP = 1
```

顶点形成三角形条带. 从第三个顶点开始，每个顶点与前两个顶点构成三角形.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-PrimitiveTopology-TRIANGLE_STRIP = 1--><!--Device-PrimitiveTopology-TRIANGLE_STRIP = 1-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

