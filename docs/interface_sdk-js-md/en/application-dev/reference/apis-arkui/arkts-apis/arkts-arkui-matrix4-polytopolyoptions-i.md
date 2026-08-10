# PolyToPolyOptions

多边形到多边形的映射选项。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-matrix4-export interface PolyToPolyOptions--><!--Device-matrix4-export interface PolyToPolyOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { matrix4 } from 'kits/@kit.ArkUI';
```

## dst

```TypeScript
dst: Array<Point>
```

目标点坐标。

**Type:** Array&lt;Point&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PolyToPolyOptions-dst: Array<Point>--><!--Device-PolyToPolyOptions-dst: Array<Point>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## dstIndex

```TypeScript
dstIndex?: int
```

目标坐标起始索引。

默认值: src.length/2 

取值范围：[0, +∞)

**Type:** int

**Default:** src.Length/2

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PolyToPolyOptions-dstIndex?: int--><!--Device-PolyToPolyOptions-dstIndex?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## pointCount

```TypeScript
pointCount?: int
```

使用到的点数量。

默认值: 0 

取值范围：[0, +∞)

**Type:** int

**Default:** 0

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PolyToPolyOptions-pointCount?: int--><!--Device-PolyToPolyOptions-pointCount?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## src

```TypeScript
src: Array<Point>
```

源点坐标。

**Type:** Array&lt;Point&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PolyToPolyOptions-src: Array<Point>--><!--Device-PolyToPolyOptions-src: Array<Point>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## srcIndex

```TypeScript
srcIndex?: int
```

源点坐标起始索引。

默认值:0 

取值范围：[0, +∞)

**Type:** int

**Default:** 0

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PolyToPolyOptions-srcIndex?: int--><!--Device-PolyToPolyOptions-srcIndex?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

