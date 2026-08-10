# VertexMode

顶点绘制的连接方式枚举。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-drawing-enum VertexMode--><!--Device-drawing-enum VertexMode-End-->

**System capability:** SystemCapability.Graphics.Drawing

## TRIANGLES_VERTEXMODE

```TypeScript
TRIANGLES_VERTEXMODE = 0
```

顶点按顺序每三个一组，分别构成独立的三角形。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-VertexMode-TRIANGLES_VERTEXMODE = 0--><!--Device-VertexMode-TRIANGLES_VERTEXMODE = 0-End-->

**System capability:** SystemCapability.Graphics.Drawing

## TRIANGLESSTRIP_VERTEXMODE

```TypeScript
TRIANGLESSTRIP_VERTEXMODE = 1
```

连续的三角形共享一条边，对于连续表面效率高。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-VertexMode-TRIANGLESSTRIP_VERTEXMODE = 1--><!--Device-VertexMode-TRIANGLESSTRIP_VERTEXMODE = 1-End-->

**System capability:** SystemCapability.Graphics.Drawing

## TRIANGLESFAN_VERTEXMODE

```TypeScript
TRIANGLESFAN_VERTEXMODE = 2
```

所有三角形共享一个顶点。适用于绘制圆形/扇形的场景。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-VertexMode-TRIANGLESFAN_VERTEXMODE = 2--><!--Device-VertexMode-TRIANGLESFAN_VERTEXMODE = 2-End-->

**System capability:** SystemCapability.Graphics.Drawing

